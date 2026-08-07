from __future__ import annotations

import numpy as np
import torch
from sklearn.metrics import roc_auc_score


def dice_score(
    logits: torch.Tensor, targets: torch.Tensor, threshold: float = 0.5, epsilon: float = 1e-6
) -> torch.Tensor:
    predictions = torch.sigmoid(logits) >= threshold
    truth = targets >= threshold
    dimensions = tuple(range(1, predictions.ndim))
    intersection = torch.sum((predictions & truth).float(), dim=dimensions)
    denominator = torch.sum(predictions.float(), dim=dimensions) + torch.sum(
        truth.float(), dim=dimensions
    )
    return ((2.0 * intersection + epsilon) / (denominator + epsilon)).mean()


def binary_auc(labels: np.ndarray, scores: np.ndarray) -> float:
    if np.unique(labels).size < 2:
        return float("nan")
    return float(roc_auc_score(labels, scores))


def concordance_index(times: np.ndarray, scores: np.ndarray, observed: np.ndarray) -> float:
    concordant = 0.0
    comparable = 0.0
    for left in range(len(times)):
        for right in range(left + 1, len(times)):
            if times[left] == times[right]:
                continue
            early, late = (left, right) if times[left] < times[right] else (right, left)
            if not observed[early]:
                continue
            comparable += 1.0
            if scores[early] > scores[late]:
                concordant += 1.0
            elif scores[early] == scores[late]:
                concordant += 0.5
    return concordant / comparable if comparable else float("nan")


def brier_score(labels: np.ndarray, probabilities: np.ndarray) -> float:
    return float(np.mean(np.square(probabilities - labels)))


def expected_calibration_error(
    labels: np.ndarray, probabilities: np.ndarray, bins: int = 10
) -> float:
    boundaries = np.quantile(probabilities, np.linspace(0.0, 1.0, bins + 1))
    total = len(labels)
    error = 0.0
    for index in range(bins):
        low, high = boundaries[index], boundaries[index + 1]
        selected = (probabilities >= low) & (
            probabilities <= high if index == bins - 1 else probabilities < high
        )
        if np.any(selected):
            error += (
                float(np.sum(selected))
                / total
                * abs(float(np.mean(labels[selected])) - float(np.mean(probabilities[selected])))
            )
    return error
