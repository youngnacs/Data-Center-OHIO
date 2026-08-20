# Q09 — Vendor replaceability

**Question:** How easily can equipment, technologies, and vendors be replaced without redesigning the entire campus? Where is vendor standardization beneficial, and where is vendor independence necessary?

## Decision (v0.1)

**Standardize the interfaces. Compete the boxes.** Thirty-year layers (HV, ducts, tags, zones, module geometry) must not be proprietary. Three-to-seven-year layers (CDU skids, GPUs, BMS servers, agents) must be swappable.

NVIDIA exclusivity on **AI compute** is a program fact. It does **not** grant any OEM a monopoly on BMS, EMS, CDUs, or the twin.

## Standardize (lock for P1, copy to 10 GW)

| Layer | Why lock |
| --- | --- |
| CM geometry, loads, pipe diameters, electrical SLA | Copy/paste civil |
| Tag dictionary and alarm classes | Twin, AI, ops |
| OT zones and PAM | Security |
| IST scripts and LOTO templates | Safety |
| 34.5 kV campus voltage class | Spares |
| Closed-loop liquid constitution | Water politics + density |

Picking **one** CDU OEM and **one** BMS OEM for Phase 1 is allowed **if** gateways emit the standard tags. That is standardization of *fleet*, not of *ICOA*.

## Keep replaceable (adapters required in the contract)

| Layer | Independence mechanism |
| --- | --- |
| BMS / EPMS brand | Gateway + tag FAT |
| CDU / cold plate OEM | Hydraulic and protocol spec |
| Historian / twin / AI platform | Bus is SoR-adjacent; apps are consumers |
| CMMS / ITSM | API |
| GPU generation (inside NVIDIA path) | CM envelope 200 kW/rack |
| Dry coolers | Performance spec, Ohio ice |
| BESS integrator | Electrical spec, NFPA 855 |

## May be single-source (document the lock)

| Layer | Reason |
| --- | --- |
| NVIDIA compute | Program |
| AEP interconnection product | Utility |
| USG-owned generation | Program |
| Certain DOE security systems | Site |
| 765 kV OEM once selected | Lead time / spares — still specify a spare strategy |

## Contract language the ICOA office insists on

- Point lists and protocols in **our** dictionary, not only native
- 5-year data-export and 90-day transition assistance
- No license that dies if we change the twin vendor
- Spare-part pricing and firmware escrow for OT

## Test

If replacing the BMS in CM-05 requires retagging CM-01..04 or rewriting the agent, Q09 has failed.
