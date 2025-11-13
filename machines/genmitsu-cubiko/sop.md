# SOP — Genmitsu Cubiko (CNC)

**Purpose:** Cut wood, plastics, and soft metals safely on the enclosed Genmitsu Cubiko desktop CNC.
**Skill level:** Intermediate (comfortable with CAM post-processing and workholding).
**Last verified:** 2025-02-14 — Omar Velez & Casey Lin (operator debrief at shift change)

> Operator quip (Casey, 2025-02-14): “If the spoilboard feels fuzzy, surface it before the job. Cubiko hates fuzzy.”

## Preflight (before every job)
- [ ] PPE: safety glasses, hearing protection, and dust mask when machining MDF.
- [ ] Clear 1 m perimeter; confirm enclosure doors latch and dust shoe bristles intact.
- [ ] Inspect tool: confirm collet clean, bit seated ≥15 mm, and torque to 6 N·m with wrench.
- [ ] Verify spoilboard flatness; surface if >0.3 mm ridge felt across 200 mm straightedge per **Cubiko User Manual §3.2**.
- [ ] Mount stock using hybrid T-slot + cam clamps; tug-test corners.
- [ ] Check probe puck and grounding clip; position on clean bare metal area.
- [ ] Power controller and connect USB to host PC; launch Candle Cubiko Edition.
- [ ] Load G-code; verify units (mm), origin (front-left), tool number, and feed overrides from post.
- [ ] Run “Dry Run” (no spindle) with door closed to confirm clearance.
- [ ] Confirm E-stop reachable; test door interlock weekly (record in maintenance log).

## Operation
1. Home all axes via Candle (**$H**) and confirm machine coordinates reset.
2. Jog to front-left top of stock; zero X/Y (Set Work Zero) and use probe puck for Z (Probe Z).
3. Remove probe, attach dust shoe, and verify hose connected to shop-vac (auto switch on).
4. Start spindle via software; wait for RPM to stabilize (per tool chart) before starting program.
5. Hit **Send** to stream G-code; watch first toolpath pass for chatter or missed steps.
6. Adjust feed override ±10% if chips not clearing; pause immediately if tool load spikes.
7. For tool changes, pause program, power spindle off, change bit, re-probe Z, and resume from last line.
8. Document any unexpected vibration, lost steps, or hold-down adjustments in log.

## Postflight
- [ ] Stop spindle and allow to coast to zero before opening enclosure.
- [ ] Remove stock carefully; deburr edges away from machine.
- [ ] Vacuum chips from spoilboard, linear rails, and dust shoe.
- [ ] Inspect tool—retire if dull or chipped; return to labeled rack.
- [ ] Power down controller, disconnect USB, and close enclosure doors.
- [ ] Update `/machines/genmitsu-cubiko/logs/maintenance-log.csv` with tool wear, surfacing notes, and interlock tests.

## Photos / Diagrams
```mermaid
flowchart LR
    Prep[PPE + clear zone] --> Clamp[Mount & clamp stock]
    Clamp --> Probe[Probe XYZ]
    Probe --> DryRun[Run dry simulation]
    DryRun --> Cut[Start spindle & cut]
    Cut --> Clean[Vacuum & log]
```

**Reference manuals:**
- SainSmart, *Genmitsu Cubiko User Manual* (2024), https://docs.sainsmart.com/article/cubiko-user-manual.
- SainSmart, *Candle Cubiko Edition Guide* (2023), https://docs.sainsmart.com/article/candle-cubiko-guide.
