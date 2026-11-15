---
baslik: EEM474 Power Electronics: ZVS Buck Converter Project Report
ozet: A zero-voltage-switching buck converter, its switching intervals, and PSIM waveforms.
---

This student report, dated 31 May 2013, examines the step-down DC/DC converter and zero-voltage switching. The cover page and report PDFs, with personal information removed, can be downloaded at the end of the post.

## Switching DC/DC converter

The report describes PWM control, fast transient response, and an adjustable DC output. The basic circuit elements are a controlled power switch, a diode, and an inductor. Under the continuous-conduction assumption, the inductor current never drops to zero; energy transfer continues during the conduction intervals of both the switch and the diode.

## The two intervals of the buck converter

While the switch is on, vL = Vs − Vo and diL/dt = (Vs − Vo)/L. Since the duration is DT, the change in current is ΔiL = (Vs − Vo)DT/L.

When the switch is off, the diode takes over the current: vL = −Vo, diL/dt = −Vo/L. The duration is (1 − D)T and ΔiL = −Vo(1 − D)T/L.

In steady state, the net change in current over one period is zero. From these equations, Vo = DVs follows for ideal continuous conduction.

## The ZVS approach

The source describes limiting the rate of voltage rise at turn-off by placing a small capacitor in parallel with the switch. It focuses on transferring the switching energy to the capacitor and recovering it in suitable cells. It emphasizes that zero-current or zero-voltage conditions in resonant converters reduce switching losses.

*Note: The report defines ZVS only in terms of the turn-off transition. Zero-voltage switching is a more general concept; turning on at zero voltage also falls within its scope. Because of resonance and parasitic element losses, not all losses are zero in a real circuit.*

## PSIM example

The "ZVS Resonant-Switch Converter" example included with PSIM 6.0 is used. The report contains three groups of results: inductor voltage, switch Q current, and the voltage across the switch/capacitor terminals. The waveforms show the distinct structure of the conduction interval and the resonant transition; the source does not provide a separate numerical efficiency or loss table.
