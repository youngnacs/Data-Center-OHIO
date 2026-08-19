# Vendors, platforms, EPCs, integrators

The ICOA office does **not** pick winners in a vacuum. It owns **technical scoring** so procurement cannot buy eight islands.

## What we score (every major package)

| Lens | Fail if |
| --- | --- |
| Module boundary | Package spans Core + CM without a split |
| Tags / bus | Native-only, no dictionary FAT |
| Zones | Requires flat Level-2/IT merge |
| Autonomy | Cloud AI must write breakers to “work” |
| Live expansion | Needs campus blackout to add a peer |
| Replaceability | License or protocol dies at swap (Q09) |
| Ohio / DOE | No ice story, no site security story |
| Ops | No LOTO, no spares lead time, no PAM |

## Classes (illustrative — not a down-select)

- **EPC / integrator:** must execute IST against S-IDs, not only substantial completion photos
- **EMS / protection:** SoR for electrical; IEC 61850 mapping
- **BMS / CDU / liquid:** SoR for mechanical; gateway required
- **BESS / GT OEM:** Core; island interface
- **Twin / historian / AI ops:** consumers; never SoR
- **PAM / IAM:** Core; Q06 engine
- **NVIDIA / cluster:** tenant compute; shed API to bus

## Process

Day 60: scoring sheet in use. Day 90: sheet is an RFP appendix. Bake-offs happen **on CM-01 tags**, not slideware.
