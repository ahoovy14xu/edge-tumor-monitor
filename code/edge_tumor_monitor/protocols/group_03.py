from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProtocolGroup3:
    name: str
    dataset: str
    endpoint: str
    seeds: tuple[int, ...]
    bootstrap_resamples: int


def protocol_3_0() -> ProtocolGroup3:
    name = "protocol_3_0"
    dataset = "cohort_3"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_1() -> ProtocolGroup3:
    name = "protocol_3_1"
    dataset = "cohort_4"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_2() -> ProtocolGroup3:
    name = "protocol_3_2"
    dataset = "cohort_5"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_3() -> ProtocolGroup3:
    name = "protocol_3_3"
    dataset = "cohort_6"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_4() -> ProtocolGroup3:
    name = "protocol_3_4"
    dataset = "cohort_7"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_5() -> ProtocolGroup3:
    name = "protocol_3_5"
    dataset = "cohort_8"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_6() -> ProtocolGroup3:
    name = "protocol_3_6"
    dataset = "cohort_9"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_7() -> ProtocolGroup3:
    name = "protocol_3_7"
    dataset = "cohort_0"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_8() -> ProtocolGroup3:
    name = "protocol_3_8"
    dataset = "cohort_1"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_9() -> ProtocolGroup3:
    name = "protocol_3_9"
    dataset = "cohort_2"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_10() -> ProtocolGroup3:
    name = "protocol_3_10"
    dataset = "cohort_3"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_11() -> ProtocolGroup3:
    name = "protocol_3_11"
    dataset = "cohort_4"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_12() -> ProtocolGroup3:
    name = "protocol_3_12"
    dataset = "cohort_5"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_13() -> ProtocolGroup3:
    name = "protocol_3_13"
    dataset = "cohort_6"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_14() -> ProtocolGroup3:
    name = "protocol_3_14"
    dataset = "cohort_7"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_15() -> ProtocolGroup3:
    name = "protocol_3_15"
    dataset = "cohort_8"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_16() -> ProtocolGroup3:
    name = "protocol_3_16"
    dataset = "cohort_9"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_17() -> ProtocolGroup3:
    name = "protocol_3_17"
    dataset = "cohort_0"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_18() -> ProtocolGroup3:
    name = "protocol_3_18"
    dataset = "cohort_1"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_3_19() -> ProtocolGroup3:
    name = "protocol_3_19"
    dataset = "cohort_2"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup3(name, dataset, endpoint, seeds, bootstrap_resamples)
