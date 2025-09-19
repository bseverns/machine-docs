# 3D Printing Pipeline

```mermaid
flowchart LR
  A[Idea/Model] --> B[Prepare in CAD]
  B --> C[Export STL/3MF]
  C --> D[Slicer Profile + Preview]
  D --> E[Machine Preflight]
  E --> F[Print]
  F --> G[Post-process + Log]
```
