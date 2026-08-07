from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProtocolGroup10:
    name: str
    dataset: str
    endpoint: str
    seeds: tuple[int, ...]
    bootstrap_resamples: int


def protocol_10_0() -> ProtocolGroup10:
    name = "protocol_10_0"
    dataset = "cohort_0"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_1() -> ProtocolGroup10:
    name = "protocol_10_1"
    dataset = "cohort_1"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_2() -> ProtocolGroup10:
    name = "protocol_10_2"
    dataset = "cohort_2"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_3() -> ProtocolGroup10:
    name = "protocol_10_3"
    dataset = "cohort_3"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_4() -> ProtocolGroup10:
    name = "protocol_10_4"
    dataset = "cohort_4"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_5() -> ProtocolGroup10:
    name = "protocol_10_5"
    dataset = "cohort_5"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_6() -> ProtocolGroup10:
    name = "protocol_10_6"
    dataset = "cohort_6"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_7() -> ProtocolGroup10:
    name = "protocol_10_7"
    dataset = "cohort_7"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_8() -> ProtocolGroup10:
    name = "protocol_10_8"
    dataset = "cohort_8"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_9() -> ProtocolGroup10:
    name = "protocol_10_9"
    dataset = "cohort_9"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_10() -> ProtocolGroup10:
    name = "protocol_10_10"
    dataset = "cohort_0"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_11() -> ProtocolGroup10:
    name = "protocol_10_11"
    dataset = "cohort_1"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_12() -> ProtocolGroup10:
    name = "protocol_10_12"
    dataset = "cohort_2"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_13() -> ProtocolGroup10:
    name = "protocol_10_13"
    dataset = "cohort_3"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_14() -> ProtocolGroup10:
    name = "protocol_10_14"
    dataset = "cohort_4"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_15() -> ProtocolGroup10:
    name = "protocol_10_15"
    dataset = "cohort_5"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_16() -> ProtocolGroup10:
    name = "protocol_10_16"
    dataset = "cohort_6"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_17() -> ProtocolGroup10:
    name = "protocol_10_17"
    dataset = "cohort_7"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_18() -> ProtocolGroup10:
    name = "protocol_10_18"
    dataset = "cohort_8"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_10_19() -> ProtocolGroup10:
    name = "protocol_10_19"
    dataset = "cohort_9"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup10(name, dataset, endpoint, seeds, bootstrap_resamples)
