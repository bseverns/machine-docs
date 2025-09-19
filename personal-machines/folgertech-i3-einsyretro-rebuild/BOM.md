# BOM — FolgerTech i3 with EinsyRetro 1.0a

> Choose parts that match your PSU voltage (12/24V) and bed/heater currents. When in doubt, overspec safety components and add ferrules/strain relief.

See `BOM.csv` for a sortable table. Add vendor links in-column as you source parts.

## Controller & Power
- **EinsyRetro 1.0a** (UltiMachine) — on‑board TMC2130s, SPI; sensorless homing optional.
- **SSR for bed** (optional): if your bed draws near/over the board limit, offload with a properly‑rated SSR and protected wiring.
- **IEC C14 inlet with fused switch**, sized to PSU.

## Wiring discipline
- Crimp **ferrules** on all high‑current lines.
- Use proper **JST‑XH** for endstops/fans and matching headers for steppers.
- Label everything; route endstop wires away from motor bundles.

## Nice‑to‑have
- Quiet 40mm fan aimed at the driver area.
- Ferrite clips on endstop lines if you see false triggers.
- Printed board mount and cable guide (add STL link when chosen).
