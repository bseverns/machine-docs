# Machine Card - MakerBot Sketch

**Machine type:** Enclosed FDM 3D printer  
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
| Controller / mainboard | Stock MakerBot Sketch electronics | README fact snapshot + OEM docs; physical audit still needed for installed board identifiers | 2026-04-04 |
| Firmware baseline | MakerBot Sketch v1.15.0 | README fact snapshot + MakerBot firmware release notes | 2026-04-04 |
| Toolhead / extruder | Single 0.4 mm Smart Extruder-style hot end, 1.75 mm filament | README fact snapshot + OEM user guide | 2026-04-04 |
| Build surface | Removable spring-steel build plate | README fact snapshot + OEM docs; exact spare part number still needs capture | 2026-04-04 |
| Motion / kinematics notes | Stock enclosed Cartesian system; watch camera mast clearance on tall parts | README fact snapshot | 2026-04-04 |
| Approved materials / stock | MakerBot Sketch PLA, Tough PLA, and PETG | README fact snapshot + material guidance | 2026-04-04 |
| Host software / slicer / sender | MakerBot CloudPrint or MakerBot Print, depending on station | README fact snapshot + support docs | 2026-04-04 |
| Safety controls | Enclosed chamber, locking door, onboard controls, standard power cutoff | README fact snapshot + safety doc | 2026-04-04 |

## Access and dependencies

- **Power path:** dedicated lab outlet to printer PSU; exact circuit label still needs capture during physical audit
- **Data path:** CloudPrint or MakerBot Print on the assigned workstation; record station name and USB/network path during setup audit
- **Consumables:** 1.75 mm approved filament, glue/adhesion supplies if policy allows, build plate cleaning supplies, spare filter media if fitted
- **Companion assets:** [`quickstart.md`](./quickstart.md), [`sop.md`](./sop.md), [`calibration.md`](./calibration.md), [`materials.md`](./materials.md), [`troubleshooting.md`](./troubleshooting.md), [`profiles/`](./profiles/)

## Known-good operating envelope

- **Baseline job:** [`profiles/sample/calibration-cube-20mm.stl`](./profiles/sample/calibration-cube-20mm.stl) with the current standard profile
- **Normal quality band:** clean first layer, consistent extrusion, no frame rattle, and no head contact with curled corners or the camera mast area
- **No-go conditions:** damaged build plate, persistent feed clicking, door latch issues, unknown firmware state, or network/slicer mismatch that cannot be explained
- **Post-service smoke test:** home axes, preheat, load filament, print the 20 mm cube, then update calibration and maintenance logs

## Ownership and escalation

- **Normal operator:** certified lab users
- **Maintainer:** fabrication lab staff
- **Escalate when:** repeated extrusion faults, firmware update planning, wiring or door interlock concerns, or any part replacement beyond routine consumables
- **Related docs:** [`parts-and-spares.md`](./parts-and-spares.md), [`local-deviations.md`](./local-deviations.md), [`calibration.md`](./calibration.md), [`materials.md`](./materials.md), [`troubleshooting.md`](./troubleshooting.md)

## Sources

- [MakerBot SKETCH user guide (PDF)](https://downloads.makerbot.com/manuals/MakerBot_SKETCH_User_Guide.pdf) - accessed 2026-04-04, applies to stock setup and maintenance
- [Sketch firmware releases](https://support.makerbot.com/s/article/1667416351090-SKETCH-Firmware-Release-Notes) - accessed 2026-04-04, applies to firmware baseline
- [MakerBot CloudPrint overview](https://support.makerbot.com/s/article/1667416350874-MakerBot-CloudPrint-Overview) - accessed 2026-04-04, applies to host software workflow
