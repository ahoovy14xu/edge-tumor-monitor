#!/usr/bin/env bash
set -euo pipefail
torchrun --standalone --nproc_per_node=4 -m edge_tumor_monitor.cli.train --config configs/main.yaml "$@"
