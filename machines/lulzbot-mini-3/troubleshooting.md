# Troubleshooting — LulzBot Mini 3

## Quick Table

| Symptom | Likely Causes | Quick Fix | If persists |
|---|---|---|---|
| First layer smears after wipe | Wipe pad saturated; purge length too long | Swap pad, reset purge to profile default, rerun start script | Escalate to Operations so we can tune start G-code and audit wipe station |
| False filament runout alarms | Dusty sensor window; loose guide tube | Clean sensor, reseat guide tube, restart print | Escalate to Facilities if sensor keeps misfiring and request replacement |
| Z homing timeout with skewed gantry | Dry lead screws; loose left coupler | Lube screws, snug coupler, rerun home | Escalate to Ops for full gantry tram if timeout repeats |

## Details
### 1) First layer smears after wipe
- Causes:
  - 2024-06-01 [incident](./logs/incident-log.csv#L2) logged a saturated wiper pad dumping goo on the nozzle.
  - Purge length was bumped but never reset when switching materials.
- Steps to diagnose:
  1. Inspect the wiper pad — if it's shiny or dripping, replace it.
  2. Review the start G-code in CuraLE; confirm purge length matches the [Quickstart SOP](../quickstart.md).
  3. Run a nozzle clean cycle and watch for clean wipe action.
- Fix:
  - Swap the pad, reset purge length, and document the change in the [maintenance log](./logs/maintenance-log.csv#L2).
  - If smearing returns, escalate so we can tweak the start script and check the wipe station alignment.

### 2) False filament runout alarms
- Causes:
  - Dust on the sensor window triggered the 2024-05-19 pause.
  - Guide tube pulling sideways on the switch.
- Steps to diagnose:
  1. Pop the sensor cover and blow out dust with compressed air.
  2. Verify the PTFE tube seats fully and isn't kinked.
  3. Run a dry run (no filament) to confirm the alarm stays clear.
- Fix:
  - Clean and reseat. If alarms persist more than once a week, log it and escalate so Facilities can meter the sensor and order a replacement.

### 3) Z homing timeout with skewed gantry
- Causes:
  - Dry left lead screw and loose coupler (see 2024-05-09 [incident log](./logs/incident-log.csv#L4)).
  - Missed lubrication interval noted in the [maintenance log](./logs/maintenance-log.csv#L4).
- Steps to diagnose:
  1. Power down, manually spin both screws to feel drag.
  2. Check coupler set screws and torque to spec.
  3. Rerun homing while watching both sides — they should move in sync.
- Fix:
  - Lube with PTFE, tighten couplers, and record in the log.
  - If the gantry still racks, escalate so Ops can tram the X-bridge using the [OHAI tram guide](https://ohai.lulzbot.com/project/lulzbot-mini-3/).
