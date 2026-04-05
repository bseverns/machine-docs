# Local Deviations - MakerBot Sketch+

**Purpose:** record every approved way this machine differs from the OEM stock configuration.  
**Stock baseline reference:** stock MakerBot Sketch Large hardware, firmware, and CloudPrint workflow as documented by MakerBot  
**Last reviewed:** 2026-04-04  

## Rules

- No undocumented hardware, firmware, profile, or workflow changes.
- Any approved change must identify the owner, reason, and rollback path.
- If a change affects training, calibration, safety, or materials, update the linked docs in the same PR.

## Controlled deviations

| Date | Subsystem | Stock baseline | Installed state | Why we changed it | Risks introduced | Rollback path | Verification / evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-04 | Fleet record | OEM stock MakerBot Sketch Large configuration | No approved local deviations documented | Preserve a clean baseline for large-format maintenance and training | If undocumented field changes exist, this doc is stale and misleading | Physical audit the machine, document any drift, and update this file immediately | Documentation review of current repo state |

## Required post-change checks

- Safety check: confirm enclosure, door behavior, filter fit, and tall-travel clearances
- Functional smoke test: power on, load filament, and verify homing/preheat behavior
- Calibration or baseline print: first-layer sheet plus 20 mm cube with current standard profile
- Docs updated: `README.md`, `calibration.md`, `materials.md`, `troubleshooting.md`, logs as needed

## Open questions

- Capture exact asset tag, serial number, and physical location.
- Confirm whether any local large-bed shims, alternate plate stacks, or station-specific workflows exist.
- Record whether dissolvable-support capability is actually installed or only permitted when a specific add-on is present.

## Sources

- [MakerBot Sketch Large user guide](https://support.makerbot.com/s/article/1667416351178) - accessed 2026-04-04
- [Sketch Large firmware releases](https://support.makerbot.com/s/article/1667416351184-SKETCH-Large-Firmware-Release-Notes) - accessed 2026-04-04
