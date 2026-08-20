# Naming and tagging

## Asset ID

```text
PORTS.<node>.<discipline>.<object>[.<suffix>]
```

Examples:

- `PORTS.CM03.EL.XFMR.A`
- `PORTS.CM03.ME.CDU.07`
- `PORTS.CORE.EL.345KV.CB.12`
- `PORTS.CORE.IT.BUS.TELEMETRY`

`<node>` is `CM01`–`CM99`, `CORE`, `GEN`, `LOG`, `SEC`. Do not use EPC names (`Bldg-West-2`) as the primary key.

## Point ID

```text
<asset_id>.<measurement>
```

Examples: `PORTS.CM03.EL.XFMR.A.kW`, `PORTS.CM03.ME.CDU.07.leak`.

Alarm **class** is global (`LEAK.ROW`, `UF.SHED`); CM-ID is a dimension.

FAT of any BMS/EMS/CDU includes a **tag compliance pack** against this dictionary (Q09).
