# Machine Card — Mac mini M1

**Atlas ID:** `mac-mini-m1-01`  
**Machine type:** Apple Mac mini (`Macmini9,1`, Apple M1, 8 GB unified memory)  
**Location:** TBD  
**Owner / steward:** Ben  
**Asset tag / serial:** verified locally; not published  
**Acquired:** TBD  
**Last host-verified:** 2026-10-22  
**Primary reference README:** `README.md`

## Snapshot

| Field | Current state | Verification method | Last checked |
| --- | --- | --- | --- |
| CPU / architecture | Apple M1, 8 cores, arm64 | `system_profiler` | 2026-10-22 |
| Memory | 8 GB unified memory | `system_profiler` | 2026-10-22 |
| OS | macOS 27.0.1 (`26A434`) | `system_profiler` | 2026-10-22 |
| Boot/security | normal boot; secure VM and SIP enabled | `system_profiler` | 2026-10-22 |
| Internal storage | approximately 500 GB; critically low headroom during audit | `disk_usage` | 2026-10-22 |
| External work volume | `/Volumes/Studio-AI`, backed by `/Volumes/BS_SKETCH/Studio-AI.sparsebundle` | `hdiutil`, filesystem inspection | 2026-10-22 |
| Local model service | Ollama on loopback with `qwen3:4b` and `embeddinggemma` | `ollama list`, listener inspection | 2026-10-22 |
| Research software | BenLab Local Analyst; supervised single-job use only | dependency-complete test suite and smoke test | 2026-10-22 |
| Hermes state | external `HERMES_HOME`; machine-scoped profile `macminim101` created | path resolution and `hermes profile show` | 2026-10-22 |

## Identity reconciliation

The owner confirmed that this inspected machine corresponds to the existing M1 records in Systems Atlas and Studio Compute. This does not promote the proposed `mini-core` alias into the configured hostname or make the proposed role operationally ready.

## Current operating boundary

Allowed now:

- one supervised `qwen3:4b` research job at a time;
- explicit trusted inputs;
- staged, noncanonical outputs;
- human review before promotion;
- local fleet documentation and read-only coordination.

Not ready:

- unattended general research execution;
- public or LAN model/API exposure;
- remote administration;
- unique data without a tested off-device restore;
- service persistence that depends on an unproved post-restart external mount.

## Open physical verification

- [ ] Record location and asset tag privately.
- [ ] Photograph the chassis and label for private evidence.
- [ ] Prove restart → backing volume → sparsebundle → `Studio-AI` attachment.
- [ ] Complete an isolated restore drill.
