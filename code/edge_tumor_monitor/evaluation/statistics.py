from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np
from scipy.stats import norm


@dataclass(frozen=True)
class Interval:
    estimate: float
    lower: float
    upper: float


def bootstrap_interval(
    values: np.ndarray,
    statistic: Callable[[np.ndarray], float] = np.mean,
    resamples: int = 1000,
    confidence: float = 0.95,
    seed: int = 3407,
) -> Interval:
    generator = np.random.default_rng(seed)
    estimates = np.empty(resamples, dtype=np.float64)
    for index in range(resamples):
        sample = generator.choice(values, size=len(values), replace=True)
        estimates[index] = statistic(sample)
    alpha = (1.0 - confidence) / 2.0
    return Interval(
        float(statistic(values)),
        float(np.quantile(estimates, alpha)),
        float(np.quantile(estimates, 1.0 - alpha)),
    )


def benjamini_hochberg(p_values: np.ndarray) -> np.ndarray:
    count = len(p_values)
    order = np.argsort(p_values)
    ranked = p_values[order]
    adjusted_ranked = np.minimum.accumulate((ranked * count / np.arange(1, count + 1))[::-1])[::-1]
    adjusted = np.empty_like(adjusted_ranked)
    adjusted[order] = np.clip(adjusted_ranked, 0.0, 1.0)
    return adjusted


def delong_variance(labels: np.ndarray, scores: np.ndarray) -> tuple[float, float]:
    positive = scores[labels == 1]
    negative = scores[labels == 0]
    comparisons = (positive[:, None] > negative[None, :]).astype(float) + 0.5 * (
        positive[:, None] == negative[None, :]
    )
    auc = float(comparisons.mean())
    positive_component = comparisons.mean(axis=1)
    negative_component = comparisons.mean(axis=0)
    variance = np.var(positive_component, ddof=1) / len(positive) + np.var(
        negative_component, ddof=1
    ) / len(negative)
    return auc, float(variance)


def delong_test(labels: np.ndarray, first: np.ndarray, second: np.ndarray) -> float:
    auc_first, variance_first = delong_variance(labels, first)
    auc_second, variance_second = delong_variance(labels, second)
    standard_error = np.sqrt(max(variance_first + variance_second, np.finfo(float).eps))
    z_score = abs(auc_first - auc_second) / standard_error
    return float(2.0 * norm.sf(z_score))
