---
baslik: EEM474 Power Electronics: Buck, boost, buck–boost and PWM control
ozet: Operating regions of DC choppers, conversion ratios in continuous current, ripple, and voltage/current mode control.
---

The explanations and formulas from the English-language presentations in the EEM474 course folder have been transferred into text. The author's name is not stated explicitly in the documents. Photographs and images taken from books were not transferred, so this post has no download file.

## Chopper and duty ratio

D = ton/T = ton fs is the fraction of a period during which the switch remains on. For 0–Vs pulses applied to a resistive load, Vavg = DVs and Vrms = Vs√D. Varying the pulse width at a constant frequency is called PWM. The other method is to keep the on-time or off-time constant and vary the frequency.

In the presentation's example with 48 V, 24 Ω and 250 Hz, T = 4 ms. For ton = 1 ms, D = 0.25, Iavg = 0.5 A, Irms = 1 A and P = 24 W. For ton = 3 ms, D = 0.75, Iavg = 1.5 A, Irms ≈ 1.732 A and P = 72 W.

*Note: In the source, the second power result is given as approximately 71.8 W by rounding the rms current to 1.73 A; computed without rounding, it is 72 W.*

## Steady-state conditions

The change in inductor current over one period is zero. The average inductor voltage is zero, and the average capacitor current is zero. In an ideal circuit, the input and output powers are equal. Continuous conduction is the mode of operation in which the inductor current stays above zero throughout the period.

## Buck

When the switch is on, vL = Vs − Vo; when it is off, vL = −Vo through the freewheeling diode. Volt-second balance gives Vo = DVs. The current slopes are (Vs − Vo)/L and −Vo/L, respectively.

ΔiL = Vo(1 − D)/(Lfs)

ΔVo/Vo = (1 − D)/(8LCfs²)

The last relation is the result given under the assumptions of an ideal capacitor and small ripple. The capacitor's ESR effect is not included in this simple expression.

## Boost

When the switch is closed, the inductor stores energy from the source; when it opens, the source and the inductor together supply the load. For continuous current and ideal components, Vo = Vs/(1 − D). An output larger than the input is obtained. The voltage stress on the switch and the diode is related to the output voltage.

## Inverting buck–boost and Ćuk

In the buck–boost converter, energy is stored in the inductor while the switch is on and transferred to the output while it is off. The minus sign in the relation Vo/Vs = −D/(1 − D) indicates the polarity reversal. For D < 0.5 the output magnitude is smaller than the input; for D > 0.5 it is larger. The presentation also shows the Ćuk converter with the same ideal voltage ratio; it uses a capacitor for energy transfer.

*Note: In the buck–boost comparisons in the source, Vo > Vs and Vo < Vs are written. Because of the reversed-polarity output, these comparisons should be read as referring to the magnitudes of the voltages. The phrase "output ... connected to load" in the same section is inconsistent; what is described is that there is no direct energy transfer path between the input and the output.*

## Operating regions and full bridge

In the first quadrant, the chopper supplies the load. In the second quadrant, the current direction reverses and energy can be returned to the source. Two-quadrant arrangements allow the voltage or current to be in one direction and the other in both directions. A four-quadrant bridge can reverse the direction of both quantities. With bipolar drive, zero average output occurs at D = 0.5.

## Closed loop

In voltage mode, a sample taken from the output is compared with the reference; the error voltage is compared with a sawtooth carrier to generate the duty ratio. In current mode, the error signal sets the peak limit of the switch current. The aim is to regulate the output when the input voltage and load current vary.

The simplified PWM model in the presentation: D = Vcontrol/Vst,m; Vcontrol = A(Vref − Vsam); Vsam = kDVs. From this, D = Vref/(Vst,m/A + kVs) is obtained. This static relation does not replace a stability analysis of the closed loop.
