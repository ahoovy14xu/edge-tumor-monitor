from __future__ import annotations

import argparse
import logging
from pathlib import Path

import torch

from edge_tumor_monitor.config import ExperimentConfig
from edge_tumor_monitor.model.system import LongitudinalTumorMonitor
from edge_tumor_monitor.training.checkpoint import save_checkpoint
from edge_tumor_monitor.utils.seed import set_seed


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(prog="edge-monitor-train")
    value.add_argument("--config", type=Path, default=Path("configs/main.yaml"))
    value.add_argument("--output", type=Path, default=Path("outputs/main"))
    return value


def main() -> None:
    arguments = parser().parse_args()
    logging.basicConfig(level=logging.INFO)
    config = ExperimentConfig.from_yaml(arguments.config)
    set_seed(config.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = LongitudinalTumorMonitor(
        config.metadata_features, resync_period=config.resync_period
    ).to(device)
    optimizer = torch.optim.AdamW(
        model.parameters(), lr=config.learning_rate, weight_decay=config.weight_decay
    )
    arguments.output.mkdir(parents=True, exist_ok=True)
    logging.info(
        "configured %d epochs with effective batch %d", config.epochs, config.effective_batch_size
    )
    save_checkpoint(arguments.output / "initialized.pt", model, optimizer, 0, config.seed)


if __name__ == "__main__":
    main()
