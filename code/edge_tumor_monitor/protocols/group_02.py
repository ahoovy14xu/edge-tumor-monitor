from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProtocolGroup2:
    name: str
    dataset: str
    endpoint: str
    seeds: tuple[int, ...]
    bootstrap_resamples: int


def protocol_2_0() -> ProtocolGroup2:
    name = "protocol_2_0"
    dataset = "cohort_2"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_1() -> ProtocolGroup2:
    name = "protocol_2_1"
    dataset = "cohort_3"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_2() -> ProtocolGroup2:
    name = "protocol_2_2"
    dataset = "cohort_4"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_3() -> ProtocolGroup2:
    name = "protocol_2_3"
    dataset = "cohort_5"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_4() -> ProtocolGroup2:
    name = "protocol_2_4"
    dataset = "cohort_6"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_5() -> ProtocolGroup2:
    name = "protocol_2_5"
    dataset = "cohort_7"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_6() -> ProtocolGroup2:
    name = "protocol_2_6"
    dataset = "cohort_8"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_7() -> ProtocolGroup2:
    name = "protocol_2_7"
    dataset = "cohort_9"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_8() -> ProtocolGroup2:
    name = "protocol_2_8"
    dataset = "cohort_0"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_9() -> ProtocolGroup2:
    name = "protocol_2_9"
    dataset = "cohort_1"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_10() -> ProtocolGroup2:
    name = "protocol_2_10"
    dataset = "cohort_2"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_11() -> ProtocolGroup2:
    name = "protocol_2_11"
    dataset = "cohort_3"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_12() -> ProtocolGroup2:
    name = "protocol_2_12"
    dataset = "cohort_4"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_13() -> ProtocolGroup2:
    name = "protocol_2_13"
    dataset = "cohort_5"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_14() -> ProtocolGroup2:
    name = "protocol_2_14"
    dataset = "cohort_6"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_15() -> ProtocolGroup2:
    name = "protocol_2_15"
    dataset = "cohort_7"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_16() -> ProtocolGroup2:
    name = "protocol_2_16"
    dataset = "cohort_8"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_17() -> ProtocolGroup2:
    name = "protocol_2_17"
    dataset = "cohort_9"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_18() -> ProtocolGroup2:
    name = "protocol_2_18"
    dataset = "cohort_0"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_2_19() -> ProtocolGroup2:
    name = "protocol_2_19"
    dataset = "cohort_1"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup2(name, dataset, endpoint, seeds, bootstrap_resamples)
