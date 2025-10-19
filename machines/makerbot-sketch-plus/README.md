# MakerBot Sketch+

_Aim: reliable, repeatable results with clear guardrails._

## Start here
- [Quick Start](./quickstart.md) — land a quality print fast while learning the flow.
- [Safety](./safety.md) — hazards, ventilation cues, and the E-stop drill.
- [SOP](./sop.md) — authoritative checklist for preflight → run → postflight.

## Reference set
- [MakerBot Sketch Large user guide](https://support.makerbot.com/s/article/1667416351178) — OEM maintenance and setup playbook.
- [Sketch Large firmware releases](https://support.makerbot.com/s/article/1667416351184-SKETCH-Large-Firmware-Release-Notes) — keep the fleet on v1.6.x unless QA approves testing.
- [MakerBot CloudPrint docs](https://support.makerbot.com/s/article/1667416350874-MakerBot-CloudPrint-Overview) — slicer + queue workflow for this platform.
- [Lab cheat: large-format calibration notes](./calibration.md) — track dual-Z sync, bed shims, and nozzle offsets.

## Machine facts at a glance
- **Build volume:** 335 × 240 × 240 mm (13.2 × 9.4 × 9.4 in); clear the rear filament guide before maxing Y travel.
- **Firmware baseline:** MakerBot Sketch Large v1.6.1; stage USB flashes and capture release notes in the maintenance log.
- **Toolhead:** Single 0.4 mm Smart Extruder-style hot end (1.75 mm filament) with quick-release latch and hardened drive gears.
- **Approved materials:** MakerBot Sketch PLA, Tough PLA, PETG, and support PVA (dual extruder add-on) with instructor approval for dissolvables.
- **Unique hardware:** Oversized flexible steel build plate with alignment pins, locking enclosure with HEPA filter, dual spool runout sensing, and twin Z lead screws for tall prints.

## Keep the trail warm
- [Maintenance log](./logs/maintenance-log.csv) — record tune-ups, offsets, or consumable swaps.
- [Incident log](./logs/incident-log.csv) — log misfires or material issues inside 24 hours.
- [Profiles](./profiles/) — slicer configs; tag versions by slicer + nozzle combo.
- [Checklists](./checklists/) — laminated aides for students and mentors.
- [Training assets](./training/) — quizzes, slides, and QR-ready references.

## Field notes
- Shares workflow DNA with the Sketch, but keep profiles separate to respect build volume differences.
- Document nozzle swaps or alternate build surfaces directly in the [materials](./materials.md) and [calibration](./calibration.md) notes.

## Source-of-truth links
- [MakerBot Sketch Series overview](https://www.makerbot.com/3d-printers/sketch-series/) — official comparison of Sketch and Sketch+.
- [MakerBot Sketch+ tech specs (PDF)](https://downloads.makerbot.com/manuals/MakerBot_SKETCHPlus_TechSpecs.pdf) — dimensions, build volume, and power requirements.
- [MakerBot support: Sketch+ knowledge base](https://support.makerbot.com/s/article/1667416063609) — maintenance and troubleshooting notes direct from MakerBot.

