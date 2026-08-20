# Q02 — Campus core vs distributed modules

**Question:** Which capabilities should be provided by the campus core, and which should remain within supporting or distributed modules?

## Decision (v0.1)

**One Campus Core. Many Compute Modules.** Core things are those whose duplication would create operational islands, split identity, or unsafe electrical/water islands. Module things are those whose failure must not take the campus down.

## Campus Core (provide once, consume N times)

| Capability | Why it is core | Phase 1 note |
| --- | --- | --- |
| 765/345 kV yard, campus 34.5 kV topology | One grid/generation truth | Oversize bus for 10 GW path |
| Generation dispatch interface (GT, later nuclear) | Plant ≠ hall | Even if GTs sit on another pad |
| Campus BESS (minutes-to-hours) vs CM ride-through | Energy vs power quality | Do not conflate the two |
| Makeup water, treatment, fire water | One chemistry, one report to ODNR/OEPA | Closed-loop fill events |
| Dual fiber MMRs + WAN | Two paths, not eight contracts | P0 critical path |
| Identity, PKI, access policy engine | Q5/Q6 | Includes vendor and tenant |
| Telemetry bus, historian, twin, AI ops platform | One SoR pattern | Modules are publishers |
| Gold IT (DNS, IAM, out-of-band, secrets) | Training halls may die; core must not | Separate fire zone |
| Physical security command, DOE interface | Site is not a strip mall | Adjacency to D&D |
| Time (GPS/PTP) for protection **and** fabric | Two consumers, one campus time | Holdover required |
| Knowledge base / procedures | One runbook family | Agentic AI reads this, not SharePoint chaos |

## Distributed (inside each CM)

| Capability | Why distributed |
| --- | --- |
| Block power conversion, CM-level BESS seconds-to-minutes | Failure domain = CM |
| CDU / liquid / hall BMS | Isolate a row, not the campus |
| GPU fabric and cluster schedulers for that CM (or CM group) | Latency and blast radius |
| Local protection (breakers, leak, fire) | Speed; core is too far |
| Local HMI for IST and emergency | Must work if the twin is down |

## Supporting modules (neither core nor CM)

Named once on the site plan, copied as needed:

- **Logistics / warehouse** (transformers are not next-day parts)
- **Construction village** (P1–P4 overlap live ops)
- **Admin / NOC** (on-site + remote)
- **Fuel / water treatment** buildings

These publish telemetry to the core bus but are not 100 MW CMs.

## Anti-pattern

A “Phase 2 core” (second historian, second IAM, second water chemistry, second tagging standard) is how 800 MW becomes two campuses that share a fence. **New phases add CMs and may add HV/generation *capacity* to the same core — they do not add a second operating system.**
