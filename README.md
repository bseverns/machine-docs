# Fabrication Machines — Living Docs

_A practical, evolving field manual for our digital fabrication lab. Built to help people make more, better, and safer._

- **Scope:** 3D printers (MakerBot Sketch, Sketch+, Method X; LulzBot Mini 3) and **CNC** (Genmitsu Cubiko).
- **Audience:** students, staff, and community members — from first-timers to battle-tested maintainers.
- **Status:** initial scaffold · 2025-09-19. Treat it like a handbook and a lab log that never sleeps.

## Why this repo exists

We keep tripping over the same questions: _Which profile do I use?_ _Where do I log the weird noise?_ Rather than repeat tribal knowledge, this repo captures the intent behind every job. Every doc should teach you how to succeed today **and** how to leave breadcrumbs for the next operator.

> _The lab is a chorus; every operator should leave it singing a little more in tune._

## Quick orientation

- **Machines** — Start with your rig’s folder and read the local `README.md`:
  - [MakerBot Sketch](machines/makerbot-sketch/)
  - [MakerBot Sketch+](machines/makerbot-sketch-plus/)
  - [MakerBot Method X](machines/makerbot-method-x/)
  - [LulzBot Mini 3](machines/lulzbot-mini-3/)
  - [Genmitsu Cubiko (CNC)](machines/genmitsu-cubiko/)
- **Shared docs** — Lab-wide standards, pipelines, and training live in [`/docs`](docs/). Highlights:
  - [Lab Safety](docs/lab-safety.md)
  - [3D Printing Pipeline](docs/printing-pipeline.md) & [CNC Pipeline](docs/cnc-pipeline.md)
  - [Onboarding](docs/onboarding.md) and [Training Pathways](docs/training-pathways.md)
- **Templates** — Drop-in scaffolds for SOPs, job sheets, and forms live in [`/templates`](templates/).
- **Personal rigs** — Ben’s side quests and retrofit notes are in [`/personal-machines`](personal-machines/).

## How to use these docs

1. Start in your **machine folder** → read the local [`README`](machines/) → follow its linked **Quick Start**, **Safety**, and **SOP**.
2. Grab the relevant **Operator Checklist**, templates, or slicer profiles directly from the folder paths linked in each doc.
3. After every run, update the maintenance or incident logs so the next human sees the full story, then hit the [Machine Logging Playbook](docs/logging-playbook.md) to stay synced on review cadence.
4. Found a better trick? **Submit a PR** with context, photos, or data. This repo only stays alive if we feed it.

## Contribution rhythm

- **Small fixes** — Quick typo, new photo, or parameter tweak? Open a PR with a tight diff and before/after notes.
- **New procedures** — Fork the [`SOP template`](templates/SOP-template.md) or other scaffolds and document the “why” alongside the “how”.
- **Incidents** — Log the event in the machine’s [`incident log`](machines/) within 24 hours and open an issue so we can swarm it.

## Firmware policy

All machines run **stock firmware** unless their machine page calls out a controlled deviation. Personal machines include explicit firmware notes and links; don’t freestyle without documenting the rollback path.

---

Need something that isn’t here yet? Open an issue, drop your context, and let’s hack the gap together.
