"""Command-line planner for PORTS-Pike Technology Campus."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict

from ports.capacity import CampusPlan
from ports.cooling import compare_cooling
from ports.tariff import aep_contract_term_years, aep_minimum_billing_kw


def _fmt_mw(value: float) -> str:
    return f"{value:,.1f} MW"


def _fmt_usd(value: float) -> str:
    if value >= 1_000_000_000:
        return f"${value / 1_000_000_000:,.2f} B"
    return f"${value / 1_000_000:,.0f} M"


def cmd_plan(year: int) -> int:
    plan = CampusPlan()
    snap = plan.snapshot(year)
    print(f"{plan.program['name']}  |  year {snap.year}  |  phase {snap.phase_id} {snap.phase_name}")
    print(f"  Modules       {snap.building_counts}")
    print(f"  IT load       {_fmt_mw(snap.it_mw)}  ({snap.progress_to_target:.0%} of {snap.target_it_mw:.0f} MW target)")
    print(f"  Facility      {_fmt_mw(snap.facility_mw)}")
    print(f"  Site load     {_fmt_mw(snap.site_mw)}")
    print(f"  Racks         {snap.racks:,}")
    print(f"  Water         {snap.annual_water_million_gal:,.1f} million gal / year")
    print(f"  Grid / on-site {_fmt_mw(snap.grid_mw)} / {_fmt_mw(snap.btm_mw)}")
    print(f"  Energy envelope {_fmt_mw(snap.contracted_interconnection_mw)}")
    print(f"  Capex (shell) {_fmt_usd(snap.total_capex_usd)}  [modules {_fmt_usd(snap.building_capex_usd)}]")
    print("  Note: gas generation and 765 kV transmission are separate FIDs.")
    return 0


def cmd_roadmap() -> int:
    plan = CampusPlan()
    print(f"{'Phase':<6} {'Years':<13} {'IT MW':>10} {'Site MW':>10} {'CMs':>8} {'Capex':>12}")
    for phase, snap in zip(plan.phases, plan.roadmap(), strict=True):
        years = f"{phase.start_year}-{phase.end_year}"
        cms = snap.building_counts.get("CM", 0)
        print(
            f"{snap.phase_id:<6} {years:<13} {snap.it_mw:10.0f} {snap.site_mw:10.0f} "
            f"{cms:8} {_fmt_usd(snap.total_capex_usd):>12}"
        )
    return 0


def cmd_module() -> int:
    plan = CampusPlan()
    cm = plan.types["CM"]
    print("Compute Module (repeatable campus unit)")
    print(f"  IT            {_fmt_mw(cm.it_mw)}")
    print(f"  Facility      {_fmt_mw(cm.facility_mw)}  (PUE {cm.design_pue})")
    print(f"  Racks         {cm.racks:,}  @ {cm.avg_rack_kw:.0f} kW avg")
    print(f"  Phase 1       {int(plan.program['phase_1_it_mw'] / cm.it_mw)} modules = {plan.program['phase_1_it_mw']:.0f} MW")
    print(f"  Full campus   {int(plan.program['target_it_mw'] / cm.it_mw)} modules = {plan.program['target_it_mw']:.0f} MW IT")
    return 0


def cmd_tariff(it_mw: float) -> int:
    contract_kw = it_mw * 1000.0
    minimum = aep_minimum_billing_kw(contract_kw)
    print(f"Contract capacity     {contract_kw:,.0f} kW")
    print(f"DCT minimum demand    {minimum:,.0f} kW  ({minimum / contract_kw:.0%} of contract)")
    print(f"Contract term         {aep_contract_term_years()} years (4 ramp + 8 firm)")
    return 0


def cmd_cooling(it_mw: float) -> int:
    result = compare_cooling(it_mw)
    print(f"IT load                         {_fmt_mw(result.it_mw)}")
    print(f"Closed-loop water               {result.closed_loop_million_gal:,.1f} Mgal/yr")
    print(f"Evaporative counterfactual      {result.evaporative_million_gal:,.1f} Mgal/yr")
    print(f"Water avoided                   {result.water_saved_million_gal:,.1f} Mgal/yr ({result.savings_ratio:.0%})")
    return 0


def cmd_json(year: int) -> int:
    snap = CampusPlan().snapshot(year)
    print(json.dumps(asdict(snap), indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="ports",
        description="PORTS-Pike Integrated Campus Operating Architecture — planning model",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    plan = sub.add_parser("plan", help="capacity snapshot for a given year")
    plan.add_argument("--year", type=int, default=2040)

    sub.add_parser("roadmap", help="phase-by-phase build table")
    sub.add_parser("module", help="repeatable 100 MW Compute Module")

    tariff = sub.add_parser("tariff", help="AEP Ohio DCT minimum billing demand")
    tariff.add_argument("--it-mw", type=float, required=True)

    cooling = sub.add_parser("cooling", help="closed-loop vs evaporative water")
    cooling.add_argument("--it-mw", type=float, required=True)

    dump = sub.add_parser("json", help="machine-readable snapshot")
    dump.add_argument("--year", type=int, default=2040)

    args = parser.parse_args(argv)
    if args.cmd == "plan":
        return cmd_plan(args.year)
    if args.cmd == "roadmap":
        return cmd_roadmap()
    if args.cmd == "module":
        return cmd_module()
    if args.cmd == "tariff":
        return cmd_tariff(args.it_mw)
    if args.cmd == "cooling":
        return cmd_cooling(args.it_mw)
    if args.cmd == "json":
        return cmd_json(args.year)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
