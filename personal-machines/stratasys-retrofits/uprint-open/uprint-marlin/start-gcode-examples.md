# Start G-code Examples (Chamber preheat)

Preheat and wait for chamber to reach temp, then start the job:

```
M141 S60        ; set chamber target to 60C
M191 S60        ; wait for chamber to reach 60C
M104 S240       ; set hotend temp
M140 S100       ; set bed temp
M190 S100       ; wait for bed
M109 S240       ; wait for hotend
; ... purge, wipe, etc.
```

Adjust temps to material; use `M191 Rxx` to wait even if **cooling**.
