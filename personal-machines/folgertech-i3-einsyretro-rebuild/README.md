# FolgerTech i3 — Planned **EinsyRetro 1.0a** Rebuild

**Goal:** Transplant an **EinsyRetro 1.0a** into the FolgerTech i3 clone, standardize on Marlin, and document a safe, reversible wiring plan.

## Links (reference set)
- UltiMachine **Einsy Retro 1.0a** (product): https://ultimachine.com/products/einsy-retro
- RepRap wiki — EinsyRetro: https://reprap.org/wiki/EinsyRetro
- Alternate reseller (spec confirmation): https://www.amazon.com/UltiMachine-Printer-Motherboard-Mechanical-Complete/dp/B0BF64357M

## Plan (draft)
1. **Survey** frame, PSU, motors (NEMA17), endstops, heaters; photograph connectors.  
2. **Bench-wire** EinsyRetro; verify USB comms and basic I/O.  
3. **Marlin config**: start from Einsy family example; set bed size/steps, endstop polarity, thermistors.  
4. **Power domains**: map heaters/fans/logic rails; confirm fusing.  
5. **Smoke test**: jog axes, verify endstops, PID tune hotend/bed, check fans.  
6. **Cable discipline**: labels, ferrules, strain relief, shielding for endstop lines.

> Record all steps/mm, PID, and offsets in `firmware-notes.md`.
