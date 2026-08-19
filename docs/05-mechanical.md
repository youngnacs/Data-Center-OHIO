# 05 — Mechanical and cooling architecture

Cooling is the other half of power. In Ohio in 2026 it is also **politics**.

## Constitution

1. **No evaporative primary cooling** on any new hall.
2. **Closed-loop DLC** is the Type B baseline and the Type A refresh path.
3. Water on site is for **fill, makeup, domestic, and fire** — not for dumping heat into vapor every summer afternoon.
4. Heat rejection is **dry coolers first**, adiabatic assist only above a high outdoor-dry-bulb threshold, metered and reported.

This is not a green slogan. It is how the campus remains buildable if the General Assembly mandates closed-loop systems and water reporting, and how it stays off Upper Scioto optics even if the site is not on the Scioto.

## Ohio climate (ASHRAE 5A)

Columbus-class weather: cold winters, shoulder seasons that are a gift, humid but not Gulf-Coast summers. Design dry-bulb ~35 °C for dry coolers. Thousands of hours where liquid loops reject heat with **no water and little mechanical cooling**.

Winter is the real mechanical risk: **icing on dry-cooler coils, freeze of neglected piping, stratification**. Specify coil geometry, defrost, glycol strategy, and maintenance access for ice, not for a Phoenix brochure.

## Thermal chain — Type B

```text
GPU / CPU cold plate
    → facility liquid (PG25 or specified dielectric via CDU isolation)
        → CDU gallery (N+1 skids, redundant pumps)
            → warm facility water
                → dry cooler field (roof + yard)
                    → optional adiabatic pads on 95th–99th percentile days
```

- **CDUs** are the unit of maintainability. Hot-swap, isolation valves, leak detection, and a spare skid per hall.
- **Two-story** Type B: liquid and optical risers in dedicated shafts; no “we’ll core it later.”
- **Leak philosophy:** detect, isolate a row, keep the hall. Coolant selection (inhibited glycol vs dielectric) is a P1 specification with fire, material compatibility, and ops training — not a vendor surprise.

## Thermal chain — Type A and Type C

- Air economizer / CRAH as primary for 8–15 kW racks
- **Rear-door or in-row** for the hot 20–30 kW islands that appear the day after COD
- **Empty liquid mains** in the ceiling or gallery, valved and flushed, so a 2034 refresh does not take the hall down for a year
- Type C stays conservative: no experiments, 2N mechanical, independent from Type B plants

## Plant topology

- **Building-level plants**, not one mega-chiller yard for 1.2 GW. A campus-wide single plant is an outage domain.
- Shared **make-up water, water treatment, and glycol storage** at campus level.
- Process-water mains sized for **200 kW/rack on Type B pads** even if P1 lands at 80–100 kW.
- Prefabricated pump/CDU modules. Ohio winter construction calendar is not theoretical.

## Water budget

Order of magnitude from the living model at 1,200 MW IT:

| Mode | Annual water |
| --- | --- |
| Closed-loop campus (design WUE ~0.03 L/kWh) | tens of millions of gallons |
| Evaporative counterfactual (~1.8 L/kWh) | **an order of magnitude more** — hundreds of millions of gallons |

P1 fill is a one-time industrial water event. After that, makeup is leaks, sampling, and adiabatic-assist hours. **Instrument WUE continuously** and publish a yearly figure as part of the community compact.

Sources, in preference order:

1. Non-potable / industrial / reuse
2. On-site well (with ODNR) where hydrogeology allows
3. Rural district surplus
4. Potable municipal — last, and never for heat rejection

Fire water is a separate, large, code-driven tank farm. Do not combine mentally with cooling makeup.

## Heat reuse

Ohio winters make **heat reuse real** if a customer sits on the fence line: greenhouse, industry, or a district loop. It is a P2 option on the south / generation side of the campus, not a P1 promise. Do not let a reuse customer become a single point of thermal rejection.

## Refrigerants and ASHRAE 15

If any DX remains (CRAH, office, network closets), pick a low-GWP path that will still be legal in 2036. Do not build a 20-year campus on a refrigerant that is already being phased out.

## Controls

- One campus BMS/EPMS with hall autonomy: a dead campus controller must not trip every CDU
- Tight coupling to the power desk (see [04](04-electrical.md)): liquid pumps are electrical load; GPU power is thermal load
- Water meters on every makeup path, reported the way OEPA/ODNR will eventually require

## What we explicitly reject

- Cooling towers as the Type B workhorse
- “We’ll add liquid in phase 2” without the mains in the slab
- A single 1 GW chilled-water loop
- Using Columbus potable water as a heat sink
