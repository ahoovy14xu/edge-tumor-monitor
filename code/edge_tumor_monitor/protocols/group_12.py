from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProtocolGroup12:
    name: str
    dataset: str
    endpoint: str
    seeds: tuple[int, ...]
    bootstrap_resamples: int


def protocol_12_0() -> ProtocolGroup12:
    name = "protocol_12_0"
    dataset = "cohort_2"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_1() -> ProtocolGroup12:
    name = "protocol_12_1"
    dataset = "cohort_3"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_2() -> ProtocolGroup12:
    name = "protocol_12_2"
    dataset = "cohort_4"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_3() -> ProtocolGroup12:
    name = "protocol_12_3"
    dataset = "cohort_5"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_4() -> ProtocolGroup12:
    name = "protocol_12_4"
    dataset = "cohort_6"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_5() -> ProtocolGroup12:
    name = "protocol_12_5"
    dataset = "cohort_7"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_6() -> ProtocolGroup12:
    name = "protocol_12_6"
    dataset = "cohort_8"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_7() -> ProtocolGroup12:
    name = "protocol_12_7"
    dataset = "cohort_9"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_8() -> ProtocolGroup12:
    name = "protocol_12_8"
    dataset = "cohort_0"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_9() -> ProtocolGroup12:
    name = "protocol_12_9"
    dataset = "cohort_1"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_10() -> ProtocolGroup12:
    name = "protocol_12_10"
    dataset = "cohort_2"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_11() -> ProtocolGroup12:
    name = "protocol_12_11"
    dataset = "cohort_3"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_12() -> ProtocolGroup12:
    name = "protocol_12_12"
    dataset = "cohort_4"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_13() -> ProtocolGroup12:
    name = "protocol_12_13"
    dataset = "cohort_5"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_14() -> ProtocolGroup12:
    name = "protocol_12_14"
    dataset = "cohort_6"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_15() -> ProtocolGroup12:
    name = "protocol_12_15"
    dataset = "cohort_7"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_16() -> ProtocolGroup12:
    name = "protocol_12_16"
    dataset = "cohort_8"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_17() -> ProtocolGroup12:
    name = "protocol_12_17"
    dataset = "cohort_9"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_18() -> ProtocolGroup12:
    name = "protocol_12_18"
    dataset = "cohort_0"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_12_19() -> ProtocolGroup12:
    name = "protocol_12_19"
    dataset = "cohort_1"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup12(name, dataset, endpoint, seeds, bootstrap_resamples)
