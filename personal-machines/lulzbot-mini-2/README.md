# LulzBot Mini 2 — Keep the classroom workhorse weird and reliable

**Intent:** Keep this Mini 2 battle-ready for rapid prototyping, while documenting every tweak so the next tech can pick it up without losing a beat.

## Reference set
- Official LulzBot Marlin firmware builds: https://gitlab.com/lulzbot3d/firmware/marlin/-/releases
- E3D Titan Aero assembly and tuning guide: https://e3d-online.zendesk.com/hc/en-us/sections/360003129357-Titan-Aero
- LulzBot magnetic flex plate primer: https://support.lulzbot.com/hc/en-us/articles/360022995173-Magnetic-Flex-Steel-Print-Beds

## Machine facts
- Runs an **UltiMachine Einsy Retro** control board — reuse the Einsy profiles, cable ferrules, and fusing guidelines when you swap parts.
- Ships with an **E3D Titan Aero** hotend and direct-drive extruder — expect 0.5 mm nozzle stock, but log any swaps in `firmware-notes.md`.
- Lives on a **magnetic flex steel build plate** — keep the PEI faces paired and record Z-offset and sheet swaps in `logs/`.

---

Use this folder as the shared memory: drop fresh offsets in `logs/`, capture tune-ups in `maintenance.md`, and stash firmware diffs or configs in `firmware-notes.md`.
