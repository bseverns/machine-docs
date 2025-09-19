# Stratasys **Mojo → Marlin** Conversion

**Intent:** Replace proprietary control with an open Marlin stack to unlock materials and maintenance.

## Reference Links (Marlin‑focused)
- Mojo retrofit (repo; includes Marlin configs/CAD): https://github.com/PicoPlanetDev/Stratasys-Mojo-Conversion
- Overview article: https://sigmondkukla.dev/stratasys-mojo-conversion.html
- Printables listing: https://www.printables.com/model/847720-stratasys-mojo-conversion
- Marlin controller/display overview: https://marlinfw.org/docs/hardware/controllers.html

## Controller Options
- **SKR 1.4/Turbo + TMC2209**, or **Einsy(‑Retro)**, or **RAMPS 1.4 + Mega 2560** (legacy, inexpensive).  
- Choose based on IO count, enclosure control, and your comfort level.

## High‑level Procedure
1. **Reverse‑map** stock wiring: steppers, heaters, thermistors, fans, endstops, chamber sensors. Photograph and label.  
2. **Select board** + **PSU strategy** (retain stock PSU if appropriate; add SSR for heated bed/chamber if needed).  
3. **Marlin config**: set bed volume, steps/mm, thermistor tables, safety limits, fans, chamber controls.  
4. **Panel control**: pick LCD (e.g., 128×64, DWIN/TJC, or host via USB).  
5. **Smoke test** on bench, then in chassis.  
6. **Calibration**: PID tune, steps/mm, endstop offsets; log all values here.

> Heated chambers and mains wiring require proper fusing, wiring gauges, and enclosures. Treat this as an electrical project first, a printer project second.
