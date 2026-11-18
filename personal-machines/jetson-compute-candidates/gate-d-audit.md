# Gate D — reported Jetson audit and experiment preparation

**Status:** preparation only. This worksheet creates no identity, configuration, service, or execution approval.

## Reported equipment

The reported fleet is:

- two original NVIDIA Jetson Nano boards, probably 4 GB each;
- one NVIDIA Jetson Orin Nano developer kit, probably 8 GB.

The reported Orin Nano characteristics are: fan present, DisplayPort-only video output, and USB-C near Ethernet. These are owner reports to verify on the physical unit; they are not canonical identity or installed-state evidence.

| Documentation label only | Reported hardware | Atlas ID | Installed OS / JetPack | Status |
| --- | --- | --- | --- | --- |
| `jetson-nano-reported-a` | Original Jetson Nano, probably 4 GB | unresolved | unknown | needs physical audit |
| `jetson-nano-reported-b` | Original Jetson Nano, probably 4 GB | unresolved | unknown | needs physical audit |
| `jetson-orin-nano-reported` | Jetson Orin Nano developer kit, probably 8 GB; reported fan / DisplayPort / USB-C-near-Ethernet | unresolved | unknown | needs physical audit |

Do not assign an Atlas ID, serial number, hostname, JetPack version, CUDA version, or operational role from this table.

## Before touching a board

- [ ] Obtain explicit authorization for the physical audit and any power-on.
- [ ] Prepare a private photo destination for labels, serials, and board/module markings.
- [ ] Bring power supplies, display adapter/cable, keyboard, removable-media reader, and network cable only if separately approved.
- [ ] Read the applicable NVIDIA documentation for the exact observed board before changing boot media or power mode.
- [ ] Keep the two original Nanos in the `legacy_cuda_edge` compatibility/security tier until their installed software is observed.

## Per-board physical audit

Complete this table separately for each row above. A blank/unknown result stays unknown.

| Evidence needed | Observation | Method / private evidence reference | Outcome |
| --- | --- | --- | --- |
| Exact module and carrier-board label |  |  |  |
| Private serial / asset tag record |  |  |  |
| RAM evidence |  |  |  |
| Power supply, fan/heatsink, and visible condition |  |  |  |
| Ports and attached storage |  |  |  |
| Current boot medium |  |  |  |
| OS / L4T / JetPack release if bootable |  |  |  |
| CUDA / TensorRT availability if bootable |  |  |  |
| Current network state, recorded without addresses or credentials |  |  |  |
| Existing data and recovery/rebuild material |  |  |  |

For the reported Orin, explicitly confirm or correct the fan, DisplayPort-only output, and USB-C-near-Ethernet report.

## Gate D preflight

Do not begin an inference workload until all applicable rows below have a reviewed result.

- [ ] One physical unit has a private evidence packet and a machine-docs profile based on `templates/compute-device-profile-template.md`.
- [ ] `systems-atlas` reconciliation has either established the unit's stable ID or explicitly kept it unresolved for this experiment.
- [ ] `studio-compute` has a reviewed candidate manifest with reported versus observed hardware kept separate.
- [ ] The workload uses synthetic or explicitly approved non-sensitive input.
- [ ] Backend/model format, memory requirement, local storage location, and expected output destination are declared.
- [ ] Power, cooling, shutdown, and recovery path are observed and acceptable for this bounded run.
- [ ] The experiment has a human operator, explicit start/stop authority, and an output receipt plan.
- [ ] No public endpoint, remote execution path, firewall/router/VPN/DNS/SSH change, or persistent listener is required.

## First supervised experiment receipt

Record only directly observed values:

| Field | Value / evidence |
| --- | --- |
| Physical documentation label and reconciled Atlas ID, if any |  |
| Operator / date / authorization reference |  |
| Model, backend, precision, and version |  |
| Input classification and source hash |  |
| Time to first token / completion / throughput, when applicable |  |
| Memory pressure, thermal/throttling observation, and directly measured power if available |  |
| Output hash and storage destination |  |
| Stop/cancel result and recovery outcome |  |
| Unexpected behavior / refusal / no-go decision |  |

A successful result proves only this bounded experiment. It does not authorize a service, a remote worker, a new role, or future unattended execution.
