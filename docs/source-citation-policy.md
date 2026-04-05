# Source Citation Policy

_If a fact matters to safety, maintenance, procurement, or training, it needs a trail._

## Purpose

This repo mixes manufacturer documentation, local measurements, and shop knowledge. Future maintainers need to know which statements came from the OEM, which came from our own testing, and which are still provisional.

Use this policy when you add or edit machine facts, maintenance procedures, firmware notes, sourcing info, or troubleshooting guidance.

## What must be cited

- Build volume, firmware version, controller type, and approved materials
- Replacement parts, consumables, and vendor recommendations
- Safety requirements, maintenance intervals, and calibration procedures
- Any change from stock hardware, stock firmware, or stock workflow
- Troubleshooting claims that are not obvious from direct observation

If you cannot cite it, label it as an observation, hypothesis, or TODO instead of presenting it as fact.

## Source priority

Use sources in this order whenever possible:

1. Manufacturer manuals, service guides, firmware release notes, BOMs, and support articles
2. Vendor documentation for installed aftermarket components
3. Recognized standards or software project documentation
4. Internal measurements, photos, maintenance logs, and calibration results
5. Community threads, forum posts, and videos

Community sources are useful for leads, not final authority. Validate them before they become shop policy.

## Citation format

For important claims, include enough metadata that a future maintainer can relocate the source even if the link changes.

- `Title`
- `URL`
- `Document version / revision` if available
- `Date accessed`
- `Applies to` machine, revision, or subsystem

Short inline citations are fine in prose. For pages with many references, add a "Sources" or "Reference set" section near the bottom.

## Machine doc rules

- Every machine `README.md` should include a first-party reference section.
- `machine-card.md` should identify when the installed state was last physically verified.
- `parts-and-spares.md` should distinguish exact part numbers from "needs confirmation" placeholders.
- `local-deviations.md` should cite both the stock baseline and the installed replacement when possible.
- `troubleshooting.md` should separate OEM guidance from internal heuristics.

## Link-rot strategy

- Prefer direct manual, support, firmware, and download URLs over generic marketing pages.
- Record document filenames and revisions for critical manuals and firmware bundles.
- If licensing allows, keep a local copy or checksum of must-have reference material.
- If a source disappears, do not silently replace it with memory. Mark the doc as needing re-verification.

## Local evidence

Our own evidence is a source too. Use it well.

- Link to maintenance rows, incident rows, calibration tables, photos, and issue threads.
- When a claim comes from internal testing, say so directly.
- When a process has only been validated on one machine, name that machine.

## Language rules

- Use `verified` when the fact was checked against a cited source or physical inspection.
- Use `observed` when the statement comes from a real run, photo, or measurement in our shop.
- Use `suspected` or `hypothesis` when the cause is not yet proven.
- Use `TBD` when a field needs confirmation.

Write so an intern can tell the difference in one pass.
