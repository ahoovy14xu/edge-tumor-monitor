from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class LossWeights:
    burden: float = 1.0
    efficacy: float = 0.5
    pneumonitis: float = 0.4
    consistency: float = 0.1
    hardware: float = 0.05


@dataclass(frozen=True)
class HardwareCoefficients:
    latency: float = 0.002
    energy: float = 0.001


@dataclass(frozen=True)
class ProgressiveSchedule:
    largest: int = 200
    kernel: int = 100
    depth: int = 100
    width: int = 200


@dataclass(frozen=True)
class ExperimentConfig:
    seed: int = 3407
    epochs: int = 600
    batch_size_per_gpu: int = 32
    world_size: int = 4
    gradient_accumulation: int = 1
    learning_rate: float = 3e-4
    weight_decay: float = 5e-5
    optimizer: str = "adamw"
    scheduler: str = "cosine"
    precision: str = "bf16"
    early_stopping_patience: int = 40
    volume_shape: tuple[int, int, int] = (128, 128, 128)
    metadata_features: int = 32
    resync_period: int = 4
    widths: tuple[float, ...] = (0.5, 0.625, 0.75, 1.0)
    depths: tuple[tuple[int, int], ...] = ((2, 1), (2, 2), (3, 2))
    kernel_sizes: tuple[int, ...] = (3, 5)
    loss_weights: LossWeights = field(default_factory=LossWeights)
    hardware_coefficients: HardwareCoefficients = field(default_factory=HardwareCoefficients)
    progressive_schedule: ProgressiveSchedule = field(default_factory=ProgressiveSchedule)

    @property
    def effective_batch_size(self) -> int:
        return self.batch_size_per_gpu * self.world_size * self.gradient_accumulation

    @classmethod
    def from_yaml(cls, path: str | Path) -> "ExperimentConfig":
        raw = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
        values: dict[str, Any] = dict(raw)
        values["volume_shape"] = tuple(values.get("volume_shape", (128, 128, 128)))
        values["widths"] = tuple(values.get("widths", cls.widths))
        values["depths"] = tuple(tuple(x) for x in values.get("depths", cls.depths))
        values["kernel_sizes"] = tuple(values.get("kernel_sizes", cls.kernel_sizes))
        if "loss_weights" in values:
            values["loss_weights"] = LossWeights(**values["loss_weights"])
        if "hardware_coefficients" in values:
            values["hardware_coefficients"] = HardwareCoefficients(
                **values["hardware_coefficients"]
            )
        if "progressive_schedule" in values:
            values["progressive_schedule"] = ProgressiveSchedule(**values["progressive_schedule"])
        return cls(**values)
