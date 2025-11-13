# Troubleshooting — MakerBot Sketch

## Quick Table

| Symptom | Likely Causes | Quick Fix | If persists |
|---|---|---|---|
| Extrusion stops mid-print | Moist PLA baking into the hotend; worn 0.4 mm nozzle | Pause, unload, run cleaning filament, then reload dry spool | Loop in Operations so we can pull the drive gear and log a support ticket if clogs recur twice in a week |
| Layers shift or parts get dragged | Build surface out of grip; Y belt tension low | Re-stick the BuildTak or hit the plate with glue stick, then re-tension the Y belt | Escalate to shop lead for belt alignment and check-in with Facilities if adhesion keeps failing |
| Touchscreen freezes during preheat | Firmware hiccup; loose USB from last update | Power-cycle, reseat USB, and clear old update files | Capture logs per [MakerBot SKETCH user guide](https://downloads.makerbot.com/manuals/MakerBot_SKETCH_User_Guide.pdf) and ping MakerBot support with ticket number |

## Details
### 1) Extrusion stops mid-print
- Causes:
  - Spools left exposed per [incident log](./logs/incident-log.csv#L2-L4) show moisture popping clogs.
  - Nozzle tips wear after long PLA runs; see the 2024-06-03 swap in the [maintenance log](./logs/maintenance-log.csv#L2).
- Steps to diagnose:
  1. Pause and unload filament; inspect for steam pops or brittle snaps.
  2. Run the built-in purge with cleaning filament until flow is even.
  3. Check slicer temps versus the [Quickstart checklist](../quickstart.md) to make sure we're not under-heating.
- Fix:
  - Dry the spool (45 °C for 4 h) or swap to sealed stock.
  - If extrusion is still weak, replace the nozzle and record it in the log.
  - When two clogs land in the same week, escalate to Operations so we can inspect the drive gear and document with MakerBot.

### 2) Layers shift or parts get dragged
- Causes:
  - Adhesion loss noted on 2024-05-18 when the BuildTak sheet aged out.
  - Y belt tension drifts below 3.5 kg — see [maintenance log](./logs/maintenance-log.csv#L3) adjustments.
- Steps to diagnose:
  1. Inspect the build surface; if glossy or scarred, replace it.
  2. Jog Y by hand to feel for slack, then measure belt tension with the sonic tuner (112 Hz target).
  3. Verify the slicer slowed first-layer speed to 20 mm/s per [SOP](../quickstart.md).
- Fix:
  - Refresh adhesion with new sheet or glue.
  - Re-tension the belt using the rear adjusters and lock nuts.
  - Still seeing drift? Flag Facilities for a deeper gantry square-up.

### 3) Touchscreen freezes during preheat
- Causes:
  - Firmware 1.15.0 occasionally hung during heat-up (see 2024-05-07 [incident log](./logs/incident-log.csv#L4)).
  - USB drive left in after update confuses the bootloader.
- Steps to diagnose:
  1. Hold the power button for 10 seconds to hard reset.
  2. Pull any USB drives and reboot.
  3. Review `/makerbot/logs/` per the OEM guide for repeated UI faults.
- Fix:
  - Update to v1.15.1 and delete the `update.mbbin` file.
  - If the panel still locks, escalate with captured logs and tag Support in Slack so we track the case ID.
