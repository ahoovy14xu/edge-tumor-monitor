from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProtocolGroup13:
    name: str
    dataset: str
    endpoint: str
    seeds: tuple[int, ...]
    bootstrap_resamples: int


def protocol_13_0() -> ProtocolGroup13:
    name = "protocol_13_0"
    dataset = "cohort_3"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_1() -> ProtocolGroup13:
    name = "protocol_13_1"
    dataset = "cohort_4"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_2() -> ProtocolGroup13:
    name = "protocol_13_2"
    dataset = "cohort_5"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_3() -> ProtocolGroup13:
    name = "protocol_13_3"
    dataset = "cohort_6"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_4() -> ProtocolGroup13:
    name = "protocol_13_4"
    dataset = "cohort_7"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_5() -> ProtocolGroup13:
    name = "protocol_13_5"
    dataset = "cohort_8"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_6() -> ProtocolGroup13:
    name = "protocol_13_6"
    dataset = "cohort_9"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_7() -> ProtocolGroup13:
    name = "protocol_13_7"
    dataset = "cohort_0"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_8() -> ProtocolGroup13:
    name = "protocol_13_8"
    dataset = "cohort_1"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_9() -> ProtocolGroup13:
    name = "protocol_13_9"
    dataset = "cohort_2"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_10() -> ProtocolGroup13:
    name = "protocol_13_10"
    dataset = "cohort_3"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_11() -> ProtocolGroup13:
    name = "protocol_13_11"
    dataset = "cohort_4"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_12() -> ProtocolGroup13:
    name = "protocol_13_12"
    dataset = "cohort_5"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_13() -> ProtocolGroup13:
    name = "protocol_13_13"
    dataset = "cohort_6"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_14() -> ProtocolGroup13:
    name = "protocol_13_14"
    dataset = "cohort_7"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_15() -> ProtocolGroup13:
    name = "protocol_13_15"
    dataset = "cohort_8"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_16() -> ProtocolGroup13:
    name = "protocol_13_16"
    dataset = "cohort_9"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_17() -> ProtocolGroup13:
    name = "protocol_13_17"
    dataset = "cohort_0"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_18() -> ProtocolGroup13:
    name = "protocol_13_18"
    dataset = "cohort_1"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_13_19() -> ProtocolGroup13:
    name = "protocol_13_19"
    dataset = "cohort_2"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup13(name, dataset, endpoint, seeds, bootstrap_resamples)
