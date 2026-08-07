from __future__ import annotations

import argparse
import json
from pathlib import Path


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(prog="edge-monitor-evaluate")
    value.add_argument("--manifest", type=Path, required=True)
    value.add_argument("--weights", type=Path, required=True)
    value.add_argument("--output", type=Path, required=True)
    return value


def main() -> None:
    arguments = parser().parse_args()
    arguments.output.mkdir(parents=True, exist_ok=True)
    payload = {
        "manifest": arguments.manifest.name,
        "weights": arguments.weights.name,
        "status": "configured",
    }
    (arguments.output / "evaluation.json").write_text(json.dumps(payload), encoding="utf-8")


if __name__ == "__main__":
    main()
