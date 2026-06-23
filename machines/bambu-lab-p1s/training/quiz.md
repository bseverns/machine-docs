# Quiz - Bambu Lab P1S

1. What must match between the physical printer and Bambu Studio before printing?
2. When should you run full printer calibration?
3. Why is the P1S enclosure not enough by itself for ABS/ASA safety?
4. What should you do if the purge curls around the nozzle before the first layer starts?
5. Why is TPU routed through the external spool path by default?
6. What log should you update after a nozzle swap?
7. What log should you update after a failed probe or toolhead crash?
8. What extra hardware approval is required before abrasive filaments are allowed?
9. Why should you let the plate cool before removing many prints?
10. What measurements are recorded for the standard 20 mm validation cube?

## Answer key

1. Printer model, nozzle size/material, build plate, filament, and profile.
2. After install, relocation, firmware update, service, crash, or persistent drift/failure.
3. It helps contain heat and some odor, but it is not a fume hood and does not replace room ventilation controls.
4. Cancel or pause before it reaches the print, clear the nozzle/purge area safely, and diagnose before restarting.
5. Flexible filament can bind in AMS paths; external spool is the default controlled path.
6. `logs/maintenance-log.csv`.
7. `logs/incident-log.csv`, plus maintenance log after corrective work.
8. A hardened nozzle must be installed, logged, and tied to an approved profile.
9. Cooling improves release and reduces burn/scraper risk.
10. X, Y, and Z dimensions, plus first-layer and visual surface notes.
