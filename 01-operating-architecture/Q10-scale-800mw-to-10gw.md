# Q10 — 800 MW → 10 GW without operational islands

**Question:** How can the initial 800 MW phase expand toward a multi-gigawatt campus without creating incompatible operational islands, while maintaining achievable targets for PUE, WUE, reliability, availability, and operational cost?

## Decision (v0.1)

Phase 1 is **not a pilot**. It is **instance zero of the 10 GW operating system**: same module, same core, same tags, same desks, same IST, same KPIs. Capacity grows by **adding CMs and generation/transmission capacity to the Core**, not by inventing Phase-2-OS.

## Scale arithmetic

| | Phase 1 | Full envelope |
| --- | --- | --- |
| Compute Modules | 8 × 100 MW | ~80 × 100 MW |
| IT | **800 MW** | **~8 GW** |
| Energy / gen | First GT/BESS blocks + interconnect | **~10 GW** including ~9.2 GW gas |
| Operating system | ICOA v1 | ICOA v1 + more instances |

If P2 needs a new historian schema, a new module size, or a new autonomy model, stop and treat it as an ICOA revision — a governed event, not a silent hall-level experiment.

## KPI targets (achievable, campus-wide)

| KPI | Phase 1 design | Stretch / later CMs | Island anti-pattern |
| --- | --- | --- | --- |
| PUE (trailing 12, CM) | ≤ **1.15** | ≤ 1.10 | Each EPC promises a private PUE |
| WUE | ≤ **0.05** L/kWh IT | ≤ 0.03 | Evaporative “just this phase” |
| Gold availability | 99.999% | same | Core colocated in a CM fire zone |
| Titanium power availability | 99.99% + checkpoint | same | 2N UPS copied onto 100 MW |
| Isolation | S1–S15 catalog | same IDs | New phase, new alarm philosophy |
| Opex | Shared warehouse, one qualification | Linear-ish per CM | New CMMS per phase |
| Staff | Desks scale by CM count | see [../05-operations-and-teams](../05-operations-and-teams/README.md) | New org chart per EPC |

## What must be oversized in Phase 1 (cheap now, impossible later)

- 345 kV ring / spare breaker positions toward 765 kV
- Duct banks, process-water mains diameter, loop road
- Tag namespace (`CM01`–`CM99`)
- Historian/bus capacity
- Warehouse and LOTO culture
- Access engine modes (Q6)

## What may change per generation (without islands)

- GPU SKU, fabric generation, CDU efficiency, dry-cooler fans, agent models
- Number of GTs / BESS MWh
- Tenant overlay

## Governance

Every new CM FID includes an **ICOA compliance sheet**: module ID, core attachments, SoR list, failure domain, live-expansion method, vendor adapters, KPI budget. If it cannot be filled, it is not a PORTS module yet.

## The opex rule

Operational cost stays achievable only if **people, spares, and software stay linear in CM count**. Islands (second BMS dialect, second AI platform, second water chemistry) make opex **combinatorial**. That is the actual 10 GW risk, more than concrete.
