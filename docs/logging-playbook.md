# Machine Logging Playbook

_Keep the logs loud, honest, and useful. If we don't write it down, it didn't happen._

## Why this exists
Our lab's heartbeat lives in two CSVs:
- [`logs/maintenance-log.csv`](../logs/maintenance-log.csv) — running tally of every tune-up, swap, and calibration tweak.
- [`logs/incident-log.csv`](../logs/incident-log.csv) — when a print fails spectacularly or a spindle screams, this is where the truth goes.

Consistent review turns raw data into signal so we can retire flaky components before they bite us twice.

## Routine review workflow
1. **Pull the latest main branch** so you aren't reading stale data.
2. **Open `logs/maintenance-log.csv`.** Sort by `machine` then `date`.
   - Look for overdue preventative tasks (`status` != `closed`).
   - Flag repeated notes for the same subsystem (e.g., "Z wobble" twice in a month).
   - Cross-check that any parts ordered in prior entries now show an install date.
3. **Scan `logs/incident-log.csv`.** Sort by `severity` high→low, then `date`.
   - Confirm each incident has a `resolution_owner` and `follow_up` status.
   - Add links to supporting evidence (photos, gcode, tickets) if missing.
   - If an incident required decommissioning, ensure the machine folder README reflects it.
4. **Capture deltas.** Drop bullets in the audit template (see [`templates/monthly-log-audit-checklist.csv`](../templates/monthly-log-audit-checklist.csv)) noting:
   - Machines needing action this month.
   - Parts to order, training gaps, and open root-cause hunts.
5. **Publish the notes.** Commit the filled audit template back to `logs/audits/YYYY-MM/` with a short PR explaining themes.

## Audit cadence
| Cadence | Who | Scope | Output |
| --- | --- | --- | --- |
| **Weekly spot-check** | Shift lead (rotating) | New entries only | Slack ping or lab notebook note; update owners if missing |
| **Monthly deep audit** | Maintenance captain + apprentice | Full maintenance + incident logs | Completed audit template + issue/PR backlog |
| **Quarterly retro** | Lab manager + safety officer | Trends across 3 months | Retro doc with theme clusters + policy tweaks |

Miss a beat? Catch up within 48 hours and log why so we can fix the blockage.

## Escalation pathways
- **Recurring faults (same subsystem ≥3 times in 60 days):**
  1. Tag the machine steward and lab manager in the incident entry.
  2. Open a GitHub issue labeled `recurring-fault` with links to the relevant log rows.
  3. Draft a containment plan within 72 hours (temporary downtime, restricted operators, etc.).
- **Safety-critical incidents (injury, near-miss, fire):**
  1. Halt the machine immediately and mark it "LOCKED OUT" on-site.
  2. Notify campus safety per lab SOP and file the formal report.
  3. Update `logs/incident-log.csv` with full details + `severity=critical`.
  4. Schedule an emergency review within 24 hours and document outcomes in `/docs/safety-retros/`.
- **Data quality rot (missing fields, duplicate entries):**
  - Fix the rows, note the correction in the audit template, and coach the operator who missed the mark.

## Keep it punk, not chaotic
The goal is radical transparency. We document to keep each other safe, to ship better prints, and to build a trail we can trust when the dean walks in. When in doubt, log it and let the data tell the story.
