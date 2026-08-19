# 08 — Operations and reliability

A 20-year campus is an operating company from P1-24 months, not from COD.

## Reliability model

| Domain | Target | Method |
| --- | --- | --- |
| Type C + campus control | 99.999% | 2N, dual NOC (on-site + remote), no shared fire zone with Type B |
| Type A | 99.995%+ | 2N UPS, N+1 mechanical |
| Type B training | 99.99% power | Block redundant + BESS + checkpoint |
| Water / liquid | no unplanned hall loss | N+1 CDUs, leak isolate-to-row |
| Network to Columbus | no dual-cut | Two laterals, two MMRs |

Incident command: power desk has switching authority; mechanical desk has liquid isolation authority; they train **together**. GPU jobs are shed by procedure, not by panic.

## Staffing (order of magnitude)

| Era | On-site + near-site |
| --- | --- |
| P1 COD | ~120 campus + vendors |
| P2 | ~200 |
| P4 | ~350–450 plus embedded vendors |

Roles that New Albany already taught Ohio to value: HV switching, liquid operations, controls, security, and vendor management. Roles we must grow: **BTM generation operators** if we own CCGT/SMR.

Apprenticeships with IBEW/UA and community colleges start in P0, not after the first outage.

## Maintenance

- Live-campus culture: no “annual shutdown of Ohio.”
- Spares warehouse: transformers are not a next-day Amazon item. 345 kV and large 34.5 kV spares have a **multi-year** lead time — order on P1 FID, not after the first failure.
- Dry-cooler ice, glycol chemistry, and CDU hoses are the unsexy reliability program.
- Cyber: BMS/EPMS on a separate trust domain; no vendor VPN that bypasses Type C.

## Refresh

| Layer | Life | Rule |
| --- | --- | --- |
| Silicon / racks | 3–5 years | Fit-out package; hall stays |
| Optics | 5–7 years | SMF plant stays |
| CDUs / pumps | 10–15 years | Skid swap |
| UPS / conversion | 10–15 years | Gold halls first |
| Buildings / yards | 30–50 years | Never redesigned for a GPU generation |
| 345 kV | 40–60 years | Oversize once |

Type A densification in P4 (12 kW → 20–30 kW hybrid) is how we close the gap from 1,122 MW toward the 1,200 MW program target without a ninth AI factory.

## Construction while live

From P2 onward the campus is a **hot site with a hard-hat city next door**. Lock-out, vehicle paths, and RF/cyber boundaries between construction and operations are a standing design — see [03](03-campus-master-plan.md) logistics.
