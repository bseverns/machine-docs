# Template Field Guide

_Shortcuts for the docs we keep cloning, plus the knobs you should twist before sharing them._

## TL;DR roster

| Template | Use it when | Tune these fields |
| --- | --- | --- |
| [`SOP-template.md`](SOP-template.md) | Documenting the canonical runbook for a machine or recurring job. | Machine name, skill level, pre/postflight steps. |
| [`quickstart-template.md`](quickstart-template.md) | Giving a newcomer their first win without reading the whole library. | Machine name, sample job path, log destinations. |
| [`checklist-template.md`](checklist-template.md) | Creating a preflight inspection or shift-start ritual. | Machine name, safety checks, verification items. |
| [`troubleshooting-template.md`](troubleshooting-template.md) | Capturing symptoms and recovery paths when stuff breaks weird. | Symptom table entries, diagnostic steps, escalation plan. |
| [`cnc-job-sheet.md`](cnc-job-sheet.md) | Tracking CNC runs that need human + machine context. | Operator, tooling, workholding, program order. |
| [`cnc-tool-database.csv`](cnc-tool-database.csv) | Sharing vetted CNC tool parameters across jobs. | Tool rows (diameter, flutes, material, notes). |
| [`maintenance-log.csv`](maintenance-log.csv) | Logging service actions, cleanings, calibrations. | Each row: date, operator, task, notes, next due. |
| [`material-profile.yaml`](material-profile.yaml) | Recording slicer-ready material settings. | Material metadata, temps, speed, notes. |
| [`risk-assessment.md`](risk-assessment.md) | Preflight hazard analysis before sketchy tasks. | Machine, task, hazard controls, approval line. |

---

## SOP Template
- **When to deploy:** Every time a process graduates from sticky-notes to official lore. Perfect for machine operations, calibration rituals, or anything that could injure pride or fingers.
- **Dial these in:**
  - `{{MACHINE_NAME}}`, `Skill level`, `Last verified` date to signal freshness.
  - Preflight/Postflight checkboxes; write them like you’re coaching future-you at 3 AM.
  - Numbered steps under “Operation” — make each one a single verb + outcome.
- **First-use boost:**
  - Drop in a hero photo or thumbnail of the machine at the top (even a phone snap beats nothing).
  - Add a one-line “Abort if…” callout near Preflight to keep new operators safe.

## Quick Start Template
- **When to deploy:** Handing someone the keys for a first solo run. It’s the “don’t read the whole manual, just do this” doc.
- **Dial these in:**
  - Swap `{{MACHINE_NAME}}` and point “Sample Job” at an actual repo path or USB stick filename.
  - Update the referenced SOP, safety doc, and log locations so links don’t dead-end.
- **First-use boost:**
  - Embed a three-shot photo strip: materials laid out, machine UI, finished part.
  - Add a micro-checklist box (“Do these three things before you press START”).

## Checklist Template
- **When to deploy:** Building repeatable inspections for opening/closing shifts, material swaps, or post-maintenance smoke tests.
- **Dial these in:**
  - Customize the line items with the actual PPE, machine checks, and weekly safety verifications.
  - Consider a “Last updated” line at the top so operators know it’s current.
- **First-use boost:**
  - Print it, laminate it, and throw a dry-erase marker on a lanyard next to the machine.
  - Add icons or color coding (✅ / ⚠️) to highlight critical items.

## Troubleshooting Template
- **When to deploy:** The moment a symptom shows up twice. Capture the failure, fix, and when to escalate.
- **Dial these in:**
  - Fill the quick table with the top three “it always does this” issues.
  - In the detailed section, write diagnosis steps like a choose-your-own-adventure: “If A, go to step 3.”
  - Note who to call/text when the quick fix doesn’t work.
- **First-use boost:**
  - Add a QR code linking to a 60-second video showing the fix-in-action.
  - Include thumbnails of error screens or bad prints so operators can match symptoms fast.

## CNC Job Sheet
- **When to deploy:** Anytime you’re running a CNC job that isn’t obvious or is shareable. It turns tribal knowledge into a logbook entry.
- **Dial these in:**
  - Capture operator name, material, workholding, tool offsets, and CAM program order.
  - Note coolant/dust collection status and anything hacky in “Notes / risks”.
- **First-use boost:**
  - Attach a quick pen sketch or screenshot of the setup.
  - Add a checkbox for “Posted to CNC run log” so the paper trail continues.

## CNC Tool Database
- **When to deploy:** When more than one person is programming the CNC and you want them cutting with the same assumptions.
- **Dial these in:**
  - Each row should include tool number, diameter, flutes, material, operation, and notes. Keep units explicit (mm vs imperial).
  - Add columns if you routinely tweak feeds/speeds or stick-out.
- **First-use boost:**
  - Export a filtered view (e.g., “aluminum roughing go-tos”) and pin it near the CNC workstation.
  - Consider a thumbnail grid of each tool to reduce “is this the right one?” moments.

## Maintenance Log
- **When to deploy:** Always-on log for cleanings, calibrations, part swaps, and E-stop drills.
- **Dial these in:**
  - Date + operator + task are mandatory. Use “Notes” to capture readings, consumables, or symptoms.
  - `next_due` should be a real date or runtime hour mark; don’t leave it blank.
- **First-use boost:**
  - Print a weekly checklist that references this log so staff actually write things down.
  - Plot the CSV in a dashboard (even a Google Sheet) for trend spotting.

## Material Profile
- **When to deploy:** Any time you validate slicer settings for a specific filament or stock. Keeps experiments from evaporating.
- **Dial these in:**
  - Update material metadata (vendor, color, machines) and dial in temps, speeds, retraction, adhesion method.
  - Use `notes` for quirks (“likes 0.4 mm layers”, “needs slow first layer”).
- **First-use boost:**
  - Attach a thumbnail of the best print made with this profile.
  - Link out to the slicer profile file so users can download/import immediately.

## Risk Assessment
- **When to deploy:** Before running anything spicy — new materials, flammable finishes, unattended prints, or maintenance with guards off.
- **Dial these in:**
  - Spell out machine, task, hazards, likelihood/severity, controls, and residual risk honestly.
  - Fill the approval line with a real signature/date; this is the CYA document.
- **First-use boost:**
  - Embed a mini flowchart (“If residual risk stays High → escalate to lab manager”).
  - Snap a photo of the setup annotated with hazard zones.

---

### Next steps & wish list
- Add thumbnail photos or annotated screenshots for SOP, Quick Start, and Troubleshooting templates to make them instantly recognizable.
- Build printable “first-use” mini checklists (half-page) that reference the most common templates and hang them near each machine.
- Consider lightweight Loom/YouTube clips tied to each template for new operators who learn better by watching than reading.
