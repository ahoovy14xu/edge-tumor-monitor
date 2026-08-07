import torch

from edge_tumor_monitor.losses.classification import weighted_focal_loss
from edge_tumor_monitor.losses.segmentation import burden_loss, soft_dice_loss
from edge_tumor_monitor.losses.survival import cox_partial_log_likelihood


def test_perfect_dice_has_near_zero_loss() -> None:
    target = torch.ones(2, 1, 4, 4, 4)
    logits = torch.full_like(target, 20.0)
    assert soft_dice_loss(logits, target) < 1e-6


def test_losses_have_gradients() -> None:
    logits = torch.randn(4, requires_grad=True)
    focal = weighted_focal_loss(logits, torch.tensor([0, 1, 0, 1]))
    cox = cox_partial_log_likelihood(logits, torch.tensor([4.0, 3.0, 2.0, 1.0]), torch.ones(4))
    total = focal + cox + burden_loss(logits.view(1, 1, 1, 1, 4), torch.ones(1, 1, 1, 1, 4))
    total.backward()
    assert torch.isfinite(logits.grad).all()
