from __future__ import annotations

from dataclasses import dataclass

from edge_tumor_monitor.deployment.hardware import Platform, Precision


@dataclass(frozen=True)
class Subnet:
    width: float
    depth: tuple[int, int]
    precision: Precision
    task_loss: float
    latency_ms: float
    energy_mj: float


@dataclass(frozen=True)
class Selection:
    subnet: Subnet
    objective: float
    platform: Platform


def lagrangian(
    subnet: Subnet, latency_coefficient: float = 0.002, energy_coefficient: float = 0.001
) -> float:
    return (
        subnet.task_loss
        + latency_coefficient * subnet.latency_ms
        + energy_coefficient * subnet.energy_mj
    )


def pareto_frontier(candidates: list[Subnet]) -> list[Subnet]:
    frontier = []
    for candidate in candidates:
        dominated = any(
            other.task_loss <= candidate.task_loss
            and other.latency_ms <= candidate.latency_ms
            and other.energy_mj <= candidate.energy_mj
            and other != candidate
            for other in candidates
        )
        if not dominated:
            frontier.append(candidate)
    return sorted(frontier, key=lambda item: (item.task_loss, item.latency_ms, item.energy_mj))


def select_subnet(platform: Platform, candidates: list[Subnet]) -> Selection:
    supported = [
        candidate for candidate in candidates if candidate.precision in platform.precisions
    ]
    if not supported:
        raise ValueError(f"no candidate supports {platform.name}")
    selected = min(supported, key=lagrangian)
    return Selection(selected, lagrangian(selected), platform)
