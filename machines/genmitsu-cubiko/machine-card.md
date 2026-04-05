# Machine Card - Genmitsu Cubiko

**Machine type:** Enclosed desktop CNC router  
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
| Controller / mainboard | Stock GRBL motion board | README fact snapshot + OEM docs; physical audit still needed for controller revision capture | 2026-04-04 |
| Firmware baseline | GRBL 1.1h | README fact snapshot + GRBL release reference | 2026-04-04 |
| Spindle / tool interface | 300 W brushless spindle with ER11 collet | README fact snapshot + OEM docs | 2026-04-04 |
| Workholding / spoilboard | Quick-swap spoilboard pinned to T-slot base | README fact snapshot + OEM docs | 2026-04-04 |
| Motion / kinematics notes | Stock enclosed desktop CNC travel envelope, magnetic chip tray, integrated lighting | README fact snapshot | 2026-04-04 |
| Approved materials / stock | Hardwood, cast acrylic, machinable wax, FR-1, limited 6061 aluminum | README fact snapshot + materials guidance | 2026-04-04 |
| Host software / sender | Candle or UGS with staged `$N` macros; Fusion 360 CAM workflow | README fact snapshot + software docs | 2026-04-04 |
| Safety controls | Enclosure, standard power cutoff, chip containment, operator-controlled dust handling | README fact snapshot + safety doc | 2026-04-04 |

## Access and dependencies

- **Power path:** dedicated lab outlet to controller and spindle PSU; exact circuit label still needs capture during physical audit
- **Data path:** USB-connected sender workstation; record workstation name, sender version, and macro source during audit
- **Consumables:** endmills, ER11 collets, spoilboard stock, hold-down materials, chip cleanup supplies
- **Companion assets:** [`quickstart.md`](./quickstart.md), [`sop.md`](./sop.md), [`calibration.md`](./calibration.md), [`materials.md`](./materials.md), [`troubleshooting.md`](./troubleshooting.md), [`profiles/`](./profiles/)

## Known-good operating envelope

- **Baseline job:** [`profiles/sample/sample-pocket.nc`](./profiles/sample/sample-pocket.nc) on the matching stock blank with current workholding policy
- **Normal quality band:** quiet spindle, predictable chip evacuation, square pockets, no lost steps, and repeatable Z-zero behavior
- **No-go conditions:** loose workholding, spindle noise, collet damage, unexplained lost steps, unknown firmware settings, or dust/chip management problems
- **Post-service smoke test:** home axes, dry-run above stock, run the sample pocket in approved material, then update calibration and maintenance logs

## Ownership and escalation

- **Normal operator:** certified lab users with CNC sign-off
- **Maintainer:** fabrication lab staff
- **Escalate when:** spindle faults, collet or runout problems, firmware/macros changes, recurring lost steps, or enclosure safety concerns
- **Related docs:** [`parts-and-spares.md`](./parts-and-spares.md), [`local-deviations.md`](./local-deviations.md), [`calibration.md`](./calibration.md), [`materials.md`](./materials.md), [`troubleshooting.md`](./troubleshooting.md)

## Sources

- [Genmitsu Cubiko user manual](https://www.sainsmart.com/pages/download/genmitsu-cubiko-user-guide) - accessed 2026-04-04, applies to stock setup and maintenance
- [GRBL releases](https://github.com/gnea/grbl/releases) - accessed 2026-04-04, applies to firmware baseline
- [Fusion 360 Manufacturing workspace docs](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-D83A14C5-07DB-4E7D-9865-3CE0A1C46589) - accessed 2026-04-04, applies to CAM workflow
