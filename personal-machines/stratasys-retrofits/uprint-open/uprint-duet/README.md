# uPrint → **Duet / RepRapFirmware** Conversion Path

A pragmatic alternative to Marlin using **Duet 2/3** hardware and **RepRapFirmware (RRF)**.

## Controller Options
- **Duet 2 WiFi/Ethernet** — proven, add-on daughterboards for thermocouples/PT100.
- **Duet 3 6HC** — more I/O and expansion, tool boards possible; flexible chamber control.
- **Expansion** — use Duet thermocouple/PT100 daughterboards or supported SPI thermocouple modules.

## K‑type Strategy
- Prefer Duet **thermocouple daughterboards** (MAX31856‑based) for hotend/bed/chamber.
- Alternatively, use supported SPI thermocouple interfaces per RRF docs.

## Chamber Control
- Map a spare heater output to **chamber heater** via SSR.
- Use `M141 Sxx` to set and `M191 Sxx` to wait for chamber temp.
- Assign chamber sensor as a named temperature channel and bind it to the chamber heater.

See `config-g-examples.md`, `wiring-map.md`, and `BOM.md`.
