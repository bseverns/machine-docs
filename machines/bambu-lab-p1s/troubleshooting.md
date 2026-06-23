# Troubleshooting - Bambu Lab P1S

## Quick table

| Symptom | Likely causes | Quick fix | If persists |
| --- | --- | --- | --- |
| First layer too high/low or inconsistent | Dirty plate, wrong plate selected, bed leveling skipped, worn plate, nozzle debris | Clean plate, verify plate in Bambu Studio, enable bed leveling, rerun full calibration | Inspect nozzle/plate, run validation cube, escalate if probing errors repeat |
| Corners lift / warping | Plate contamination, insufficient bed temp/profile, draft, material not approved, enclosure workflow wrong | Clean plate, use correct profile/plate, add brim if appropriate, control chamber/door per material | Escalate ABS/ASA jobs for ventilation and profile review |
| Under-extrusion or gaps | Wet filament, partial clog, spool drag, worn nozzle, incorrect flow profile | Dry/replace filament, check spool path, purge, run flow calibration | Hotend/nozzle service and incident log |
| Blobs or purge carried into print | Nozzle buildup, wiper/chute dirty, filament too wet, temperature too high | Clean nozzle area, empty purge, inspect wiper, dry filament | Replace wiper/nozzle parts and log maintenance |
| AMS fails to load/unload | Spool drag, brittle filament, PTFE drag, humidity, incompatible material | Remove suspect spool, trim filament end, clear path, use external spool for TPU | Inspect AMS feeder/PTFE/buffer and log service |
| Ringing / ghosting | Calibration stale, loose printer bench, belt/motion issue, profile too aggressive | Run full printer calibration on stable bench and print validation cube | Escalate for belt/motion inspection |
| Excess odor | Material not approved, ventilation not active, filter overdue, overheated filament | Pause/cancel if unsafe, improve ventilation, verify material/profile | Log incident and require maintainer approval before repeat |
| Print pauses with thermal/motion error | Hotend, bed, fan, enclosure, or motion fault | Preserve error message, cancel if needed, power cycle only after noting state | Escalate; do not return to service without maintenance log |

## First-layer recovery

1. Stop the job before the nozzle damages the plate.
2. Let the machine cool enough for safe handling.
3. Wash and dry the build plate; avoid fingerprints.
4. Verify Bambu Studio printer, nozzle, plate, and filament selections.
5. Inspect nozzle tip for stuck filament.
6. Run bed leveling with the next validation print.
7. If failure repeats, run full printer calibration and log the result.

## Clog / extrusion recovery

1. Confirm the filament is not tangled, brittle, wet, or bound in AMS/external spool path.
2. Heat and purge using the approved UI workflow.
3. If purge is weak or curls sharply, stop and escalate for hotend/nozzle service.
4. After service, run full printer calibration and print the validation cube.

## AMS recovery

1. Do not force filament backward through AMS.
2. Note the slot number, material, spool type, and error message.
3. Remove the spool, trim filament cleanly, and check the path for broken fragments.
4. Use external spool path for flexible filament under default policy.
5. Log repeated slot-specific errors as maintenance, not operator error.

## Sources

- Bambu Lab, *P1 Series Wiki*, https://wiki.bambulab.com/en/p1 - accessed 2026-06-23; official setup, operation, maintenance, and troubleshooting hub.
- Bambu Lab, *AMS Wiki*, https://wiki.bambulab.com/en/ams - accessed 2026-06-23; AMS handling and troubleshooting context.
