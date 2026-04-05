# Parts and Spares - MakerBot Sketch+

**Purpose:** track the replacement parts and consumables that keep the large-format Sketch online.  
**Last inventory check:** TBD  
**Doc audit updated:** 2026-04-04  
**Shelf / bin location:** TBD  
**Primary buyer / maintainer:** Fabrication lab staff  

## Procurement rules

- Record exact MakerBot part numbers before reordering.
- Keep large-format-specific parts separate from standard Sketch stock where incompatibility is possible.
- Mark unknown numbers as `TBD` rather than inferring compatibility.
- Link installs from logs after a part is proven in service.

## Critical spares

| Subsystem | Part | Manufacturer part number | Preferred vendor / SKU | Qty on hand | Reorder point | Shelf location | Approved substitute | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Toolhead | Sketch+ hot-end / extruder assembly | TBD | MakerBot direct or approved reseller | TBD | 1 | TBD | None approved | Confirm compatibility with Sketch+ hardware before swapping with standard Sketch stock. |
| Build surface | Large flexible steel build plate | TBD | MakerBot direct | TBD | 1 | TBD | None approved | Replace if warping, gouging, or pin misalignment affects first-layer consistency. |
| Motion | Z lead screw / synchronization hardware | TBD | TBD | TBD | 1 set | TBD | None approved | Capture exact spare strategy after physical audit. |
| Filtration | HEPA / enclosure filter kit | TBD | MakerBot direct | TBD | 1 | TBD | TBD | Confirm filter service interval in OEM docs. |
| Sensors | Filament runout sensor assembly | TBD | TBD | TBD | 1 | TBD | None approved | Verify fault is not spool drag or feed path friction before ordering. |

## Consumables

| Item | Spec | Preferred source | Qty on hand | Reorder point | Notes |
| --- | --- | --- | --- | --- | --- |
| Filament | 1.75 mm approved PLA, Tough PLA, PETG, support material | Approved lab vendors | TBD | TBD | Keep support-material policy synced with [`materials.md`](./materials.md). |
| Plate cleaning supplies | Build-surface-safe wipes / IPA | Lab stock | TBD | TBD | Avoid damaging the coated surface. |
| Removal tools | Plastic scraper | Lab stock | TBD | 1 | Do not pry against alignment pins. |

## Parts we do not keep stocked

| Part | Why not stocked | Typical lead time | Trigger to order | Notes |
| --- | --- | --- | --- | --- |
| Mainboard / controller | Higher cost, lower failure rate | TBD | Motion or power faults confirmed beyond serviceable harness issues | Record exact board identifier during physical audit. |
| Door / enclosure panels | Bulky and low-use | TBD | Damage affecting safe enclosed operation | Review incident history before ordering. |
| Camera module | Non-critical to basic operation | TBD | Workflow requires camera and failure is confirmed | Confirm whether the installed workflow depends on camera health. |

## Sources

- [MakerBot Sketch+ tech specs (PDF)](https://downloads.makerbot.com/manuals/MakerBot_SKETCHPlus_TechSpecs.pdf) - accessed 2026-04-04
- [MakerBot support: Sketch+ knowledge base](https://support.makerbot.com/s/article/1667416063609) - accessed 2026-04-04
