# Troubleshooting — MakerBot Method X

## Quick Table

| Symptom | Likely Causes | Quick Fix | If persists |
|---|---|---|---|
| Chamber stalls below setpoint with error 508 | Door not latched; gasket dirty; thermal sensor offset | Stop job, fully latch door, clean gasket, rerun preheat | Escalate to Facilities to inspect latch alignment and open a MakerBot ticket if temperature fault repeats |
| SR-30 extruder clicks and stops feeding | Support spool moisture; drive gears packed | Dry the spool, run cleaning filament, brush gears | Escalate to Operations to pull the extruder and replace PTFE path |
| Material bay says "Spool Not Detected" | Oxidized cartridge contacts; firmware lag | Power-cycle, clean contacts, reseat cartridge | Escalate to Ops/IT to run diagnostics and capture logs for MakerBot support |

## Details
### 1) Chamber stalls below setpoint with error 508
- Causes:
  - 2024-06-04 incident shows a half-latched door stopped the chamber at 70 °C.
  - Dusty gaskets break the seal; see cleaning in the [maintenance log](./logs/maintenance-log.csv#L2).
- Steps to diagnose:
  1. Pause the print, latch the door hard, and check the seal for gaps.
  2. Clean the gasket with a lint-free wipe and ensure magnets snap shut.
  3. Restart preheat and monitor the temperature graph via the touchscreen.
  4. If it still hangs, check the [OEM guide](https://downloads.makerbot.com/manuals/MakerBot_MethodX_UserGuide.pdf) for sensor diagnostics.
- Fix:
  - Align the latch cam, wipe the gasket, and rerun the job.
  - If two faults log in a row, tag Facilities to inspect the latch hardware and capture logs for MakerBot support.

### 2) SR-30 extruder clicks and stops feeding
- Causes:
  - Moisture-laden support material from the 2024-05-25 incident.
  - Drive gears clog with SR-30 shavings (see [maintenance log](./logs/maintenance-log.csv#L3)).
- Steps to diagnose:
  1. Check material bay humidity (keep <25% RH).
  2. Manually feed 100 mm; if it clicks, unload and inspect the filament.
  3. Run the cleaning filament cycle; inspect drive gears for packed material.
- Fix:
  - Bake the spool (60 °C for 4 h) and clean gears.
  - If clicking remains, escalate to Operations to pull the extruder apart and replace the PTFE guide tube.

### 3) Material bay says "Spool Not Detected"
- Causes:
  - Oxidized reader pins caused the 2024-05-12 idle fault.
  - Firmware after long uptime occasionally misses cartridge handshakes.
- Steps to diagnose:
  1. Power-cycle the printer and reseat the cartridge.
  2. Clean contacts with electronics wipes (see [maintenance log](./logs/maintenance-log.csv#L4)).
  3. Check for pending firmware updates in the [Quickstart SOP](../quickstart.md).
- Fix:
  - After cleaning, reload the cartridge.
  - If the bay keeps flaking out, log the error codes and escalate to Ops/IT so we can involve MakerBot support.
