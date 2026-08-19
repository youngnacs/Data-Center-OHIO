# 02 — Ohio siting and market

Ohio is a real hyperscale market. It is also a constrained one. Siting Heartland as “another New Albany building” would be an architectural failure.

## Market facts the design must absorb (2026)

**Load.** AEP Ohio reported **5,642 MW** of Data Center Tariff contracts plus **12,219 MW** of legacy contracts — **17,861 MW** scheduled through 2035. AEP Ohio’s historic peak is **8,000–10,500 MW**. The campus is arriving into a utility that is already re-rating itself around data centers.

**Tariff.** PUCO approved AEP Ohio Schedule DCT (effective 23 Jul 2025) for customers above 25 MW. Material terms:

- Minimum monthly billing demand up to **85% of contract capacity** (bracketed; large load hits the 85% cap)
- Load ramp **≤ 4 years**, then **8 years firm** (12-year commercial relationship)
- Collateral **50% of total minimum charges** unless the customer (or co-signing sponsor) is **A-/A3** and has cash ≥ **10×** the collateral
- Exit fee = three years of minimum charges, and only after year five of the firm term
- Applies in AEP Ohio territory (Columbus, Canton, Chillicothe, Newark and surrounding). Duke, AES Ohio, and FirstEnergy are different games.

**Tax.** The 100% sales-and-use exemption on qualified data center equipment is **paused for new applications** (May 2026) after costing **$1.6 B in 2025** vs a **$136 M** forecast. Draft bills point to a **50% exemption**, **75% if brownfield + own power**, water reporting, and closed-loop mandates. Heartland’s commercial model **does not depend on 100% exemption**. Brownfield + BTM is the hedge that preserves the 75% path if the bill lands that way.

**Water.** Columbus / Upper Scioto holds **~95% of Ohio’s operating data center capacity** (~1.9 GW, with bullish talk of 10–15 GW). Direct data center water is still a small share of the Scioto system, but **infrastructure delivery, public optics, and local moratoria** are the binding constraints — not statewide hydrology. Eighteen-plus municipalities have considered or enacted pauses. Closed-loop is how the campus stays off that battlefield.

**Capacity market.** PJM capacity prices moved from **$28.92/MW-day (2024/25)** to **$269.92 (2025/26)** to **$329.17 (2026/27)**. Data center load is the dominant cited driver. Heartland’s energy cost model uses **stressed PJM capacity**, not 2023 nostalgia.

## Where not to put the flagship

| Location | Why it is the wrong first site |
| --- | --- |
| New Albany / Licking core | Queue depth, municipal fatigue, Scioto optics, land price, neighbor hyperscalers already holding the 765 kV |
| Inside a moratorium township | Entitlement risk dominates engineering |
| On potable Columbus water as the cooling source | Political and infrastructure risk; fights the cooling constitution |
| A site with only 138 kV in sight | Cannot host a gigawatt without a multi-year transmission project that we do not control |

New Albany remains useful as a **meet-me / cloud on-ramp**, not as the 1,100-acre factory.

## Site strategy: one winner, two backups

Screen for **all** of the following. Fail any one, fail the site.

1. **345 kV on or next to the parcel**, with a constructable second corridor (different ROW) for diversity. 765 kV adjacency is a plus.
2. **AEP Ohio or a utility with a published large-load tariff** so cost shifting is priced, not improvised.
3. **Non-potable or self-sourced water** for process fill and fire; domestic from a rural district is fine.
4. **No municipal moratorium**; township zoning that already names data center or heavy industrial.
5. **Dual long-haul fiber** within a 24-month build, with a path to Columbus carrier hotels.
6. **Geotech that accepts 1,200+ kPa pad loads**, dry-cooler roofs, and a 345 kV yard.
7. **Community that will take a PILOT and apprenticeships** over a lawsuit.

### Track A — Brownfield generation (preferred)

Former AEP (or similar) generating stations: Conesville-class, Muskingum River-class, other retired steam sites.

**Why they win:** existing 138/345/765 kV yards, industrial water permits, rail, a workforce that already understands high voltage, and the **brownfield + own-power** tax path. PJM interconnection is still real work, but starting from a generation node beats a green cornfield tap.

**Why they lose if we are sloppy:** soil remediation, remaining structures, floodplain (Muskingum, Ohio River), and distance to Columbus fiber. Budget a **dark-fiber lateral** as a first-class P0 project, not an afterthought.

### Track B — Greenfield on the 765/345 kV spine, off the Scioto

Madison, Clark, Pickaway, Knox, Muskingum, or southern Union / Champaign — counties that see the AEP backbone but are not the New Albany overlay.

**Why they win:** cleaner geotech, easier pad geometry, potentially friendlier townships, room for BTM generation setbacks.

**Why they lose:** new tap lines (2–4 years), agricultural land politics, and the need to bring water and sewer from scratch.

### Track C — Western / southwestern Ohio (AES or Duke)

Dayton–Cincinnati corridor: smaller existing DC base (~65 MW), **Great Miami buried-valley aquifer**, no AEP DCT.

**Why it is a backup, not the flagship:** different utility (must invent the large-load commercial terms ourselves), weaker 765 kV story, and the campus would be a pioneer rather than a neighbor to an existing hyperscale labor pool. Keep it alive if AEP collateral or queue becomes intolerable.

## Recommended search box

```text
Primary: AEP Ohio 345/765 kV corridor, 40–90 minutes from Columbus, NOT in
         New Albany / Johnstown / Hartford overlay, NOT on Griggs/O'Shaughnessy
         potable allocation.

Parcel:  800–1,400 acres controllable, 400+ acres contiguous buildable,
         two independent HV approaches, rail optional, interstate < 15 miles.
```

P0 delivers a scored matrix of three named parcels. This document does not freeze a county: **the architecture is site-class specific (brownfield-HV vs greenfield-HV), not address-specific**, until G0.

## Interconnection product (commercial architecture)

Do not request 1,600 MW on day one of DCT.

| Contract block | When signed | Purpose |
| --- | --- | --- |
| Block 1 — 250 MW | P0/G1 | Covers P1 site load with margin; 4-year ramp to ~230 MW IT |
| Block 2 — 350 MW | P1 COD | Covers P2; stacked only when P1 load is real |
| Block 3 — 500 MW | P2 | P3 AI factories |
| Block 4 — 500 MW | P3 | P4 + densification + spare |
| BTM | FID per phase | 150–400 MW blocks so DCT contract capacity stays honest |

The 85% ratchet punishes vanity reservations. **Undersize the tariff, oversize the land and the yard.** That is the opposite of how most Ohio announcements are written, and it is why this campus can survive a 12-year contract.

Collateral: assume we are **not** A-/A3 unless the sponsor is a hyperscaler or investment-grade utility affiliate. Treasury must size letters of credit against **50% of 12 years of 85% minimum demand**. That number belongs in the investment memo, not in a footnote.

## Fiber and latency

Columbus is the meet-me. Heartland is a **factory with a dedicated dual lateral**, not a building that hopes a carrier shows up.

- Two providers minimum (e.g. combinations of Zayo, Lumen, Everstream, FirstLight, utility dark fiber)
- Diverse laterals: physically separate ROWs, separate Columbus entries
- Design latency budget: **< 2 ms** to a Columbus carrier hotel, **< 12 ms** to Chicago, **< 15 ms** to Ashburn on lit waves
- Campus MMRs at opposite corners; no single manhole that kills the region

## Climate and natural hazard

ASHRAE 5A: cold winters, humid summers, excellent economizer and dry-cooler hours (~4,500+ hours where dry coolers win without adiabatic assist).

Design for **ice, freeze–thaw, and severe thunderstorm / tornado**. Ohio is not a hurricane coast and not a desert. Failure modes are icing on dry-cooler fins, frozen fire loops, and wind-borne debris — not wet-bulb 32 °C for six months. See [07](07-civil-security.md).

## Labor and logistics

Central Ohio has a proven hyperscale trades base (IBEW, UA, ironworkers, operators). A campus 60–90 minutes out must **bus, lodge, and apprentice**, or it will lose every bid to New Albany. P0 includes a construction village plan and a community-college curriculum (electrical, liquid cooling, HV switching).

Heavy equipment: interstate access for transformers (345 kV GSU-class and 34.5 kV), CDU skids, and prefabricated electrical rooms. Rail on a brownfield site is a transformer-delivery asset.
