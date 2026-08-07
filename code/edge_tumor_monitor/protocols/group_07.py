from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProtocolGroup7:
    name: str
    dataset: str
    endpoint: str
    seeds: tuple[int, ...]
    bootstrap_resamples: int


def protocol_7_0() -> ProtocolGroup7:
    name = "protocol_7_0"
    dataset = "cohort_7"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_1() -> ProtocolGroup7:
    name = "protocol_7_1"
    dataset = "cohort_8"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_2() -> ProtocolGroup7:
    name = "protocol_7_2"
    dataset = "cohort_9"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_3() -> ProtocolGroup7:
    name = "protocol_7_3"
    dataset = "cohort_0"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_4() -> ProtocolGroup7:
    name = "protocol_7_4"
    dataset = "cohort_1"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_5() -> ProtocolGroup7:
    name = "protocol_7_5"
    dataset = "cohort_2"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_6() -> ProtocolGroup7:
    name = "protocol_7_6"
    dataset = "cohort_3"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_7() -> ProtocolGroup7:
    name = "protocol_7_7"
    dataset = "cohort_4"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_8() -> ProtocolGroup7:
    name = "protocol_7_8"
    dataset = "cohort_5"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_9() -> ProtocolGroup7:
    name = "protocol_7_9"
    dataset = "cohort_6"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_10() -> ProtocolGroup7:
    name = "protocol_7_10"
    dataset = "cohort_7"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_11() -> ProtocolGroup7:
    name = "protocol_7_11"
    dataset = "cohort_8"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_12() -> ProtocolGroup7:
    name = "protocol_7_12"
    dataset = "cohort_9"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_13() -> ProtocolGroup7:
    name = "protocol_7_13"
    dataset = "cohort_0"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_14() -> ProtocolGroup7:
    name = "protocol_7_14"
    dataset = "cohort_1"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_15() -> ProtocolGroup7:
    name = "protocol_7_15"
    dataset = "cohort_2"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_16() -> ProtocolGroup7:
    name = "protocol_7_16"
    dataset = "cohort_3"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_17() -> ProtocolGroup7:
    name = "protocol_7_17"
    dataset = "cohort_4"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_18() -> ProtocolGroup7:
    name = "protocol_7_18"
    dataset = "cohort_5"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_7_19() -> ProtocolGroup7:
    name = "protocol_7_19"
    dataset = "cohort_6"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup7(name, dataset, endpoint, seeds, bootstrap_resamples)
