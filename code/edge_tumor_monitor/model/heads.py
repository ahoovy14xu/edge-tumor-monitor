from __future__ import annotations

import torch
from torch import nn
import torch.nn.functional as functional

from edge_tumor_monitor.model.blocks import ConvNormAct


class BurdenDecoder(nn.Module):
    def __init__(self, channels: tuple[int, int, int, int]) -> None:
        super().__init__()
        c1, c2, c3, c4 = channels
        self.up_three = ConvNormAct(c4 + c3, c3)
        self.up_two = ConvNormAct(c3 + c2, c2)
        self.up_one = ConvNormAct(c2 + c1, c1)
        self.refine = nn.Sequential(ConvNormAct(c1, c1), ConvNormAct(c1, c1))
        self.output = nn.Conv3d(c1, 1, 1)

    def forward(
        self,
        latent: torch.Tensor,
        skips: tuple[torch.Tensor, ...],
        output_shape: tuple[int, int, int],
    ) -> torch.Tensor:
        first, second, third = skips
        value = functional.interpolate(
            latent, size=third.shape[-3:], mode="trilinear", align_corners=False
        )
        value = self.up_three(torch.cat((value, third), dim=1))
        value = functional.interpolate(
            value, size=second.shape[-3:], mode="trilinear", align_corners=False
        )
        value = self.up_two(torch.cat((value, second), dim=1))
        value = functional.interpolate(
            value, size=first.shape[-3:], mode="trilinear", align_corners=False
        )
        value = self.up_one(torch.cat((value, first), dim=1))
        value = self.refine(value)
        return functional.interpolate(
            self.output(value), size=output_shape, mode="trilinear", align_corners=False
        )


class PooledExpert(nn.Module):
    def __init__(self, channels: int, hidden: int, outputs: int = 1) -> None:
        super().__init__()
        self.pool = nn.AdaptiveAvgPool3d(1)
        self.layers = nn.Sequential(
            nn.Flatten(),
            nn.Linear(channels, hidden),
            nn.SiLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden, hidden),
            nn.SiLU(),
            nn.Linear(hidden, outputs),
        )

    def forward(self, latent: torch.Tensor) -> torch.Tensor:
        return self.layers(self.pool(latent))


class TaskExperts(nn.Module):
    def __init__(self, channels: tuple[int, int, int, int]) -> None:
        super().__init__()
        self.burden = BurdenDecoder(channels)
        self.efficacy = PooledExpert(channels[-1], 256)
        self.pneumonitis = PooledExpert(channels[-1], 320)

    def forward_burden(
        self,
        latent: torch.Tensor,
        skips: tuple[torch.Tensor, ...],
        output_shape: tuple[int, int, int],
    ) -> torch.Tensor:
        return self.burden(latent, skips, output_shape)

    def forward_efficacy(self, latent: torch.Tensor) -> torch.Tensor:
        return self.efficacy(latent).squeeze(-1)

    def forward_pneumonitis(self, latent: torch.Tensor) -> torch.Tensor:
        return self.pneumonitis(latent).squeeze(-1)
