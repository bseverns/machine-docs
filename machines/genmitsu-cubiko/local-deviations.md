# Local Deviations - Genmitsu Cubiko

**Purpose:** record every approved way this machine differs from the OEM stock configuration.  
**Stock baseline reference:** stock Genmitsu Cubiko hardware, GRBL configuration, and approved sender workflow as documented by SainSmart and internal setup docs  
**Last reviewed:** 2026-04-04  

## Rules

- No undocumented hardware, firmware, macro, CAM, or workholding changes.
- Any approved change must identify the owner, reason, and rollback path.
- If a change affects training, calibration, safety, or approved stock, update the linked docs in the same PR.

## Controlled deviations

| Date | Subsystem | Stock baseline | Installed state | Why we changed it | Risks introduced | Rollback path | Verification / evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-04 | Fleet record | OEM stock Genmitsu Cubiko configuration | No approved local deviations documented | Preserve a clean baseline for GRBL settings, tooling, and workholding support | If undocumented field changes exist, this doc is stale and misleading | Physical audit the machine, document any drift, and update this file immediately | Documentation review of current repo state |

## Required post-change checks

- Safety check: confirm enclosure, spindle mount, workholding, and chip-management readiness
- Functional smoke test: power on, connect sender, verify homing and macro behavior, dry-run above stock
- Calibration or baseline cut: sample pocket with approved stock and tool
- Docs updated: `README.md`, `calibration.md`, `materials.md`, `troubleshooting.md`, logs as needed

## Open questions

- Capture exact asset tag, serial number, and physical location.
- Confirm whether the staged `$N` macros match pure OEM defaults or contain local edits that should be documented here.
- Record any local spoilboard, fixture, or dust-handling practices that count as deliberate workflow deviations.

## Sources

- [Genmitsu Cubiko user manual](https://www.sainsmart.com/pages/download/genmitsu-cubiko-user-guide) - accessed 2026-04-04
- [GRBL releases](https://github.com/gnea/grbl/releases) - accessed 2026-04-04
