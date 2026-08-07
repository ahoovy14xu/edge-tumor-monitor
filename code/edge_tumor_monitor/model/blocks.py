from __future__ import annotations

import math

import torch
from torch import nn


class ConvNormAct(nn.Module):
    def __init__(
        self, source: int, target: int, kernel: int = 3, stride: int = 1, groups: int = 1
    ) -> None:
        super().__init__()
        padding = kernel // 2
        self.block = nn.Sequential(
            nn.Conv3d(
                source, target, kernel, stride=stride, padding=padding, groups=groups, bias=False
            ),
            nn.BatchNorm3d(target),
            nn.SiLU(inplace=True),
        )

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        return self.block(inputs)


class InvertedResidual(nn.Module):
    def __init__(self, channels: int, expansion: int = 2, kernel: int = 3) -> None:
        super().__init__()
        hidden = channels * expansion
        self.expand = ConvNormAct(channels, hidden, 1)
        self.depthwise = ConvNormAct(hidden, hidden, kernel, groups=hidden)
        self.project = nn.Sequential(
            nn.Conv3d(hidden, channels, 1, bias=False), nn.BatchNorm3d(channels)
        )

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        return inputs + self.project(self.depthwise(self.expand(inputs)))


class EfficientAttention3d(nn.Module):
    def __init__(self, channels: int, heads: int = 4) -> None:
        super().__init__()
        if channels % heads != 0:
            raise ValueError("channels must be divisible by heads")
        self.heads = heads
        self.scale = (channels // heads) ** -0.5
        self.qkv = nn.Conv3d(channels, channels * 3, 1, bias=False)
        self.output = nn.Conv3d(channels, channels, 1)
        self.norm = nn.BatchNorm3d(channels)

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        batch, channels, depth, height, width = inputs.shape
        tokens = depth * height * width
        qkv = self.qkv(inputs).reshape(batch, 3, self.heads, channels // self.heads, tokens)
        query, key, value = qkv.unbind(1)
        query = query.softmax(dim=-2)
        key = key.softmax(dim=-1)
        context = torch.einsum("bhcn,bhdn->bhcd", key, value)
        attended = torch.einsum("bhcd,bhcn->bhdn", context, query * self.scale)
        attended = attended.reshape(batch, channels, depth, height, width)
        return self.norm(inputs + self.output(attended))


class MetadataBottleneck(nn.Module):
    def __init__(self, image_channels: int, metadata_features: int, bottleneck: int = 32) -> None:
        super().__init__()
        self.metadata = nn.Sequential(
            nn.Linear(metadata_features, bottleneck),
            nn.SiLU(),
            nn.Linear(bottleneck, image_channels * 2),
        )

    def forward(self, image: torch.Tensor, metadata: torch.Tensor) -> torch.Tensor:
        parameters = self.metadata(metadata)
        scale, shift = parameters.chunk(2, dim=-1)
        shape = (image.shape[0], image.shape[1], 1, 1, 1)
        return image * (1.0 + torch.tanh(scale).view(shape)) + shift.view(shape)


class SqueezeExcitation3d(nn.Module):
    def __init__(self, channels: int, reduction: int = 4) -> None:
        super().__init__()
        hidden = max(channels // reduction, 4)
        self.pool = nn.AdaptiveAvgPool3d(1)
        self.layers = nn.Sequential(
            nn.Conv3d(channels, hidden, 1), nn.SiLU(), nn.Conv3d(hidden, channels, 1), nn.Sigmoid()
        )

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        return inputs * self.layers(self.pool(inputs))


def parameter_count(module: nn.Module) -> int:
    return sum(parameter.numel() for parameter in module.parameters())


def channel_count(base: int, multiplier: float, divisor: int = 8) -> int:
    raw = base * multiplier
    return max(divisor, int(math.ceil(raw / divisor) * divisor))
