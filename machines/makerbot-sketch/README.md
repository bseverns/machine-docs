# MakerBot Sketch

_Aim: reliable, repeatable results with clear guardrails._

## Start here
- [Quick Start](./quickstart.md) — get a successful print out in about 15 minutes.
- [Safety](./safety.md) — hazards, PPE, and how to slam the E-stop without flinching.
- [SOP](./sop.md) — the canonical preflight → run → postflight flow.

## Reference set
- [MakerBot Sketch user guide](https://support.makerbot.com/s/article/1667416351114) — OEM walkthrough for setup, maintenance, and calibration.
- [Sketch firmware releases](https://support.makerbot.com/s/article/1667416351090-SKETCH-Firmware-Release-Notes) — keep us parked on v1.15.x unless QA signs off.
- [MakerBot CloudPrint docs](https://support.makerbot.com/s/article/1667416350874-MakerBot-CloudPrint-Overview) — slicer + queue management used on the lab workstations.
- [Lab cheat: Z-offset & bed map](./calibration.md) — capture shim stacks and live-levelling tweaks.

## Machine facts at a glance
- **Build volume:** 150 × 150 × 150 mm (5.9 in cube) — watch the front camera mast when placing tall parts.
- **Firmware baseline:** MakerBot Sketch v1.15.0; stage updates via USB and paste release notes into the maintenance log.
- **Toolhead:** Single 0.4 mm Smart Extruder-style hot end (1.75 mm filament) with quick-release latch and PTFE-lined throat.
- **Approved materials:** MakerBot Sketch PLA, Tough PLA, and PETG; flexibles or abrasive fills need written approval.
- **Unique hardware:** Locking acrylic door with particulate filter, removable spring-steel build plate, onboard camera, and dual spool runout sensing.

## Keep the trail warm
- [Maintenance log](./logs/maintenance-log.csv) — record tweaks, swaps, or weird noises.
- [Incident log](./logs/incident-log.csv) — document anything sketchy within 24 hours.
- [Profiles](./profiles/) — slicer configs; version them by slicer + material combo.
- [Checklists](./checklists/) — printable aides for training or checkout.
- [Training assets](./training/) — quizzes, slide decks, or QR codes.

## Field notes
- Runs MakerBot cloud or desktop slicers depending on the lab station; confirm before you slice.
- Double-check filament diameter and units (mm) in any imported profile before pressing go.
- Keep [materials](./materials.md) and [calibration](./calibration.md) docs updated as the machine drifts.

## Source-of-truth links
- [MakerBot SKETCH product page](https://www.makerbot.com/3d-printers/sketch/) — official specs and marketing copy.
- [MakerBot SKETCH user guide (PDF)](https://downloads.makerbot.com/manuals/MakerBot_SKETCH_User_Guide.pdf) — factory setup, maintenance, and calibration.
- [MakerBot support: SKETCH resource hub](https://support.makerbot.com/s/article/1667416063529) — troubleshooting articles curated by MakerBot.

