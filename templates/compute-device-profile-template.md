# Compute Device Profile — {{MACHINE_NAME}}

Use this only for a physically distinct compute device. Keep planning roles in `studio-compute`, live availability in its observing system, and stable IDs in `systems-atlas` after reconciliation.

**Atlas ID:** `TBD — do not infer`
**Documentation label:**
**Location:** `TBD`
**Owner / steward:**
**Asset tag / serial:** record privately; do not publish
**Last physically inspected:** `TBD`

## Owner report

| Field | Reported value | Source / reporter | Date reported |
| --- | --- | --- | --- |
| Model / board |  |  |  |
| Memory |  |  |  |
| Intended role |  |  |  |

Reported values are leads for an inspection, not installed-state facts.

## Vendor specification

| Field | Vendor specification | Reference / revision | Applies to this unit? |
| --- | --- | --- | --- |
| CPU / accelerator |  |  | `TBD` |
| Memory / storage interface |  |  | `TBD` |
| Display / USB / network ports |  |  | `TBD` |
| Power / cooling |  |  | `TBD` |

## Physical inspection

| Field | Observed value | Method / photo reference | Checked |
| --- | --- | --- | --- |
| Exact module / carrier-board label |  |  |  |
| Memory evidence |  |  |  |
| Asset tag / serial recorded privately |  |  |  |
| Power supply and cooling |  |  |  |
| Ports and attached storage |  |  |  |
| OS / firmware / accelerator stack |  |  |  |

Do not copy reported values into a verified field until the actual device or an on-device command supports them.

## Benchmark evidence

| Workload | Input classification | Backend / model version | Measured result | Evidence path | Date |
| --- | --- | --- | --- | --- | --- |
| `TBD — no workload authorized` |  |  |  |  |  |

A benchmark is point-in-time evidence, not permission for unattended or remote use.

## Recovery and thermal limits

- **Known recovery path:** `TBD`
- **Off-device backup / rebuild material:** `TBD`
- **Restore drill:** `TBD`
- **Thermal / power limit evidence:** `TBD`
- **No-go conditions:** `TBD`
- **Shutdown / rollback procedure:** `TBD`

## Gate status

- [ ] Physical identity is reconciled with `systems-atlas`.
- [ ] Installed software and acceleration backend are observed.
- [ ] Recovery path and shutdown procedure are documented.
- [ ] Thermal and power limits are measured for the intended workload.
- [ ] A separately approved Gate D experiment may begin.

## Boundaries

- Do not record credentials, private network addresses, or raw security observations.
- Do not treat this profile as live availability, scheduling authorization, or a service runbook.
- Do not expose a listener, change networking, flash firmware, or start an inference workload as part of documentation alone.
