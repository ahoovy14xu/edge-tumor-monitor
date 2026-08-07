from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ConformalSet:
    include_negative: np.ndarray
    include_positive: np.ndarray
    threshold: float


def calibration_threshold(
    labels: np.ndarray, probabilities: np.ndarray, coverage: float = 0.9
) -> float:
    correct_probabilities = np.where(labels == 1, probabilities, 1.0 - probabilities)
    scores = 1.0 - correct_probabilities
    level = min(1.0, np.ceil((len(scores) + 1) * coverage) / len(scores))
    return float(np.quantile(scores, level, method="higher"))


def prediction_sets(probabilities: np.ndarray, threshold: float) -> ConformalSet:
    include_negative = probabilities <= threshold
    include_positive = probabilities >= 1.0 - threshold
    return ConformalSet(include_negative, include_positive, threshold)


def empirical_coverage(sets: ConformalSet, labels: np.ndarray) -> float:
    covered = np.where(labels == 1, sets.include_positive, sets.include_negative)
    return float(np.mean(covered))
