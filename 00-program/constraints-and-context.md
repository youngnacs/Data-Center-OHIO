# Constraints and context

Architecture that ignores PORTS’ actual envelope will be elegant and unused. These constraints are design inputs.

## Site

- **PORTS-Pike Technology Campus**, Pike County, Ohio (Scioto Township / Piketon area).
- Former **Portsmouth Gaseous Diffusion Plant** — DOE-managed industrial area with long-running D&D / remediation. The technology campus sits on **private and remediated DOE land**, adjacent to remaining cleanup. Safety-basis, residual contamination, and DOE interface are **campus-core** issues, not hall fit-out issues.
- Climate: **ASHRAE 5A**. Ice, freeze–thaw, and severe thunderstorms matter more than wet-bulb 32 °C.

## Program envelope (public, 2026)

| Item | Envelope |
| --- | --- |
| Phase 1 | **800 MW**, construction start 2026, capacity from **2028** in steps |
| Full build | **10 GW** class campus; ~**8 GW IT** AI factory capacity in partner materials |
| Generation | New on-site / dedicated generation including **~9.2 GW natural gas**, described as **U.S. Government-owned**, funded in part via the U.S.–Japan Strategic Trade and Investment Agreement (~**$33 B** gas generation) |
| Grid | SB Energy **$4.2 B** through **AEP Ohio** for HV / **765 kV** transmission; stated **no ratepayer** funding of those upgrades |
| Compute | **NVIDIA** exclusive AI compute infrastructure provider |
| Customer | **OpenAI**, 20-year lease; SB Energy build / own / operate |
| Community | Combined **$80 M** community benefits (SB Energy + OpenAI) |
| Jobs (program-scale) | Construction and operating figures are large; Phase 1 ops is hundreds, full build thousands |

Treat press-range dollars as **context**, not as the cost model. The living model in `data/assumptions.yaml` tracks **module counts and IT MW**. Generation and 765 kV are separate FIDs that the ICOA must still **integrate**.

## Power market and Ohio

- AEP Ohio **Data Center Tariff** (2025): 85% take-or-pay class terms, 4-year ramp + 8-year firm, heavy collateral — even with behind-the-meter generation, **grid interconnection product design still matters**.
- PJM capacity prices have spiked; PORTS’ generation-first strategy is the response, not an optional green feature.
- Ohio water and tax politics (exemption pause, closed-loop proposals) still apply. Closed-loop liquid is the cooling constitution.

## What this means for architecture

1. **Generation and the AI factory are one campus.** The ICOA must include gas turbines, BESS, substations, and (later) nuclear options as first-class objects, not “utility stuff over the fence.”
2. **DOE adjacency is a security and safety domain.** Physical, cyber, and data-sharing rules are stricter than a greenfield cornfield campus.
3. **800 MW is already super-scale.** Phase 1 is eight 100 MW modules, not a pilot hall. If P1 is not copyable, 10 GW is impossible.
4. **NVIDIA + OpenAI + SB Energy + DOE + AEP** is a multi-sovereign data problem. Q5 (authority) and Q6 (access) are not IT hygiene; they are the project.
