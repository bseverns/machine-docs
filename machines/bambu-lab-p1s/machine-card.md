# Machine Card - Bambu Lab P1S

**Machine type:** Enclosed CoreXY FDM 3D printer  
**Location:** TBD  
**Owner / steward:** Fabrication lab ops  
**Asset tag / serial:** TBD  
**Acquired:** TBD  
**Last physically verified:** TBD  
**Doc audit updated:** 2026-06-23  
**Primary reference README:** [`README.md`](./README.md)

## Snapshot

| Field | Current state | Verification method | Last checked |
| --- | --- | --- | --- |
| Controller / mainboard | Stock P1S electronics; exact board revision `TBD` | OEM P1 Series docs; physical audit still needed | 2026-06-23 |
| Firmware baseline | `TBD` | Read from printer UI or Bambu Studio device page | TBD |
| Toolhead / extruder | Stock single direct-drive toolhead; installed nozzle material and size `TBD` | Physical audit + Bambu Studio device/nozzle config | TBD |
| Build surface | Removable spring-steel plate; exact plate type(s) `TBD` | Physical audit + slicer plate setting | TBD |
| Motion / kinematics notes | Enclosed CoreXY with printer-side bed leveling and vibration compensation workflow | OEM P1 Series docs; validate on first calibration | 2026-06-23 |
| Approved materials / stock | PLA and PETG pending profile validation; ABS/ASA gated by ventilation approval; TPU via external spool | Local material policy draft | 2026-06-23 |
| Host software / slicer / sender | Bambu Studio; Bambu Handy optional if approved | Local workflow draft + Bambu software source | 2026-06-23 |
| Safety controls | Enclosure, front power switch/rear inlet switch as installed, thermal firmware protections, removable build plate | Physical audit needed for exact power path and room ventilation | TBD |
| AMS / accessories | AMS presence, serials, PTFE path, hub/buffer, and drybox state `TBD` | Physical audit | TBD |

## Access and dependencies

- **Power path:** dedicated lab outlet to P1S PSU; exact circuit label still needs capture during physical audit.
- **Data path:** Bambu Studio workstation/account, LAN/cloud mode policy, and SD card workflow all `TBD`.
- **Consumables:** filament, build plates, glue/release agents where required, nozzle wipers, filament cutters, PTFE tube, chamber carbon filter, AMS desiccant.
- **Companion assets:** [`quickstart.md`](./quickstart.md), [`sop.md`](./sop.md), [`calibration.md`](./calibration.md), [`materials.md`](./materials.md), [`troubleshooting.md`](./troubleshooting.md), [`profiles/`](./profiles/)

## Known-good operating envelope

- **Baseline job:** [`profiles/sample/calibration-cube-20mm.stl`](./profiles/sample/calibration-cube-20mm.stl) using an approved Bambu Studio P1S PLA profile, after full printer calibration.
- **Normal quality band:** clean first layer, no skipped extrusion, no abnormal belt/toolhead noise, no AMS feed errors, and a 20 mm cube inside the local tolerance recorded in [`calibration.md`](./calibration.md).
- **No-go conditions:** unknown firmware state after update, damaged/dirty build plate, unverified nozzle after abrasive material, repeated first-layer failure, chamber odor complaint, AMS humidity warning, or toolhead crash.
- **Post-service smoke test:** run full printer calibration, load known dry PLA, print the baseline cube, inspect dimensions/surfaces, then update calibration and maintenance logs.

## Ownership and escalation

- **Normal operator:** certified lab users with P1S approval.
- **Maintainer:** fabrication lab staff.
- **Escalate when:** hotend service, nozzle material changes, AMS feed system work, firmware changes, belt/mechanical adjustments, repeated first-layer failure, smoke/odor complaints, or unlisted material requests.
- **Related docs:** [`parts-and-spares.md`](./parts-and-spares.md), [`local-deviations.md`](./local-deviations.md), [`calibration.md`](./calibration.md), [`materials.md`](./materials.md), [`troubleshooting.md`](./troubleshooting.md)

## Sources

- Bambu Lab, *P1 Series product page*, https://bambulab.com/en/p1 - accessed 2026-06-23, applies to stock specifications and feature claims; browser re-check required because Codex page body access was unavailable.
- Bambu Lab, *P1 Series Wiki*, https://wiki.bambulab.com/en/p1 - accessed 2026-06-23, applies to setup, operation, calibration, and maintenance; browser re-check required because Codex page body access was unavailable.
- Bambu Lab, *Bambu Studio*, https://bambulab.com/en/download/studio - accessed 2026-06-23, applies to slicer source and profile workflow.
