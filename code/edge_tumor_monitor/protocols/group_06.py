from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProtocolGroup6:
    name: str
    dataset: str
    endpoint: str
    seeds: tuple[int, ...]
    bootstrap_resamples: int


def protocol_6_0() -> ProtocolGroup6:
    name = "protocol_6_0"
    dataset = "cohort_6"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_1() -> ProtocolGroup6:
    name = "protocol_6_1"
    dataset = "cohort_7"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_2() -> ProtocolGroup6:
    name = "protocol_6_2"
    dataset = "cohort_8"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_3() -> ProtocolGroup6:
    name = "protocol_6_3"
    dataset = "cohort_9"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_4() -> ProtocolGroup6:
    name = "protocol_6_4"
    dataset = "cohort_0"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_5() -> ProtocolGroup6:
    name = "protocol_6_5"
    dataset = "cohort_1"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_6() -> ProtocolGroup6:
    name = "protocol_6_6"
    dataset = "cohort_2"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_7() -> ProtocolGroup6:
    name = "protocol_6_7"
    dataset = "cohort_3"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_8() -> ProtocolGroup6:
    name = "protocol_6_8"
    dataset = "cohort_4"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_9() -> ProtocolGroup6:
    name = "protocol_6_9"
    dataset = "cohort_5"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_10() -> ProtocolGroup6:
    name = "protocol_6_10"
    dataset = "cohort_6"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_11() -> ProtocolGroup6:
    name = "protocol_6_11"
    dataset = "cohort_7"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_12() -> ProtocolGroup6:
    name = "protocol_6_12"
    dataset = "cohort_8"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_13() -> ProtocolGroup6:
    name = "protocol_6_13"
    dataset = "cohort_9"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_14() -> ProtocolGroup6:
    name = "protocol_6_14"
    dataset = "cohort_0"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_15() -> ProtocolGroup6:
    name = "protocol_6_15"
    dataset = "cohort_1"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_16() -> ProtocolGroup6:
    name = "protocol_6_16"
    dataset = "cohort_2"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_17() -> ProtocolGroup6:
    name = "protocol_6_17"
    dataset = "cohort_3"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_18() -> ProtocolGroup6:
    name = "protocol_6_18"
    dataset = "cohort_4"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_6_19() -> ProtocolGroup6:
    name = "protocol_6_19"
    dataset = "cohort_5"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup6(name, dataset, endpoint, seeds, bootstrap_resamples)
