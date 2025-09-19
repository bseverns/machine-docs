# Stratasys uPrint — Open Controller Paths (No DRM)

**Goal:** Replace the stock controller to run **open firmware** (Marlin / RepRapFirmware / Klipper), bypassing filament DRM and enabling standard spools.

## Options at a glance
| Path | Pros | Cons | Notes |
|---|---|---|---|
| **Duet (RepRapFirmware)** | Mature web UI, flexible I/O, chamber features | Cost | DuePrint project and forum threads are rich references |
| **Marlin (SKR/Einsy/RAMPS)** | Familiar, huge community | Less native chamber control | Cheapest path; plenty of docs |
| **Klipper (MCU + host)** | High‑performance, flexible UI | Requires SBC host | Great if you want macros/UI extensibility |

## Core steps (high‑level)
1. **Reverse‑map** wiring (steppers, heaters, thermistors, fans, endstops, chamber sensors), photograph everything.  
2. **Select controller** and **PSU plan**. Decide if you’ll reuse stock power or re‑wire.  
3. **Mechanical adapters** for board mounting and spool path changes.  
4. **Firmware config**: volume, thermistors, chamber/HEPA fans, safety limits.  
5. **Panel/UI**: stand‑alone LCD, or headless with web UI (Duet, Klipper).  
6. **Calibration**: PID tunes, steps/mm, offsets.  
7. **Document** every mapping and value in this folder.

See `links.md` and `controller-matrix.md`.
