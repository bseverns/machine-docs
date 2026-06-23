# Materials - Bambu Lab P1S

## Approval levels

| Level | Materials | Requirements |
| --- | --- | --- |
| Starter | PLA | Stock P1S PLA profile, clean verified plate, bed leveling enabled, validation cube pass |
| Standard | PETG | Dry filament, PETG-specific plate/adhesion plan, profile logged |
| Controlled | ABS, ASA | Ventilation approval, closed-enclosure workflow, odor check, trained operator |
| Controlled | TPU | External spool path, slow profile, no AMS unless a local exception is tested and documented |
| Restricted | PA, PC, support materials, filled or abrasive filaments | Maintainer approval, drying plan, nozzle/material compatibility check, profile validation |

## AMS rules

- Use AMS for compatible rigid filaments only.
- Do not load TPU through AMS under the default policy.
- Avoid cardboard spools, damaged spools, or undersized/oversized spools unless the spool adapter/path has been tested.
- Track AMS slot, filament brand, material, color, and dry state for multi-material validation jobs.
- Keep desiccant active and log replacement/reactivation.

## Nozzle and abrasion gates

- Stock nozzle material must be physically verified before approving anything abrasive.
- Carbon fiber, glass fiber, glow, metal-filled, wood-filled, and other abrasive materials require a hardened nozzle and a logged profile.
- After abrasive use, inspect nozzle wear and reprint the validation cube before returning the machine to student PLA use.

## Plate and adhesion notes

- Select the exact plate type in Bambu Studio before slicing.
- Clean smooth/textured PEI plates according to the plate-specific OEM guidance and local material notes.
- Use glue/release agent only when the plate/material pair requires it. Overuse can hide adhesion problems and contaminate measurements.
- Retire plates with deep gouges, bubbles, peeling, or repeated first-layer inconsistency.

## Drying notes

- PLA: store sealed; dry if brittle, popping, or stringy.
- PETG: dry before fit-critical or transparent prints.
- TPU: dry before every controlled job.
- ABS/ASA/PA/PC/support: dry per material supplier and Bambu profile guidance; record drying time/temp in the run notes.

## Profile naming

Use the profile naming rules in [`profiles/README.md`](./profiles/README.md). Each approved material should identify:

- Bambu Studio version.
- Printer model and nozzle size/material.
- Plate type.
- Filament brand/type/color.
- Flow dynamics / K value if calibrated.
- Flow ratio if calibrated.
- Validation artifact result.

## Sources

- Bambu Lab, *P1 Series product page*, https://bambulab.com/en/p1 - accessed 2026-06-23; stock printer material and thermal context.
- Bambu Lab, *Bambu Studio*, https://bambulab.com/en/download/studio - accessed 2026-06-23; slicer/profile source.
- Bambu Lab, *AMS Wiki*, https://wiki.bambulab.com/en/ams - accessed 2026-06-23; AMS compatibility and handling context.
