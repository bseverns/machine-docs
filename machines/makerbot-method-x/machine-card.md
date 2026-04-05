# Machine Card - MakerBot Method X

**Machine type:** Enclosed industrial FDM 3D printer  
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
| Controller / mainboard | Stock Method X electronics and chamber system | README fact snapshot + OEM docs; physical audit still needed for serial and bay identifiers | 2026-04-04 |
| Firmware baseline | MakerBot OS 2.9.2 | README fact snapshot + Method software release notes | 2026-04-04 |
| Toolhead / extruder | Model 1XA and Support 2XA extruders; LABS Experimental head only when cleared | README fact snapshot + OEM user guide | 2026-04-04 |
| Build surface | Flex steel plate keyed for alignment | README fact snapshot + OEM docs | 2026-04-04 |
| Motion / kinematics notes | Enclosed heated-chamber system with dual bays and high-temperature material path | README fact snapshot | 2026-04-04 |
| Approved materials / stock | MakerBot ABS, ABS-R, ASA, PC-ABS, Nylon Carbon Fiber (LABS), SR-30 support | README fact snapshot + material guidance | 2026-04-04 |
| Host software / slicer / sender | MakerBot Print and CloudPrint workflow | README fact snapshot + support docs | 2026-04-04 |
| Safety controls | Heated chamber, enclosed spool bays, filtration, standard power cutoff | README fact snapshot + safety doc | 2026-04-04 |

## Access and dependencies

- **Power path:** dedicated lab outlet to Method X PSU; exact circuit label still needs capture during physical audit
- **Data path:** approved MakerBot workstation / cloud workflow; record exact station and account dependencies during audit
- **Consumables:** approved model and support materials, desiccant, build plate prep supplies if allowed, purge material, filter service items
- **Companion assets:** [`quickstart.md`](./quickstart.md), [`sop.md`](./sop.md), [`calibration.md`](./calibration.md), [`materials.md`](./materials.md), [`troubleshooting.md`](./troubleshooting.md), [`profiles/`](./profiles/)

## Known-good operating envelope

- **Baseline job:** [`profiles/sample/calibration-cube-20mm.stl`](./profiles/sample/calibration-cube-20mm.stl) or a standard ABS verification part using the approved queue workflow
- **Normal quality band:** stable chamber temperature, consistent raft adhesion, no extruder feed faults, and predictable support separation or dissolution
- **No-go conditions:** chamber heat instability, spool bay humidity issues, unexplained purge failures, unknown extruder history, or unknown firmware state
- **Post-service smoke test:** verify chamber heat, load model/support materials, purge both bays, print a baseline part, then update calibration and maintenance logs

## Ownership and escalation

- **Normal operator:** certified lab users with Method X approval
- **Maintainer:** fabrication lab staff
- **Escalate when:** chamber heating faults, dual-bay material issues, LABS head changes, firmware planning, or filtration problems
- **Related docs:** [`parts-and-spares.md`](./parts-and-spares.md), [`local-deviations.md`](./local-deviations.md), [`calibration.md`](./calibration.md), [`materials.md`](./materials.md), [`troubleshooting.md`](./troubleshooting.md)

## Sources

- [MakerBot Method X user guide (PDF)](https://downloads.makerbot.com/manuals/MakerBot_MethodX_UserGuide.pdf) - accessed 2026-04-04, applies to stock setup and maintenance
- [MakerBot OS Method software release notes](https://support.makerbot.com/s/article/1267528410370-Method-Software-Release-Notes) - accessed 2026-04-04, applies to firmware baseline
- [MakerBot Print overview](https://support.makerbot.com/s/article/1667416350829-MakerBot-Print-Overview) - accessed 2026-04-04, applies to host software workflow
