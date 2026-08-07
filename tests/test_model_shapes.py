import torch

from edge_tumor_monitor.model.system import LongitudinalTumorMonitor


def test_all_expert_shapes() -> None:
    model = LongitudinalTumorMonitor(
        metadata_features=8, width=0.5, depths=(1, 1), kernel=3, resync_period=2
    )
    model.eval()
    volume = torch.randn(2, 2, 1, 32, 32, 32)
    metadata = torch.randn(2, 2, 8)
    with torch.no_grad():
        burden = model(volume, metadata, "burden").prediction
        efficacy = model(volume, metadata, "efficacy").prediction
        pneumonitis = model(volume, metadata, "pneumonitis").prediction
    assert burden.shape == (2, 1, 32, 32, 32)
    assert efficacy.shape == (2,)
    assert pneumonitis.shape == (2,)
