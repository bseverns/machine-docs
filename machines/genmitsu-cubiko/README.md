# Genmitsu Cubiko (CNC)

_Aim: reliable, repeatable results with clear guardrails._

## Start here
- [Quick Start](./quickstart.md) — practice run that covers CAM-to-machine basics.
- [Safety](./safety.md) — chip containment, PPE, and emergency stops.
- [SOP](./sop.md) — the authoritative preflight → run → cleanup sequence.

## Keep the trail warm
- [Maintenance log](./logs/maintenance-log.csv) — document tram checks, fixture changes, or firmware notes.
- [Incident log](./logs/incident-log.csv) — capture tool breaks or near-misses within 24 hours.
- [Profiles & CAM assets](./profiles/) — post processors, tool libraries, and sample jobs.
- [Checklists](./checklists/) — setup and teardown aides.
- [Training assets](./training/) — skill ladders, CAM exercises, and QR references.

## Field notes
- Workflow is GRBL-based; keep the tool database synced with [`templates/cnc-tool-database.csv`](../../templates/cnc-tool-database.csv).
- Always dry-run above stock to verify safe Z and work offsets before cutting chips.
- Use the [`cnc-job-sheet`](../../templates/cnc-job-sheet.md) for every job and store completed sheets per project policy.
