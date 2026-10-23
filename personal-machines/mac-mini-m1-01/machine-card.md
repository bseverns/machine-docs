# Machine Card — Mac mini M1

**Atlas ID:** `mac-mini-m1-01`  
**Machine type:** Apple Mac mini (`Macmini9,1`, Apple M1, 8 GB unified memory)  
**Location:** TBD  
**Owner / steward:** Ben  
**Asset tag / serial:** verified locally; not published  
**Acquired:** TBD  
**Last host-verified:** 2026-10-23<br>
**Primary reference README:** `README.md`

## Snapshot

| Field | Current state | Verification method | Last checked |
| --- | --- | --- | --- |
| CPU / architecture | Apple M1, 8 cores, arm64 | `system_profiler` | 2026-10-22 |
| Memory | 8 GB unified memory | `system_profiler` | 2026-10-22 |
| OS | macOS 27.0.1 (`26A434`) | `system_profiler` | 2026-10-22 |
| Boot/security | normal boot; secure VM and SIP enabled | `system_profiler` | 2026-10-22 |
| Internal storage | 26.158497 GiB available; about 1.16 GiB above the experiment floor | `disk_usage`, experiment preflight | 2026-10-23 |
| External work volume | `/Volumes/Studio-AI`, backed by `/Volumes/BS_SKETCH/Studio-AI.sparsebundle` | `hdiutil`, filesystem inspection | 2026-10-22 |
| Local model service | Ollama on loopback; bounded generation and embedding checks passed | loopback API generation/embedding probes | 2026-10-23 |
| Research software | BenLab Local Analyst; supervised single-job use only | 153 tests, CLI help, smoke test, maintenance and experiment preflights | 2026-10-23 |
| Hermes state | external `HERMES_HOME`; machine-scoped profile `macminim101` created | path resolution and `hermes profile show` | 2026-10-22 |
| Corpus readiness | blocked; configured manifest, card-store, and SQLite inputs absent or unreadable | corpus preflight, exit 2 | 2026-10-23 |
| Recovery material | verified `/usr/local` quarantine archive; restore not tested | SHA-256, tar listing, sampled-content verification | 2026-10-23 |

## Identity reconciliation

The owner confirmed that this inspected machine corresponds to the existing M1 records in Systems Atlas and Studio Compute and formally approved `mini-core` as its alias. The alias is not the configured hostname and does not make the proposed role operationally ready.

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

## Migration residue

- Intel Homebrew manager roots were retired after quarantine; native Homebrew, system tools, NVM, and Hermes command paths were verified.
- MacPorts was preserved but is not operational because its Tcl interpreter is Intel-only and Rosetta is unavailable.
- Three broken `certifi/cacert.pem` links remain outside the authorized retirement scope; they are not active command paths.
- The recovery archive was verified but has not been restored in an isolated drill.

## Open physical verification

- [ ] Record location and asset tag privately.
- [ ] Photograph the chassis and label for private evidence.
- [ ] Prove restart → backing volume → sparsebundle → `Studio-AI` attachment.
- [ ] Complete an isolated restore drill.
