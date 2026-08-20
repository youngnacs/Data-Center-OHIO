# Blueprint — IT, OT, and network

## OT

Purdue-style zones, per-CM process networks, campus protection network, OT DMZ with the telemetry bus ([Q04](../01-operating-architecture/Q04-it-ot-data-flow.md)). No GPU VLAN on BMS.

## IT / AI fabric

NVIDIA path is exclusive for compute. Still: **standard CM envelope, standard shed API, standard OOB**. Tenant payloads never enter historians (Q05).

## WAN

Two MMRs, two laterals, two providers. Latency is a Core SLA. Brownfield/DOE routing is a P0 path equal to HV.

## Time

GPS/PTP for relays **and** fabric; holdover; not a best-effort NTP from corporate IT.
