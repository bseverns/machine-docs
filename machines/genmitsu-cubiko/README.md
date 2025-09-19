# Genmitsu Cubiko (CNC)

_Aim: reliable, repeatable results with clear guardrails._

- Start with `quickstart.md` and `sop.md`.
- Keep `logs/maintenance-log.csv` up to date.
- Profiles live in `profiles/` and should be **versioned** and labeled by slicer.

## Notes
- GRBL-based workflow. Keep tool database (`templates/cnc-tool-database.csv`) synced.
- Always dry-run above stock and confirm safe Z.
- Use `templates/cnc-job-sheet.md` for each job.
