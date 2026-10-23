# Mac mini M1 — `mac-mini-m1-01`

This folder records physical and host-local facts for the personal Mac mini reconciled with Atlas ID `mac-mini-m1-01`. Planning assignments remain in `studio-compute`; current runtime health is not established by this document.

## Verified host facts

| Field | Observation | Evidence | Checked |
| --- | --- | --- | --- |
| Product | Apple Mac mini | `system_profiler SPHardwareDataType` | 2026-10-22 |
| Model identifier | `Macmini9,1` | `system_profiler SPHardwareDataType` | 2026-10-22 |
| Chip | Apple M1, 8 CPU cores | `system_profiler SPHardwareDataType` | 2026-10-22 |
| Unified memory | 8 GB | `system_profiler SPHardwareDataType` | 2026-10-22 |
| Operating system | macOS 27.0.1 (`26A434`) | `system_profiler SPSoftwareDataType` | 2026-10-22 |
| Boot volume | `Macintosh HD` | `system_profiler SPSoftwareDataType` | 2026-10-22 |
| Secure boot mode | normal boot; secure VM enabled; SIP enabled | `system_profiler SPSoftwareDataType` | 2026-10-22 |

The serial number and platform UUID were verified locally and deliberately omitted from the repository. The owner confirmed that this inspected host corresponds to the M1 records already present in both `systems-atlas` and `studio-compute`.

## Authority links

- Stable identity: `systems-atlas/inventory/fleet.yaml#mac-mini-m1-01`
- Planning record: `studio-compute/inventory/machines.csv#SC-003`
- Planning/runbook: `studio-compute/docs/machines/mini-core.md`
- Physical/host facts: this folder

## Boundaries

- `mini-core` remains a planning alias, not a configured hostname.
- The proposed coordination role remains conditional, not proof of deployment.
- Do not publish serial numbers, platform UUIDs, credentials, or private network addressing.
- Keep Ollama loopback-only unless a separately reviewed access contract requires otherwise.

## First-party references

- [Identify your Mac mini](https://support.apple.com/en-us/102852) — Apple Support, accessed 2026-10-22.
- [Allow a remote computer to access your Mac](https://support.apple.com/guide/mac-help/allow-a-remote-computer-to-access-your-mac-mchlp1066/mac) — Apple Support, accessed 2026-10-22; reference only, not evidence that Remote Login is enabled.
