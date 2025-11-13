# Troubleshooting — MakerBot Sketch Large

## Quick Table

| Symptom | Likely Causes | Quick Fix | If persists |
|---|---|---|---|
| Auto-level aborts with probe timeout | Inductive puck fouled with chips; loose bed cable | Power down, wipe probe face, reseat bed harness | Escalate to Facilities for probe replacement and log ticket with MakerBot if timeouts continue |
| Under-extrusion / sparse infill | Spool drag at drybox port; feeder idler dry | Free the filament path, lubricate idler, rerun load | Escalate to Operations to inspect drive gears and consider feeder rebuild |
| Corners curl and collide with nozzle | Enclosure left open, chamber too cold; build surface tired | Close the enclosure, preheat chamber, refresh adhesive sheet | Notify Operations if warping repeats so we can audit heater & gasket per OEM SOP |

## Details
### 1) Auto-level aborts with probe timeout
- Causes:
  - Metallic dust on the front inductive puck triggered the 2024-05-30 pause in the [incident log](./logs/incident-log.csv#L2).
  - Bed harness slack can interrupt the probe circuit.
- Steps to diagnose:
  1. Kill power (safety first) and wipe the puck with alcohol; confirm LED pulses again.
  2. Inspect the bed cable for pinch marks; reseat both ends.
  3. Run the calibration wizard per the [MakerBot Sketch Large user guide](https://support.makerbot.com/s/article/1667416351178).
- Fix:
  - After cleaning, rerun auto-level. If the puck still times out, file a ticket so Facilities can meter the probe and replace it if needed.

### 2) Under-extrusion / sparse infill
- Causes:
  - Drybox misalignment on 2024-05-14 forced the spool to drag.
  - Feeder idler dries out; see lubrication in the [maintenance log](./logs/maintenance-log.csv#L3).
- Steps to diagnose:
  1. Pop the drybox lid and confirm the PTFE feed tube is straight.
  2. Jog the extruder 100 mm and watch for skipping or filings.
  3. Check slicer flow multipliers; match the [Quickstart profile](../quickstart.md).
- Fix:
  - Realign the drybox, apply graphite to the idler cam, and rerun the load routine.
  - Still starving? Escalate so Operations can pull the feeder assembly and log the tear-down.

### 3) Corners curl and collide with nozzle
- Causes:
  - Chamber door open overnight on 2024-04-28 left the build at room temp.
  - Build surface loses bite after long ABS runs.
- Steps to diagnose:
  1. Verify enclosure closes flush and heater toggles to 45 °C (watch on-screen graph).
  2. Inspect the build sheet; replace if glossy.
  3. Confirm the slicer uses a brim and the ABS preset from the [Quickstart guide](../quickstart.md).
- Fix:
  - Close and latch the enclosure, run a 10-minute preheat, and refresh adhesives.
  - If warping persists, log the job and pull in Operations to inspect heaters and gasket per the OEM SOP.
