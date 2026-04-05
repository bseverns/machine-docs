# Local Deviations - MakerBot Sketch

**Purpose:** record every approved way this lab machine differs from the OEM stock configuration.  
**Stock baseline reference:** stock MakerBot Sketch hardware, firmware, and CloudPrint/Print workflow as documented by MakerBot  
**Last reviewed:** 2026-04-04  

## Rules

- No undocumented hardware, firmware, profile, or workflow changes.
- Any approved change must identify the owner, reason, and rollback path.
- If a change affects training, calibration, safety, or materials, update the linked docs in the same PR.

## Controlled deviations

| Date | Subsystem | Stock baseline | Installed state | Why we changed it | Risks introduced | Rollback path | Verification / evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-04 | Fleet record | OEM stock MakerBot Sketch configuration | No approved local deviations documented | Maintain a clear stock baseline for interns and future service work | If undocumented field changes exist, this doc is stale and misleading | Physical audit the machine, document any drift, and update this file immediately | Documentation review of current repo state |

## Required post-change checks

- Safety check: confirm enclosure, door behavior, and hot-end clearances
- Functional smoke test: power on, load filament, and verify homing/preheat behavior
- Calibration or baseline print: 20 mm cube with current standard profile
- Docs updated: `README.md`, `calibration.md`, `materials.md`, `troubleshooting.md`, logs as needed

## Open questions

- Capture exact asset tag, serial number, and physical location.
- Confirm whether the camera and filter assemblies are still fully stock.
- Record any station-specific CloudPrint or MakerBot Print quirks that operators should treat as local workflow, not OEM default behavior.

## Sources

- [MakerBot SKETCH user guide (PDF)](https://downloads.makerbot.com/manuals/MakerBot_SKETCH_User_Guide.pdf) - accessed 2026-04-04
- [Sketch firmware releases](https://support.makerbot.com/s/article/1667416351090-SKETCH-Firmware-Release-Notes) - accessed 2026-04-04
