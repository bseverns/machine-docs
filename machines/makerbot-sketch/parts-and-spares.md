# Parts and Spares - MakerBot Sketch

**Purpose:** track the parts and consumables that keep this printer running without last-minute sourcing.  
**Last inventory check:** TBD  
**Doc audit updated:** 2026-04-04  
**Shelf / bin location:** TBD  
**Primary buyer / maintainer:** Fabrication lab staff  

## Procurement rules

- Record exact MakerBot part numbers before reordering from memory.
- If a replacement part is not OEM, note who approved it and what test verified it.
- Mark unknown numbers as `TBD` instead of guessing.
- Link successful installs from the maintenance or incident log once available.

## Critical spares

| Subsystem | Part | Manufacturer part number | Preferred vendor / SKU | Qty on hand | Reorder point | Shelf location | Approved substitute | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Toolhead | Smart Extruder-style hot-end assembly | TBD | MakerBot direct or approved reseller | TBD | 1 | TBD | None approved | Replace only after logging symptoms and confirming the failure is not filament path related. |
| Build surface | Flexible build plate | TBD | MakerBot direct | TBD | 1 | TBD | None approved | Keep one clean spare to reduce downtime after plate damage. |
| Filtration | Chamber filter / particulate media | TBD | MakerBot direct | TBD | 1 | TBD | TBD | Confirm exact filter kit part number from OEM docs or current inventory. |
| Feed path | PTFE tube / feed guide | TBD | TBD | TBD | 1 | TBD | None approved | Capture exact length and connector style during next physical audit. |
| Sensors | Filament runout sensor assembly | TBD | TBD | TBD | 1 | TBD | None approved | Order only after verifying sensor failure versus spool drag. |

## Consumables

| Item | Spec | Preferred source | Qty on hand | Reorder point | Notes |
| --- | --- | --- | --- | --- | --- |
| Filament | 1.75 mm MakerBot-approved PLA, Tough PLA, PETG | Approved lab vendors | TBD | TBD | Keep color and material approvals synced with [`materials.md`](./materials.md). |
| Plate cleaning supplies | Build-surface-safe wipes / IPA | Lab stock | TBD | TBD | Do not use solvents that damage the coated surface. |
| Removal tools | Plastic scraper | Lab stock | TBD | 1 | Avoid metal tools that gouge the plate. |

## Parts we do not keep stocked

| Part | Why not stocked | Typical lead time | Trigger to order | Notes |
| --- | --- | --- | --- | --- |
| Mainboard / controller | Higher cost, lower failure rate | TBD | Power or motion faults confirmed beyond harness issues | Capture exact board identifier during physical audit. |
| Door / enclosure panels | Bulky and rarely needed | TBD | Damage affecting safe enclosure use | Consider ordering only after incident review. |
| Camera module | Non-critical to basic printing | TBD | Repeated queue workflow issues that require camera confirmation | Verify whether the installed workflow depends on camera health. |

## Sources

- [MakerBot SKETCH user guide (PDF)](https://downloads.makerbot.com/manuals/MakerBot_SKETCH_User_Guide.pdf) - accessed 2026-04-04
- [MakerBot support: SKETCH resource hub](https://support.makerbot.com/s/article/1667416063529) - accessed 2026-04-04
