# Safety - Bambu Lab P1S

## Scope

This safety brief covers the Bambu Lab P1S in stock or near-stock enclosed FDM configuration, with optional AMS. Any modified heater, nozzle, chamber, electronics, firmware, or third-party enclosure change must be recorded in [`local-deviations.md`](./local-deviations.md) before routine use.

## Required controls

- Safety glasses for operation and part removal.
- Heat-resistant caution around the nozzle, bed, chamber air, freshly printed parts, and purge waste.
- Fitted sleeves, tied hair, and no loose jewelry around moving axes and filament paths.
- Ventilation approval for ABS, ASA, PA, PC, filled materials, or any material that creates noticeable odor.
- No unattended first run after service, firmware update, relocation, new material, new plate, or nozzle change.

## Hot and moving hazards

- The hotend can reach temperatures that cause immediate burns. Do not touch the nozzle, heater block, silicone sock, purge, or fresh extrudate.
- The bed remains hot after a job. Let the build plate cool before flexing or handling large prints.
- Keep hands out of the chamber during homing, probing, purging, and printing. Pause the printer before reaching into the work envelope.
- Do not defeat covers, cable guides, AMS lid checks, or enclosure parts to keep a job running.

## Fumes and material controls

- PLA and PETG are the starter materials, but still require normal room ventilation.
- ABS and ASA require the local ventilation plan, closed door workflow, and odor monitoring. The P1S enclosure and carbon filter reduce nuisance odor; they are not a fume hood.
- TPU should be run from the external spool path unless a local AMS exception is documented.
- Abrasive filaments require a hardened nozzle and a logged profile. Do not run carbon/glass-filled materials through an unknown stock nozzle.
- Dry hygroscopic filaments before use and document drying conditions in the job notes.

## Build plate and tool handling

- Verify the exact plate selected in Bambu Studio before printing. Wrong plate settings can cause adhesion failure or nozzle/plate damage.
- Use scrapers carefully and away from hands. Prefer cooling and flexing the removable plate before prying.
- Use glue/release agent only when the specific plate/material pair calls for it in [`materials.md`](./materials.md).

## Emergency stop / shutdown

1. For a print defect without danger, pause or cancel from the printer UI or Bambu Studio.
2. For collision, smoke, electrical smell, runaway noise, or unsafe motion, cut power using the accessible power switch or outlet path identified during physical audit.
3. Do not reopen the machine for service until heaters have cooled and motion has stopped.
4. Log the event in [`logs/incident-log.csv`](./logs/incident-log.csv) before returning the printer to service.

## Sources

- Bambu Lab, *P1 Series product page*, https://bambulab.com/en/p1 - accessed 2026-06-23; stock thermal and enclosure context.
- Bambu Lab, *P1 Series Wiki*, https://wiki.bambulab.com/en/p1 - accessed 2026-06-23; setup, safety-adjacent operation, and maintenance hub.
- Bambu Lab, *AMS Wiki*, https://wiki.bambulab.com/en/ams - accessed 2026-06-23; AMS handling and filament path context.
