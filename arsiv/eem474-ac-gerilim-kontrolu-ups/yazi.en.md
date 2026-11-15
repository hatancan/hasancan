---
baslik: EEM474 Power Electronics: AC Voltage Control and Uninterruptible Power Supplies
ozet: Integral-cycle and phase-angle control, cycloconverters, AC–DC–AC conversion, and UPS operating blocks.
---

The explanations and formulas from the English-language presentations in the EEM474 course folder were transferred into text. The preparer's name is not stated explicitly in the documents. Photographs and images taken from books were not transferred, so this post has no download file.

## AC–AC Conversion

An AC voltage controller changes the rms value of the output. Frequency conversion can be carried out directly with a cycloconverter or indirectly through a rectifier, a DC link, and an inverter. In the presentation, the main applications are heating, lighting, and motor control.

## Integral-Cycle Control

For n cycles of conduction and m cycles of blocking, k = n/(n + m) is defined. For a resistive load, Vo,rms = Vs,rms√k, Po = kVs,rms²/R, and the input power factor is √k. The switches are kept on for whole groups of cycles.

For a 120 V supply with n = 25 and m = 75, k = 0.25, the output is 60 Vrms, and the power factor is 0.5. Loads with long thermal time constants are given as examples of this mode of operation.

## Phase-Angle Control

Two antiparallel thyristors, or a suitable triac, are triggered after waiting until angle α in each half cycle. For a resistive load, conduction ends at the end of the half cycle. The rms output value is:

Vo,rms = Vs,rms √[(π − α + sin(2α)/2)/π]

For R = 10 Ω, Vs = 120 Vrms, f = 60 Hz, and α = π/2, Vo,rms ≈ 84.85 V; the power factor is approximately 0.707. For an inductive load, since the current zero does not coincide with the voltage zero, the conduction and extinction angles are calculated separately.

## Cycloconverter and Indirect Conversion

In the direct method, positive and negative rectifier groups form a low-frequency output from segments of the source voltage. In the indirect method, a DC link voltage is produced first, and then an inverter is driven at the desired frequency. The filter and energy storage elements of the link connect the two conversion stages.

## UPS Blocks

An uninterruptible power supply contains a rectifier/charger circuit, a battery, an inverter, and a transfer or bypass arrangement. The energy path under normal mains conditions and during a mains outage are shown separately. In the online configuration, the load is continuously supplied through the inverter; in the standby configuration, the system switches to the backup energy path during an outage.

The presentation describes the block relationships of AC generation from the battery, a transformer output, and PWM control. Circuit pages taken from the book and product photographs were not included in this text.

*Note: The expression "power factor = cosφ" is not sufficient by itself for phase-controlled, non-sinusoidal current. The PF calculations here are based on the ratio of active power to apparent power.*
