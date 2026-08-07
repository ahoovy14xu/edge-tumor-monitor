from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import torch
from torch import nn
from torch.optim import Optimizer


def save_checkpoint(
    path: str | Path,
    model: nn.Module,
    optimizer: Optimizer,
    epoch: int,
    seed: int,
    extra: dict[str, Any] | None = None,
) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    state = {
        "model": model.state_dict(),
        "optimizer": optimizer.state_dict(),
        "epoch": epoch,
        "seed": seed,
        "extra": extra or {},
    }
    torch.save(state, temporary)
    os.replace(temporary, destination)


def load_checkpoint(
    path: str | Path, model: nn.Module, optimizer: Optimizer | None = None
) -> tuple[int, int, dict[str, Any]]:
    state = torch.load(Path(path), map_location="cpu", weights_only=False)
    model.load_state_dict(state["model"])
    if optimizer is not None:
        optimizer.load_state_dict(state["optimizer"])
    return int(state["epoch"]), int(state["seed"]), dict(state["extra"])
