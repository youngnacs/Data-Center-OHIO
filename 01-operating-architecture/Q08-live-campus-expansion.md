# Q08 — Connecting new modules to a live campus

**Question:** How should new, expanded, or refurbished modules be connected to the live campus? Which additions can be commissioned while adjacent systems remain energized, and which require planned shutdowns or isolation?

## Decision (v0.1)

**Live expansion is the default after CM-01.** Phase 1’s later modules and all later gigawatts must attach without a campus blackout. Shutdowns are reserved for Core assets that were not built with N+1.

## Energized-adjacent (no campus outage)

| Work | How |
| --- | --- |
| New CM shell, liquid, BMS | Construction island; separate LOTO; no tap onto live process-water without double block and bleed |
| New 34.5 kV feeder pair | Yard designed with spare breakers; close onto an **empty** CM after IST |
| Twin / tag instantiation | Software; CM template clone |
| Fiber laterals into a new CM | Diverse ducts; never a live cut of both MMRs |
| CDU / skid swap in an existing CM | Row or gallery isolation; derate that CM |
| GPU refresh | Hall procedure; Titanium SLA |

## Planned isolation (CM or feeder only)

| Work | Outage domain |
| --- | --- |
| CM transformer | That CM |
| 34.5 kV bus section | Only if breaker-and-a-half / ring was built; else that CM pair |
| Hall liquid refill | That CM |

## Campus or Core outage (avoid; design out of P1)

| Work | If we did not oversize |
| --- | --- |
| 345 kV ring node add | Possible live if ring bus exists; **not** if single tap |
| Makeup plant major | Need redundant trains from P1 |
| IAM / historian cutover | Blue-green in Core; never “weekend we turn off tags” |
| First 765 kV cut-in | Utility outage window — schedule as Core, not as eight-CM event |

## Construction vs operations boundary

From the second CM onward the site is a **hot plant next to a hard-hat city**. ICOA requires:

- Separate vehicle paths (transformer alley ≠ employee gate)
- Construction network **not** the OT network (Q6)
- Permit-to-energize signed by power desk + mechanical desk + ICOA checklist
- A **construction freeze** radius when a neighbor CM is in IST

## Refurbish / replace

A 2034 GPU generation is a **CM fit-out**, not a new ICOA. A 2036 BMS OEM change is an adapter + tag compliance test ([Q09](Q09-vendor-replaceability.md)). A 2038 liquid-to-next-liquid is pipe-capacity we already bought in Q01.
