import torch

from edge_tumor_monitor.config import ExperimentConfig
from edge_tumor_monitor.data.records import LongitudinalBatch
from edge_tumor_monitor.model.system import LongitudinalTumorMonitor
from edge_tumor_monitor.training.engine import Trainer


def test_two_epoch_training_integration() -> None:
    config = ExperimentConfig(
        epochs=2,
        batch_size_per_gpu=1,
        world_size=1,
        metadata_features=8,
        volume_shape=(16, 16, 16),
        precision="fp32",
    )
    model = LongitudinalTumorMonitor(
        metadata_features=8, width=0.5, depths=(1, 1), kernel=3, resync_period=2
    )
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
    trainer = Trainer(model, optimizer, config, torch.device("cpu"))
    volumes = torch.randn(2, 1, 1, 16, 16, 16)
    metadata = torch.randn(2, 1, 8)
    masks = (volumes > 0).float()
    batch = LongitudinalBatch(
        volumes, metadata, masks, None, None, None, torch.ones(2, 3), ("a", "b")
    )
    first = trainer.train_epoch([batch]).loss
    second = trainer.train_epoch([batch]).loss
    assert torch.isfinite(torch.tensor(first + second))
