# LulzBot Mini 2 — personal rig

**Intent:** keep this little beast honest as a reference build. It still wears the stock bones, but every mod is logged so we can retell the story without guessing.

## Configuration snapshot (Fall 2025)
| Subsystem | Current state | Why we care | Reference |
| --- | --- | --- | --- |
| Controller | **Einsy Retro 1.0a** (RAMBo-class board; drop-in for Mini 2 harness) | Matches the lab's Einsy service stock and keeps sensorless homing available. | [OHAI: LulzBot Mini 2 Bill of Materials](https://ohai.lulzbot.com/project/mini-2-bill-of-materials/) · [UltiMachine Einsy Retro overview](https://ultimachine.com/products/einsy-retro) |
| Toolhead | **Titan Aero** 2.85 mm, 0.5 mm nozzle | Direct-drive, short filament path; mirrors the official Mini 2 `TA` toolhead. | [LulzBot Titan Aero toolhead page](https://www.lulzbot.com/products/titan-aero-tool-head) · [E3D Titan Aero docs](https://e3d-online.com/blogs/guides/getting-started-with-the-titan-aero) |
| Build surface | **LulzBot Magnetic Flex Bed** (PEI-coated flex plate + magnetic base) | Fast swaps between PEI sheets, keeps adhesion consistent across labs. | [LulzBot Magnetic Flex Bed System](https://www.lulzbot.com/products/lulzbot-mini-2-magnetic-flex-bed-system) |
| Firmware | Stock Mini 2 firmware via **Cura LulzBot Edition** 3.x | Guarantees compatibility with OHAI procedures and material presets. | [Cura LulzBot Edition release notes](https://www.lulzbot.com/learn/software/cura-lulzbot-edition) |

## How we run it
1. Slice with **Cura LulzBot Edition** using Mini 2 + Titan Aero profiles; log any temperature tweaks in the job notes.
2. Verify the magnetic base is clean, then slap down the flex plate you need (PEI smooth vs textured) and confirm Z-offset against the [calibration log](./calibration.md) before printing.
3. Run nozzle wipes manually if the wiper pad looks tired; replace pads in pairs and call it out in the maintenance log.
4. After every job, record material, nozzle hours, and any odd noises in [`logs/maintenance-log.csv`](./logs/maintenance-log.csv).

## Habits + guardrails
- Keep a spare Einsy Retro on the shelf; flash it with the current Cura profile before swapping boards.
- Titan Aero likes to run hotter than stock; document any temperature nudges so we can back-calculate if filament cooks.
- Flex plates warp if scraped like a griddle — use plastic scrapers and reapply PEI when it clouds.
- Treat this as our _playground_ Mini: every experiment must leave breadcrumbs in `experiments/` with slicer profiles and before/after photos.

## Reference basecamp
- [LulzBot Mini 2 Support Portal](https://www.lulzbot.com/mini-2-support) — manuals, wiring diagrams, and firmware packages straight from LulzBot.
- [OHAI Mini 2 maintenance guides](https://ohai.lulzbot.com/project/mini-2-maintenance/) — official step-by-step for cleaning, lubrication, and board swaps.
- [Titan Aero knowledge base](https://e3d-online.dozuki.com/c/Titan_Aero) — exploded views and assembly torque specs from E3D.
- [Magnetic Flex Bed install guide](https://ohai.lulzbot.com/project/mini-2-magnetic-flex-bed-installation/) — how to reseat magnets and align pins without drama.

---

_If the machine does something rad (or terrifying), write it down. Future-you is the target audience._
