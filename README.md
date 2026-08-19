# Heartland Super Campus (HSC-OH)

Twenty-year architecture for a **gigawatt-class data center campus in Ohio**.

This repository is the master-plan set for **Heartland Super Campus**: a 1,100-acre, 1.2 GW IT, dual-power, liquid-first campus designed to be built in five phases from 2026 through 2046. Buildings, yards, and easements are sized so four generations of compute can land without tearing the campus apart.

## Design thesis

1. **Power is the critical path**, not land or steel. PJM capacity and AEP Ohio interconnection govern the schedule. The campus is therefore a power plant that happens to compute, not a warehouse that happens to buy megawatts.
2. **Do not pile into New Albany.** Columbus/New Albany is already the congested #3 U.S. hyperscale cluster. The flagship site sits on the AEP 345/765 kV backbone, off the Upper Scioto potable system, outside municipal moratoria.
3. **Closed-loop liquid is the 20-year cooling default.** Ohio's water politics and AI rack density (80–150 kW, heading higher) make evaporative cooling a stranded-asset risk.
4. **Grid plus behind-the-meter.** Contract 1,600 MW of interconnection. Build on-site generation and storage so the campus can keep ramping when the queue does not.
5. **License to operate is a design constraint.** Take-or-pay tariffs, tax-exemption reform, water reporting, and community benefit are engineered into the plan, not bolted on after entitlements.

## Campus at full build (2046)

| Metric | Value |
| --- | --- |
| IT capacity | **1,122 MW** (program target 1,200 MW with in-hall densification) |
| Site electrical load | ~1,330 MW |
| Contracted interconnection | 1,600 MW |
| Behind-the-meter share | ~30% of site load |
| Land | 1,100 acres |
| Buildings | 3 cloud, 8 AI factory, 1 core |
| Design PUE (blended) | 1.12–1.18 |
| Design WUE | ≤ 0.05 L/kWh IT |
| Shell + campus capex (2026 USD) | order of **$18–22 B** excluding IT gear |

## 20-year phases

| Phase | Years | What energizes | Cumulative IT |
| --- | --- | --- | --- |
| P0 Enablement | 2026–2028 | Land, 345 kV, water, fiber, generation offtake | 0 MW |
| P1 Foundation | 2028–2031 | 2 cloud + 1 AI factory + core | 234 MW |
| P2 Scale | 2031–2035 | +1 cloud + 2 AI factories | 522 MW |
| P3 Super | 2035–2040 | +3 AI factories, SMR/CCGT block | 882 MW |
| P4 Horizon | 2040–2046 | +2 AI factories, densify existing halls | 1,122 MW |

## Architecture set

| Document | Contents |
| --- | --- |
| [00 Executive brief](docs/00-executive-brief.md) | Decision memo for owners and capital |
| [01 Program charter](docs/01-program-charter.md) | Mission, SLAs, governance |
| [02 Ohio siting](docs/02-ohio-siting.md) | Market, sites, tariff, tax, water |
| [03 Campus master plan](docs/03-campus-master-plan.md) | Land plan, building types, phasing |
| [04 Electrical](docs/04-electrical.md) | 765/345 kV to the rack |
| [05 Mechanical](docs/05-mechanical.md) | Liquid-first cooling, Ohio climate |
| [06 Network](docs/06-network.md) | Fiber, campus fabric, AI scale-out |
| [07 Civil, structure, security](docs/07-civil-security.md) | Soils, wind/ice, physical security |
| [08 Operations](docs/08-operations.md) | Reliability, staffing, refresh |
| [09 Sustainability and community](docs/09-sustainability-community.md) | Carbon, water, jobs, benefit |
| [10 Roadmap and risks](docs/10-roadmap-and-risks.md) | Schedule, money, risk register |

## Living model

Planning numbers in `data/assumptions.yaml` are executable:

```bash
python3 -m pip install -e ".[dev]"
python3 -m pytest
python3 -m heartland roadmap
python3 -m heartland plan --year 2035
python3 -m heartland tariff --it-mw 240
python3 -m heartland cooling --it-mw 1200
```

The model is a master-planning instrument: order-of-magnitude capex, AEP Data Center Tariff minimum demand, and closed-loop vs evaporative water. It is not a bid estimate, interconnection study, or stamped design.

## What this is not

This is not a site civil package, PE-stamped set, or PJM queue position. Those follow site control. This repository is the **architectural constitution** a delivery team, utility, and capital partner should argue from for the next twenty years.
