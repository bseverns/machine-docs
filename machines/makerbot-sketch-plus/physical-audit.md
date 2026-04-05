# Physical Audit - MakerBot Sketch+

**Audit date:**  
**Auditor(s):**  
**Machine location:**  
**Asset tag / serial:**  
**Machine downtime required:** No  
**Photo set path:**  

## Priority gaps to close

- Confirm exact location, asset tag, serial, and acquisition date for [`machine-card.md`](./machine-card.md).
- Verify whether dissolvable-support capability is actually installed or only allowed when an add-on is present.
- Capture exact part numbers for the large build plate, filter kit, hot-end assembly, and any Z-synchronization-related spares in [`parts-and-spares.md`](./parts-and-spares.md).
- Confirm whether any local bed shims, alternate surfaces, or workflow quirks should be recorded in [`local-deviations.md`](./local-deviations.md).

## Bench-side checklist

- [ ] Photograph front, rear, serial/asset labels, dual-Z area, toolhead, build plate, and posted instructions.
- [ ] Record outlet / circuit label and host workstation / CloudPrint path.
- [ ] Verify firmware version from UI or service workflow.
- [ ] Verify build plate style, alignment-pin condition, and filter assembly.
- [ ] Confirm whether support-material workflow is physically present and approved.
- [ ] Count stocked spare hot ends, plates, filters, sensors, and any large-format-specific hardware.
- [ ] Verify shelf/bin labels for Sketch+ stock.

## Installed state verification

| Subsystem | Expected from docs | Observed on machine | Verified? | Notes / follow-up |
| --- | --- | --- | --- | --- |
| Firmware | MakerBot Sketch Large v1.6.1 |  |  |  |
| Toolhead | Single 0.4 mm Smart Extruder-style hot end |  |  |  |
| Build surface | Large flexible steel plate with alignment pins |  |  |  |
| Motion | Twin Z lead screws |  |  |  |
| Host workflow | CloudPrint workflow |  |  |  |
| Support capability | Approved only if the add-on is present |  |  |  |

## Spares verification

| Item | Expected from docs | Qty observed | Part number / SKU observed | Shelf/bin location | Action needed |
| --- | --- | --- | --- | --- | --- |
| Hot-end assembly | 1 spare target |  |  |  |  |
| Large build plate | 1 spare target |  |  |  |  |
| Filter kit | 1 spare target |  |  |  |  |
| Runout sensor assembly | 1 spare target |  |  |  |  |
| Z-motion spare set | 1 set target |  |  |  |  |

## Deviation review

- [ ] No undocumented deviations observed
- [ ] Deviations observed and copied into [`local-deviations.md`](./local-deviations.md)

Notes:

- 

## Smoke test

- **Authorized:** Yes / No
- **Test run:** 20 mm cube plus broad first-layer test with the approved standard profile
- **Result:** Pass / Fail / Deferred
- **Notes:**  

## Docs updated

- [ ] `machine-card.md`
- [ ] `parts-and-spares.md`
- [ ] `local-deviations.md`
- [ ] related logs if needed
- [ ] photos linked
