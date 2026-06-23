# Quick Start - Bambu Lab P1S

**Goal:** Produce a clean PLA validation print in about 20-30 minutes while proving the machine, plate, filament, and profile are in a known-good state.

1. Study the [safety brief](./safety.md); confirm ventilation expectations before any ABS/ASA work.
2. Confirm the installed nozzle, build plate, firmware, AMS state, and active Bambu Studio version in the [machine card](./machine-card.md). If any item is still `TBD`, keep the run to dry PLA until audited.
3. Clean the build plate according to the exact plate type. When in doubt, wash with dish soap and water, dry fully, then avoid touching the print surface.
4. Open Bambu Studio, select **Bambu Lab P1S**, select the actual installed nozzle size and plate, then import `calibration-cube-20mm.stl` from [`profiles/sample`](./profiles/sample/).
5. Use the approved starter profile once one is exported to [`profiles/`](./profiles/). Until then, use the stock P1S PLA profile and record that it is an unmodified stock profile.
6. In the print dialog, enable bed leveling for the validation run. If the printer was moved, serviced, updated, or crashed, run the full printer calibration first per [`calibration.md`](./calibration.md).
7. Watch the purge, nozzle wipe, probing, and first layer. Cancel if the purge curls around the nozzle, the plate is wrong, or the first layer drags/lifts.
8. After the print, measure X/Y/Z, inspect corners and top surface, then record the run in [`logs/sample-run-log.csv`](./logs/sample-run-log.csv).
9. Log calibration changes, nozzle swaps, AMS work, or plate changes in [`logs/maintenance-log.csv`](./logs/maintenance-log.csv). Log faults in [`logs/incident-log.csv`](./logs/incident-log.csv).

## First-run pass criteria

- First layer is continuous with no gouging, gaps, or edge lift.
- Cube releases without damaging the plate after cooling.
- Measured dimensions are within the active tolerance documented in [`calibration.md`](./calibration.md).
- No abnormal belt noise, fan rub, AMS clicking, heat-creep symptoms, or odor complaint.
