# Blueprint — Telemetry, digital twin, and Agentic AI

## Telemetry

One campus bus. Standard tags ([../03-standards/naming-and-tagging.md](../03-standards/naming-and-tagging.md)). Historian HA in Core. CMs publish; they do not each own a philosophy.

## Digital twin

**Derived.** Instantiated from a CM template. Used for capacity, what-if, IST playback, operator training. If twin ≠ BMS/EMS, the SoR wins and the twin is defected.

## Agentic AI (bounded)

| Use | Q03 class | Notes |
| --- | --- | --- |
| Anomaly ranking | S | Not detector of record for trips |
| Maintenance procedures / knowledge | S | Reads the one knowledge base |
| Energy efficiency | S | Band-limited; IST before any auto setpoint |
| Engineering decision support | S | Never silent ICOA change |
| Work-order drafts | S | Human close |

Southbound writes: deny by default, per-CM, logged, dead on cyber/IST/emergency modes (Q06).

## Capacity management

Module counts, feeder headroom, water makeup, transformer spares — twin + CMDB, not a spreadsheet per EPC.
