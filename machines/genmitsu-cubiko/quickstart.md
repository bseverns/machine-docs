# Quick Start — Genmitsu Cubiko (CNC)

**Goal:** Execute a safe, clean cut in ~15 minutes while validating work offsets and feeds.

1. Read the [safety brief](./safety.md) and confirm chip containment and dust collection are ready.
2. Grab `sample-pocket.nc` plus the MDF reference block from [`profiles/sample`](./profiles/sample/) and sanity-check the work offset, tool, and feeds before spooling up.
3. Walk through the [SOP](./sop.md): Preflight → Operation → Postflight — include an air-cut above stock.
4. After the pass, record spindle/tool/material notes in the [sample run log](./logs/sample-run-log.csv) so we keep a running baseline.
5. Document tool changes, tram adjustments, or fixture tweaks in the [maintenance log](./logs/maintenance-log.csv).
6. Log broken tools, stock pull-outs, or near-misses in the [incident log](./logs/incident-log.csv) so we can adjust procedures.
