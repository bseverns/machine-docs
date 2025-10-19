# MakerBot Method X

_Aim: reliable, repeatable results with clear guardrails._

## Start here
- [Quick Start](./quickstart.md) — get oriented and run a controlled first print.
- [Safety](./safety.md) — ventilation, PPE, and emergency stops for this enclosed system.
- [SOP](./sop.md) — canonical checklist from preflight through shutdown.

## Reference set
- [MakerBot Method X user guide](https://support.makerbot.com/s/article/1267528400550) — wiring, maintenance intervals, and material handling straight from MakerBot.
- [MakerBot OS firmware releases](https://support.makerbot.com/s/article/1267528410370-Method-Software-Release-Notes) — track Method OS 2.9.x updates before you schedule a flash.
- [MakerBot Print & CloudPrint docs](https://support.makerbot.com/s/article/1667416350829-MakerBot-Print-Overview) — slicer workflow we standardize on for queue control.
- [Lab cheat: Method X material matrix](./materials.md) — local approvals, purge strips, and chamber temp targets.

## Machine facts at a glance
- **Build volume:** 190 × 190 × 196 mm (dual extrusion); keep rafts inside the 1 mm chamber safety band.
- **Firmware baseline:** MakerBot OS 2.9.2 on both bays; log staged updates before flashing.
- **Toolheads:** Model 1XA and Support 2XA extruders (0.4 mm hardened steel + soluble support) with LABS Experimental head when cleared.
- **Approved materials:** MakerBot ABS, ABS-R, ASA, PC-ABS, Nylon Carbon Fiber (LABS), and SR-30 soluble support; purge after carbon-filled runs.
- **Unique hardware:** Circulating 110 °C heated chamber, dual sealing spool bays with desiccant, HEPA + carbon filtration, and a flex steel build plate keyed for alignment.

## Keep the trail warm
- [Maintenance log](./logs/maintenance-log.csv) — capture chamber temp tweaks, offsets, and consumables.
- [Incident log](./logs/incident-log.csv) — log jams, purge issues, or enclosure alarms within 24 hours.
- [Profiles](./profiles/) — Method X slicer profiles; version them by material + support strategy.
- [Checklists](./checklists/) — training aides and run cards.
- [Training assets](./training/) — quizzes, videos, and QR resources.

## Field notes
- Treat ABS/ASA jobs with proper ventilation and schedule them when the lab can handle fumes.
- Document soluble support usage and disposal steps in the [materials](./materials.md) file.
- Keep [calibration](./calibration.md) data current; the enclosed environment can drift with chamber heat.

## Source-of-truth links
- [MakerBot Method X product page](https://www.makerbot.com/3d-printers/method-x/) — official spec sheet and marketing claims.
- [MakerBot Method X user guide (PDF)](https://downloads.makerbot.com/manuals/MakerBot_MethodX_UserGuide.pdf) — first-party setup, calibration, and maintenance.
- [MakerBot support: Method X topic](https://support.makerbot.com/s/topic/0TO6S000000PC4EWAW/method-x) — curated troubleshooting and materials articles.

