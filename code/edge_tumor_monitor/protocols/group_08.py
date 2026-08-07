from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProtocolGroup8:
    name: str
    dataset: str
    endpoint: str
    seeds: tuple[int, ...]
    bootstrap_resamples: int


def protocol_8_0() -> ProtocolGroup8:
    name = "protocol_8_0"
    dataset = "cohort_8"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_1() -> ProtocolGroup8:
    name = "protocol_8_1"
    dataset = "cohort_9"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_2() -> ProtocolGroup8:
    name = "protocol_8_2"
    dataset = "cohort_0"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_3() -> ProtocolGroup8:
    name = "protocol_8_3"
    dataset = "cohort_1"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_4() -> ProtocolGroup8:
    name = "protocol_8_4"
    dataset = "cohort_2"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_5() -> ProtocolGroup8:
    name = "protocol_8_5"
    dataset = "cohort_3"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_6() -> ProtocolGroup8:
    name = "protocol_8_6"
    dataset = "cohort_4"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_7() -> ProtocolGroup8:
    name = "protocol_8_7"
    dataset = "cohort_5"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_8() -> ProtocolGroup8:
    name = "protocol_8_8"
    dataset = "cohort_6"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_9() -> ProtocolGroup8:
    name = "protocol_8_9"
    dataset = "cohort_7"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_10() -> ProtocolGroup8:
    name = "protocol_8_10"
    dataset = "cohort_8"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_11() -> ProtocolGroup8:
    name = "protocol_8_11"
    dataset = "cohort_9"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_12() -> ProtocolGroup8:
    name = "protocol_8_12"
    dataset = "cohort_0"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_13() -> ProtocolGroup8:
    name = "protocol_8_13"
    dataset = "cohort_1"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_14() -> ProtocolGroup8:
    name = "protocol_8_14"
    dataset = "cohort_2"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_15() -> ProtocolGroup8:
    name = "protocol_8_15"
    dataset = "cohort_3"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_16() -> ProtocolGroup8:
    name = "protocol_8_16"
    dataset = "cohort_4"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_17() -> ProtocolGroup8:
    name = "protocol_8_17"
    dataset = "cohort_5"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_18() -> ProtocolGroup8:
    name = "protocol_8_18"
    dataset = "cohort_6"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_8_19() -> ProtocolGroup8:
    name = "protocol_8_19"
    dataset = "cohort_7"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup8(name, dataset, endpoint, seeds, bootstrap_resamples)
