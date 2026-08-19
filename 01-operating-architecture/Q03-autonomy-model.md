# Q03 — Autonomy model

**Question:** Which systems must operate autonomously, which require human supervision, and which should remain entirely manual?

## Decision (v0.1)

Speed of physics decides, not vendor marketing. Protection and leak isolation are autonomous. Generation and hall energization are supervised. Opening the campus to a vendor or changing ICOA standards is manual.

Agentic AI starts **supervised / advisory**. It earns closed-loop rights only inside the autonomous band, with an inhibit, and only after IST.

## Control matrix

| Class | Meaning | Examples | Human role |
| --- | --- | --- | --- |
| **A — Autonomous** | Must act in cycles faster than a desk | Relay trip, CDU leak isolate-to-row, fire release per code, under-frequency load shed of Titanium jobs, BMS interlock | After-action review; never “approve the trip” |
| **S — Supervised** | Machine proposes or holds a setpoint; human confirms or a bounded policy confirms | GT dispatch, CM energize/de-energize, breaker close after IST, AI anomaly → work order, energy-mode changes, vendor remote session enable | Power/mechanical desk; recorded |
| **M — Manual** | Procedure, two-person, or governance | 345/765 kV first-time switching, DOE notifications, regulatory reports, ICOA changes, new vendor in the trust list, bypass of safety interlock | Named authority |

## AI-specific

| Use case | Day-90 class | Later path |
| --- | --- | --- |
| Equipment anomaly ranking | S (advisory) | S with auto work-order draft |
| Maintenance procedure retrieval | S | S |
| Energy-efficiency recommendations | S | A only for *non-safety* setpoints inside a band |
| Knowledge management | S | S |
| Engineering decision support | S | S — never autonomous design change |
| Closed-loop CDU or GPU shed | **Not allowed** until A-class IST and Q6 inhibit | A with desk inhibit |

## Operating modes that change the matrix

Access and autonomy **collapse toward M** when:

- Campus in **emergency** or **island**
- **Unknown** alarm flood
- **IST / first energization** of a CM
- **Cyber yellow/red** (see [Q06](Q06-access-control.md))

A digital twin or agent that keeps writing setpoints during those modes is a hazard. Default: **shed AI closed-loop, keep protection autonomous, keep desks in charge.**
