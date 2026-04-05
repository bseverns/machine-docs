# Machine Card - LulzBot Mini 2

**Machine type:** FDM 3D printer  
**Location:** Ben personal shop; label exact bench position on the next physical audit  
**Owner / steward:** Ben Severns  
**Asset tag / serial:** TBD  
**Acquired:** TBD  
**Last physically verified:** TBD  
**Doc audit updated:** 2026-04-04  
**Primary reference README:** [`README.md`](./README.md)

## Snapshot

| Field | Current state | Verification method | Last checked |
| --- | --- | --- | --- |
| Controller / mainboard | Einsy Retro 1.0a | Repo configuration snapshot + physical confirmation needed on next bench audit | 2026-04-04 |
| Firmware baseline | Stock Mini 2 firmware loaded via Cura LulzBot Edition 3.x workflow | Repo notes; flash bundle version still needs capture in `firmware-notes.md` | 2026-04-04 |
| Toolhead / extruder | Titan Aero, 2.85 mm filament, 0.5 mm nozzle | Repo configuration snapshot + baseline print history | 2026-04-04 |
| Build surface | LulzBot Magnetic Flex Bed system | Repo configuration snapshot + physical confirmation needed | 2026-04-04 |
| Motion / kinematics notes | Stock Mini 2 motion system; no documented frame or axis geometry changes | Documentation review | 2026-04-04 |
| Approved materials / stock | Start with LulzBot-profiled materials for Mini 2 + Titan Aero; experimental materials require an experiment folder and calibration notes | README policy + slicer workflow | 2026-04-04 |
| Host software / slicer / sender | Cura LulzBot Edition with Mini 2 + Titan Aero profiles | README policy | 2026-04-04 |
| Safety controls | Standard Mini 2 power switch and thermal protections; operators still need hot-end and moving-axis awareness | OEM docs + local practice | 2026-04-04 |

## Access and dependencies

- **Power path:** standard bench AC feed to printer PSU; exact outlet/circuit label TBD
- **Data path:** local workstation running Cura LulzBot Edition; document USB cable path and host machine name when fixed
- **Consumables:** 2.85 mm filament, nozzle wipes, PEI-safe scraper, bed-cleaning supplies, spare nozzles
- **Companion assets:** [`calibration.md`](./calibration.md), [`maintenance.md`](./maintenance.md), [`firmware-notes.md`](./firmware-notes.md), [`experiments/`](./experiments/)

## Known-good operating envelope

- **Baseline job:** add a reference STL/3MF and a photo of a known-good print to `experiments/baselines/`
- **Normal quality band:** clean first layer, consistent wipe, no audible skipping from the Titan Aero, dimensional drift documented in `calibration.md`
- **No-go conditions:** damaged flex plate, inconsistent nozzle wipe, unexplained extrusion clicking, loose toolhead wiring, or unknown firmware state
- **Post-service smoke test:** preheat, home, wipe cycle, 20 mm calibration cube, then update calibration and maintenance docs

## Ownership and escalation

- **Normal operator:** trained shop staff or Ben
- **Maintainer:** Ben
- **Escalate when:** thermal issues, repeated extrusion faults across multiple materials, board swaps, or any change that affects stock safety behavior
- **Related docs:** [`parts-and-spares.md`](./parts-and-spares.md), [`local-deviations.md`](./local-deviations.md), [`firmware-notes.md`](./firmware-notes.md), [`calibration.md`](./calibration.md), [`maintenance.md`](./maintenance.md)

## Sources

- [LulzBot Mini 2 Support Portal](https://www.lulzbot.com/mini-2-support) - accessed 2026-04-04, applies to stock Mini 2 service references
- [OHAI: LulzBot Mini 2 Bill of Materials](https://ohai.lulzbot.com/project/mini-2-bill-of-materials/) - accessed 2026-04-04, applies to stock hardware references
- [OHAI Mini 2 maintenance guides](https://ohai.lulzbot.com/project/mini-2-maintenance/) - accessed 2026-04-04, applies to stock service procedures
- [UltiMachine Einsy Retro overview](https://ultimachine.com/products/einsy-retro) - accessed 2026-04-04, applies to installed controller
- [LulzBot Titan Aero toolhead page](https://www.lulzbot.com/products/titan-aero-tool-head) - accessed 2026-04-04, applies to installed toolhead
