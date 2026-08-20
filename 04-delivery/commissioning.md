# Commissioning and IST

Phase 1 later CMs (and all later gigawatts) commission **while neighbors are live** (Q08).

## Sequence (per CM)

1. Construction island complete; construction SSID dead
2. Tag FAT vs dictionary
3. Local protection / leak / fire (class A) — twin not required
4. Connect 34.5 kV to **empty** CM; energize per power desk
5. Liquid fill; closed-loop chemistry
6. Integrated test: power + liquid + BMS + EPMS + bus
7. Fault injection: S1, S2, S7 (bus down), S10 (LOTO) as applicable
8. Scheduler shed API (S4/S12 dry run)
9. Permit-to-production; twin instance goes from IST to production mode

## Roles

Power desk + mechanical desk + ICOA checklist + EPC. AI agents **blocked** southbound in IST mode (Q06).
