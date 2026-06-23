# Calibration - Bambu Lab P1S

## Purpose

Keep a defensible baseline for first-layer reliability, ringing control, extrusion consistency, and dimensional checks. The P1S is highly automated, but local calibration records still matter because nozzle swaps, plates, materials, firmware, and AMS paths change behavior.

## Calibration triggers

Run the relevant calibration before returning the printer to normal use when any of these occur:

- New installation, relocation, table change, or significant vibration near the printer.
- Firmware update or factory reset.
- Nozzle, hotend, extruder, front cover, belt, bed, toolhead, or motion service.
- Toolhead crash, nozzle scrape, failed probe, skipped belt, or abnormal vibration.
- New build plate type or visibly worn plate.
- New filament brand/type/profile, especially PETG, ABS, ASA, TPU, support, or filled materials.
- Repeated first-layer defects, ringing/ghosting, under-extrusion, blobs, corner lift, or dimensional drift.

## Printer-side calibration

Use the printer/Bambu Studio calibration workflow for machine state.

1. Empty the chamber and purge waste.
2. Install a clean verified build plate and known dry PLA.
3. Confirm the printer is on a stable bench and the enclosure is assembled normally.
4. Run the full machine calibration from the printer UI or Bambu Studio after installation, relocation, service, crash, or firmware update.
5. Include bed leveling on the first validation print after calibration.
6. If the firmware offers separate vibration compensation, motor-noise calibration, or similar routines, run them as part of the same maintenance event and log the exact names shown on screen.
7. Do not tune belts, rods, or screws by feel unless following current OEM maintenance guidance and logging the action.

## Filament calibration in Bambu Studio

The P1S does not use the X1-series lidar automatic flow workflow. Treat filament calibration as a slicer/profile task unless local verification proves a newer firmware/hardware path.

For each new material or brand:

1. Start with an appropriate stock P1S preset in Bambu Studio.
2. Run manual flow dynamics / pressure advance calibration and record the selected K value or profile value.
3. Run flow rate calibration and record the selected flow ratio.
4. Save the profile using the repo naming pattern in [`profiles/README.md`](./profiles/README.md).
5. Print the 20 mm cube validation artifact and log dimensions and visual defects.

## Validation artifact

Use [`profiles/sample/calibration-cube-20mm.stl`](./profiles/sample/calibration-cube-20mm.stl) for baseline checks.

Record:

| Field | Value |
| --- | --- |
| Date / operator | TBD |
| Firmware | TBD |
| Bambu Studio version | TBD |
| Nozzle size/material | TBD |
| Plate type | TBD |
| Filament brand/type/color/dry state | TBD |
| Profile name/version | TBD |
| Bed leveling enabled | Yes/No |
| Full machine calibration run | Yes/No |
| Flow dynamics / K value | TBD |
| Flow ratio | TBD |
| X / Y / Z measurement | TBD |
| First-layer result | Pass/Fail + notes |
| Surface result | Pass/Fail + notes |
| Action taken | None / profile update / maintenance / escalation |

## Local pass criteria

Use these as starting criteria until the first maintained baseline is established:

- First layer is continuous, bonded, and not gouged.
- No corner lift or nozzle collision.
- No repeated ringing, layer shift, or skipped extrusion.
- 20 mm cube measures within +/-0.20 mm on X/Y/Z for routine PLA validation, measured after the part cools.
- Profile-specific tolerances may be stricter for fit-critical work, but must be documented with the job.

## Calibration log

Append calibration events to [`logs/maintenance-log.csv`](./logs/maintenance-log.csv) using this note pattern:

```text
Full calibration; PLA cube; Studio <version>; firmware <version>; nozzle <size/material>; plate <type>; K=<value>; flow=<value>; cube X/Y/Z=<values>; result=<pass/fail>
```

Use [`logs/incident-log.csv`](./logs/incident-log.csv) if calibration fails, if the printer reports an error, or if a crash occurs.

## Sources

- Bambu Lab, *P1 Series Wiki*, https://wiki.bambulab.com/en/p1 - accessed 2026-06-23; applies to printer setup, calibration, and maintenance hub.
- Bambu Lab, *Bambu Studio*, https://bambulab.com/en/download/studio - accessed 2026-06-23; applies to slicer and profile workflow.
