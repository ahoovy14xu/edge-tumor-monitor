from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import torch
from torch.optim import Optimizer

from edge_tumor_monitor.config import ExperimentConfig
from edge_tumor_monitor.data.records import LongitudinalBatch
from edge_tumor_monitor.losses.classification import pneumonitis_loss
from edge_tumor_monitor.losses.segmentation import burden_loss
from edge_tumor_monitor.losses.survival import efficacy_loss
from edge_tumor_monitor.model.system import LongitudinalTumorMonitor


@dataclass(frozen=True)
class EpochReport:
    loss: float
    batches: int


class Trainer:
    def __init__(
        self,
        model: LongitudinalTumorMonitor,
        optimizer: Optimizer,
        config: ExperimentConfig,
        device: torch.device,
    ) -> None:
        self.model = model
        self.optimizer = optimizer
        self.config = config
        self.device = device

    def compute_loss(self, batch: LongitudinalBatch) -> torch.Tensor:
        total = batch.volumes.sum() * 0.0
        weights = self.config.loss_weights
        if batch.burden_masks is not None:
            output = self.model(batch.volumes, batch.metadata, "burden")
            total = (
                total
                + weights.burden * burden_loss(output.prediction, batch.burden_masks[:, -1])
                + weights.consistency * output.consistency
            )
        if batch.event_times is not None and batch.event_observed is not None:
            output = self.model(batch.volumes, batch.metadata, "efficacy")
            total = (
                total
                + weights.efficacy
                * efficacy_loss(output.prediction, batch.event_times, batch.event_observed)
                + weights.consistency * output.consistency
            )
        if batch.pneumonitis_labels is not None:
            output = self.model(batch.volumes, batch.metadata, "pneumonitis")
            total = (
                total
                + weights.pneumonitis
                * pneumonitis_loss(output.prediction, batch.pneumonitis_labels)
                + weights.consistency * output.consistency
            )
        return total

    def train_epoch(self, batches: Iterable[LongitudinalBatch]) -> EpochReport:
        self.model.train()
        accumulated = 0.0
        count = 0
        self.optimizer.zero_grad(set_to_none=True)
        for count, source in enumerate(batches, start=1):
            batch = source.to(self.device)
            with torch.autocast(
                device_type=self.device.type,
                dtype=torch.bfloat16,
                enabled=self.config.precision == "bf16",
            ):
                loss = self.compute_loss(batch) / self.config.gradient_accumulation
            loss.backward()
            if count % self.config.gradient_accumulation == 0:
                self.optimizer.step()
                self.optimizer.zero_grad(set_to_none=True)
            accumulated += float(loss.detach()) * self.config.gradient_accumulation
        return EpochReport(accumulated / max(count, 1), count)
