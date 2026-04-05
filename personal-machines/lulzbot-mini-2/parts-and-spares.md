# Parts and Spares - LulzBot Mini 2

**Purpose:** keep procurement repeatable and keep downtime caused by missing parts to a minimum.  
**Last inventory check:** TBD  
**Doc audit updated:** 2026-04-04  
**Shelf / bin location:** TBD  
**Primary buyer / maintainer:** Ben Severns  

## Procurement rules

- Do not order from descriptions alone when an exact part number exists.
- Rows marked `TBD` still need physical or invoice confirmation.
- If a substitute has not been tested on this machine, it is not approved just because it "looks right."
- When a part gets installed, link the maintenance note or experiment that proved it.

## Critical spares

| Subsystem | Part | Manufacturer part number | Preferred vendor / SKU | Qty on hand | Reorder point | Shelf location | Approved substitute | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Controller | Einsy Retro 1.0a spare board | TBD | UltiMachine direct or verified reseller | TBD | 1 | TBD | None approved | Keep one ready to flash before emergency swaps. |
| Toolhead | Titan Aero nozzle, 0.5 mm, 2.85 mm setup | TBD | TBD | TBD | 2 | TBD | None approved | Capture exact nozzle spec and vendor after next order. |
| Toolhead | Heater cartridge | TBD | TBD | TBD | 1 | TBD | None approved | Confirm wattage and connector style from installed hardware. |
| Toolhead | Thermistor / sensor lead | TBD | TBD | TBD | 1 | TBD | None approved | Match installed harness length before ordering. |
| Build surface | Magnetic flex plate / PEI sheet | TBD | LulzBot or approved equivalent | TBD | 1 | TBD | TBD | Replace once surface damage affects adhesion consistency. |
| Maintenance | Nozzle wipe pads | TBD | TBD | TBD | 2 sets | TBD | TBD | Replace in pairs and note the date in maintenance history. |

## Consumables

| Item | Spec | Preferred source | Qty on hand | Reorder point | Notes |
| --- | --- | --- | --- | --- | --- |
| Filament | 2.85 mm PLA / PETG / approved materials | LulzBot-profiled vendors first | TBD | TBD | Record validated brands in experiments and promote them into regular docs. |
| Bed cleaning supplies | PEI-safe wipes / isopropyl alcohol | Local shop stock | TBD | TBD | Avoid cleaners that haze the surface. |
| Removal tools | Plastic scraper | Local shop stock | TBD | 1 | Do not use metal blades on the flex plate. |

## Parts we do not keep stocked

| Part | Why not stocked | Typical lead time | Trigger to order | Notes |
| --- | --- | --- | --- | --- |
| Full Titan Aero assembly | Higher cost than the common failure items | TBD | Repeated hot-end damage or major crash | Keep subcomponents on hand first. |
| Power supply | Low failure rate so far | TBD | Voltage instability, fan failure, or visible damage | Capture exact PSU model during next teardown photo set. |
| Motion components | Not enough wear data yet | TBD | Belt wear, bearing noise, or crash damage | Add exact belt and pulley specs after physical audit. |

## Sources

- [LulzBot Mini 2 Bill of Materials](https://ohai.lulzbot.com/project/mini-2-bill-of-materials/) - accessed 2026-04-04
- [UltiMachine Einsy Retro overview](https://ultimachine.com/products/einsy-retro) - accessed 2026-04-04
- [LulzBot Titan Aero toolhead page](https://www.lulzbot.com/products/titan-aero-tool-head) - accessed 2026-04-04
- [Magnetic Flex Bed install guide](https://ohai.lulzbot.com/project/mini-2-magnetic-flex-bed-installation/) - accessed 2026-04-04
