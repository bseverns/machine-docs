# Parts and Spares - Genmitsu Cubiko

**Purpose:** track the cutters, machine parts, and consumables that keep the CNC router serviceable.  
**Last inventory check:** TBD  
**Doc audit updated:** 2026-04-04  
**Shelf / bin location:** TBD  
**Primary buyer / maintainer:** Fabrication lab staff  

## Procurement rules

- Record exact cutter geometry, collet sizes, and OEM part numbers before reordering.
- Distinguish consumable tooling from machine-service parts.
- Mark unknown numbers as `TBD` instead of guessing.
- Link successful installs or tool validations from logs and job sheets once available.

## Critical spares

| Subsystem | Part | Manufacturer part number | Preferred vendor / SKU | Qty on hand | Reorder point | Shelf location | Approved substitute | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Toolholding | ER11 collet set, 1/8 in and 1/4 in | TBD | SainSmart or approved precision supplier | TBD | 1 set | TBD | Approved only if runout is verified | Replace if wear, crash damage, or poor runout appears. |
| Spindle | 300 W spindle service assembly | TBD | SainSmart direct or approved reseller | TBD | 1 | TBD | None approved | Escalate before ordering; verify fault through troubleshooting. |
| Limits / motion | Limit switch assemblies | TBD | TBD | TBD | 1 set | TBD | None approved | Capture exact switch type during physical audit. |
| Workholding | Spare spoilboard blank / pinned board | TBD | Local fabrication or OEM-compatible source | TBD | 1 | TBD | Approved local remake if dimensions are verified | Keep one ready to reduce downtime after surfacing or damage. |
| Motion | Belts / lead hardware service kit | TBD | TBD | TBD | 1 set | TBD | None approved | Record exact axis hardware specs during physical audit. |

## Consumables

| Item | Spec | Preferred source | Qty on hand | Reorder point | Notes |
| --- | --- | --- | --- | --- | --- |
| Endmills | Approved 1/8 in and 1/4 in cutters by material | Approved tooling vendors | TBD | TBD | Keep the tool database synced with validated cutters. |
| Stock blanks | Approved wood, acrylic, wax, FR-1, limited aluminum | Approved lab vendors | TBD | TBD | Match to [`materials.md`](./materials.md) and job-sheet policy. |
| Cleanup supplies | Vacuum / chip brush / wipes | Lab stock | TBD | TBD | Keep cleanup tools separate from measuring tools. |

## Parts we do not keep stocked

| Part | Why not stocked | Typical lead time | Trigger to order | Notes |
| --- | --- | --- | --- | --- |
| Main controller board | Higher cost, lower routine failure rate | TBD | Persistent GRBL faults confirmed beyond wiring and sender issues | Capture exact board revision during physical audit. |
| Enclosure panels | Bulky and low-use | TBD | Damage affecting chip containment or safe use | Review incident history before ordering. |
| Full axis assemblies | Rarely needed as stocked items | TBD | Crash damage or backlash beyond serviceable wear parts | Escalate before ordering. |

## Sources

- [Genmitsu Cubiko user manual](https://www.sainsmart.com/pages/download/genmitsu-cubiko-user-guide) - accessed 2026-04-04
- [Genmitsu support downloads](https://www.sainsmart.com/pages/genmitsu-cubiko-download) - accessed 2026-04-04
