from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProtocolGroup0:
    name: str
    dataset: str
    endpoint: str
    seeds: tuple[int, ...]
    bootstrap_resamples: int


def protocol_0_0() -> ProtocolGroup0:
    name = "protocol_0_0"
    dataset = "cohort_0"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_1() -> ProtocolGroup0:
    name = "protocol_0_1"
    dataset = "cohort_1"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_2() -> ProtocolGroup0:
    name = "protocol_0_2"
    dataset = "cohort_2"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_3() -> ProtocolGroup0:
    name = "protocol_0_3"
    dataset = "cohort_3"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_4() -> ProtocolGroup0:
    name = "protocol_0_4"
    dataset = "cohort_4"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_5() -> ProtocolGroup0:
    name = "protocol_0_5"
    dataset = "cohort_5"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_6() -> ProtocolGroup0:
    name = "protocol_0_6"
    dataset = "cohort_6"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_7() -> ProtocolGroup0:
    name = "protocol_0_7"
    dataset = "cohort_7"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_8() -> ProtocolGroup0:
    name = "protocol_0_8"
    dataset = "cohort_8"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_9() -> ProtocolGroup0:
    name = "protocol_0_9"
    dataset = "cohort_9"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_10() -> ProtocolGroup0:
    name = "protocol_0_10"
    dataset = "cohort_0"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_11() -> ProtocolGroup0:
    name = "protocol_0_11"
    dataset = "cohort_1"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_12() -> ProtocolGroup0:
    name = "protocol_0_12"
    dataset = "cohort_2"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_13() -> ProtocolGroup0:
    name = "protocol_0_13"
    dataset = "cohort_3"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_14() -> ProtocolGroup0:
    name = "protocol_0_14"
    dataset = "cohort_4"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_15() -> ProtocolGroup0:
    name = "protocol_0_15"
    dataset = "cohort_5"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_16() -> ProtocolGroup0:
    name = "protocol_0_16"
    dataset = "cohort_6"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_17() -> ProtocolGroup0:
    name = "protocol_0_17"
    dataset = "cohort_7"
    endpoint = "pneumonitis"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_18() -> ProtocolGroup0:
    name = "protocol_0_18"
    dataset = "cohort_8"
    endpoint = "burden"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)


def protocol_0_19() -> ProtocolGroup0:
    name = "protocol_0_19"
    dataset = "cohort_9"
    endpoint = "efficacy"
    seeds = tuple(range(20))
    bootstrap_resamples = 1000
    return ProtocolGroup0(name, dataset, endpoint, seeds, bootstrap_resamples)
