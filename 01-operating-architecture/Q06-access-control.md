# Q06 — External and remote access

**Question:** How should external and remote access be authenticated, authorized, monitored, limited, or blocked based on security policies, operational conditions, alarms, and predefined events?

## Decision (v0.1)

**Deny by default.** Every external path (vendor, OEM, corporate remote, tenant NOC, regulator viewer, agent) is a **named session** with a time bound, a zone bound, and an operational-mode bound.

Identity is Campus Core. A CM must not grow its own VPN culture.

## Who can connect

| Subject | Path | Standing? |
| --- | --- | --- |
| On-site operator | Physical + IAM | Yes, role-based |
| Remote SB Energy NOC | Privileged access mgmt (PAM), MFA, device posture | Yes, Gold |
| OpenAI / NVIDIA | Tenant IT only; OT via **aggregates and tickets** | Contractual, not OT admin |
| OEM / EPC | PAM broker, recorded, CM-scoped | **No** standing; per work order |
| Agentic AI | Service identity, southbound allow-list | Yes, but Q3-bounded |
| AEP / plant operator | Interconnect ICCP or agreed ICS only | Yes, those points only |

## Policy states (campus mode)

| Mode | Vendor remote | AI southbound | Tenant OT views |
| --- | --- | --- | --- |
| **Normal** | PAM if work order active | Advisory + listed setpoints | Aggregates |
| **IST / first energize** | On-site preferred; remote dual-control | **Blocked** | Restricted |
| **Alarm flood / unknown** | Freeze new sessions | **Blocked** | Restricted |
| **Cyber yellow** | Existing sessions reviewed; new = security + ops | **Blocked** | Restricted |
| **Cyber red / island / emergency** | **Blocked** except named emergency OEM under escort | **Blocked** | **Blocked** |
| **DOE / physical security event** | Per security command | **Blocked** | **Blocked** |

Modes are **inputs to the access engine**, not an email. BMS, EMS, and IAM must read the same campus mode tag.

## Controls that must exist in Phase 1

- MFA + hardware-backed identity for any OT-adjacent human
- PAM recording for vendors
- Jump hosts in OT DMZ; no direct RDP to a CDU
- Certificate rotation; no shared “Siemens” passwords
- Session kill switch on the power desk **and** security desk
- Monitoring: who, from where, which CM, which tag writes

## Explicit blocks

- Direct internet to BMS/EMS
- GPU cluster as a path into OT
- Twin admin credentials reused on OT
- “Temporary” construction Wi-Fi that survives COD (see Q8)
