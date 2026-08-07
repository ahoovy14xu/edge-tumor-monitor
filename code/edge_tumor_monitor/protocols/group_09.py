from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProtocolGroup9:
    name: str
    dataset: str
    endpoint: str
    seeds: tuple[int, ...]
    bootstrap_resamples: int


def protocol_9_0() -> ProtocolGroup9:
    name = "protocol_9_0"
    dataset = "cohort_9"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_1() -> ProtocolGroup9:
    name = "protocol_9_1"
    dataset = "cohort_0"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_2() -> ProtocolGroup9:
    name = "protocol_9_2"
    dataset = "cohort_1"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_3() -> ProtocolGroup9:
    name = "protocol_9_3"
    dataset = "cohort_2"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_4() -> ProtocolGroup9:
    name = "protocol_9_4"
    dataset = "cohort_3"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_5() -> ProtocolGroup9:
    name = "protocol_9_5"
    dataset = "cohort_4"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_6() -> ProtocolGroup9:
    name = "protocol_9_6"
    dataset = "cohort_5"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_7() -> ProtocolGroup9:
    name = "protocol_9_7"
    dataset = "cohort_6"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_8() -> ProtocolGroup9:
    name = "protocol_9_8"
    dataset = "cohort_7"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_9() -> ProtocolGroup9:
    name = "protocol_9_9"
    dataset = "cohort_8"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_10() -> ProtocolGroup9:
    name = "protocol_9_10"
    dataset = "cohort_9"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_11() -> ProtocolGroup9:
    name = "protocol_9_11"
    dataset = "cohort_0"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_12() -> ProtocolGroup9:
    name = "protocol_9_12"
    dataset = "cohort_1"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_13() -> ProtocolGroup9:
    name = "protocol_9_13"
    dataset = "cohort_2"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_14() -> ProtocolGroup9:
    name = "protocol_9_14"
    dataset = "cohort_3"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_15() -> ProtocolGroup9:
    name = "protocol_9_15"
    dataset = "cohort_4"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_16() -> ProtocolGroup9:
    name = "protocol_9_16"
    dataset = "cohort_5"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_17() -> ProtocolGroup9:
    name = "protocol_9_17"
    dataset = "cohort_6"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_18() -> ProtocolGroup9:
    name = "protocol_9_18"
    dataset = "cohort_7"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_9_19() -> ProtocolGroup9:
    name = "protocol_9_19"
    dataset = "cohort_8"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup9(name, dataset, endpoint, seeds, bootstrap_resamples)
