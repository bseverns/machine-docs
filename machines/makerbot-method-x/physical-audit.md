# Physical Audit - MakerBot Method X

**Audit date:**  
**Auditor(s):**  
**Machine location:**  
**Asset tag / serial:**  
**Machine downtime required:** Usually yes for full verification  
**Photo set path:**  

## Priority gaps to close

- Confirm exact location, asset tag, serial, and acquisition date for [`machine-card.md`](./machine-card.md).
- Verify installed extruder bays, firmware version, chamber labels, and whether the LABS Experimental head is physically on-site.
- Capture exact part numbers for 1XA and 2XA extruders, build plate, filters, desiccant/humidity consumables, and any chamber-service items in [`parts-and-spares.md`](./parts-and-spares.md).
- Confirm whether any local material-storage, humidity-control, or queue-workflow differences should be recorded in [`local-deviations.md`](./local-deviations.md).

## Bench-side checklist

- [ ] Photograph front, rear, serial/asset labels, extruder bays, spool bays, filter access, and posted instructions.
- [ ] Record outlet / circuit label and exact host workstation / cloud path.
- [ ] Verify Method OS version from the machine UI.
- [ ] Verify installed extruders and whether LABS hardware is present.
- [ ] Check spool-bay condition, desiccant workflow, and filter service status.
- [ ] Count stocked extruders, plates, filters, and material-handling consumables.
- [ ] Verify shelf/bin labels for Method X spares and materials.

## Installed state verification

| Subsystem | Expected from docs | Observed on machine | Verified? | Notes / follow-up |
| --- | --- | --- | --- | --- |
| Firmware | MakerBot OS 2.9.2 |  |  |  |
| Extruder bays | Model 1XA + Support 2XA |  |  |  |
| Optional hardware | LABS head only when cleared |  |  |  |
| Build surface | Keyed flex build plate |  |  |  |
| Material handling | Sealed spool bays with desiccant |  |  |  |
| Safety / filtration | Chamber, filter, and enclosure labels intact |  |  |  |

## Spares verification

| Item | Expected from docs | Qty observed | Part number / SKU observed | Shelf/bin location | Action needed |
| --- | --- | --- | --- | --- | --- |
| Model 1XA extruder | 1 spare target |  |  |  |  |
| Support 2XA extruder | 1 spare target |  |  |  |  |
| Flex build plate | 1 spare target |  |  |  |  |
| Filter kit | 1 spare target |  |  |  |  |
| Desiccant / humidity consumables | stocked as needed |  |  |  |  |

## Deviation review

- [ ] No undocumented deviations observed
- [ ] Deviations observed and copied into [`local-deviations.md`](./local-deviations.md)

Notes:

- 

## Smoke test

- **Authorized:** Yes / No
- **Test run:** approved baseline part using the standard material pairing
- **Result:** Pass / Fail / Deferred
- **Notes:**  

## Docs updated

- [ ] `machine-card.md`
- [ ] `parts-and-spares.md`
- [ ] `local-deviations.md`
- [ ] related logs if needed
- [ ] photos linked
