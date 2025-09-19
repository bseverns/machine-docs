# Path Choices — Extruder & Sensors

## Extruder
- **A. Stepper-based** (recommended): drop a stepper extruder + high-temp hotend in the existing carriage.
- **B. Servo-based** (advanced): keep the DC servo, add a step/dir servo driver. Requires tuning and space.

## Sensors
- **Keep K-type** with amplifier boards (SPI or analog). Fewer physical changes; more config.
- **Swap to PT100/PT1000/NTC** for simpler Marlin config; ensure sensor rating supports chamber temps.
