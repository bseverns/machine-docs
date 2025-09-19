# uPrint → **Marlin** Conversion Path

A practical outline to run a Stratasys uPrint on **Marlin** while preserving as much stock hardware as is sensible.

> Strategy: keep the chassis, motion system, chamber hardware, and as many sensors as practical; replace the controller with a modern Marlin board and add any necessary interface electronics.

## Control Board Options (pick one)
- **BTT SKR 1.4 / 1.4 Turbo** + TMC2209 drivers — affordable, enough I/O with add‑ons.
- **BTT Octopus / Octopus Pro** — more I/O, breakouts for multiple thermistors/fans; good if you want chamber control and extras.
- **EinsyRetro 1.0a** — reuse if on hand; I/O is tighter, plan expansions carefully.

## Temperature Sensing
Two viable routes:

1) **Keep the stock K‑type thermocouples** with amplifier boards supported by Marlin (e.g., MAX31855/31856, AD8495/AD595).  
   - Pros: Reuses sensors rated for high temps.  
   - Cons: Needs SPI/analog interface boards and config.  

2) **Swap to PT100/ PT1000 or NTC thermistors** at the hotend/bed + add a chamber thermistor.  
   - Pros: Simpler Marlin config, abundant parts.  
   - Cons: More hardware replacement.

> uPrints commonly use **K‑type thermocouples** for chamber / tool sensing; plan accordingly if you keep them.

## Extruder Strategy
- **Option A (simpler):** Replace the stock DC‑servo extruder with a stepper‑based unit (e.g., Bondtech BMG + high‑temp hotend).  
- **Option B (advanced):** Retain the DC‑servo with a **step/dir servo driver** (e.g., GeckoDrive G320X) so Marlin still outputs step/dir to “E”.

## Chamber & Safety
Enable Marlin’s **heated chamber** feature (heater via SSR, chamber sensor, managed fan). Use **M141/M191** in start G‑code to preheat and hold chamber temperature.

See `config-notes.md`, `wiring-map.md`, and `start-gcode-examples.md`.
