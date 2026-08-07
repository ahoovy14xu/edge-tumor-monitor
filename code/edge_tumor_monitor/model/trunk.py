from __future__ import annotations

import torch
from torch import nn

from edge_tumor_monitor.model.blocks import (
    ConvNormAct,
    EfficientAttention3d,
    InvertedResidual,
    MetadataBottleneck,
    SqueezeExcitation3d,
    channel_count,
)


class HybridTrunk(nn.Module):
    def __init__(
        self,
        metadata_features: int = 32,
        width: float = 1.0,
        depths: tuple[int, int] = (2, 2),
        kernel: int = 5,
    ) -> None:
        super().__init__()
        c1 = channel_count(32, width)
        c2 = channel_count(64, width)
        c3 = channel_count(96, width)
        c4 = channel_count(128, width)
        self.stem = nn.Sequential(
            ConvNormAct(1, c1, 5, 2), ConvNormAct(c1, c1, 3, 2), ConvNormAct(c1, c1, 3, 2)
        )
        self.conv_stage = nn.Sequential(
            *[InvertedResidual(c1, 2, kernel) for _ in range(depths[0])]
        )
        self.down_one = ConvNormAct(c1, c2, 3, 2)
        self.conv_stage_two = nn.Sequential(
            *[InvertedResidual(c2, 2, kernel) for _ in range(depths[1])]
        )
        self.down_two = ConvNormAct(c2, c3, 3, 2)
        self.attention_one = nn.Sequential(EfficientAttention3d(c3, 4), SqueezeExcitation3d(c3))
        self.down_three = ConvNormAct(c3, c4, 3, 2)
        self.attention_two = nn.Sequential(EfficientAttention3d(c4, 4), SqueezeExcitation3d(c4))
        self.fusion = MetadataBottleneck(c4, metadata_features)
        self.channels = (c1, c2, c3, c4)

    def forward(
        self, volume: torch.Tensor, metadata: torch.Tensor
    ) -> tuple[torch.Tensor, tuple[torch.Tensor, ...]]:
        first = self.conv_stage(self.stem(volume))
        second = self.conv_stage_two(self.down_one(first))
        third = self.attention_one(self.down_two(second))
        fourth = self.attention_two(self.down_three(third))
        fused = self.fusion(fourth, metadata)
        return fused, (first, second, third)
