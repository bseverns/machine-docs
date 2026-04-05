# Machine Card - MakerBot Sketch+

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
| Controller / mainboard | Stock MakerBot Sketch Large electronics | README fact snapshot + OEM docs; physical audit still needed for board identifiers | 2026-04-04 |
| Firmware baseline | MakerBot Sketch Large v1.6.1 | README fact snapshot + MakerBot firmware release notes | 2026-04-04 |
| Toolhead / extruder | Single 0.4 mm Smart Extruder-style hot end, 1.75 mm filament | README fact snapshot + OEM user guide | 2026-04-04 |
| Build surface | Oversized flexible steel build plate with alignment pins | README fact snapshot + OEM docs | 2026-04-04 |
| Motion / kinematics notes | Large-format enclosed Cartesian system with twin Z lead screws | README fact snapshot | 2026-04-04 |
| Approved materials / stock | MakerBot Sketch PLA, Tough PLA, PETG, and approved dissolvable support workflows | README fact snapshot + materials guidance | 2026-04-04 |
| Host software / slicer / sender | MakerBot CloudPrint workflow | README fact snapshot + support docs | 2026-04-04 |
| Safety controls | Enclosure, locking access, onboard controls, standard power cutoff | README fact snapshot + safety doc | 2026-04-04 |

## Access and dependencies

- **Power path:** dedicated lab outlet to printer PSU; exact circuit label still needs capture during physical audit
- **Data path:** assigned CloudPrint workstation or approved MakerBot management path; record station name during bench audit
- **Consumables:** 1.75 mm approved filament, large build plate cleaning supplies, spare filter media, nozzle purge material as needed
- **Companion assets:** [`quickstart.md`](./quickstart.md), [`sop.md`](./sop.md), [`calibration.md`](./calibration.md), [`materials.md`](./materials.md), [`troubleshooting.md`](./troubleshooting.md), [`profiles/`](./profiles/)

## Known-good operating envelope

- **Baseline job:** [`profiles/sample/calibration-cube-20mm.stl`](./profiles/sample/calibration-cube-20mm.stl) or a standard large-bed first-layer test
- **Normal quality band:** even first layer across the bed, no dual-Z skew artifacts, stable extrusion, and no plate-slip at tall print heights
- **No-go conditions:** visible dual-Z mismatch, damaged alignment pins, recurring under-extrusion, door or filter issues, or unknown firmware state
- **Post-service smoke test:** home axes, confirm bed alignment, print a 20 mm cube plus a broad first-layer test, then update calibration and maintenance logs

## Ownership and escalation

- **Normal operator:** certified lab users
- **Maintainer:** fabrication lab staff
- **Escalate when:** repeated large-format warping, dual-Z synchronization issues, firmware planning, or any enclosure or filtration fault
- **Related docs:** [`parts-and-spares.md`](./parts-and-spares.md), [`local-deviations.md`](./local-deviations.md), [`calibration.md`](./calibration.md), [`materials.md`](./materials.md), [`troubleshooting.md`](./troubleshooting.md)

## Sources

- [MakerBot Sketch Large user guide](https://support.makerbot.com/s/article/1667416351178) - accessed 2026-04-04, applies to stock setup and maintenance
- [Sketch Large firmware releases](https://support.makerbot.com/s/article/1667416351184-SKETCH-Large-Firmware-Release-Notes) - accessed 2026-04-04, applies to firmware baseline
- [MakerBot CloudPrint overview](https://support.makerbot.com/s/article/1667416350874-MakerBot-CloudPrint-Overview) - accessed 2026-04-04, applies to host software workflow
