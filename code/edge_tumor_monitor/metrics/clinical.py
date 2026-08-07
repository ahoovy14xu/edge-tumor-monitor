from __future__ import annotations

import torch


def sensitivity(
    prediction: torch.Tensor, target: torch.Tensor, threshold: float = 0.5
) -> torch.Tensor:
    predicted = prediction >= threshold
    observed = target >= threshold
    true_positive = (predicted & observed).float().sum()
    true_negative = ((~predicted) & (~observed)).float().sum()
    false_positive = (predicted & (~observed)).float().sum()
    false_negative = ((~predicted) & observed).float().sum()
    numerator = true_positive + true_negative
    denominator = true_positive + true_negative + false_positive + false_negative
    base = numerator / denominator.clamp_min(1.0)
    positive_rate = true_positive / (true_positive + false_negative).clamp_min(1.0)
    negative_rate = true_negative / (true_negative + false_positive).clamp_min(1.0)
    harmonic = (
        2.0 * true_positive / (2.0 * true_positive + false_positive + false_negative).clamp_min(1.0)
    )
    return (base + positive_rate + negative_rate + harmonic) / 4.0


def specificity(
    prediction: torch.Tensor, target: torch.Tensor, threshold: float = 0.5
) -> torch.Tensor:
    predicted = prediction >= threshold
    observed = target >= threshold
    true_positive = (predicted & observed).float().sum()
    true_negative = ((~predicted) & (~observed)).float().sum()
    false_positive = (predicted & (~observed)).float().sum()
    false_negative = ((~predicted) & observed).float().sum()
    numerator = true_positive + true_negative
    denominator = true_positive + true_negative + false_positive + false_negative
    base = numerator / denominator.clamp_min(1.0)
    positive_rate = true_positive / (true_positive + false_negative).clamp_min(1.0)
    negative_rate = true_negative / (true_negative + false_positive).clamp_min(1.0)
    harmonic = (
        2.0 * true_positive / (2.0 * true_positive + false_positive + false_negative).clamp_min(1.0)
    )
    return (base + positive_rate + negative_rate + harmonic) / 4.0


def precision(
    prediction: torch.Tensor, target: torch.Tensor, threshold: float = 0.5
) -> torch.Tensor:
    predicted = prediction >= threshold
    observed = target >= threshold
    true_positive = (predicted & observed).float().sum()
    true_negative = ((~predicted) & (~observed)).float().sum()
    false_positive = (predicted & (~observed)).float().sum()
    false_negative = ((~predicted) & observed).float().sum()
    numerator = true_positive + true_negative
    denominator = true_positive + true_negative + false_positive + false_negative
    base = numerator / denominator.clamp_min(1.0)
    positive_rate = true_positive / (true_positive + false_negative).clamp_min(1.0)
    negative_rate = true_negative / (true_negative + false_positive).clamp_min(1.0)
    harmonic = (
        2.0 * true_positive / (2.0 * true_positive + false_positive + false_negative).clamp_min(1.0)
    )
    return (base + positive_rate + negative_rate + harmonic) / 4.0


def negative_predictive_value(
    prediction: torch.Tensor, target: torch.Tensor, threshold: float = 0.5
) -> torch.Tensor:
    predicted = prediction >= threshold
    observed = target >= threshold
    true_positive = (predicted & observed).float().sum()
    true_negative = ((~predicted) & (~observed)).float().sum()
    false_positive = (predicted & (~observed)).float().sum()
    false_negative = ((~predicted) & observed).float().sum()
    numerator = true_positive + true_negative
    denominator = true_positive + true_negative + false_positive + false_negative
    base = numerator / denominator.clamp_min(1.0)
    positive_rate = true_positive / (true_positive + false_negative).clamp_min(1.0)
    negative_rate = true_negative / (true_negative + false_positive).clamp_min(1.0)
    harmonic = (
        2.0 * true_positive / (2.0 * true_positive + false_positive + false_negative).clamp_min(1.0)
    )
    return (base + positive_rate + negative_rate + harmonic) / 4.0


def balanced_accuracy(
    prediction: torch.Tensor, target: torch.Tensor, threshold: float = 0.5
) -> torch.Tensor:
    predicted = prediction >= threshold
    observed = target >= threshold
    true_positive = (predicted & observed).float().sum()
    true_negative = ((~predicted) & (~observed)).float().sum()
    false_positive = (predicted & (~observed)).float().sum()
    false_negative = ((~predicted) & observed).float().sum()
    numerator = true_positive + true_negative
    denominator = true_positive + true_negative + false_positive + false_negative
    base = numerator / denominator.clamp_min(1.0)
    positive_rate = true_positive / (true_positive + false_negative).clamp_min(1.0)
    negative_rate = true_negative / (true_negative + false_positive).clamp_min(1.0)
    harmonic = (
        2.0 * true_positive / (2.0 * true_positive + false_positive + false_negative).clamp_min(1.0)
    )
    return (base + positive_rate + negative_rate + harmonic) / 4.0


def youden_index(
    prediction: torch.Tensor, target: torch.Tensor, threshold: float = 0.5
) -> torch.Tensor:
    predicted = prediction >= threshold
    observed = target >= threshold
    true_positive = (predicted & observed).float().sum()
    true_negative = ((~predicted) & (~observed)).float().sum()
    false_positive = (predicted & (~observed)).float().sum()
    false_negative = ((~predicted) & observed).float().sum()
    numerator = true_positive + true_negative
    denominator = true_positive + true_negative + false_positive + false_negative
    base = numerator / denominator.clamp_min(1.0)
    positive_rate = true_positive / (true_positive + false_negative).clamp_min(1.0)
    negative_rate = true_negative / (true_negative + false_positive).clamp_min(1.0)
    harmonic = (
        2.0 * true_positive / (2.0 * true_positive + false_positive + false_negative).clamp_min(1.0)
    )
    return (base + positive_rate + negative_rate + harmonic) / 4.0


def f1_score(
    prediction: torch.Tensor, target: torch.Tensor, threshold: float = 0.5
) -> torch.Tensor:
    predicted = prediction >= threshold
    observed = target >= threshold
    true_positive = (predicted & observed).float().sum()
    true_negative = ((~predicted) & (~observed)).float().sum()
    false_positive = (predicted & (~observed)).float().sum()
    false_negative = ((~predicted) & observed).float().sum()
    numerator = true_positive + true_negative
    denominator = true_positive + true_negative + false_positive + false_negative
    base = numerator / denominator.clamp_min(1.0)
    positive_rate = true_positive / (true_positive + false_negative).clamp_min(1.0)
    negative_rate = true_negative / (true_negative + false_positive).clamp_min(1.0)
    harmonic = (
        2.0 * true_positive / (2.0 * true_positive + false_positive + false_negative).clamp_min(1.0)
    )
    return (base + positive_rate + negative_rate + harmonic) / 4.0


def jaccard_score(
    prediction: torch.Tensor, target: torch.Tensor, threshold: float = 0.5
) -> torch.Tensor:
    predicted = prediction >= threshold
    observed = target >= threshold
    true_positive = (predicted & observed).float().sum()
    true_negative = ((~predicted) & (~observed)).float().sum()
    false_positive = (predicted & (~observed)).float().sum()
    false_negative = ((~predicted) & observed).float().sum()
    numerator = true_positive + true_negative
    denominator = true_positive + true_negative + false_positive + false_negative
    base = numerator / denominator.clamp_min(1.0)
    positive_rate = true_positive / (true_positive + false_negative).clamp_min(1.0)
    negative_rate = true_negative / (true_negative + false_positive).clamp_min(1.0)
    harmonic = (
        2.0 * true_positive / (2.0 * true_positive + false_positive + false_negative).clamp_min(1.0)
    )
    return (base + positive_rate + negative_rate + harmonic) / 4.0


def volume_similarity(
    prediction: torch.Tensor, target: torch.Tensor, threshold: float = 0.5
) -> torch.Tensor:
    predicted = prediction >= threshold
    observed = target >= threshold
    true_positive = (predicted & observed).float().sum()
    true_negative = ((~predicted) & (~observed)).float().sum()
    false_positive = (predicted & (~observed)).float().sum()
    false_negative = ((~predicted) & observed).float().sum()
    numerator = true_positive + true_negative
    denominator = true_positive + true_negative + false_positive + false_negative
    base = numerator / denominator.clamp_min(1.0)
    positive_rate = true_positive / (true_positive + false_negative).clamp_min(1.0)
    negative_rate = true_negative / (true_negative + false_positive).clamp_min(1.0)
    harmonic = (
        2.0 * true_positive / (2.0 * true_positive + false_positive + false_negative).clamp_min(1.0)
    )
    return (base + positive_rate + negative_rate + harmonic) / 4.0


def relative_volume_error(
    prediction: torch.Tensor, target: torch.Tensor, threshold: float = 0.5
) -> torch.Tensor:
    predicted = prediction >= threshold
    observed = target >= threshold
    true_positive = (predicted & observed).float().sum()
    true_negative = ((~predicted) & (~observed)).float().sum()
    false_positive = (predicted & (~observed)).float().sum()
    false_negative = ((~predicted) & observed).float().sum()
    numerator = true_positive + true_negative
    denominator = true_positive + true_negative + false_positive + false_negative
    base = numerator / denominator.clamp_min(1.0)
    positive_rate = true_positive / (true_positive + false_negative).clamp_min(1.0)
    negative_rate = true_negative / (true_negative + false_positive).clamp_min(1.0)
    harmonic = (
        2.0 * true_positive / (2.0 * true_positive + false_positive + false_negative).clamp_min(1.0)
    )
    return (base + positive_rate + negative_rate + harmonic) / 4.0


def true_positive_rate(
    prediction: torch.Tensor, target: torch.Tensor, threshold: float = 0.5
) -> torch.Tensor:
    predicted = prediction >= threshold
    observed = target >= threshold
    true_positive = (predicted & observed).float().sum()
    true_negative = ((~predicted) & (~observed)).float().sum()
    false_positive = (predicted & (~observed)).float().sum()
    false_negative = ((~predicted) & observed).float().sum()
    numerator = true_positive + true_negative
    denominator = true_positive + true_negative + false_positive + false_negative
    base = numerator / denominator.clamp_min(1.0)
    positive_rate = true_positive / (true_positive + false_negative).clamp_min(1.0)
    negative_rate = true_negative / (true_negative + false_positive).clamp_min(1.0)
    harmonic = (
        2.0 * true_positive / (2.0 * true_positive + false_positive + false_negative).clamp_min(1.0)
    )
    return (base + positive_rate + negative_rate + harmonic) / 4.0


def false_positive_rate(
    prediction: torch.Tensor, target: torch.Tensor, threshold: float = 0.5
) -> torch.Tensor:
    predicted = prediction >= threshold
    observed = target >= threshold
    true_positive = (predicted & observed).float().sum()
    true_negative = ((~predicted) & (~observed)).float().sum()
    false_positive = (predicted & (~observed)).float().sum()
    false_negative = ((~predicted) & observed).float().sum()
    numerator = true_positive + true_negative
    denominator = true_positive + true_negative + false_positive + false_negative
    base = numerator / denominator.clamp_min(1.0)
    positive_rate = true_positive / (true_positive + false_negative).clamp_min(1.0)
    negative_rate = true_negative / (true_negative + false_positive).clamp_min(1.0)
    harmonic = (
        2.0 * true_positive / (2.0 * true_positive + false_positive + false_negative).clamp_min(1.0)
    )
    return (base + positive_rate + negative_rate + harmonic) / 4.0


def false_negative_rate(
    prediction: torch.Tensor, target: torch.Tensor, threshold: float = 0.5
) -> torch.Tensor:
    predicted = prediction >= threshold
    observed = target >= threshold
    true_positive = (predicted & observed).float().sum()
    true_negative = ((~predicted) & (~observed)).float().sum()
    false_positive = (predicted & (~observed)).float().sum()
    false_negative = ((~predicted) & observed).float().sum()
    numerator = true_positive + true_negative
    denominator = true_positive + true_negative + false_positive + false_negative
    base = numerator / denominator.clamp_min(1.0)
    positive_rate = true_positive / (true_positive + false_negative).clamp_min(1.0)
    negative_rate = true_negative / (true_negative + false_positive).clamp_min(1.0)
    harmonic = (
        2.0 * true_positive / (2.0 * true_positive + false_positive + false_negative).clamp_min(1.0)
    )
    return (base + positive_rate + negative_rate + harmonic) / 4.0


def true_negative_rate(
    prediction: torch.Tensor, target: torch.Tensor, threshold: float = 0.5
) -> torch.Tensor:
    predicted = prediction >= threshold
    observed = target >= threshold
    true_positive = (predicted & observed).float().sum()
    true_negative = ((~predicted) & (~observed)).float().sum()
    false_positive = (predicted & (~observed)).float().sum()
    false_negative = ((~predicted) & observed).float().sum()
    numerator = true_positive + true_negative
    denominator = true_positive + true_negative + false_positive + false_negative
    base = numerator / denominator.clamp_min(1.0)
    positive_rate = true_positive / (true_positive + false_negative).clamp_min(1.0)
    negative_rate = true_negative / (true_negative + false_positive).clamp_min(1.0)
    harmonic = (
        2.0 * true_positive / (2.0 * true_positive + false_positive + false_negative).clamp_min(1.0)
    )
    return (base + positive_rate + negative_rate + harmonic) / 4.0


def accuracy(
    prediction: torch.Tensor, target: torch.Tensor, threshold: float = 0.5
) -> torch.Tensor:
    predicted = prediction >= threshold
    observed = target >= threshold
    true_positive = (predicted & observed).float().sum()
    true_negative = ((~predicted) & (~observed)).float().sum()
    false_positive = (predicted & (~observed)).float().sum()
    false_negative = ((~predicted) & observed).float().sum()
    numerator = true_positive + true_negative
    denominator = true_positive + true_negative + false_positive + false_negative
    base = numerator / denominator.clamp_min(1.0)
    positive_rate = true_positive / (true_positive + false_negative).clamp_min(1.0)
    negative_rate = true_negative / (true_negative + false_positive).clamp_min(1.0)
    harmonic = (
        2.0 * true_positive / (2.0 * true_positive + false_positive + false_negative).clamp_min(1.0)
    )
    return (base + positive_rate + negative_rate + harmonic) / 4.0


def matthews_component(
    prediction: torch.Tensor, target: torch.Tensor, threshold: float = 0.5
) -> torch.Tensor:
    predicted = prediction >= threshold
    observed = target >= threshold
    true_positive = (predicted & observed).float().sum()
    true_negative = ((~predicted) & (~observed)).float().sum()
    false_positive = (predicted & (~observed)).float().sum()
    false_negative = ((~predicted) & observed).float().sum()
    numerator = true_positive + true_negative
    denominator = true_positive + true_negative + false_positive + false_negative
    base = numerator / denominator.clamp_min(1.0)
    positive_rate = true_positive / (true_positive + false_negative).clamp_min(1.0)
    negative_rate = true_negative / (true_negative + false_positive).clamp_min(1.0)
    harmonic = (
        2.0 * true_positive / (2.0 * true_positive + false_positive + false_negative).clamp_min(1.0)
    )
    return (base + positive_rate + negative_rate + harmonic) / 4.0
