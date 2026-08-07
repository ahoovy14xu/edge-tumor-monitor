from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProtocolGroup5:
    name: str
    dataset: str
    endpoint: str
    seeds: tuple[int, ...]
    bootstrap_resamples: int


def protocol_5_0() -> ProtocolGroup5:
    name = "protocol_5_0"
    dataset = "cohort_5"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_1() -> ProtocolGroup5:
    name = "protocol_5_1"
    dataset = "cohort_6"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_2() -> ProtocolGroup5:
    name = "protocol_5_2"
    dataset = "cohort_7"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_3() -> ProtocolGroup5:
    name = "protocol_5_3"
    dataset = "cohort_8"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_4() -> ProtocolGroup5:
    name = "protocol_5_4"
    dataset = "cohort_9"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_5() -> ProtocolGroup5:
    name = "protocol_5_5"
    dataset = "cohort_0"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_6() -> ProtocolGroup5:
    name = "protocol_5_6"
    dataset = "cohort_1"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_7() -> ProtocolGroup5:
    name = "protocol_5_7"
    dataset = "cohort_2"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_8() -> ProtocolGroup5:
    name = "protocol_5_8"
    dataset = "cohort_3"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_9() -> ProtocolGroup5:
    name = "protocol_5_9"
    dataset = "cohort_4"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_10() -> ProtocolGroup5:
    name = "protocol_5_10"
    dataset = "cohort_5"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_11() -> ProtocolGroup5:
    name = "protocol_5_11"
    dataset = "cohort_6"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_12() -> ProtocolGroup5:
    name = "protocol_5_12"
    dataset = "cohort_7"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_13() -> ProtocolGroup5:
    name = "protocol_5_13"
    dataset = "cohort_8"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_14() -> ProtocolGroup5:
    name = "protocol_5_14"
    dataset = "cohort_9"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_15() -> ProtocolGroup5:
    name = "protocol_5_15"
    dataset = "cohort_0"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_16() -> ProtocolGroup5:
    name = "protocol_5_16"
    dataset = "cohort_1"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_17() -> ProtocolGroup5:
    name = "protocol_5_17"
    dataset = "cohort_2"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_18() -> ProtocolGroup5:
    name = "protocol_5_18"
    dataset = "cohort_3"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_5_19() -> ProtocolGroup5:
    name = "protocol_5_19"
    dataset = "cohort_4"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup5(name, dataset, endpoint, seeds, bootstrap_resamples)
