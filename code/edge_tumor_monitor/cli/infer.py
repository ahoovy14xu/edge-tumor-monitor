from __future__ import annotations

import argparse
from pathlib import Path


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(prog="edge-monitor-infer")
    value.add_argument("--volume", type=Path, required=True)
    value.add_argument("--metadata", type=Path, required=True)
    value.add_argument("--query", choices=("burden", "efficacy", "pneumonitis"), required=True)
    value.add_argument("--weights", type=Path, required=True)
    return value


def main() -> None:
    parser().parse_args()


if __name__ == "__main__":
    main()
