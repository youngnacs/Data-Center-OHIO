"""Cooling water comparison: closed-loop DLC vs evaporative heat rejection."""

from __future__ import annotations

from dataclasses import dataclass

from heartland.assumptions import load_assumptions


@dataclass(frozen=True)
class CoolingComparison:
    it_mw: float
    annual_it_mwh: float
    closed_loop_million_gal: float
    evaporative_million_gal: float
    water_saved_million_gal: float
    savings_ratio: float


LITERS_PER_MILLION_GALLONS = 3_785_412.0


def compare_cooling(it_mw: float, wue_l_per_kwh: float | None = None) -> CoolingComparison:
    assumptions = load_assumptions()
    hours = float(assumptions["campus_common"]["hours_per_year"])
    evaporative = float(assumptions["cooling"]["evaporative_liters_per_kwh"])
    closed = wue_l_per_kwh if wue_l_per_kwh is not None else 0.03
    annual_mwh = it_mw * hours
    closed_liters = closed * it_mw * 1000.0 * hours
    evap_liters = evaporative * it_mw * 1000.0 * hours
    closed_mgal = closed_liters / LITERS_PER_MILLION_GALLONS
    evap_mgal = evap_liters / LITERS_PER_MILLION_GALLONS
    saved = evap_mgal - closed_mgal
    return CoolingComparison(
        it_mw=it_mw,
        annual_it_mwh=annual_mwh,
        closed_loop_million_gal=closed_mgal,
        evaporative_million_gal=evap_mgal,
        water_saved_million_gal=saved,
        savings_ratio=(saved / evap_mgal) if evap_mgal else 0.0,
    )
