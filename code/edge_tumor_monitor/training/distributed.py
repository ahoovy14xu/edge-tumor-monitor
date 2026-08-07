from __future__ import annotations

import os

import torch
import torch.distributed as distributed
from torch import nn
from torch.nn.parallel import DistributedDataParallel


def initialize_distributed() -> tuple[int, int, int]:
    world_size = int(os.environ.get("WORLD_SIZE", "1"))
    rank = int(os.environ.get("RANK", "0"))
    local_rank = int(os.environ.get("LOCAL_RANK", "0"))
    if world_size > 1 and not distributed.is_initialized():
        distributed.init_process_group(backend="nccl", init_method="env://")
        torch.cuda.set_device(local_rank)
    return rank, local_rank, world_size


def wrap_distributed(model: nn.Module, local_rank: int, world_size: int) -> nn.Module:
    if world_size == 1:
        return model
    return DistributedDataParallel(
        model, device_ids=[local_rank], output_device=local_rank, find_unused_parameters=True
    )


def reduce_mean(value: torch.Tensor, world_size: int) -> torch.Tensor:
    if world_size == 1:
        return value
    result = value.detach().clone()
    distributed.all_reduce(result, op=distributed.ReduceOp.SUM)
    return result / world_size


def shutdown_distributed() -> None:
    if distributed.is_initialized():
        distributed.destroy_process_group()
