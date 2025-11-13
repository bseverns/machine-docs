# Troubleshooting — Genmitsu Cubiko (CNC)

## Quick Table

| Symptom | Likely Causes | Quick Fix | If persists |
|---|---|---|---|
| Spindle overload fault mid-cut | Feed too hot; dull cutter; loose collet | Pause, clear chips, swap to sharp tool, verify feeds | Escalate to CNC lead to review tool library and spindle health |
| Random limit switch trips | Chips under switches; cable strain | Vacuum switches, check cable routing, rerun job | Escalate to Facilities for switch replacement or reroute |
| Stock slips in vise | Dirty/oily parallels; vise out of tram | Clean jaws, re-tram, torque clamps | Escalate to CNC lead to inspect fixture plate and replace hardware |

## Details
### 1) Spindle overload fault mid-cut
- Causes:
  - 2024-06-06 [incident](./logs/incident-log.csv#L2) recorded overload with a dull 1/8" cutter and aggressive feed.
  - Collet wear leads to chatter; see the fresh ER11 swap in the [maintenance log](./logs/maintenance-log.csv#L2).
- Steps to diagnose:
  1. Pause the program and let the spindle coast to a stop.
  2. Inspect the cutter — if edges are dull or blue, retire it.
  3. Check CAM feeds against the table in the [Quickstart guide](../quickstart.md).
  4. Verify collet torque (tighten to 7 N·m) and that the tool is seated 75% of shank length.
- Fix:
  - Load a sharp cutter, lower feed by 20% for the next pass, and log the change.
  - If overload alarms keep popping, escalate so the CNC lead can scope spindle current draw and refresh the tool library.

### 2) Random limit switch trips
- Causes:
  - Chips behind the X-min switch (see 2024-05-22 [incident](./logs/incident-log.csv#L3)).
  - Switch cables pulling tight during long runs; see cleaning in the [maintenance log](./logs/maintenance-log.csv#L3).
- Steps to diagnose:
  1. Jog each axis to the limit and inspect switches for debris.
  2. Vacuum chips, then cycle the switch by hand; listen for a crisp click.
  3. Check cable strain relief — add a zip tie if it's flopping.
- Fix:
  - Clean thoroughly and reroute the cable.
  - If false trips return, escalate so Facilities can swap the switch and evaluate wiring per the [Genmitsu manual](https://www.sainsmart.com/pages/download/genmitsu-cubiko-user-guide).

### 3) Stock slips in vise
- Causes:
  - Oily parallels from 2024-05-11 [incident](./logs/incident-log.csv#L4).
  - Vise drifted out of tram; corrected in the [maintenance log](./logs/maintenance-log.csv#L4).
- Steps to diagnose:
  1. Remove stock and clean jaws/parallels with degreaser.
  2. Verify tram with a dial indicator; aim for ≤0.02 mm runout.
  3. Check clamp torque — target 40 N·m with the torque wrench.
- Fix:
  - Clean, re-tram, and log the adjustments.
  - If parts still walk, escalate to the CNC lead to inspect the fixture plate and consider new jaws.
