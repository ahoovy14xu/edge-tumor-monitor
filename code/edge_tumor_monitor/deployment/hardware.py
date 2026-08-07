from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


Precision = Literal["int4", "int8", "fp16", "bf16", "fp32"]


@dataclass(frozen=True)
class Platform:
    name: str
    int8_tops: float
    bandwidth_gbps: float
    tdp_watts: float
    precisions: tuple[Precision, ...]
    compiler: str


PLATFORMS = {
    "jetson_orin_nano": Platform(
        "Jetson Orin Nano", 40.0, 68.0, 15.0, ("int8", "fp16", "fp32"), "TensorRT 9.3"
    ),
    "coral_edge_tpu": Platform(
        "Coral Edge TPU", 4.0, 8.0, 2.0, ("int8",), "Edge TPU Compiler 16.0"
    ),
    "hailo8": Platform("Hailo-8", 26.0, 16.0, 2.5, ("int8",), "Hailo Dataflow Compiler 4.14"),
    "apple_a17": Platform("Apple A17 Pro", 35.0, 51.2, 8.0, ("int8", "fp16"), "Core ML Tools 7.1"),
    "snapdragon_8_gen_3": Platform(
        "Snapdragon 8 Gen 3",
        45.0,
        77.0,
        8.5,
        ("int4", "int8", "fp16"),
        "Qualcomm AI Engine Direct 2.21",
    ),
    "raspberry_pi_5": Platform(
        "Raspberry Pi 5", 0.1, 17.0, 12.0, ("int8", "fp32"), "ONNX Runtime XNNPACK"
    ),
}
