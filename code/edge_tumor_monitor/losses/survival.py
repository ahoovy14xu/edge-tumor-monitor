from __future__ import annotations

import torch
import torch.nn.functional as functional


def cox_partial_log_likelihood(
    risk: torch.Tensor, times: torch.Tensor, observed: torch.Tensor
) -> torch.Tensor:
    order = torch.argsort(times, descending=True)
    sorted_risk = risk[order]
    sorted_observed = observed[order].float()
    log_cumulative = torch.logcumsumexp(sorted_risk, dim=0)
    terms = (sorted_risk - log_cumulative) * sorted_observed
    return -terms.sum() / sorted_observed.sum().clamp_min(1.0)


def pairwise_ranking_loss(
    risk: torch.Tensor, times: torch.Tensor, observed: torch.Tensor, margin: float = 0.0
) -> torch.Tensor:
    earlier = times[:, None] < times[None, :]
    valid = earlier & observed[:, None].bool()
    differences = risk[:, None] - risk[None, :]
    losses = functional.softplus(margin - differences)
    if not torch.any(valid):
        return risk.sum() * 0.0
    return losses[valid].mean()


def efficacy_loss(
    risk: torch.Tensor, times: torch.Tensor, observed: torch.Tensor, ranking_weight: float = 0.1
) -> torch.Tensor:
    return cox_partial_log_likelihood(
        risk, times, observed
    ) + ranking_weight * pairwise_ranking_loss(risk, times, observed)
