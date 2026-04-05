# Local Deviations - LulzBot Mini 2

**Purpose:** document every intentional way this machine differs from a stock Mini 2 so future maintainers can troubleshoot and roll back cleanly.  
**Stock baseline reference:** stock LulzBot Mini 2 hardware and firmware as documented by LulzBot/OHAI  
**Last reviewed:** 2026-04-04  

## Rules

- No undocumented machine changes.
- Every deviation must state why it exists and how to back it out.
- If a change affects safety, calibration, firmware, or training, update the related doc in the same PR.

## Controlled deviations

| Date | Subsystem | Stock baseline | Installed state | Why we changed it | Risks introduced | Rollback path | Verification / evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2025 | Controller | Stock Mini 2 controller | Einsy Retro 1.0a | Aligns with available Einsy service stock and preserves sensorless-homing-capable ecosystem | Firmware mismatch risk, wiring assumptions must be documented | Reinstall stock board and restore stock firmware bundle after harness check | [`README.md`](./README.md), [`firmware-notes.md`](./firmware-notes.md) |
| 2025 | Toolhead | Stock Mini 2 toolhead | Titan Aero, 2.85 mm, 0.5 mm nozzle | Short filament path and alignment with official Titan Aero ecosystem | Temperature tuning may differ from stock assumptions; spare compatibility changes | Reinstall stock toolhead, confirm wiring, rerun calibration, and restore stock profile set | [`README.md`](./README.md), [`calibration.md`](./calibration.md) |
| 2025 | Build surface | Stock glass/PEI bed setup | Magnetic Flex Bed system | Faster plate swaps and more repeatable surface management | Plate damage or misalignment can corrupt first-layer assumptions | Remove magnetic system, return to stock bed stack, and re-verify Z offsets | [`README.md`](./README.md), [`calibration.md`](./calibration.md) |

## Required post-change checks

- Safety check: inspect harness routing, thermal behavior, and moving-clearance points
- Functional smoke test: power on, home, heat, and verify wipe behavior
- Calibration or baseline print: 20 mm cube plus first-layer inspection on the active plate
- Docs updated: `README.md`, `calibration.md`, `firmware-notes.md`, `parts-and-spares.md`, `maintenance.md`

## Open questions

- Capture exact install dates from maintenance history or receipts.
- Record controller wiring photos and board orientation.
- Record exact replacement part numbers for the Titan Aero hot-end stack and flex-bed consumables.

## Sources

- [LulzBot Mini 2 Support Portal](https://www.lulzbot.com/mini-2-support) - accessed 2026-04-04
- [OHAI Mini 2 Bill of Materials](https://ohai.lulzbot.com/project/mini-2-bill-of-materials/) - accessed 2026-04-04
- [UltiMachine Einsy Retro overview](https://ultimachine.com/products/einsy-retro) - accessed 2026-04-04
- [LulzBot Titan Aero toolhead page](https://www.lulzbot.com/products/titan-aero-tool-head) - accessed 2026-04-04
- [Magnetic Flex Bed install guide](https://ohai.lulzbot.com/project/mini-2-magnetic-flex-bed-installation/) - accessed 2026-04-04
