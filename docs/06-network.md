# 06 — Network and fiber architecture

A gigawatt campus with one fiber path is a warehouse. Heartland is a **region**.

## Off-campus

- **Two long-haul laterals**, diverse ROWs, diverse Columbus entries, diverse providers.
- Terminate in **two campus MMRs** (east and west). A backhoe in one manhole cannot isolate Ohio.
- Lit and dark: own or IRU enough dark fiber that 2040’s 1.6T and CPO generations are a transponder swap, not a new ditch.
- Latency budgets: **< 2 ms** to Columbus meet-me, competitive inland paths to Chicago and Ashburn.
- If the site is a brownfield on the river, the lateral **is a P0 critical path** equal to the 345 kV tap.

## Campus outside plant

- Duct banks along the loop road: **2× P1 count**, innerduct, traceable, never under a Type B slab.
- Diverse campus rings for:

  - Production WAN
  - AI / research fabric (if physically separate)
  - Out-of-band / ILO / serial
  - Physical security and BMS (isolated)
  - Utility teleprotection (IEC 61850) — **not** on the IT LAN

## Inside the halls

### Type A / C

Classic leaf-spine, EVPN, 100/400G today, 800G as the P1 standard optic, 1.6T planned. Type C holds anycast services, DNS, PKI, and the campus route reflectors.

### Type B

The AI factory network is a **first-class building system**:

- Rail-optimized Ethernet (RoCE) or InfiniBand — tenant choice, **structured cabling and tray sized for either**
- Two-story geometry exists to shorten the diameter of the training domain
- Optical circuit switching / co-packaged optics appear in P2–P4; leave **power, cooling, and tray** for them in P1
- Do not share the Type B fabric control plane with the corporate campus LAN

## Time, out-of-band, and the electrical desk

- GPS/PTP for both the GPU fabric and the 34.5 kV relaying — with holdover
- Out-of-band network survives a production fabric disaster
- Power-desk automation and job-scheduler signals (checkpoint, load-shed) need a **deterministic, isolated** path

## Security of the network

- Zero-trust between halls; Type C is the trust anchor
- MMR cages as physically dual-control as the 345 kV yard
- No “temporary” construction Wi-Fi that becomes the BMS in 2029

## 20-year optic plan

| Window | Campus standard |
| --- | --- |
| P1 | 400/800G, SMF spine, dual vendor |
| P2 | 800G ubiquitous, 1.6T on Type B spine |
| P3 | CPO/CBO trials in one Type B |
| P4 | CPO default on new halls; SMF plant still valid |

The **fiber plant is the 40-year asset**. Transponders are consumables.
