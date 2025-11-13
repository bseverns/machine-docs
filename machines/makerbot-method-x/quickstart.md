# Quick Start — MakerBot Method X

**Goal:** Produce a clean, enclosed-chamber print in ~15 minutes while respecting fumes and supports.

1. Study the [safety brief](./safety.md); confirm ventilation and purge paths are active.
2. Import `calibration-cube-20mm.stl` with the `makerbot-print-4.12.1-method-x-standard.json` profile from [`profiles/sample`](./profiles/sample/) to lock in baseline ABS-R + RapidRinse settings.
3. Execute the [SOP](./sop.md) in order: Preflight → Operation → Postflight — no skipping warmups.
4. After the print, note chamber temp, purge outcome, and soak results in the [sample run log](./logs/sample-run-log.csv).
5. Log temperature offsets, purge strips, or material swaps in the [maintenance log](./logs/maintenance-log.csv).
6. Capture jams, enclosure alarms, or anomalies in the [incident log](./logs/incident-log.csv) so we can troubleshoot fast.
