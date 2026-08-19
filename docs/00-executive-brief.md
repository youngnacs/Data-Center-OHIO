# 00 — Executive brief

**Program:** Heartland Super Campus (HSC-OH)  
**Horizon:** 2026–2046  
**Ask:** Approve the siting logic, power strategy, and P0 enablement so Ohio can host a durable gigawatt-class campus rather than a stranded first building.

## Recommendation

Authorize a **1,100-acre, 1.2 GW IT campus** on the AEP Ohio 345/765 kV backbone, **outside the New Albany / Upper Scioto choke point**, with **closed-loop liquid cooling as the default** and a **dual power stack**: 1,600 MW of contracted interconnection plus behind-the-meter generation sized to about 30% of site load at full build.

Do not start with a single 48 MW air-cooled hall and “figure out AI later.” The building that is cheap in 2028 and unusable in 2034 is the most expensive building we will ever pour.

## Why Ohio, why now

Ohio is one of the few inland U.S. markets that simultaneously offers:

- AEP's 765 kV transmission spine and PJM market access
- Central-U.S. latency to Chicago, Ashburn, and Dallas
- A construction workforce that has already built hyperscale at New Albany, Marysville, and New Carlisle
- A climate (ASHRAE 5A) that makes dry-cooler heat rejection viable most of the year
- Industrial brownfields with legacy 345 kV yards — the fastest path through a congested interconnection queue

It is also a market under political stress. As of 2026:

- AEP Ohio has **~17.9 GW** of data center load under contract through 2035 against a historic system peak of **8–10.5 GW**
- The PUCO Data Center Tariff imposes an **85% take-or-pay** on large new load, a **4-year ramp + 8-year firm term**, and heavy collateral
- Governor DeWine **paused new sales-tax exemption applications** in May 2026 after the exemption cost **$1.6 B in 2025**
- Proposed legislation would cut the exemption to 50% (75% if brownfield + own power), mandate water reporting, and require closed-loop cooling

A campus that ignores those facts will lose either the queue, the community, or the incentive stack. Heartland is designed to use them.

## What “super scale” means here

Not a 30 MW colo. A **campus that can absorb three AI-factory generations**.

| Layer | 20-year decision |
| --- | --- |
| Land | 1,100 acres with 400 acres of buildable pads, 200 acres of electrical / generation, 200 acres of setback, stormwater, and habitat |
| Power | Dual 345 kV (future 765 kV), on-site 345/34.5 kV, BESS, BTM CCGT now / SMR or H2-ready later |
| Buildings | Type A cloud (48 MW), Type B AI factory (120 MW, two-story), Type C core (18 MW) |
| Cooling | Facility water + CDU + cold plate; dry coolers; adiabatic only on extreme days |
| Network | Dual diverse long-haul into Columbus carrier hotels; 800G now, 1.6T then co-packaged optics |
| Time | Five phases. First IT watt in 2031. Last new hall in 2046. Continuous refresh inside the halls. |

## Capital shape (2026 USD, shell only)

| Block | Order of magnitude |
| --- | --- |
| Land | ~$50 M |
| P0 enablement (substation, civil spine, fiber, water, security) | ~$250 M |
| Buildings at full mix | ~$16–18 B |
| Campus common (yards, loops, roads) | ~$2 B |
| BTM generation (not in the Python shell model) | $0.8–3 B depending on CCGT vs SMR |
| IT gear (owner, not this package) | several times shell, refreshed 3–5 years |

The Python model in this repo prices **shell + campus + land** at about **$19 B** at 1,122 MW IT. That is the number to use for land, EPC, and utility strategy. It is not the all-in enterprise cost.

## Decisions required in P0 (2026–2028)

1. **Site control** on a shortlist of three parcels (see [02](02-ohio-siting.md)), with exclusive utility pre-app on the winner.
2. **Interconnection product**: AEP Schedule DCT at a honest contract capacity, not a vanity MW number we cannot ramp.
3. **Generation path**: offtake + option on a BTM CCGT pad; SMR / long-duration storage as a P3 gate.
4. **Cooling constitution**: closed-loop DLC in every new hall; no evaporative primary.
5. **Community compact**: PILOT, water transparency, apprenticeship seats, and a no-NDA-on-water rule — because the legislature is already writing it.

## What would make this the wrong plan

- A tenant that only needs 20 MW of air-cooled colo for five years. Build a hall in an existing park; do not entitle 1,100 acres.
- A site that cannot see 345 kV within a constructable corridor. Transmission will consume the 20-year schedule.
- A capital stack that cannot post DCT collateral (50% of minimum charges for the full term unless A-/A3 and 10× liquidity).

If those are not the constraints, this is the right plan: **one Ohio campus, twenty years, gigawatt scale, liquid-first, dual-powered, community-legal.**
