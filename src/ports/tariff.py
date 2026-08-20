"""AEP Ohio Data Center Tariff minimum billing demand.

Implements the PUCO-approved Schedule DCT brackets (effective 2025):

- 25,001–75,000 kW: 15,000 kW + 85% of capacity above 25,000 kW
- >75,000 kW: 57,500 kW + 100% of capacity above 75,000 kW
- In all cases the minimum cannot exceed 85% of contract capacity
- Compared against 85% of the highest billing demand in the prior 11 months
  when that history exists
"""

from __future__ import annotations


DCT_FRACTION_CAP = 0.85


def aep_bracket_minimum_kw(contract_capacity_kw: float) -> float:
    if contract_capacity_kw <= 0:
        return 0.0
    if contract_capacity_kw <= 25_000:
        return contract_capacity_kw
    if contract_capacity_kw <= 75_000:
        bracket = 15_000.0 + 0.85 * (contract_capacity_kw - 25_000.0)
    else:
        bracket = 57_500.0 + 1.00 * (contract_capacity_kw - 75_000.0)
    return min(bracket, DCT_FRACTION_CAP * contract_capacity_kw)


def aep_minimum_billing_kw(
    contract_capacity_kw: float,
    highest_prior_11_month_kw: float | None = None,
) -> float:
    """Return monthly minimum billing demand in kW."""
    bracket = aep_bracket_minimum_kw(contract_capacity_kw)
    if highest_prior_11_month_kw is None:
        return bracket
    ratchet = DCT_FRACTION_CAP * highest_prior_11_month_kw
    return max(bracket, ratchet)


def aep_contract_term_years(ramp_years: int = 4, term_after_ramp: int = 8) -> int:
    return ramp_years + term_after_ramp
