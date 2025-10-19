# LulzBot Mini 3

_Aim: reliable, repeatable results with clear guardrails._

## Start here
- [Quick Start](./quickstart.md) — dial in your first print with Cura and lab checks.
- [Safety](./safety.md) — hazards, hot surfaces, and emergency stops.
- [SOP](./sop.md) — the definitive runbook from preflight to shutdown.

## Reference set
- [LulzBot Mini 3 user guide](https://download.lulzbot.com/Mini_3/documentation/LulzBot_Mini_3_User_Guide.pdf) — official setup, maintenance, and wiring diagrams.
- [Marlin 2.x firmware builds](https://download.lulzbot.com/Software/Marlin2/) — grab the Mini 3 hex + release notes before scheduling a flash.
- [Cura LulzBot Edition docs](https://www.lulzbot.com/learn/tutorials/cura-lulzbot-edition-user-manual) — slicer workflow we certify for this printer.
- [Lab cheat: Mini 3 calibration tracker](./calibration.md) — record Z offsets per bed plate and keep probe offsets honest.

## Machine facts at a glance
- **Build volume:** 205 × 195 × 196 mm (8.1 × 7.7 × 7.7 in) — nozzle wipe happens front-left; leave clearance.
- **Firmware baseline:** Marlin 2.1.4.3 (LulzBot branch) loaded via CuraLE; document any config edits in the maintenance log.
- **Toolhead:** HE 0.5 (0.5 mm brass nozzle, 1.75 mm filament) with direct-drive dual-geared feeder and automatic nozzle wiping pad.
- **Approved materials:** LulzBot-profiled PLA, Tough PLA, PETG, ABS, ASA, nGen, TPU 95A, and Nylon co-polymers; anything exotic needs instructor sign-off.
- **Unique hardware:** Modular PEI-on-glass bed with auto-leveling corner washers, always-on HEPA filter housing, and reversible build surface plates.

## Keep the trail warm
- [Maintenance log](./logs/maintenance-log.csv) — note nozzle wipes, offsets, or bed swaps.
- [Incident log](./logs/incident-log.csv) — record jams or anomalies within 24 hours.
- [Profiles](./profiles/) — Cura profiles; version them by material and layer height.
- [Checklists](./checklists/) — training aides and certification forms.
- [Training assets](./training/) — quizzes, demos, and QR codes.

## Field notes
- Use Cura (LulzBot Edition or vanilla Cura) profiles from the [profiles](./profiles/) folder; keep lab-specific adjustments documented.
- Track Z-offset per build surface in the [calibration](./calibration.md) doc.
- Update the [materials](./materials.md) list when adding filaments or changing temperature ranges.

## Source-of-truth links
- [LulzBot Mini 3 product page](https://www.lulzbot.com/products/lulzbot-mini-3) — official specs, bundle contents, and firmware downloads.
- [OHAI: LulzBot Mini 3 guides](https://ohai.lulzbot.com/project/lulzbot-mini-3/) — step-by-step maintenance and calibration direct from LulzBot.
- [LulzBot support knowledge base](https://www.lulzbot.com/learn/tutorials/lulzbot-mini-3) — application notes and material presets maintained by LulzBot.

