# Firmware — MRiscoC ProUI on SKR Mini E3 V3 (Aquila) — **TJC Screen**

- **Base:** Marlin, MRiscoC ProUI
- **Board:** BTT SKR Mini E3 V3.0
- **Screen:** **TJC** (smart display variant)

## Choose the right build
- Use a **ProUI build that matches TJC**. Some releases include `-TJC` display assets or instructions for TJC screens.
- If using a Creality-branded color screen, prefer `-TJC` builds; if Aquila stock, pick the Aquila color or C2 (128×64) variant accordingly.

## Update flow — Display assets (TJC)
1. Prepare µSD ≤ 8GB, **MBR + FAT32**, 4KB sectors.  
2. Copy the **`TJC_SET`** folder to the root of the card.  
3. Power **off**, open the display, insert µSD into the screen’s slot.  
4. Reconnect, power **on**, wait for asset update (color swap/indicator), then power down and remove µSD.  
5. Reboot and verify UI renders correctly.

## Flashing the mainboard
- Flash the SKR Mini E3 V3 with the matching **ProUI** binary for Aquila + TJC. Keep the exact `.bin` in `/firmware/` for rollback.

## Post‑flash checklist
- Run: **Home → Bed Leveling → Probe Z‑Offset → Store**.  
- Validate thermistor tables for the **Sprite** hotend and bed.  
- Confirm CR‑Touch pin mapping and deploy/retract behavior before any print.

## Version Log
| Date | ProUI build | Board | Screen | Probe | Notes |
|---|---|---|---|---|---|
| 2025-09-19 |  | SKR Mini E3 V3 | TJC | CR‑Touch | scaffold |
