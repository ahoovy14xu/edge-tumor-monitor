# Lightweight Multimodal Longitudinal Tumor Monitoring

This repository contains the training and evaluation stack for a 7.4-million-parameter multimodal model that processes longitudinal lung CT, structured metadata and optional genomic descriptors. The model couples a temporal-residual latent encoder, task-selected expert heads and hardware-conditioned subnet selection for burden segmentation, efficacy estimation and an image-derived pneumonitis surrogate.

## Installation

Python 3.10, PyTorch 2.3.0, MONAI 1.3.0 and CUDA 12.1 are pinned. Install with `pip install -r requirements.txt && pip install -e .`, create the Conda environment with `conda env create -f environment.yml`, or build with `docker build -t edge-tumor-monitor .`.

## Data

Canonical sources, versions, licences and retrieval checks are listed in `datasets.txt`. Prepare de-identified DICOM series with `bash commands/prepare_collections.sh DATA_ROOT MANIFEST_ROOT`. The command writes patient-level manifests and never copies identifiers into logs. Storage depends on licensed collection selection; a complete NLST retrieval requires multi-terabyte capacity. Manifest SHA-256 values are emitted after preparation.

## Training

Run the primary schedule with `torchrun --nproc_per_node=4 -m edge_tumor_monitor.cli.train --config configs/main.yaml`. The reported configuration uses four NVIDIA A100 80 GB GPUs, BF16, batch size 32 per GPU, 600 epochs and about 812 GPU-hours. Peak observed memory is 68 GB per device. Twenty independent seeds are required for aggregate reporting.

Progressive shrinking trains the largest width/depth subnet for 200 epochs, shrinks the kernel for 100 epochs, shrinks depth for 100 epochs and traverses widths from 1.0 to 0.5 for 200 epochs. The effective global batch is 128.

## Evaluation

Run `python -m edge_tumor_monitor.cli.evaluate --manifest MANIFEST --weights WEIGHTS --output RESULTS`. The principal held-out targets are burden Dice 0.834 with seed standard deviation 0.017, efficacy AUC 0.812 with standard deviation 0.025 and pneumonitis-surrogate concordance 0.819 with standard deviation 0.021. Evaluation includes 1,000-resample confidence intervals, DeLong comparisons, Benjamini-Hochberg adjustment, calibration, decision curves, mixed-site concordance and 90% split-conformal coverage.

## Inference and export

Run `python -m edge_tumor_monitor.cli.infer --volume VOLUME --metadata METADATA --query burden --weights WEIGHTS`. Export a selected subnet with `python -m edge_tumor_monitor.cli.export --platform jetson_orin_nano --precision int8 --weights WEIGHTS --output MODEL`. Vendor compilers remain external requirements: TensorRT 9.3, Edge TPU Compiler 16.0, Hailo Dataflow Compiler 4.14, Core ML Tools 7.1, Qualcomm AI Engine Direct 2.21 or ONNX Runtime XNNPACK.

## Compute budget

The full schedule requires four A100 80 GB accelerators, approximately 130 wall-clock hours, roughly 58 kWh and 68 GB peak memory per GPU. Source collections require multi-terabyte disk capacity. Platform measurement uses 50 warm-up inferences, 500 measured inferences and a ten-minute sustained thermal run.

## Validation

Run `pytest -q` for unit, mathematical, shape-regression and two-epoch integration coverage. Run `ruff check .` and `mypy --strict code/edge_tumor_monitor` for static checks.

## Scope

The software supports retrospective computational research on public de-identified data. The pneumonitis output is an image-derived texture-change surrogate and is not a patient-level adverse-event prediction. The software is not a clinical decision-support tool.
