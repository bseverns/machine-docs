# Training Pathways

Every pathway ramps your autonomy without ditching safety or documentation. Treat each level as a contract: you agree to carry specific skills, and we agree to sign off only when you can prove it on the machine.

## Level 1 — Operator

### Required skills
- Recite core lab safety and PPE rules without peeking.
- Launch pre-approved jobs using existing slicer/CAM profiles.
- Run the operator checklist for start-up, mid-print checks, and shutdown.
- Log every run and hiccup in the machine's maintenance/incident docs.

### Sign-off actions
- Complete the machine-specific operator checklist with a mentor shadowing.
- Pass the short quiz in each machine's `training` folder.
- Capture your mentor's name + date inside the checklist and file it back in the repo or shared drive.
- Machine checklists live here:
  - [Genmitsu Cubiko Operator Checklist](../machines/genmitsu-cubiko/training/operator-checklist.md)
  - [LulzBot Mini 3 Operator Checklist](../machines/lulzbot-mini-3/training/operator-checklist.md)
  - [MakerBot Method X Operator Checklist](../machines/makerbot-method-x/training/operator-checklist.md)
  - [MakerBot Sketch Operator Checklist](../machines/makerbot-sketch/training/operator-checklist.md)
  - [MakerBot Sketch+ Operator Checklist](../machines/makerbot-sketch-plus/training/operator-checklist.md)

### Suggested learning resources
- [Lab Safety](./lab-safety.md) and the [Onboarding walkthrough](./onboarding.md).
- Each machine's `README.md` quick start + linked SOP.
- The relevant pipeline primer: [3D Printing Pipeline](./printing-pipeline.md) or [CNC Pipeline](./cnc-pipeline.md).
- Shadow an experienced operator; narrate your steps to prove you understand the “why,” not just the button order.

### Mentors & escalation
- **Primary contact:** the machine steward listed at the top of that machine's `README.md`.
- **Backup:** drop notes in the shared maintenance log and tag the steward in your commit/PR.
- **Escalation:** open an issue in this repo and assign it to the shop manager (currently the repo maintainer). If it is a safety hold, pause the machine and page the lab manager immediately.

## Level 2 — Setup Wrangler

### Required skills
- Swap materials, tooling, beds, or fixtures without wrecking calibration.
- Edit slicer/CAM profiles for known-good variants (e.g., layer height swaps, nozzle swaps) and document rationale.
- Run preventative tasks: nozzle purges, bed tramming, enclosure checks, light maintenance.
- Diagnose common print/CNC failures and recover without additional mentor intervention.

### Sign-off actions
- Extend the machine's operator checklist with setup tasks; if the section does not exist, clone [the checklist template](../templates/checklist-template.md) into the machine's `training` folder and document the changeover flow.
- Demonstrate a full changeover in front of a mentor, including pre/post calibration checks.
- Update the machine's maintenance log with the changeover data and mentor signature.
- Reference and, when necessary, update these same checklists:
  - [Genmitsu Cubiko Operator Checklist](../machines/genmitsu-cubiko/training/operator-checklist.md) — add the CNC-specific setup block.
  - [LulzBot Mini 3 Operator Checklist](../machines/lulzbot-mini-3/training/operator-checklist.md) — fill in material/nozzle swap steps.
  - [MakerBot Method X Operator Checklist](../machines/makerbot-method-x/training/operator-checklist.md) — annotate chamber prep + purge sequences.
  - [MakerBot Sketch Operator Checklist](../machines/makerbot-sketch/training/operator-checklist.md) — include classroom-ready changeover notes.
  - [MakerBot Sketch+ Operator Checklist](../machines/makerbot-sketch-plus/training/operator-checklist.md) — sync with Sketch setup tasks.

### Suggested learning resources
- Machine-specific SOPs and maintenance sections in each `README.md`.
- Manufacturer guides linked from [`machines/README.md`](../machines/README.md) for official calibration steps.
- Pair-program with a maintainer while they perform a tune-up; capture the procedure in the checklist template for reuse.
- Post-mortem past incident reports to learn failure patterns before you have to fix them live.

### Mentors & escalation
- **Primary contact:** the machine steward or the Level 3 maintainer who owns that machine's calibration profile.
- **Backup:** log the setup session in the maintenance log and tag both the steward and the repo maintainer in your PR.
- **Escalation:** if tooling or materials are missing, open an issue and flag it “setup blocker”; for safety-critical gaps, halt usage and page the lab manager.

## Level 3 — Maintainer

### Required skills
- Perform deep maintenance: belt tension, axis alignment, lubrication, sensor checks, firmware validation.
- Author and validate new machine profiles or SOP updates, including risk assessments.
- Lead root-cause analysis for incidents and coordinate follow-up repairs.
- Coach Level 1–2 operators, providing feedback and updating documentation based on what you observe.

### Sign-off actions
- Build or update a maintainer-focused checklist (start from [the checklist template](../templates/checklist-template.md)) and commit it alongside calibration logs.
- Execute a full preventative maintenance cycle with another maintainer auditing your work.
- Deliver an after-action report (short write-up + log entry) that details findings, adjustments, and any new documentation produced.
- Maintain references inside the same machine folders so the audit trail stays tight:
  - [Genmitsu Cubiko Operator Checklist](../machines/genmitsu-cubiko/training/operator-checklist.md) — add maintainer tasks until a dedicated file exists.
  - [LulzBot Mini 3 Operator Checklist](../machines/lulzbot-mini-3/training/operator-checklist.md) — include firmware/axis checks.
  - [MakerBot Method X Operator Checklist](../machines/makerbot-method-x/training/operator-checklist.md) — document chamber calibration + filter swaps.
  - [MakerBot Sketch Operator Checklist](../machines/makerbot-sketch/training/operator-checklist.md) — track dual-head maintenance routines.
  - [MakerBot Sketch+ Operator Checklist](../machines/makerbot-sketch-plus/training/operator-checklist.md) — mirror the Sketch maintainer notes until a dedicated sheet is spun up.

### Suggested learning resources
- Deep-dive manufacturer maintenance manuals and support threads linked per machine.
- [Troubleshooting template](../templates/troubleshooting-template.md) for structured RCA notes.
- Past calibration data and maintenance logs (living inside each machine folder).
- Peer review sessions: trade maintainer checklists with another machine steward and critique for clarity.

### Mentors & escalation
- **Primary contact:** shop manager / lead maintainer (repo maintainer until we split the role).
- **Backup:** schedule quarterly audits with another Level 3 maintainer; store findings in the machine folder.
- **Escalation:** if a machine is at risk, tag the lab manager and freeze the machine in the issue tracker. Document every intervention via PR to keep the accountability chain unbroken.

---

When in doubt, document louder than you think is necessary. The future operator should be able to reproduce your work using only these breadcrumbs — that is the punk promise.
