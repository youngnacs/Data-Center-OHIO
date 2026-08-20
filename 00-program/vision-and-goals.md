# Vision and goals

## Vision

PORTS-Pike is not eight data halls next to a power plant. It is a **single industrial organism**: generation, transmission, liquid-cooled AI factories, facilities, networks, and an operations platform that can be copied from the first 100 MW module to the eightieth without rewriting how the campus is run.

The work of this architecture is to make **Phase 1 (800 MW)** the first instance of that organism — not a prototype we throw away at 2 GW.

## Mission (this technical office)

Connect **Power + HVAC/liquid cooling + Facilities + IT/OT + Telemetry + Agentic AI** into one Integrated Campus Operating Architecture (ICOA). Serve as the technical interface among the power infrastructure team, data-center construction team, IT/AI team, and operations team. Build the standards and the people who can carry that architecture from first energization to multi-gigawatt scale.

## Goals (what “good” looks like)

| ID | Goal | Phase 1 evidence | 10 GW evidence |
| --- | --- | --- | --- |
| G1 | One repeatable **Compute Module** | 8 identical 100 MW CMs, same tags, same IST script | 80th module commissions against the P1 playbook |
| G2 | One **Campus Core** (power, water, identity, twin, security) | Core services live before the first GPU job | New modules attach; they do not fork a second core |
| G3 | IT/OT is a designed system | Data-flow and zone drawings exist before BMS/SCADA FAT | Same zones, same brokers, more modules |
| G4 | Failures stop at module or feeder boundaries | Fault-injection / IST cases for isolation | A module trip does not take a generation island or the twin down |
| G5 | Live expansion is the default | P1 halls energize while neighbors are in construction | P2+ cut over without campus blackout |
| G6 | Vendor independence where the campus lives 30 years | Open telemetry, standard tags, replaceable BMS/CDU/EMS adapters | A BMS or CDU OEM can change without a new ICOA |
| G7 | Achievable PUE / WUE / availability / opex | Design PUE ≤ 1.15 CM, WUE ≤ 0.05 L/kWh, Gold vs Titanium SLAs | Same KPIs campus-wide, not a zoo of hall-specific targets |
| G8 | Agentic AI is bounded | Advisory on anomaly, energy, knowledge, work orders | Closed-loop only where Q3 autonomy allows |
| G9 | Teams exist before COD | Power desk, mechanical desk, OT security, twin, AI ops roles named | Staffing scales per module, not a new org chart per phase |
| G10 | License to operate | Water, tax, DOE adjacency, community metrics metered | Public numbers still match the meters |

## Non-goals (first 90 days)

- Finalize every one-line, pipe diameter, or GPU SKU
- Select every OEM
- Train production models on live OT
- Replace owner, DOE, AEP, or NVIDIA design authorities

The 90-day output is **ICOA v0.9**: a campus that can be designed, reviewed, commissioned, and operated as one system. Detail engineering follows it; it does not wait for detail engineering.
