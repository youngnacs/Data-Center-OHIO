# PORTS-Pike Technology Campus

**Integrated Campus Operating Architecture (ICOA)** — the system-level constitution that connects **Power + Cooling + Facilities + IT/OT + Data + AI** so Phase 1 (800 MW) can grow to a 10 GW campus without becoming a pile of incompatible islands.

This repository is not a single software system, not an HVAC package, and not a stamped electrical set. It is the **operating architecture** used by the technical interface between the power team, data-center construction team, IT/AI team, and operations team.

## How to read this repository

Read **down** the numbered folders. Each layer is allowed to change only what the layer above has already decided.

| Folder | Question it answers | When it freezes |
| --- | --- | --- |
| [00-program](00-program/README.md) | Why PORTS exists, what “done” means, who must agree | Days 1–30 |
| [01-operating-architecture](01-operating-architecture/README.md) | How the campus works as one system (the ten ICOA questions) | Days 30–90 (v0.9) |
| [02-blueprint](02-blueprint/README.md) | How each domain implements the ICOA | Rolling; P1 locked at design freeze |
| [03-standards](03-standards/README.md) | Repeatable rules (tags, zones, KPIs, gates) | v0.1 at day 60; v1.0 at day 90 |
| [04-delivery](04-delivery/README.md) | 30/60/90 plan, vendors, commissioning, live cutover | 30/60/90 is the near-term calendar |
| [05-operations-and-teams](05-operations-and-teams/README.md) | How we run it and how we hire the capability | Grows through construction into ops |
| [06-roadmap](06-roadmap/README.md) | 800 MW → 10 GW, risks, phase gates | Revisited every phase FID |

Do not start a domain design (chillers, BMS brand, GPU fabric, digital twin vendor) until you can point to the ICOA question it satisfies. That is how PORTS avoids “best-of-breed parts, un-integrable campus.”

```text
PORTS ICOA
│
├── 00-program/                     vision, goals, constraints, interfaces
├── 01-operating-architecture/      ten questions → one operating system
├── 02-blueprint/                   power, cooling, facilities, IT/OT, twin, AI, security
├── 03-standards/                   tagging, telemetry, KPIs, design-review gates
├── 04-delivery/                    30/60/90, EPC/vendors, IST, live expansion
├── 05-operations-and-teams/        run model, staffing, knowledge
├── 06-roadmap/                     Phase 1 800 MW → 10 GW
├── data/assumptions.yaml           executable planning numbers
└── src/ports/                      capacity, tariff, water, module math
```

## Campus facts this architecture assumes

| Item | Basis (public program, 2026) |
| --- | --- |
| Site | PORTS-Pike, Pike County, Ohio — private + remediated DOE land at the former Portsmouth Gaseous Diffusion Plant |
| Phase 1 | **800 MW**, construction 2026, capacity online in steps from **2028** |
| Full campus | **10 GW** class (about **8 GW IT** AI factory + losses; **~9.2 GW** new gas generation, U.S. Government-owned; **$4.2 B** AEP Ohio 765 kV / HV) |
| Compute | NVIDIA exclusive AI infrastructure; OpenAI 20-year lease; SB Energy builds, owns, operates |
| Repeatable unit | **100 MW IT Compute Module (CM)** → Phase 1 = **8 modules** |

These figures are the **program envelope**. Detailed MW, PUE, and water numbers live in `data/assumptions.yaml` and must be updated when owner/EPC packages land.

## The ten questions (ICOA spine)

The first 90 days exist to put a defensible answer in each file — not to finish every engineering calculation.

1. [What is the repeatable campus module?](01-operating-architecture/Q01-campus-module.md)
2. [What belongs in the campus core vs the modules?](01-operating-architecture/Q02-core-vs-distributed.md)
3. [What is autonomous, supervised, or manual?](01-operating-architecture/Q03-autonomy-model.md)
4. [How does IT/OT data move securely?](01-operating-architecture/Q04-it-ot-data-flow.md)
5. [What is the system of record, who owns it, who may see it?](01-operating-architecture/Q05-data-authority.md)
6. [How is external and remote access gated?](01-operating-architecture/Q06-access-control.md)
7. [Which scenarios and failures must we survive?](01-operating-architecture/Q07-scenarios-and-failures.md)
8. [How do we connect new modules to a live campus?](01-operating-architecture/Q08-live-campus-expansion.md)
9. [Where is vendor lock-in acceptable?](01-operating-architecture/Q09-vendor-replaceability.md)
10. [How does 800 MW become 10 GW without operational islands?](01-operating-architecture/Q10-scale-800mw-to-10gw.md)

Plus [additional questions](01-operating-architecture/Q11-additional-questions.md) covering nuclear/utility, BESS, gas turbines, substations, fiber, cyber, HVAC/liquid, water, predictive maintenance, IST, DR, and staffing.

## 30 / 60 / 90 days

The working calendar is [04-delivery/30-60-90-plan.md](04-delivery/30-60-90-plan.md).

- **Day 30:** program freeze + module definition (Q1–Q3) + team RACI
- **Day 60:** data, access, failures, twin/AI backlog, standards v0.1 (Q4–Q7)
- **Day 90:** ICOA v0.9 that Phase 1 drawings must pass (Q8–Q10 + additional)

## Living model

```bash
python3 -m pip install -e ".[dev]"
python3 -m pytest
python3 -m ports roadmap
python3 -m ports plan --year 2030
python3 -m ports module
python3 -m ports cooling --it-mw 800
```

## What this is not

Not a civil package, PE stamp, PJM study, DOE safety-basis document, or NVIDIA cluster design. Those are produced **against** this architecture. If a drawing cannot name its module, its core dependency, its data owner, and its failure domain, it is not ready for PORTS.
