# Machine Card - LulzBot Mini 3

**Machine type:** Open-frame FDM 3D printer with enclosure-adjacent filtration hardware  
**Location:** TBD  
**Owner / steward:** Fabrication lab ops  
**Asset tag / serial:** TBD  
**Acquired:** TBD  
**Last physically verified:** TBD  
**Doc audit updated:** 2026-04-04  
**Primary reference README:** [`README.md`](./README.md)

## Snapshot

| Field | Current state | Verification method | Last checked |
| --- | --- | --- | --- |
| Controller / mainboard | Stock LulzBot Mini 3 electronics | README fact snapshot + OEM docs; physical audit still needed for board identifier capture | 2026-04-04 |
| Firmware baseline | Marlin 2.1.4.3 (LulzBot branch) | README fact snapshot + LulzBot firmware download references | 2026-04-04 |
| Toolhead / extruder | HE 0.5 toolhead, 0.5 mm brass nozzle, 1.75 mm filament | README fact snapshot + OEM user guide | 2026-04-04 |
| Build surface | Modular PEI-on-glass bed with reversible build plates | README fact snapshot + OEM docs | 2026-04-04 |
| Motion / kinematics notes | Stock Mini 3 motion system with front-left nozzle wipe path | README fact snapshot | 2026-04-04 |
| Approved materials / stock | LulzBot-profiled PLA, Tough PLA, PETG, ABS, ASA, nGen, TPU 95A, Nylon co-polymers | README fact snapshot + materials guidance | 2026-04-04 |
| Host software / slicer / sender | Cura LulzBot Edition or approved Cura workflow | README fact snapshot + OEM docs | 2026-04-04 |
| Safety controls | Thermal protections, wipe system, standard power cutoff, operator-controlled hot-surface awareness | README fact snapshot + safety doc | 2026-04-04 |

## Access and dependencies

- **Power path:** dedicated lab outlet to printer PSU; exact circuit label still needs capture during physical audit
- **Data path:** Cura LulzBot Edition workstation and approved transfer path; record exact host setup during bench audit
- **Consumables:** 1.75 mm approved filament, PEI-safe cleaning supplies, spare nozzle wipe pads, build plate consumables
- **Companion assets:** [`quickstart.md`](./quickstart.md), [`sop.md`](./sop.md), [`calibration.md`](./calibration.md), [`materials.md`](./materials.md), [`troubleshooting.md`](./troubleshooting.md), [`profiles/`](./profiles/)

## Known-good operating envelope

- **Baseline job:** [`profiles/sample/calibration-cube-20mm.stl`](./profiles/sample/calibration-cube-20mm.stl) with the current approved profile
- **Normal quality band:** reliable wipe cycle, even first layer, stable extrusion, and predictable Z offset per active build plate
- **No-go conditions:** damaged wipe pad, unexplained first-layer inconsistency, bed-plate mismatch, loose toolhead wiring, or unknown firmware state
- **Post-service smoke test:** home axes, verify wipe behavior, print a 20 mm cube, then update calibration and maintenance logs

## Ownership and escalation

- **Normal operator:** certified lab users
- **Maintainer:** fabrication lab staff
- **Escalate when:** probe or wipe-system faults, firmware planning, repeated extrusion issues across multiple materials, or unexplained bed-level drift
- **Related docs:** [`parts-and-spares.md`](./parts-and-spares.md), [`local-deviations.md`](./local-deviations.md), [`calibration.md`](./calibration.md), [`materials.md`](./materials.md), [`troubleshooting.md`](./troubleshooting.md)

## Sources

- [LulzBot Mini 3 user guide (PDF)](https://download.lulzbot.com/Mini_3/documentation/LulzBot_Mini_3_User_Guide.pdf) - accessed 2026-04-04, applies to stock setup and maintenance
- [Marlin 2.x firmware builds](https://download.lulzbot.com/Software/Marlin2/) - accessed 2026-04-04, applies to firmware baseline
- [Cura LulzBot Edition user manual](https://www.lulzbot.com/learn/tutorials/cura-lulzbot-edition-user-manual) - accessed 2026-04-04, applies to slicer workflow
