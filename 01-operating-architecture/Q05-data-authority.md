# Q05 — Data authority, ownership, and sharing

**Question:** Which system is the authoritative source for each category of data? Who owns that data, and what information may be shared with operators, customers, vendors, partners, and regulators?

## Decision (v0.1)

Every fact has **one system of record (SoR)**. The twin, AI, and dashboards are **consumers**. Multi-party PORTS (SB Energy, NVIDIA, OpenAI, DOE, AEP, USG generation, regulators) makes this a **contract**, not a wiki.

## System of record table

| Data category | SoR | Owner | Operators | Customer (OpenAI) | NVIDIA | Vendors | AEP / PJM | DOE | Regulators |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Breaker / MW / frequency | EMS / EPMS | Power | Full | Agg. SLA / CM kW | Agg. as needed for LPS | Ticket-scoped | Interconnect points | As DOE requires | As filed |
| CDU / liquid / WUE | BMS | DC / mechanical | Full | Hall WUE/PUE | Optional | Ticket-scoped | No | Water as required | ODNR/OEPA |
| Fire / life safety | Fire panel | EHS | Full | No (except incident) | No | AHJ / vendor | No | If interface | AHJ |
| Identity / access logs | IAM / PAM | Security | Need-to-know | No | No | Session logs | No | As required | As required |
| GPU job / cluster | Scheduler | IT/AI (tenant overlay) | Health only | Full (tenant) | As contract | No | No | No | No |
| Asset / serial / warranty | CMDB | Ops + DC | Full | No | Serial as contract | Their SKUs | No | No | No |
| Work orders | CMMS | Ops | Full | Optional outage windows | As needed | Their jobs | No | No | No |
| Twin / AI features | Derived | ICOA office | Full | Dashboards as leased | As contract | No | No | No | No |
| Community / water public | Published extract | External affairs | Full | May cite | No | No | No | Coordinate | Public |

“Agg.” means **no individual breaker, no protection settings, no camera, no badge.**

## Ownership rules

1. **SoR writes; others subscribe.** If BMS and twin disagree, BMS wins for cooling; the twin has a bug.
2. **Tenant data stays tenant.** Training data, prompts, and job payloads never enter OT historians.
3. **Vendor sees a ticket, not a campus.** Remote access is a Q6 session, not a standing VPN full of tags.
4. **Regulator packs are generated**, not “give them PI access.”
5. **DOE** may have safety/security rights that override convenience — those are Core, documented, tested.

## Classification

| Class | Examples | Default sharing |
| --- | --- | --- |
| OT-Safety | Protection settings, fire | Operators + AHJ |
| OT-Ops | Temperatures, kW, valves | Operators; aggregates up |
| IT-Tenant | Jobs, models | Customer / NVIDIA per lease |
| Business | Cost, contracts | Named finance/legal |
| Public | Annual WUE, community $ | Deliberate publication |

Day-60 deliverable: this table in a data-sharing addendum the lawyers can actually attach.
