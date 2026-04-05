# Physical Audit - Genmitsu Cubiko

**Audit date:**  
**Auditor(s):**  
**Machine location:**  
**Asset tag / serial:**  
**Machine downtime required:** Usually yes for a full dry-run or cut verification  
**Photo set path:**  

## Priority gaps to close

- Confirm exact location, asset tag, serial, and acquisition date for [`machine-card.md`](./machine-card.md).
- Verify controller revision, sender workstation path, staged `$N` macro source, and spindle identity.
- Capture exact part numbers for collets, spindle service assembly, limit switches, spoilboard format, and motion-service parts in [`parts-and-spares.md`](./parts-and-spares.md).
- Confirm whether any GRBL settings, spoilboard/fixture arrangements, or sender workflows count as local deviations in [`local-deviations.md`](./local-deviations.md).

## Bench-side checklist

- [ ] Photograph front, rear, serial/asset labels, controller area, spindle label, workholding area, and posted instructions.
- [ ] Record outlet / circuit label and exact sender workstation / USB path.
- [ ] Verify GRBL version and export current settings if approved.
- [ ] Verify ER11 collet sizes on hand and spindle condition.
- [ ] Check spoilboard type, fixture method, enclosure condition, and cleanup tools.
- [ ] Count collets, spindle/service parts, limit switches, spoilboard blanks, and validated cutters.
- [ ] Verify shelf/bin labels for Cubiko-specific spares and tooling.

## Installed state verification

| Subsystem | Expected from docs | Observed on machine | Verified? | Notes / follow-up |
| --- | --- | --- | --- | --- |
| Firmware | GRBL 1.1h |  |  |  |
| Spindle | 300 W brushless spindle with ER11 collet |  |  |  |
| Workholding | Quick-swap spoilboard pinned to T-slot base |  |  |  |
| Sender workflow | Candle or UGS with staged `$N` macros |  |  |  |
| Safety / enclosure | Enclosure, cutoff, and posted safety instructions intact |  |  |  |
| Tool database alignment | Local cutters match approved tool database |  |  |  |

## Spares verification

| Item | Expected from docs | Qty observed | Part number / SKU observed | Shelf/bin location | Action needed |
| --- | --- | --- | --- | --- | --- |
| ER11 collet set | 1 set target |  |  |  |  |
| Spindle service assembly | 1 spare target |  |  |  |  |
| Limit switch set | 1 set target |  |  |  |  |
| Spoilboard blank | 1 spare target |  |  |  |  |
| Motion-service kit | 1 set target |  |  |  |  |

## Deviation review

- [ ] No undocumented deviations observed
- [ ] Deviations observed and copied into [`local-deviations.md`](./local-deviations.md)

Notes:

- 

## Smoke test

- **Authorized:** Yes / No
- **Test run:** dry-run and, if approved, [`profiles/sample/sample-pocket.nc`](./profiles/sample/sample-pocket.nc) on approved stock
- **Result:** Pass / Fail / Deferred
- **Notes:**  

## Docs updated

- [ ] `machine-card.md`
- [ ] `parts-and-spares.md`
- [ ] `local-deviations.md`
- [ ] related logs if needed
- [ ] photos linked
