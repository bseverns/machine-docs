# Controller Matrix — uPrint

| Controller | I/O fit | Heated chamber control | Web UI | Notes |
|---|---|---|---|---|
| **Duet 2/3** (RRF) | Excellent | Native tools (fans/thermistors) | Yes | Most documented community path |
| **SKR 1.4/Turbo** (Marlin) | Good | DIY (SSR/fans) | Via Octo/Klipper | Cheap, familiar Marlin configs |
| **Einsy(‑Retro)** (Marlin) | Adequate | DIY | Via Octo/Klipper | Reuse from Prusa ecosystem |
| **RAMPS 1.4 + Mega** (Marlin) | Adequate | DIY | Via Octo/Klipper | Legacy, inexpensive |

> Add your selected controller and fill the exact pin maps and power domains in a `wiring-map.md` (template copied from FolgerTech i3 folder).
