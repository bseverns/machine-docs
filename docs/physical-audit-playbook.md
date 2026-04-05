# Physical Audit Playbook

_The repo can only be as truthful as the last person who touched the machine and wrote it down._

## Purpose

Use this playbook to replace `TBD` values with verified facts. A physical audit is the bridge between "the docs say" and "we checked the actual machine."

Run this when:

- A new machine enters service
- A machine has more than a handful of `TBD`s
- You suspect undocumented field changes
- Inventory is drifting or spares are getting reordered from memory
- A maintainer turnover is coming and you want the next person to inherit reality instead of lore

## What good looks like

At the end of an audit, each machine should have:

- A current `machine-card.md` with verified location, asset tag, serial, and operating setup
- A `parts-and-spares.md` with exact part numbers, quantities on hand, and shelf/bin locations
- A `local-deviations.md` that either lists approved drift from stock or explicitly says none are documented
- A dated `Last physically verified` field
- A linked photo set for access points, labels, and unusual hardware

## Prep

Before you walk to the machine:

1. Open the machine's `README.md`, `machine-card.md`, `parts-and-spares.md`, and `local-deviations.md`.
2. Print or copy the [`physical-audit-template.md`](../templates/physical-audit-template.md) into the machine folder as `physical-audit.md`.
3. Bring the tools you actually need:
   - flashlight
   - phone/camera
   - label maker or painter's tape
   - screwdriver/hex keys only if opening panels is approved
   - inventory markers for shelf/bin verification
4. Check whether the audit requires downtime or a second person for lockout/safety coverage.

## Audit sequence

### 1. Identify the machine

- Confirm the exact machine name in the repo matches the physical machine.
- Record location, asset tag, serial number, and any local nickname posted on-site.
- Photograph the front, rear, controller label, and any service or certification stickers.

### 2. Verify power and data path

- Record the outlet/circuit label if accessible.
- Confirm PSU model/label if visible without violating service boundaries.
- Record the host workstation name, USB path, network dependency, CloudPrint path, or sender workflow.
- If the machine uses removable media, note where that media lives.

### 3. Verify installed state

- Confirm controller, toolhead/spindle, build surface/workholding, and other major hardware.
- Confirm the firmware version from the UI, host software, or maintenance records if visible.
- Note anything that does not look stock, even if you do not yet know whether it was intentional.

### 4. Check spares and consumables

- Physically count critical spares.
- Record exact part numbers from packaging, labels, invoices, or OEM markings.
- Record shelf/bin locations exactly as labeled.
- Flag anything that is stocked but undocumented, or documented but missing.

### 5. Check deviations

- Compare the machine against the OEM baseline and current `local-deviations.md`.
- If you find a field modification, do not leave it as an oral note. Add it to the deviations log with a rollback path or flag it for review.
- If nothing is changed, confirm that explicitly.

### 6. Run a smoke test if safe

- Power on and verify basic readiness.
- Confirm the normal host workflow still works.
- Run the machine's baseline print/cut only if authorized and time allows.
- If the machine fails the smoke test, stop treating the audit as paperwork and log an incident.

## Evidence standards

- Photos should be usable by someone who has never seen the machine.
- Part numbers should come from labels, packaging, or cited docs, not memory.
- If a fact was not physically checked, do not mark it verified.
- Use `observed`, `verified`, and `TBD` the same way the [Source Citation Policy](./source-citation-policy.md) defines them.

## Closeout

Before ending the audit:

1. Update `machine-card.md`.
2. Update `parts-and-spares.md`.
3. Update `local-deviations.md`.
4. Attach or reference the photo set.
5. Note any follow-up actions:
   - part orders
   - missing labels
   - undocumented modifications
   - maintenance needed
   - training gaps

If the audit uncovered a real machine problem, log it in the machine's incident or maintenance records the same day.
