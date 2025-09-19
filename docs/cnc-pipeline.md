# CNC Pipeline

```mermaid
flowchart LR
  A[Design CAD] --> B[CAM: toolpaths]
  B --> C[Post G-code]
  C --> D[Workholding + Zeroing]
  D --> E[Dry Run (air cut)]
  E --> F[Cut with dust collection]
  F --> G[Deburr + Log]
```
