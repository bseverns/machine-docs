# Physical Audit - MakerBot Sketch

**Audit date:**  
**Auditor(s):**  
**Machine location:**  
**Asset tag / serial:**  
**Machine downtime required:** No  
**Photo set path:**  

## Priority gaps to close

- Confirm exact location, asset tag, serial, and acquisition date for [`machine-card.md`](./machine-card.md).
- Verify whether this unit uses CloudPrint, MakerBot Print, or both in normal lab workflow.
- Capture exact hot-end, build plate, filter, PTFE guide, and runout-sensor part numbers for [`parts-and-spares.md`](./parts-and-spares.md).
- Confirm whether any local hardware drift exists before leaving [`local-deviations.md`](./local-deviations.md) as "no approved deviations documented."

## Bench-side checklist

- [ ] Photograph front, rear, serial/asset labels, door area, toolhead, build plate, and any posted instructions.
- [ ] Record outlet / circuit label and host workstation path.
- [ ] Verify firmware version from printer UI or service workflow.
- [ ] Verify exact build plate type and condition.
- [ ] Check filter media condition and capture the part number if visible.
- [ ] Count stocked spare hot ends, plates, filters, and feed-path parts.
- [ ] Verify shelf/bin labels for Sketch-specific stock.

## Installed state verification

| Subsystem | Expected from docs | Observed on machine | Verified? | Notes / follow-up |
| --- | --- | --- | --- | --- |
| Firmware | MakerBot Sketch v1.15.0 |  |  |  |
| Toolhead | Single 0.4 mm Smart Extruder-style hot end |  |  |  |
| Build surface | Removable spring-steel build plate |  |  |  |
| Host workflow | CloudPrint or MakerBot Print |  |  |  |
| Sensors | Dual spool runout sensing |  |  |  |
| Safety labels / enclosure | Locking door and posted safety instructions |  |  |  |

## Spares verification

| Item | Expected from docs | Qty observed | Part number / SKU observed | Shelf/bin location | Action needed |
| --- | --- | --- | --- | --- | --- |
| Hot-end assembly | 1 spare target |  |  |  |  |
| Flexible build plate | 1 spare target |  |  |  |  |
| Filter media | 1 spare target |  |  |  |  |
| PTFE feed guide | 1 spare target |  |  |  |  |
| Runout sensor assembly | 1 spare target |  |  |  |  |

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
