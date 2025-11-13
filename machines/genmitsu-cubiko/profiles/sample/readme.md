# Sample Job — Surfacing + Pocket Warm-Up

This job knocks the rust off the CubiKo and your CAM nerves. Start in **Carbide Create 7** (or drop the provided G-code straight into Candle) and run a two-stage warm-up on a scrap of 12 mm MDF.

## Files
- `stock-blank-80x40x10.stl` — reference geometry for CAM packages that want a solid model.
- `sample-pocket.nc` — verified G-code: perimeter skim plus center pocket helix.
- `preview-notes.md` — directions for capturing the simulation screenshot.

## Material + Tooling
- **Stock:** MDF or pine, 80 × 40 × 12 mm. Clamp it like you mean it.
- **Endmill:** 1/8" single-flute upcut, freshly sharpened. Stick-out ≤ 19 mm.
- **Spindle:** 18,000 RPM with dust shoe attached.

## Expectations
- Dry run first with Z lifted 5 mm to confirm workholding.
- Real cut should leave a 0.3 mm skin on the pocket floor. Measure it and log the deviation.
- Chips must come out fluffy. If you're getting powder, bump feed or swap the tool.

> 📸 Visualization missing? Run through `preview-notes.md` and stash the CAM screenshot here as `preview.png` when time allows.
