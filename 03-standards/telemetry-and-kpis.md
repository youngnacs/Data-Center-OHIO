# Telemetry and KPIs

## Bus

- One production bus (HA) in Core
- CM may buffer locally; protection does not depend on the bus (Q07 S7)
- Southbound allow-list only

## Phase 1 KPI board (design)

| KPI | Target | SoR |
| --- | --- | --- |
| CM PUE (T12) | ≤ 1.15 | EPMS + IT kWh |
| Campus WUE | ≤ 0.05 L/kWh IT | Makeup meters / BMS |
| Gold availability | 99.999% | Incident + IAM |
| Titanium power availability | 99.99% | EPMS + scheduler checkpoints |
| Isolation events contained to CM | 100% of S1–S3, S15 | Protection + fire |
| Vendor sessions | 100% PAM recorded | IAM |

Opex: track **FTE per energized CM** and **unique software stacks per CM** (should stay ~constant). That is the island detector.
