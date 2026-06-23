# Profiles - Bambu Lab P1S

Store exported Bambu Studio profiles and validation notes here. Do not treat a stock slicer preset as a lab-approved profile until it has a logged validation print.

## Naming pattern

```text
bambu-studio-<version>-p1s-<nozzle>-<plate>-<material>-<brand>-<profile-purpose>.<extension>
```

Examples:

```text
bambu-studio-1.10.0-p1s-0.4mm-textured-pei-pla-bambu-basic-standard.json
bambu-studio-1.10.0-p1s-0.4mm-textured-pei-petg-overture-standard.json
```

Use the actual Bambu Studio export format available on the lab workstation. If the slicer exports a project bundle instead of a simple profile file, include a short `readme.md` next to it with the profile settings that matter.

## Required profile notes

Each approved profile needs:

- Bambu Studio version.
- Printer firmware version.
- Nozzle size/material.
- Plate type.
- Filament brand/type/color.
- AMS or external spool path.
- Flow dynamics / K value if calibrated.
- Flow ratio if calibrated.
- Validation cube measurements and date.
- Operator who approved the profile.

## Sample folder

[`sample/`](./sample/) contains the standard validation artifact and notes for first-run checks.
