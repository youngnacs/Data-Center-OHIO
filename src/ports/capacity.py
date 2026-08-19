"""Campus capacity, water, and capex roll-up."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ports.assumptions import load_assumptions


LITERS_PER_MILLION_GALLONS = 3_785_412.0


@dataclass(frozen=True)
class BuildingType:
    code: str
    name: str
    it_mw: float
    design_pue: float
    target_pue: float
    avg_rack_kw: float
    design_wue_l_per_kwh: float
    capex_usd_per_it_mw: float
    redundancy: str

    @property
    def racks(self) -> int:
        return int(round((self.it_mw * 1000.0) / self.avg_rack_kw))

    @property
    def facility_mw(self) -> float:
        return self.it_mw * self.design_pue


@dataclass(frozen=True)
class Phase:
    id: str
    name: str
    start_year: int
    end_year: int
    buildings: dict[str, int]


@dataclass
class CapacitySnapshot:
    year: int
    phase_id: str
    phase_name: str
    building_counts: dict[str, int]
    it_mw: float
    facility_mw: float
    site_mw: float
    racks: int
    annual_it_mwh: float
    annual_water_million_gal: float
    building_capex_usd: float
    campus_capex_usd: float
    land_capex_usd: float
    total_capex_usd: float
    grid_mw: float
    btm_mw: float
    contracted_interconnection_mw: float
    target_it_mw: float
    progress_to_target: float


class CampusPlan:
    def __init__(self, assumptions: dict[str, Any] | None = None) -> None:
        self.raw = assumptions or load_assumptions()
        self.program = self.raw["program"]
        self.types = {
            code: BuildingType(code=code, **spec)
            for code, spec in self.raw["building_types"].items()
        }
        self.phases = [Phase(**phase) for phase in self.raw["phases"]]
        self.common = self.raw["campus_common"]
        self.power = self.raw["power"]

    def cumulative_buildings(self, year: int) -> dict[str, int]:
        counts: dict[str, int] = {code: 0 for code in self.types}
        for phase in self.phases:
            if year >= phase.end_year:
                for code, qty in phase.buildings.items():
                    counts[code] = counts.get(code, 0) + int(qty)
        return counts

    def active_phase(self, year: int) -> Phase:
        if year < self.program["horizon_start"]:
            return self.phases[0]
        for phase in self.phases:
            if phase.start_year <= year < phase.end_year:
                return phase
        return self.phases[-1]

    def delivered_phase(self, year: int) -> Phase:
        completed = [phase for phase in self.phases if year >= phase.end_year]
        if not completed:
            return self.phases[0]
        return completed[-1]

    def snapshot(self, year: int) -> CapacitySnapshot:
        counts = self.cumulative_buildings(year)
        it_mw = 0.0
        facility_mw = 0.0
        racks = 0
        water_liters = 0.0
        building_capex = 0.0
        hours = float(self.common["hours_per_year"])

        for code, qty in counts.items():
            btype = self.types[code]
            it_mw += btype.it_mw * qty
            facility_mw += btype.facility_mw * qty
            racks += btype.racks * qty
            building_capex += btype.capex_usd_per_it_mw * btype.it_mw * qty
            water_liters += (
                btype.design_wue_l_per_kwh * btype.it_mw * 1000.0 * hours * qty
            )

        site_mw = facility_mw * (1.0 + float(self.common["site_load_uplift"]))
        annual_it_mwh = it_mw * hours
        campus_capex = float(self.common["enablement_capex_usd"])
        if it_mw > 0:
            campus_capex += float(self.common["common_usd_per_it_mw"]) * it_mw
        land_capex = float(self.common["land_usd_per_acre"]) * float(
            self.program["land_acres"]
        )
        total_capex = building_capex + campus_capex + land_capex
        target = float(self.program["target_it_mw"])
        phase = self.delivered_phase(year)

        return CapacitySnapshot(
            year=year,
            phase_id=phase.id,
            phase_name=phase.name,
            building_counts=counts,
            it_mw=it_mw,
            facility_mw=facility_mw,
            site_mw=site_mw,
            racks=racks,
            annual_it_mwh=annual_it_mwh,
            annual_water_million_gal=water_liters / LITERS_PER_MILLION_GALLONS,
            building_capex_usd=building_capex,
            campus_capex_usd=campus_capex,
            land_capex_usd=land_capex,
            total_capex_usd=total_capex,
            grid_mw=site_mw * float(self.power["grid_share_at_full_build"]),
            btm_mw=site_mw * float(self.power["btm_share_at_full_build"]),
            contracted_interconnection_mw=float(
                self.program["contracted_interconnection_mw"]
            ),
            target_it_mw=target,
            progress_to_target=(it_mw / target) if target else 0.0,
        )

    def full_build(self) -> CapacitySnapshot:
        return self.snapshot(int(self.program["horizon_end"]))

    def roadmap(self) -> list[CapacitySnapshot]:
        return [self.snapshot(phase.end_year) for phase in self.phases]


def campus_at_year(year: int, assumptions: dict[str, Any] | None = None) -> CapacitySnapshot:
    return CampusPlan(assumptions).snapshot(year)
