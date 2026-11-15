---
baslik: EEM474 Power Electronics: Peak Current Mode Controlled Buck Report
ozet: A buck converter with slope compensation in PSIM 6: control loop, inductor current, output voltage and ramp signals.
---

This is a project report on a **peak current mode controlled buck converter**, prepared by a friend for the EEM474 Power Electronics course at Başkent University. Personal information has been removed. The document does not state a date; the cleaned-up PDF can be downloaded at the end of the post.

## Project topic

Assignment topic 11: "Peak current mode control (Buck converter) research and simulation (PSIM 6)." The report contains a peak current control circuit with slope compensation and the simulation results.

## Description of the control

Peak current mode is one of the control methods used in high-performance DC/DC converters. The report's explanation emphasizes that a fast inner current loop tracks the reference and the outer loop controls the output voltage. It is noted that bringing the inductor dynamics into the inner current loop simplifies the voltage loop.

The circuit diagram shows the buck power stage, output voltage feedback, comparator, clock, latch, and the "slope compensation" signal.

## Simulation outputs

- **I(L)–time:** The initial transient of the inductor current and its switching ripple.
- **V_o–time:** The output voltage rising and approaching steady state.
- **V_m–time:** The course of the control signal over time.
- **V_slope–time:** The periodic ramp waveform of the slope compensation.

*Note: The report's explanation of "50% Duty cycle" is incomplete in wording and meaning; it should not be interpreted as a definitive stability condition. The circuit's source schematic and numerical output file are covered separately in the archived post on converter simulations.*
