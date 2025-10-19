# Genmitsu Cubiko (CNC)

_Aim: reliable, repeatable results with clear guardrails._

## Start here
- [Quick Start](./quickstart.md) — practice run that covers CAM-to-machine basics.
- [Safety](./safety.md) — chip containment, PPE, and emergency stops.
- [SOP](./sop.md) — the authoritative preflight → run → cleanup sequence.

## Reference set
- [Genmitsu Cubiko user manual](https://www.sainsmart.com/pages/download/genmitsu-cubiko-user-guide) — full wiring, workholding, and maintenance callouts straight from SainSmart.
- [GRBL 1.1h firmware & release notes](https://github.com/gnea/grbl/releases) — controller source; confirm config diffs before flashing.
- [Fusion 360 Manufacturing workspace docs](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-D83A14C5-07DB-4E7D-9865-3CE0A1C46589) — reference for adaptive/trochoidal strategies we standardize on.
- [Lab cheat: CNC job sheet template](../../templates/cnc-job-sheet.md) — capture feeds, speeds, and setup photos every run.

## Machine facts at a glance
- **Work envelope:** 304 × 304 × 72 mm (per SainSmart spec) — respect travel; verify Z on tall stock before committing.
- **Controller / firmware:** GRBL 1.1h on the stock motion board; stream via Candle/UGS with $N macros staged.
- **Spindle & interface:** 300 W brushless spindle with ER11 collet (1/8" default, 1/4" optional) — tighten with matched wrenches, no pliers.
- **Approved stock:** Hardwood, cast acrylic, machinable wax, FR-1 PCBs; 6061 aluminum allowed with ≤0.5 mm stepover and flood-free chip clearing.
- **Unique hardware:** Fully enclosed acrylic shell, magnetic chip tray, integrated LED strips, and a quick-swap spoilboard pinned to a T-slot base.

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

## Source-of-truth links
- [SainSmart Genmitsu Cubiko product page](https://www.sainsmart.com/products/genmitsu-cubiko) — official specifications and accessory list.
- [SainSmart Docs: Cubiko introduction](https://docs.sainsmart.com/article/intro-genmitsu-cubiko) — assembly, wiring, and firmware guidance.
- [Genmitsu support downloads](https://www.sainsmart.com/pages/genmitsu-cubiko-download) — firmware, drivers, and CAM profiles maintained by SainSmart.

