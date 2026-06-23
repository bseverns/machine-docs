# Bambu Lab P1S

_Aim: fast, repeatable enclosed FDM prints with disciplined calibration records._

## Maintainer pack
- [Machine card](./machine-card.md) - installed state, stewardship, access, and known-good operating envelope.
- [Parts and spares](./parts-and-spares.md) - stock parts, upgrade gates, and items that still need SKU confirmation.
- [Local deviations](./local-deviations.md) - approved drift from stock hardware, firmware, slicer, or workflow.
- [Physical audit](./physical-audit.md) - bench-side worksheet for replacing `TBD`s with verified facts.
- [Calibration](./calibration.md) - machine calibration, filament flow checks, validation prints, and log format.
- [Materials](./materials.md) - approved materials, AMS limits, drying notes, and profile gates.
- [Troubleshooting](./troubleshooting.md) - symptom-driven recovery paths.
- [Logs](./logs/) - maintenance, incident, and sample run history.

## Start here
- [Quick Start](./quickstart.md) - get oriented and run a controlled first print.
- [Safety](./safety.md) - heat, fumes, moving hardware, AMS handling, and shutdown rules.
- [SOP](./sop.md) - canonical checklist from preflight through shutdown.

## Reference set
- [Bambu Lab P1 Series product page](https://bambulab.com/en/p1) - first-party P1S feature and specification reference.
- [Bambu Lab P1 Series Wiki](https://wiki.bambulab.com/en/p1) - first-party setup, operation, maintenance, and troubleshooting articles.
- [Bambu Studio download page](https://bambulab.com/en/download/studio) - approved slicer source.
- [Bambu Lab AMS Wiki](https://wiki.bambulab.com/en/ams) - AMS loading, humidity, spool, and maintenance guidance.
- [Lab cheat: P1S material matrix](./materials.md) - local approvals, profile gates, and drying notes.

> Source access note: Codex could resolve the official URLs above on 2026-06-23, but the page bodies were not available in this environment. Treat this pack as a structured local draft until a maintainer physically verifies the printer and checks the current Bambu Lab pages in a browser.

## Machine facts at a glance
- **Build volume:** 256 x 256 x 256 mm.
- **Printer type:** enclosed CoreXY single-nozzle FDM printer with removable spring-steel build plates.
- **Thermal envelope:** stock hotend is listed by Bambu Lab at up to 300 C and the bed at up to 100 C; installed nozzle and plate limits still need physical verification.
- **Host software:** Bambu Studio for slicing and printer management; Bambu Handy may be used for monitoring if the lab approves account and network policy.
- **Calibration model:** printer-side auto bed leveling and vibration compensation, plus slicer-side manual filament flow dynamics and flow rate calibration when a new filament/profile is introduced.
- **AMS:** optional Automatic Material System for multi-material jobs; exact installed AMS count and serials are `TBD`.
- **Approved starting materials:** PLA and PETG after profile confirmation; ABS/ASA only with ventilation and Level 2 approval; TPU through external spool path only unless a future local exception is documented.

## Keep the trail warm
- [Maintenance log](./logs/maintenance-log.csv) - capture calibration runs, lubrication, nozzle swaps, AMS service, and filter changes.
- [Incident log](./logs/incident-log.csv) - log failed first layers, toolhead crashes, jams, AMS feed faults, thermal alarms, or odor complaints within 24 hours.
- [Profiles](./profiles/) - Bambu Studio profile notes and exported profile storage rules.
- [Checklists](./checklists/) - preflight and run cards.
- [Training assets](./training/) - operator checklist and quiz.

## Field notes
- Do not treat the enclosure as ventilation. ABS/ASA jobs still need lab ventilation control and odor monitoring.
- Run the full printer calibration after relocation, firmware changes, belt/mechanical service, nozzle/toolhead service, or any crash.
- The P1S does not have the X1-series lidar workflow. Use Bambu Studio manual filament calibration for pressure advance/flow values unless local hardware or firmware verification proves otherwise.
- Keep abrasive filaments out of the machine until a hardened nozzle is installed, logged, and tied to a profile.

## Source-of-truth links
- [Bambu Lab P1 Series product page](https://bambulab.com/en/p1) - official spec and feature page; re-check before changing hard limits.
- [Bambu Lab P1 Series Wiki](https://wiki.bambulab.com/en/p1) - official setup, calibration, maintenance, and troubleshooting hub.
- [Bambu Lab AMS Wiki](https://wiki.bambulab.com/en/ams) - official AMS reference.
- [Bambu Studio](https://bambulab.com/en/download/studio) - official slicer download.
