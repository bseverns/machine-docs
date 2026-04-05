# Parts and Spares - LulzBot Mini 3

**Purpose:** track the parts and consumables that keep the Mini 3 supportable in lab use.  
**Last inventory check:** TBD  
**Doc audit updated:** 2026-04-04  
**Shelf / bin location:** TBD  
**Primary buyer / maintainer:** Fabrication lab staff  

## Procurement rules

- Record exact LulzBot part numbers before reordering.
- Distinguish toolhead, nozzle, and build-surface parts clearly; do not merge them into generic "printer spares."
- Mark unknown numbers as `TBD` instead of guessing.
- Link installs from logs after a part is proven in service.

## Critical spares

| Subsystem | Part | Manufacturer part number | Preferred vendor / SKU | Qty on hand | Reorder point | Shelf location | Approved substitute | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Toolhead | HE 0.5 toolhead / service assembly | TBD | LulzBot direct or approved reseller | TBD | 1 | TBD | None approved | Replace only after troubleshooting rules out filament and wiring faults. |
| Toolhead | 0.5 mm nozzle / hot-end consumables | TBD | TBD | TBD | 2 | TBD | TBD | Capture exact compatible nozzle and hot-end part numbers from OEM docs. |
| Build surface | Reversible bed plate / PEI plate | TBD | LulzBot direct | TBD | 1 | TBD | None approved | Keep one ready if adhesion quality drops due to damage. |
| Wipe system | Nozzle wipe pads / service kit | TBD | TBD | TBD | 2 sets | TBD | TBD | Replace whenever wiping becomes inconsistent or contamination builds up. |
| Sensors | Probe / leveling-related service parts | TBD | TBD | TBD | 1 | TBD | None approved | Confirm exact field-replaceable parts during physical audit. |

## Consumables

| Item | Spec | Preferred source | Qty on hand | Reorder point | Notes |
| --- | --- | --- | --- | --- | --- |
| Filament | 1.75 mm LulzBot-profiled materials | Approved lab vendors | TBD | TBD | Keep material approval synced with [`materials.md`](./materials.md). |
| Plate cleaning supplies | PEI-safe wipes / IPA | Lab stock | TBD | TBD | Avoid damaging the PEI surface. |
| Removal tools | Plastic scraper | Lab stock | TBD | 1 | Do not gouge the build plate. |

## Parts we do not keep stocked

| Part | Why not stocked | Typical lead time | Trigger to order | Notes |
| --- | --- | --- | --- | --- |
| Mainboard / controller | Higher cost, lower routine failure rate | TBD | Persistent motion, power, or firmware faults | Capture exact board identifier during physical audit. |
| PSU / power components | Low-frequency replacement | TBD | Voltage instability or visible damage | Escalate before ordering. |
| Frame / motion hardware | Rarely needed as stock spares | TBD | Crash damage, bearing noise, or motion backlash confirmed | Add exact axis hardware specs after physical audit. |

## Sources

- [LulzBot Mini 3 product page](https://www.lulzbot.com/products/lulzbot-mini-3) - accessed 2026-04-04
- [OHAI: LulzBot Mini 3 guides](https://ohai.lulzbot.com/project/lulzbot-mini-3/) - accessed 2026-04-04
