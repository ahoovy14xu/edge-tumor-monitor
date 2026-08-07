from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import torch
from torch import nn

from edge_tumor_monitor.model.heads import TaskExperts
from edge_tumor_monitor.model.temporal import TemporalResidualEncoder
from edge_tumor_monitor.model.trunk import HybridTrunk

Query = Literal["burden", "efficacy", "pneumonitis"]


@dataclass
class MonitorOutput:
    prediction: torch.Tensor
    consistency: torch.Tensor
    query: Query


class LongitudinalTumorMonitor(nn.Module):
    def __init__(
        self,
        metadata_features: int = 32,
        width: float = 1.0,
        depths: tuple[int, int] = (2, 2),
        kernel: int = 5,
        resync_period: int = 4,
    ) -> None:
        super().__init__()
        trunk = HybridTrunk(metadata_features, width, depths, kernel)
        self.temporal = TemporalResidualEncoder(trunk, resync_period)
        self.experts = TaskExperts(trunk.channels)

    def forward(
        self, volumes: torch.Tensor, metadata: torch.Tensor, query: Query, timepoint: int = -1
    ) -> MonitorOutput:
        encoded = self.temporal(volumes, metadata)
        latent = encoded.latents[timepoint]
        if query == "burden":
            output_shape = (volumes.shape[-3], volumes.shape[-2], volumes.shape[-1])
            prediction = self.experts.forward_burden(latent, encoded.skips[timepoint], output_shape)
        elif query == "efficacy":
            prediction = self.experts.forward_efficacy(latent)
        elif query == "pneumonitis":
            prediction = self.experts.forward_pneumonitis(latent)
        else:
            raise ValueError(f"unsupported query: {query}")
        return MonitorOutput(prediction, encoded.consistency, query)
