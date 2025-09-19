# Marlin Config Notes — uPrint

> Treat this as a *diff* checklist. Don’t paste blindly; set values to match your hardware.

- **Board selection** (`MOTHERBOARD`) — pick your SKR/Octopus/Einsy variant.
- **Heaters & sensors**
  - `TEMP_SENSOR_0`, `TEMP_SENSOR_BED`, `TEMP_SENSOR_CHAMBER` — choose sensor codes from Marlin’s docs (thermistor, PT100/PT1000, or thermocouple via amplifier).
  - Set `HEATER_CHAMBER_PIN` (or `CHAMBER_HEATER_PIN` per version) and assign a **chamber thermistor** pin.
  - Enable `THERMAL_PROTECTION_CHAMBER` and set sane limits.
- **Chamber control**
  - In `Configuration_adv.h`: enable chamber features and (optionally) an `AUTO_POWER_CHAMBER_FAN` on a spare fan pin.
- **Extruder**
  - **Stepper path:** standard `E0` step/dir. Calibrate `DEFAULT_AXIS_STEPS_PER_UNIT` for E and run PID for hotend.
  - **Servo path:** keep E as step/dir into the servo driver (e.g., G320X). Tune driver gains per vendor docs; keep Marlin’s E axis conventional.
- **Endstops & motion**
  - Map X/Y/Z endstops; confirm logic in `INVERT_*_ENDSTOP`.
  - Set bed size and homing direction to match uPrint kinematics.
- **Power & safety**
  - Size max temps, watch thermal runaway settings, and set conservative current limits for drivers.

Add your final `Configuration.h` and `Configuration_adv.h` to this folder once stable.
