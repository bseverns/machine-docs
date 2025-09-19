# Wiring Map — uPrint on Duet

| Function | Stock harness | Duet port | Notes |
|---|---|---|---|
| X motor |  |  |  |
| Y motor |  |  |  |
| Z motor |  |  |  |
| Extruder (stepper or servo+driver) |  |  | If servo, front with step/dir driver |
| X endstop |  |  |  |
| Y endstop |  |  |  |
| Z endstop/probe |  |  |  |
| Hotend heater |  | HE0 |  |
| Bed heater |  | BED / OUT0 | via SSR if required |
| Chamber heater |  | OUT1/2/... | SSR control |
| Hotend K‑type |  | TC board ch# | Daughterboard |
| Bed K‑type |  | TC board ch# | Daughterboard |
| Chamber K‑type |  | TC board ch# | Daughterboard |
| Fans (tool/part/chamber) |  | OUTx | PWM capable |
