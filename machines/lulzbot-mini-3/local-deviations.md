# Local Deviations - LulzBot Mini 3

**Purpose:** record every approved way this machine differs from the OEM stock configuration.  
**Stock baseline reference:** stock LulzBot Mini 3 hardware, firmware, and CuraLE workflow as documented by LulzBot  
**Last reviewed:** 2026-04-04  

## Rules

- No undocumented hardware, firmware, profile, or workflow changes.
- Any approved change must identify the owner, reason, and rollback path.
- If a change affects training, calibration, safety, or materials, update the linked docs in the same PR.

## Controlled deviations

| Date | Subsystem | Stock baseline | Installed state | Why we changed it | Risks introduced | Rollback path | Verification / evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-04 | Fleet record | OEM stock LulzBot Mini 3 configuration | No approved local deviations documented | Preserve a clean baseline for toolhead, bed, and firmware support | If undocumented field changes exist, this doc is stale and misleading | Physical audit the machine, document any drift, and update this file immediately | Documentation review of current repo state |

## Required post-change checks

- Safety check: confirm hot-end, wipe path, bed plate fit, and cable clearances
- Functional smoke test: power on, home, preheat, and verify wipe behavior
- Calibration or baseline print: 20 mm cube plus first-layer inspection on the active plate
- Docs updated: `README.md`, `calibration.md`, `materials.md`, `troubleshooting.md`, logs as needed

## Open questions

- Capture exact asset tag, serial number, and physical location.
- Confirm whether the reversible bed plates in service are all OEM stock or include local replacements.
- Record any local Cura profile edits that should be documented as deliberate deviations rather than normal calibration drift.

## Sources

- [LulzBot Mini 3 user guide (PDF)](https://download.lulzbot.com/Mini_3/documentation/LulzBot_Mini_3_User_Guide.pdf) - accessed 2026-04-04
- [Marlin 2.x firmware builds](https://download.lulzbot.com/Software/Marlin2/) - accessed 2026-04-04
