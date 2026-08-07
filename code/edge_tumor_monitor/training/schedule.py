from __future__ import annotations

import math
from dataclasses import dataclass

from torch.optim import Optimizer
from torch.optim.lr_scheduler import LambdaLR

from edge_tumor_monitor.config import ProgressiveSchedule


@dataclass(frozen=True)
class SubnetStage:
    width: float
    depth: tuple[int, int]
    kernel: int
    phase: str


def progressive_stage(
    epoch: int, schedule: ProgressiveSchedule = ProgressiveSchedule()
) -> SubnetStage:
    if epoch < schedule.largest:
        return SubnetStage(1.0, (2, 2), 5, "largest")
    if epoch < schedule.largest + schedule.kernel:
        return SubnetStage(1.0, (2, 2), 3, "kernel")
    if epoch < schedule.largest + schedule.kernel + schedule.depth:
        return SubnetStage(1.0, (2, 1), 3, "depth")
    progress = min(
        1.0,
        (epoch - schedule.largest - schedule.kernel - schedule.depth) / max(schedule.width - 1, 1),
    )
    levels = (1.0, 0.875, 0.75, 0.625, 0.5)
    index = min(int(progress * len(levels)), len(levels) - 1)
    return SubnetStage(levels[index], (2, 1), 3, "width")


def cosine_scheduler(optimizer: Optimizer, epochs: int, warmup_epochs: int = 0) -> LambdaLR:
    def scale(epoch: int) -> float:
        if warmup_epochs > 0 and epoch < warmup_epochs:
            return (epoch + 1) / warmup_epochs
        progress = (epoch - warmup_epochs) / max(1, epochs - warmup_epochs)
        return 0.5 * (1.0 + math.cos(math.pi * progress))

    return LambdaLR(optimizer, scale)
