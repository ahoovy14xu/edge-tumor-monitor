from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import nn

from edge_tumor_monitor.model.blocks import ConvNormAct, InvertedResidual
from edge_tumor_monitor.model.trunk import HybridTrunk


@dataclass
class TemporalEncoding:
    latents: tuple[torch.Tensor, ...]
    skips: tuple[tuple[torch.Tensor, ...], ...]
    consistency: torch.Tensor


class ResidualPathway(nn.Module):
    def __init__(self, output_channels: int) -> None:
        super().__init__()
        self.encoder = nn.Sequential(
            ConvNormAct(2, 16, 5, 2),
            InvertedResidual(16, 2, 3),
            ConvNormAct(16, 32, 3, 2),
            InvertedResidual(32, 2, 3),
            ConvNormAct(32, 64, 3, 2),
            ConvNormAct(64, output_channels, 3, 2),
            ConvNormAct(output_channels, output_channels, 3, 2),
            ConvNormAct(output_channels, output_channels, 3, 2),
        )

    def forward(self, previous: torch.Tensor, current: torch.Tensor) -> torch.Tensor:
        paired = torch.cat((previous, current), dim=1)
        return self.encoder(paired)


class TemporalResidualEncoder(nn.Module):
    def __init__(self, trunk: HybridTrunk, resync_period: int = 4) -> None:
        super().__init__()
        self.trunk = trunk
        self.residual = ResidualPathway(trunk.channels[-1])
        self.resync_period = resync_period

    def forward(self, volumes: torch.Tensor, metadata: torch.Tensor) -> TemporalEncoding:
        timepoints = volumes.shape[1]
        baseline, baseline_skips = self.trunk(volumes[:, 0], metadata[:, 0])
        latents = [baseline]
        skips = [baseline_skips]
        consistency = baseline.new_zeros(())
        for timepoint in range(1, timepoints):
            delta = self.residual(volumes[:, timepoint - 1], volumes[:, timepoint])
            current = latents[-1] + delta
            current_skips = skips[-1]
            if self.training and timepoint % self.resync_period == 0:
                reference, current_skips = self.trunk(volumes[:, timepoint], metadata[:, timepoint])
                consistency = consistency + torch.mean(torch.square(current - reference))
            latents.append(current)
            skips.append(current_skips)
        return TemporalEncoding(tuple(latents), tuple(skips), consistency)
