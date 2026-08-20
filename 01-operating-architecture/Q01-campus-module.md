# Q01 — Repeatable campus module

**Question:** What physical, operational, and digital components constitute a repeatable and scalable campus module?

## Decision (v0.1)

The unit of scale is the **Compute Module (CM): 100 MW IT**, liquid-cooled, two-story AI factory geometry, Titanium-Compute electrical SLA. Phase 1 is **eight CMs**. Full campus is on the order of **eighty CMs** (~8 GW IT) on a 10 GW energy envelope.

A CM is copyable only if **physical + operational + digital** copy together. A repeated building with a unique BMS tag dictionary is not a module; it is a future island.

## Physical (inside the CM fence)

| Layer | In the module | Not in the module |
| --- | --- | --- |
| Structure | Hall(s), CDU gallery, roof/yard dry coolers, leak containment | 345 kV yard, generation pad |
| Power | 34.5 kV feeders in, block-redundant conversion, row bus, CM BESS ride-through | 765/345 kV, GT, campus BESS energy shifting |
| Cooling | Closed-loop DLC, CDUs N+1, pumps, leak detect/isolate-to-row | Campus makeup plant, fire tanks |
| IT | GPU floor, train fabric, leaf/spine for the module, OOB | Campus MMRs, core identity, WAN |
| Life safety | Hall fire, VESDA, egress, coolant SDS | Campus fire command, security rings |
| Civil | Pad, local storm, transformer alley stub | Loop road, habitat, DOE fence line |

Design envelope: **80–150 kW/rack now, structure and pipe for 200 kW**. Average planning figure: **100 kW/rack** → ~1,000 racks per CM.

## Operational (how a CM is run)

Each CM has:

- A **named operating state**: construction / IST / energized-empty / production / isolated / decommission
- A **single incident commander** path (power desk ↔ mechanical desk) using the same runbook ID as every other CM
- **Work-order and LOTO** templates that differ only by CM-ID
- **Autonomy bounds** from [Q03](Q03-autonomy-model.md) — a CDU may isolate a row; a CM may not open a 345 kV breaker

## Digital (what must be identical)

| Object | Standard |
| --- | --- |
| Asset ID | `PORTS.CM{nn}.{discipline}.{object}` — see [../03-standards/naming-and-tagging.md](../03-standards/naming-and-tagging.md) |
| Telemetry | Same points list (kW, flow, temp, leak, breaker, CDU health) published to the campus bus |
| Alarms | Same class IDs; CM-ID is a dimension, not a new philosophy |
| Digital twin | One CM twin template, instantiated 8× then N× |
| Scheduler hook | Standard “shed / checkpoint / inhibit” API so NVIDIA/OpenAI jobs see a campus, not eight snowflakes |

## What is *not* a module

- A “phase” (Phase 1 is eight modules plus core)
- A vendor package (a CDU skid is a **component**)
- The Campus Core (there is one core; see [Q02](Q02-core-vs-distributed.md))

## Phase 1 test

If CM-01 and CM-08 cannot share IST scripts, spare parts, operator qualification, and twin dashboards without translation tables, the module definition has failed — even if both are 100 MW.
