from __future__ import annotations

import argparse
from pathlib import Path


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(prog="edge-monitor-export")
    value.add_argument("--platform", required=True)
    value.add_argument(
        "--precision", choices=("int4", "int8", "fp16", "bf16", "fp32"), required=True
    )
    value.add_argument("--weights", type=Path, required=True)
    value.add_argument("--output", type=Path, required=True)
    return value


def main() -> None:
    parser().parse_args()


if __name__ == "__main__":
    main()
