# Blueprint — Power and energy

PORTS is a **generation campus that computes**, not a compute campus that hopes for megawatts. Phase 1 still needs a copyable electrical SLA so the 80th CM looks like the first.

## Objects

| Object | Core or CM | Notes |
| --- | --- | --- |
| 765 kV / new AEP Ohio lines ($4.2 B program) | Core | Live cut-ins are Core outages (Q08) |
| 345 kV ring, spare positions | Core | Dual corridor; no single-tap 10 GW story |
| USG-owned GT fleet (~9.2 GW program) | Core | Dispatch/island modes in Q03/Q07 |
| Campus BESS (minutes–hours) | Core | Peak, island, DCT bill shape |
| CM conversion + seconds of BESS | CM | Titanium ride-through + checkpoint |
| Gold UPS / 2N | Core + any Gold rooms | Not copied onto 100 MW GPU floors |

## SLA split (same as ICOA)

- **Gold:** identity, fire, EMS, twin bus, MMRs — 2N-class
- **Titanium-Compute:** 100 MW CM — block redundant, shed jobs on under-frequency

## IT/OT

EMS/EPMS is SoR for kW, breaker, frequency ([Q05](../01-operating-architecture/Q05-data-authority.md)). Scheduler may **request** shed; it may not trip a 345 kV breaker.

## Expansion

Add GT blocks and breaker positions to the **same** ring and the **same** tag family. A second EMS with a new point book is an island (Q10).

## Nuclear

Reserve interface and land in Core planning (Q11 A3). Phase 1 must not depend on it.
