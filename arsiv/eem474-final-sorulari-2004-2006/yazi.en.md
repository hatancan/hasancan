---
baslik: EEM474 Power Electronics: 2004–2006 Final Exam Questions and Solutions
ozet: Rectifier, chopper, commutation and PWM solutions from the January 2004, September 2004, September 2005 and January 2006 exams.
---

The four final-exam solution presentations in the EEM474 folder are combined in this post: January 2004, September 2004, September 2005 and January 2006. Handwritten answers are evaluated as they appear in the source. PDF copies of the presentations are in the ZIP at the end of the post.

## January 2004

An inverter is defined as a circuit that produces an AC output with a specified amplitude and frequency from a DC source. For a chopper with a 200 V input, a 5 Ω–10 mH load, 500 Hz and a 75% duty ratio, Vavg = 150 V and Iavg = 30 A are given.

The lagging of current behind voltage in an inductive AC load, and the 90° phase difference in an ideal inductor, are sketched. In the three-phase controlled bridge question, the firing angle and a 15° commutation overlap are taken into account; the source solution gives a result of approximately 233.69 V.

In the two-thyristor circuit with capacitive commutation, the load resistance is 10 Ω for 50 V and 5 A. For a 30 µs turn-off time, the source gives Cmin ≈ 4.33 µF, a selected C = 5 µF, τ = 50 µs and fmax = 2 kHz. The final frequency is based on two commutations per period and an assumption of 5τ for each.

## September 2004

For the brightness of an AC incandescent lamp, a triac is given as the answer; for a DC chopper with high current/voltage and low frequency, a GTO is given. For the rectifier, it is stated that commutation overlap reduces the average output.

For a motor drawing 250 A from a 4 kV source, the rated power is calculated as 1000 kW. The GTO is driven at 10 kHz and an 85% duty ratio; an ideal-switch assumption is used.

For the half-wave controlled rectifier with resistive load at α = 30°, the general average expression is Vm(1 + cosα)/(2π). In the three-phase bridge with α = 60° and 15° overlap, the phase voltages, firing sequence and output voltage are sketched; the handwritten answer gives approximately 115 V.

For a 20 V → 5 V buck converter, D = 0.25. With 50 kHz switching, an LC resonance of 5 kHz (one tenth of the switching frequency) and a capacitance of 2500 µF, L = 1/[(2πfLC)²C] ≈ 0.405 µH is found.

*Note: This last L value follows only from the resonance condition given in the question. Since the continuous-current, saturation and load-current conditions are not given separately, it does not count as a complete practical design.*

## September 2005

A controlled DC supply is sketched for a DC motor operating in a single quadrant. The number of components in a fully controlled and an uncontrolled single-phase bridge is compared; both contain four rectifying elements. For PWM, the harmonics of bipolar/unipolar output are discussed.

In the single-thyristor AC controller with α = 45°, the RMS integral is set up over the conduction interval. In the three-phase bridge question, the 15° commutation overlap and firing sequence are treated again.

For an inverting buck–boost with an output magnitude of 50 V from a 24 V input, 50/24 = D/(1 − D) gives D ≈ 0.676. From the ideal power balance, |Io|/Ii = 24/50 = 0.48.

*Note: In the solution, some voltage ratios are written with positive magnitudes. The signed ratio of the inverting buck–boost is Vo/Vi = −D/(1 − D).*

## January 2006

The questions ask about the protection/limiting role of R and the zener in the gate circuit; the selection of an SCR for high voltage and current; and the buck–boost connection for an adjustable 0–50 V output from 24 V. In capacitive commutation, the initial capacitor voltage is assumed to be zero and the transient waveforms are examined.

In the fully controlled bridge supplied from a 24 V transformer output, a 45° firing angle and a 15° commutation interval are used. The approximate output result of the source solution is 13 V. If the duty ratios of the H-bridge legs are 70% and 40%, Vavg = Vd(0.7 − 0.4) = 0.3Vd is written.

*Note: The answer "less harmonics in unipolar" in the presentations should be read in the context of the given PWM conditions; it is not a statement of unconditional superiority at all frequencies and by all criteria. No day was added to the exams for which only the month is given in the source.*
