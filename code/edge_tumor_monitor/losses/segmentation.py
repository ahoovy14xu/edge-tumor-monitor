from __future__ import annotations

import torch


def soft_dice_loss(
    logits: torch.Tensor, targets: torch.Tensor, epsilon: float = 1e-6
) -> torch.Tensor:
    probabilities = torch.sigmoid(logits)
    dimensions = tuple(range(1, probabilities.ndim))
    intersection = torch.sum(probabilities * targets, dim=dimensions)
    denominator = torch.sum(probabilities, dim=dimensions) + torch.sum(targets, dim=dimensions)
    score = (2.0 * intersection + epsilon) / (denominator + epsilon)
    return 1.0 - score.mean()


def tversky_loss(
    logits: torch.Tensor,
    targets: torch.Tensor,
    alpha: float = 0.7,
    beta: float = 0.3,
    epsilon: float = 1e-6,
) -> torch.Tensor:
    probabilities = torch.sigmoid(logits)
    dimensions = tuple(range(1, probabilities.ndim))
    true_positive = torch.sum(probabilities * targets, dim=dimensions)
    false_positive = torch.sum(probabilities * (1.0 - targets), dim=dimensions)
    false_negative = torch.sum((1.0 - probabilities) * targets, dim=dimensions)
    score = (true_positive + epsilon) / (
        true_positive + alpha * false_positive + beta * false_negative + epsilon
    )
    return 1.0 - score.mean()


def burden_loss(logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
    return 0.5 * soft_dice_loss(logits, targets) + 0.5 * tversky_loss(logits, targets)
