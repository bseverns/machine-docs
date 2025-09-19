# config.g Examples — Chamber + K‑type (illustrative)

> Adapt device numbers and pins to your exact Duet model and daughterboards.

```
; ----- SENSORS -----
; Example: define thermocouple sensors (numbers illustrative)
M308 S0 P"spi.cs0" Y"thermocouple" T"k" A"Hotend"
M308 S1 P"spi.cs1" Y"thermocouple" T"k" A"Bed"
M308 S2 P"spi.cs2" Y"thermocouple" T"k" A"Chamber"

; ----- HEATERS -----
; Map chamber heater to OUT1 (via SSR), set sensor
M950 H2 C"out1" T2                          ; H2 = chamber
M141 H2                                      ; declare chamber heater
M143 H2 S90                                  ; chamber max 90C (example)

; Hotend / bed (examples)
M950 H1 C"e0heat" T0
M950 H0 C"bedheat" T1
M143 H1 S285                                 ; hotend max
M143 H0 S120                                 ; bed max

; ----- FANS -----
M950 F2 C"out4" Q25                           ; chamber fan
M106 P2 S0 H2 T50:70                          ; auto chamber fan 50–70C

; ----- START G-CODE USAGE -----
; M141 S60  ; set chamber to 60C
; M191 S60  ; wait for chamber 60C
```

These are patterns—use your board’s pin names and actual CS lines for the TC boards.
