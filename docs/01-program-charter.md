# 01 — Program charter

## Mission

Design, entitle, build, and operate an Ohio campus that can host **cloud, storage, and frontier AI** on a single electrical and fiber spine for **twenty years**, with buildings that outlive four compute generations.

## Owner outcomes

| Outcome | Target |
| --- | --- |
| Energized IT by 2031 | ≥ 230 MW |
| Energized IT by 2046 | ≥ 1,100 MW, path to 1,200 MW by densification |
| Availability — control plane / storage | 99.999% (Gold halls) |
| Availability — AI training fabric | 99.99% power, software-checkpointed jobs |
| PUE, trailing twelve months, full campus | ≤ 1.20 design, ≤ 1.12 stretch on AI halls |
| WUE, trailing twelve months | ≤ 0.05 L/kWh IT |
| Carbon | 100% annual matched CFE by 2032; 24/7 CFE on Gold halls by 2038 |
| Safety | Zero serious injuries; OSHA recordable below construction peer |
| Community | Published water and tax payments; apprenticeship pipeline |

## Scope

In scope: land, entitlements, HV/MV electrical, mechanical plants, network outside plant, security, building shells, hall fit-out to the busway and CDU, campus operations.

Out of scope: tenant silicon, model training software, public utility generation not under campus control, municipal water-plant construction.

## Governance

| Body | Cadence | Authority |
| --- | --- | --- |
| Campus board (owner + capital + independent PE) | quarterly | Phase gates, interconnection MW, BTM FID |
| Design authority (this architecture set) | standing | Variances from Type A/B/C, cooling constitution, 345 kV topology |
| Ohio external affairs | monthly | PUCO, Tax Credit Authority, county, township, ODNR/OEPA |
| Operations readiness | from P1-24 months | Staffing, spares, incident command |

No hall starts construction without a **power date certain** (interconnection + DCT collateral + BTM contingency) and a **water date certain** (closed-loop fill + fire + domestic only).

## Design principles

1. **Time-to-power beats time-to-slab.** A pad without megawatts is landscaping.
2. **One campus, two electrical SLAs.** Do not force 2N UPS onto a 120 MW training hall; do not starve the control plane of 2N.
3. **Every hall is liquid-ready on day one**, even Type A. Headers, slab penetrations, roof dry-cooler allowance, and CDU rooms are in the base building.
4. **Oversize the long-lived layers.** 345 kV yard, 34.5 kV loops, process-water mains, and fiber duct banks are cheap compared with cutting a live campus in 2039.
5. **Standardize the block, customize the silicon.** Type A/B/C are frozen; rack, GPU, and switch generations are not.
6. **Measure what Ohio will regulate.** Water, tax, and load are public metrics. Design the instrumentation before the first CU.

## Standards baseline

- Electrical: IEEE, NESC, NEC, AEP interconnection requirements, PJM manuals
- Mechanical: ASHRAE TC 9.9, ASHRAE 90.4, ASHRAE 15 (if refrigerants), IBC
- Reliability: Uptime Institute Tier III campus; selective Tier IV on Type C
- Security: TIA-942 Rated-3, ISO 27001 ops, physical ISC/UFC standoff as applicable
- Sustainability: ISO 50001, GHG Protocol, corporate CFE matching
- Fire: NFPA 75 / 76, plus liquid-coolant and battery-energy-storage supplements

## Phase gates

| Gate | Evidence required |
| --- | --- |
| G0 Site | Option or PSA, title, wetlands, cultural, 345 kV corridor opinion |
| G1 Interconnect | AEP pre-app, DCT term sheet, collateral plan, PJM queue ID |
| G2 Enablement | 30% HV/civil, water/wastewater letters, two fiber providers |
| G3 P1 FID | 60% Type A/B/C, EPC, offtake, community compact |
| G4 P2+ | Trailing PUE/WUE, actual load vs DCT, generation FID for next block |

## Organization at steady state

- Campus director
- Power (utility + BTM + BESS)
- Mechanical / water
- Network
- Security / EHS
- Construction (standing, because the campus is never “done”)
- Community / government
