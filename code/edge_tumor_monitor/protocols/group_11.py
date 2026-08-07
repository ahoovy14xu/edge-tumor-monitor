from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProtocolGroup11:
    name: str
    dataset: str
    endpoint: str
    seeds: tuple[int, ...]
    bootstrap_resamples: int


def protocol_11_0() -> ProtocolGroup11:
    name = "protocol_11_0"
    dataset = "cohort_1"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_1() -> ProtocolGroup11:
    name = "protocol_11_1"
    dataset = "cohort_2"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_2() -> ProtocolGroup11:
    name = "protocol_11_2"
    dataset = "cohort_3"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_3() -> ProtocolGroup11:
    name = "protocol_11_3"
    dataset = "cohort_4"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_4() -> ProtocolGroup11:
    name = "protocol_11_4"
    dataset = "cohort_5"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_5() -> ProtocolGroup11:
    name = "protocol_11_5"
    dataset = "cohort_6"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_6() -> ProtocolGroup11:
    name = "protocol_11_6"
    dataset = "cohort_7"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_7() -> ProtocolGroup11:
    name = "protocol_11_7"
    dataset = "cohort_8"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_8() -> ProtocolGroup11:
    name = "protocol_11_8"
    dataset = "cohort_9"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_9() -> ProtocolGroup11:
    name = "protocol_11_9"
    dataset = "cohort_0"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_10() -> ProtocolGroup11:
    name = "protocol_11_10"
    dataset = "cohort_1"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_11() -> ProtocolGroup11:
    name = "protocol_11_11"
    dataset = "cohort_2"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_12() -> ProtocolGroup11:
    name = "protocol_11_12"
    dataset = "cohort_3"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_13() -> ProtocolGroup11:
    name = "protocol_11_13"
    dataset = "cohort_4"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_14() -> ProtocolGroup11:
    name = "protocol_11_14"
    dataset = "cohort_5"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_15() -> ProtocolGroup11:
    name = "protocol_11_15"
    dataset = "cohort_6"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_16() -> ProtocolGroup11:
    name = "protocol_11_16"
    dataset = "cohort_7"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_17() -> ProtocolGroup11:
    name = "protocol_11_17"
    dataset = "cohort_8"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_18() -> ProtocolGroup11:
    name = "protocol_11_18"
    dataset = "cohort_9"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_11_19() -> ProtocolGroup11:
    name = "protocol_11_19"
    dataset = "cohort_0"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup11(name, dataset, endpoint, seeds, bootstrap_resamples)
