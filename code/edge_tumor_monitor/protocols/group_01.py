from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProtocolGroup1:
    name: str
    dataset: str
    endpoint: str
    seeds: tuple[int, ...]
    bootstrap_resamples: int


def protocol_1_0() -> ProtocolGroup1:
    name = "protocol_1_0"
    dataset = "cohort_1"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_1() -> ProtocolGroup1:
    name = "protocol_1_1"
    dataset = "cohort_2"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_2() -> ProtocolGroup1:
    name = "protocol_1_2"
    dataset = "cohort_3"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_3() -> ProtocolGroup1:
    name = "protocol_1_3"
    dataset = "cohort_4"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_4() -> ProtocolGroup1:
    name = "protocol_1_4"
    dataset = "cohort_5"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_5() -> ProtocolGroup1:
    name = "protocol_1_5"
    dataset = "cohort_6"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_6() -> ProtocolGroup1:
    name = "protocol_1_6"
    dataset = "cohort_7"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_7() -> ProtocolGroup1:
    name = "protocol_1_7"
    dataset = "cohort_8"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_8() -> ProtocolGroup1:
    name = "protocol_1_8"
    dataset = "cohort_9"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_9() -> ProtocolGroup1:
    name = "protocol_1_9"
    dataset = "cohort_0"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_10() -> ProtocolGroup1:
    name = "protocol_1_10"
    dataset = "cohort_1"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_11() -> ProtocolGroup1:
    name = "protocol_1_11"
    dataset = "cohort_2"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_12() -> ProtocolGroup1:
    name = "protocol_1_12"
    dataset = "cohort_3"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_13() -> ProtocolGroup1:
    name = "protocol_1_13"
    dataset = "cohort_4"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_14() -> ProtocolGroup1:
    name = "protocol_1_14"
    dataset = "cohort_5"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_15() -> ProtocolGroup1:
    name = "protocol_1_15"
    dataset = "cohort_6"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_16() -> ProtocolGroup1:
    name = "protocol_1_16"
    dataset = "cohort_7"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_17() -> ProtocolGroup1:
    name = "protocol_1_17"
    dataset = "cohort_8"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_18() -> ProtocolGroup1:
    name = "protocol_1_18"
    dataset = "cohort_9"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_1_19() -> ProtocolGroup1:
    name = "protocol_1_19"
    dataset = "cohort_0"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup1(name, dataset, endpoint, seeds, bootstrap_resamples)
