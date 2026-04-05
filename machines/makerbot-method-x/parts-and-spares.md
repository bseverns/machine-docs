# Parts and Spares - MakerBot Method X

**Purpose:** track the high-impact spares and consumables that keep the Method X serviceable.  
**Last inventory check:** TBD  
**Doc audit updated:** 2026-04-04  
**Shelf / bin location:** TBD  
**Primary buyer / maintainer:** Fabrication lab staff  

## Procurement rules

- Record exact MakerBot part numbers and extruder bay compatibility before ordering.
- Distinguish model-material parts from support-material parts; do not assume symmetry.
- Mark unknown numbers as `TBD` instead of guessing.
- Link installs from logs once a part has been field-tested on this machine.

## Critical spares

| Subsystem | Part | Manufacturer part number | Preferred vendor / SKU | Qty on hand | Reorder point | Shelf location | Approved substitute | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Extrusion | Model 1XA extruder | TBD | MakerBot direct or approved reseller | TBD | 1 | TBD | None approved | Track hours and replace only after confirming wear or fault history. |
| Extrusion | Support 2XA extruder | TBD | MakerBot direct or approved reseller | TBD | 1 | TBD | None approved | Keep separate from model-bay inventory to avoid mix-ups. |
| Build surface | Flex build plate | TBD | MakerBot direct | TBD | 1 | TBD | None approved | Replace if adhesion, flatness, or keyed alignment degrades. |
| Material handling | Spool bay desiccant / humidity consumables | TBD | MakerBot direct or approved equivalent | TBD | TBD | TBD | TBD | Verify the local replacement interval. |
| Filtration | HEPA / carbon filter kit | TBD | MakerBot direct | TBD | 1 | TBD | TBD | Confirm exact kit and interval from OEM docs. |

## Consumables

| Item | Spec | Preferred source | Qty on hand | Reorder point | Notes |
| --- | --- | --- | --- | --- | --- |
| Model materials | Approved ABS, ASA, PC-ABS, Nylon CF where authorized | Approved lab vendors | TBD | TBD | Match stock to the approved materials matrix. |
| Support materials | SR-30 and approved support stock | Approved lab vendors | TBD | TBD | Track use and disposal practice in [`materials.md`](./materials.md). |
| Plate prep / cleaning supplies | Method-safe prep and cleaning materials | Lab stock | TBD | TBD | Follow OEM guidance; avoid improvised chemistries. |

## Parts we do not keep stocked

| Part | Why not stocked | Typical lead time | Trigger to order | Notes |
| --- | --- | --- | --- | --- |
| Mainboard / controller assemblies | High cost, low routine failure rate | TBD | Persistent motion, power, or chamber control faults | Capture exact board and bay identifiers during physical audit. |
| Chamber heater components | Specialized and low-frequency replacement | TBD | Chamber heat faults confirmed through troubleshooting | Escalate before ordering. |
| Door / enclosure panels | Bulky and rarely needed | TBD | Damage affecting sealed operation or safety | Review incident history before ordering. |

## Sources

- [MakerBot Method X user guide (PDF)](https://downloads.makerbot.com/manuals/MakerBot_MethodX_UserGuide.pdf) - accessed 2026-04-04
- [MakerBot support: Method X topic](https://support.makerbot.com/s/topic/0TO6S000000PC4EWAW/method-x) - accessed 2026-04-04
