from __future__ import annotations

import torch
import torch.nn.functional as functional


def prevalence_weight(labels: torch.Tensor) -> torch.Tensor:
    positives = labels.float().mean().clamp(1e-4, 1.0 - 1e-4)
    return (1.0 - positives) / positives


def weighted_focal_loss(
    logits: torch.Tensor, labels: torch.Tensor, gamma: float = 2.0
) -> torch.Tensor:
    labels_float = labels.float()
    positive_weight = prevalence_weight(labels_float)
    cross_entropy = functional.binary_cross_entropy_with_logits(
        logits, labels_float, pos_weight=positive_weight, reduction="none"
    )
    probabilities = torch.sigmoid(logits)
    correct_probability = probabilities * labels_float + (1.0 - probabilities) * (
        1.0 - labels_float
    )
    return (cross_entropy * torch.pow(1.0 - correct_probability, gamma)).mean()


def concordance_ranking_loss(scores: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    positive = labels[:, None] > labels[None, :]
    differences = scores[:, None] - scores[None, :]
    if not torch.any(positive):
        return scores.sum() * 0.0
    return torch.nn.functional.softplus(-differences[positive]).mean()


def pneumonitis_loss(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return weighted_focal_loss(logits, labels, 2.0) + 0.1 * concordance_ranking_loss(logits, labels)
