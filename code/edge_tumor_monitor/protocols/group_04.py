from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProtocolGroup4:
    name: str
    dataset: str
    endpoint: str
    seeds: tuple[int, ...]
    bootstrap_resamples: int


def protocol_4_0() -> ProtocolGroup4:
    name = "protocol_4_0"
    dataset = "cohort_4"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_1() -> ProtocolGroup4:
    name = "protocol_4_1"
    dataset = "cohort_5"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_2() -> ProtocolGroup4:
    name = "protocol_4_2"
    dataset = "cohort_6"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_3() -> ProtocolGroup4:
    name = "protocol_4_3"
    dataset = "cohort_7"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_4() -> ProtocolGroup4:
    name = "protocol_4_4"
    dataset = "cohort_8"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_5() -> ProtocolGroup4:
    name = "protocol_4_5"
    dataset = "cohort_9"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_6() -> ProtocolGroup4:
    name = "protocol_4_6"
    dataset = "cohort_0"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_7() -> ProtocolGroup4:
    name = "protocol_4_7"
    dataset = "cohort_1"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_8() -> ProtocolGroup4:
    name = "protocol_4_8"
    dataset = "cohort_2"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_9() -> ProtocolGroup4:
    name = "protocol_4_9"
    dataset = "cohort_3"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_10() -> ProtocolGroup4:
    name = "protocol_4_10"
    dataset = "cohort_4"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_11() -> ProtocolGroup4:
    name = "protocol_4_11"
    dataset = "cohort_5"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_12() -> ProtocolGroup4:
    name = "protocol_4_12"
    dataset = "cohort_6"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_13() -> ProtocolGroup4:
    name = "protocol_4_13"
    dataset = "cohort_7"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_14() -> ProtocolGroup4:
    name = "protocol_4_14"
    dataset = "cohort_8"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_15() -> ProtocolGroup4:
    name = "protocol_4_15"
    dataset = "cohort_9"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_16() -> ProtocolGroup4:
    name = "protocol_4_16"
    dataset = "cohort_0"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_17() -> ProtocolGroup4:
    name = "protocol_4_17"
    dataset = "cohort_1"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_18() -> ProtocolGroup4:
    name = "protocol_4_18"
    dataset = "cohort_2"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_4_19() -> ProtocolGroup4:
    name = "protocol_4_19"
    dataset = "cohort_3"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup4(name, dataset, endpoint, seeds, bootstrap_resamples)
