# Q07 — Scenarios, use cases, and failure isolation

**Question:** Which operational scenarios, use cases, and failure events must the architecture support? How will failures be detected, isolated, and prevented from propagating across modules?

## Decision (v0.1)

The campus is designed around **failure domains the size of a CM (or a single 34.5 kV feeder pair)**, plus a **Gold core** that must survive CM deaths. Detection is local first (protection, leak, fire), then campus bus, then people and AI. Isolation is automatic for class A; containment of “interesting” failures is a desk procedure.

## Scenarios the ICOA must support (minimum catalog)

| ID | Scenario | Detect | Isolate | Must not propagate to |
| --- | --- | --- | --- | --- |
| S1 | CM feeder fault | Relays | Trip that CM pair | Other CMs, 345 kV, twin |
| S2 | Liquid leak | CDU / leak tape | Row or loop isolate (A) | Adjacent CMs, fire water |
| S3 | GPU over-temp / thermal runaway aisle | BMS + IT | Power cap / job kill (S/A as IST) | Core IAM |
| S4 | Under-frequency / gen trip | EMS + plant | Shed Titanium (A); hold Gold | Life safety, protection comms |
| S5 | 345 kV line loss | Protection | Alternate corridor + BTM | Depends; not “all eight CMs blindly” |
| S6 | BESS fire | Fire + 855 | Yard isolation | Halls, fuel |
| S7 | Twin / bus outage | Heartbeats | CMs run local (A protection stays) | Must not trip halls |
| S8 | Cyber suspected | SOC + mode tag | Q6 collapse | Must not disable protection |
| S9 | Ice storm / dry-cooler loss | BMS | Derate CM, adiabatic policy | Water panic |
| S10 | Live-expansion error (wrong LOTO) | Permits + interlocking | Stop IST, hold neighbors | Energized CMs |
| S11 | Vendor session gone wrong | PAM | Kill session (Q6) | Other CMs |
| S12 | Tenant job storm (power ramp) | EPMS + scheduler | Ramp limit / checkpoint | Voltage flicker on neighbors |
| S13 | Water makeup contamination | Chemistry | Isolate makeup; halls on closed volume | Public narrative / other CMs |
| S14 | DOE site event | Security | Physical lockdown modes | Need runbook with DOE |
| S15 | Smoke / fire in CM | Fire | Hall + HVAC dampers | Core, gen, other CMs |

## Use cases (happy path) that are also architecture

- Normal production at N CMs
- IST of CM-n while CM-1..n-1 produce
- Seasonal energy mode (dry cooler vs assist)
- Maintenance: CDU skid swap, transformer swap
- Disaster recovery: lose on-site NOC, fail to remote Gold
- Regulatory pack generation (water, emissions, interconnect)

## Isolation rules

1. **No common-mode software** that can trip all CMs (one bad agent command). Southbound is per-CM allow-list.
2. **No common-mode mechanical** (one chilled-water header for 800 MW). Plants are per CM.
3. **No common-mode identity outage** that locks out desks — break-glass Core procedure.
4. **IST fault injection** of S1, S2, S7, S10 is a Phase 1 gate, not a paper exercise.

## Detection stack

Local device → CM controller → campus bus → historian/twin → desk + optional AI ranking. **AI is not the detector of record for S1–S6.** It may rank S9/S12 and draft work orders.
