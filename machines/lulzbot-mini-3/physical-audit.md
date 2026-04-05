# Physical Audit - LulzBot Mini 3

**Audit date:**  
**Auditor(s):**  
**Machine location:**  
**Asset tag / serial:**  
**Machine downtime required:** No  
**Photo set path:**  

## Priority gaps to close

- Confirm exact location, asset tag, serial, and acquisition date for [`machine-card.md`](./machine-card.md).
- Verify firmware version, toolhead identity, active build-plate types, and wipe-system condition.
- Capture exact part numbers for the HE 0.5 toolhead, compatible nozzle/hot-end consumables, build plates, wipe pads, and leveling-related service parts in [`parts-and-spares.md`](./parts-and-spares.md).
- Confirm whether any local profile edits, alternate plates, or other field changes should be recorded in [`local-deviations.md`](./local-deviations.md).

## Bench-side checklist

- [ ] Photograph front, rear, serial/asset labels, toolhead, wipe area, bed plates, and posted instructions.
- [ ] Record outlet / circuit label and exact host workstation / transfer path.
- [ ] Verify firmware version from UI or service workflow.
- [ ] Verify installed HE 0.5 toolhead and any nozzle markings.
- [ ] Check wipe-pad condition, probe/leveling hardware, and plate inventory.
- [ ] Count stocked toolheads, build plates, wipe kits, and service parts.
- [ ] Verify shelf/bin labels for Mini 3 spares.

## Installed state verification

| Subsystem | Expected from docs | Observed on machine | Verified? | Notes / follow-up |
| --- | --- | --- | --- | --- |
| Firmware | Marlin 2.1.4.3 (LulzBot branch) |  |  |  |
| Toolhead | HE 0.5, 0.5 mm nozzle, 1.75 mm filament |  |  |  |
| Build surface | Modular PEI-on-glass bed with reversible plates |  |  |  |
| Wipe system | Automatic nozzle wipe path front-left |  |  |  |
| Host workflow | Cura LulzBot Edition or approved Cura path |  |  |  |
| Safety labels / condition | Hot-surface and service labels intact |  |  |  |

## Spares verification

| Item | Expected from docs | Qty observed | Part number / SKU observed | Shelf/bin location | Action needed |
| --- | --- | --- | --- | --- | --- |
| HE 0.5 toolhead | 1 spare target |  |  |  |  |
| Nozzle / hot-end consumables | 2 spare target |  |  |  |  |
| Build plate | 1 spare target |  |  |  |  |
| Wipe pad kit | 2 sets target |  |  |  |  |
| Leveling / probe service parts | 1 spare target |  |  |  |  |

## Deviation review

- [ ] No undocumented deviations observed
- [ ] Deviations observed and copied into [`local-deviations.md`](./local-deviations.md)

Notes:

- 

## Smoke test

- **Authorized:** Yes / No
- **Test run:** 20 mm calibration cube from [`profiles/sample/calibration-cube-20mm.stl`](./profiles/sample/calibration-cube-20mm.stl)
- **Result:** Pass / Fail / Deferred
- **Notes:**  

## Docs updated

- [ ] `machine-card.md`
- [ ] `parts-and-spares.md`
- [ ] `local-deviations.md`
- [ ] related logs if needed
- [ ] photos linked
