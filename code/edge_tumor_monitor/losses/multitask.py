from __future__ import annotations

from dataclasses import dataclass

import torch

from edge_tumor_monitor.config import HardwareCoefficients, LossWeights


@dataclass
class LossTerms:
    burden: torch.Tensor
    efficacy: torch.Tensor
    pneumonitis: torch.Tensor
    consistency: torch.Tensor
    hardware: torch.Tensor

    def total(self, weights: LossWeights) -> torch.Tensor:
        return (
            weights.burden * self.burden
            + weights.efficacy * self.efficacy
            + weights.pneumonitis * self.pneumonitis
            + weights.consistency * self.consistency
            + weights.hardware * self.hardware
        )


def hardware_lagrangian(
    task_loss: torch.Tensor,
    latency_ms: torch.Tensor,
    energy_mj: torch.Tensor,
    coefficients: HardwareCoefficients = HardwareCoefficients(),
) -> torch.Tensor:
    return task_loss + coefficients.latency * latency_ms + coefficients.energy * energy_mj


def routing_entropy(probabilities: torch.Tensor, epsilon: float = 1e-8) -> torch.Tensor:
    entropy = -(probabilities * torch.log(probabilities.clamp_min(epsilon))).sum(dim=-1)
    return -entropy.mean()
