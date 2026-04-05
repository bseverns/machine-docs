# Local Deviations - MakerBot Method X

**Purpose:** record every approved way this machine differs from the OEM stock configuration.  
**Stock baseline reference:** stock MakerBot Method X hardware, Method OS, and approved MakerBot workflow as documented by MakerBot  
**Last reviewed:** 2026-04-04  

## Rules

- No undocumented hardware, firmware, profile, material, or workflow changes.
- Any approved change must identify the owner, reason, and rollback path.
- If a change affects training, calibration, safety, or material handling, update the linked docs in the same PR.

## Controlled deviations

| Date | Subsystem | Stock baseline | Installed state | Why we changed it | Risks introduced | Rollback path | Verification / evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-04 | Fleet record | OEM stock Method X configuration | No approved local deviations documented | Preserve a clean baseline for chamber, extruder, and support-material maintenance | If undocumented field changes exist, this doc is stale and misleading | Physical audit the machine, document any drift, and update this file immediately | Documentation review of current repo state |

## Required post-change checks

- Safety check: verify chamber, filters, spool bays, and enclosure condition
- Functional smoke test: power on, heat chamber, load materials, and confirm purge behavior
- Calibration or baseline print: approved baseline part with current standard material pairing
- Docs updated: `README.md`, `calibration.md`, `materials.md`, `troubleshooting.md`, logs as needed

## Open questions

- Capture exact asset tag, serial number, and physical location.
- Confirm whether the LABS Experimental head is actually present on-site or only supported as a future option.
- Record any local humidity-control or material-storage practices that go beyond the OEM workflow.

## Sources

- [MakerBot Method X user guide (PDF)](https://downloads.makerbot.com/manuals/MakerBot_MethodX_UserGuide.pdf) - accessed 2026-04-04
- [MakerBot OS Method software release notes](https://support.makerbot.com/s/article/1267528410370-Method-Software-Release-Notes) - accessed 2026-04-04
