import numpy as np

from edge_tumor_monitor.evaluation.conformal import (
    calibration_threshold,
    empirical_coverage,
    prediction_sets,
)
from edge_tumor_monitor.evaluation.decision import decision_curve
from edge_tumor_monitor.evaluation.statistics import benjamini_hochberg, bootstrap_interval


def test_adjustment_and_interval() -> None:
    adjusted = benjamini_hochberg(np.array([0.01, 0.04, 0.03]))
    assert np.all(adjusted >= np.array([0.01, 0.04, 0.03]))
    interval = bootstrap_interval(np.arange(10.0), resamples=100, seed=2)
    assert interval.lower <= interval.estimate <= interval.upper


def test_conformal_and_decision_curve() -> None:
    labels = np.array([0, 0, 1, 1, 1, 0, 1, 0, 1, 0])
    probabilities = np.array([0.1, 0.2, 0.8, 0.9, 0.7, 0.3, 0.6, 0.4, 0.75, 0.25])
    threshold = calibration_threshold(labels, probabilities)
    sets = prediction_sets(probabilities, threshold)
    assert empirical_coverage(sets, labels) >= 0.8
    curve = decision_curve(labels, probabilities)
    assert curve.thresholds.shape == curve.model.shape
