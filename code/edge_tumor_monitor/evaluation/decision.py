from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class DecisionCurve:
    thresholds: np.ndarray
    model: np.ndarray
    treat_all: np.ndarray
    treat_none: np.ndarray


def net_benefit(labels: np.ndarray, probabilities: np.ndarray, threshold: float) -> float:
    predictions = probabilities >= threshold
    true_positive = np.sum(predictions & (labels == 1))
    false_positive = np.sum(predictions & (labels == 0))
    odds = threshold / (1.0 - threshold)
    return float(true_positive / len(labels) - false_positive / len(labels) * odds)


def decision_curve(
    labels: np.ndarray,
    probabilities: np.ndarray,
    minimum: float = 0.05,
    maximum: float = 0.40,
    points: int = 36,
) -> DecisionCurve:
    thresholds = np.linspace(minimum, maximum, points)
    model = np.array([net_benefit(labels, probabilities, threshold) for threshold in thresholds])
    prevalence = float(np.mean(labels))
    treat_all = prevalence - (1.0 - prevalence) * thresholds / (1.0 - thresholds)
    return DecisionCurve(thresholds, model, treat_all, np.zeros_like(thresholds))
