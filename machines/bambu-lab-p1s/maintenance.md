# Maintenance - Bambu Lab P1S

Record all completed work in [`logs/maintenance-log.csv`](./logs/maintenance-log.csv). If a maintenance action follows a failure, also record the original failure in [`logs/incident-log.csv`](./logs/incident-log.csv).

## Before every print

- Empty purge waste and verify the chute is clear.
- Inspect the build plate and clean it for the selected plate/material pair.
- Check the nozzle area for stuck filament, damaged silicone sock, and front-cover seating.
- Verify the selected Bambu Studio nozzle, plate, and filament match the installed hardware.
- Confirm AMS slots or external spool path are feeding freely.

## Daily / per shift

- Wipe exterior surfaces and remove scraps from the chamber floor.
- Inspect the nozzle wiper and purge area for buildup.
- Check build plates for damage and retire questionable plates from student use.
- Confirm the room has no lingering odor after ABS/ASA or other higher-emission jobs.

## Weekly

- Clean exposed carbon rods with lint-free cloth and isopropyl alcohol if current OEM guidance still matches this workflow. Do not lubricate carbon rods.
- Inspect belts, pulleys, toolhead cable chain, PTFE tubes, AMS buffer/hub, and spool paths for wear or drag.
- Vacuum loose filament dust carefully; avoid blowing debris into fans or electronics.
- Check AMS desiccant and humidity indicators if AMS is installed.
- Run a PLA validation cube if the printer had repeated student use or any unlogged failure.

## Monthly

- Lubricate Z lead screws and other OEM-specified lubrication points using the current Bambu Lab maintenance instructions.
- Inspect and clean fans, vents, chamber filter area, and enclosure seals.
- Review logs for repeated first-layer, AMS, clog, or odor issues.
- Confirm Bambu Studio and firmware versions are recorded before any update.

## Service-triggered tasks

- After nozzle/hotend/extruder service: run full printer calibration and a validation cube.
- After belt or motion service: run full printer calibration, then inspect ringing and dimensional results.
- After AMS feed service: load/unload every AMS slot and run a short multi-slot test if local policy allows.
- After firmware update: record old/new versions, run full printer calibration, and print the validation cube.

## Maintenance cautions

- Do not lubricate carbon rods.
- Do not scrape the build plate while hot unless the plate-specific instructions allow it.
- Do not run abrasives through an unknown nozzle.
- Do not use solvents on plastic, labels, screens, camera lens, or AMS parts unless the current OEM maintenance article calls for it.

## Sources

- Bambu Lab, *P1 Series Wiki*, https://wiki.bambulab.com/en/p1 - accessed 2026-06-23; maintenance hub, browser re-check required before first service.
- Bambu Lab, *AMS Wiki*, https://wiki.bambulab.com/en/ams - accessed 2026-06-23; AMS maintenance and filament path context.
