---
baslik: EEM474 Power Electronics: Power conversion, RMS and power factor
ozet: Types of power conversion in power electronics; average and effective values, harmonics, power factor, and energy storage relations.
---

The explanations and formulas from the English-language presentations in the EEM474 course folder have been transferred into text. The preparer's name is not clearly stated in the documents. Photographs and images taken from books were not transferred, so this post has no download file.

## Scope of power electronics

Electrical energy is converted into the form required by the load using semiconductor switches. The presentations list applications in industrial drives, power supplies, household appliances, transportation, and energy systems. The control circuit determines the conduction times of the switches in the power circuit.

| Conversion | Circuit |
| --- | --- |
| AC → DC | Rectifier |
| DC → DC | Chopper / DC converter |
| DC → AC | Inverter |
| AC → AC | AC voltage or frequency converter |

An ideal switch is assumed to carry zero current when off and to have zero voltage across it when on. In a real switch, the on-state voltage and the transition times cause losses. Efficiency is given by η = Pout / Pin.

## Average, effective value, and power

For a voltage with period T, the average value is defined as Vavg = (1/T) ∫₀ᵀ v(t) dt, and the effective value as Vrms = √[(1/T) ∫₀ᵀ v²(t) dt]. The same operations apply to current. The effective value is the DC value that produces the same heat in a resistor.

Instantaneous power is p(t) = v(t)i(t), and average active power is P = (1/T) ∫₀ᵀ v(t)i(t) dt. For a resistive load, P = Irms²R = Vrms²/R is used. Using the square of the average current does not give the same result for a ripple current.

For sinusoidal voltage and current, P = Vrms Irms cosφ; apparent power is S = Vrms Irms; and the power factor is PF = P/S. Reactive power is written as Q = Vrms Irms sinφ.

## Waveforms with harmonics

The Fourier expansion consists of a DC component and components at integer multiples of the fundamental frequency. For the effective values of mutually orthogonal harmonics, the relation Irms² = I₀² + Σ Iₙ,rms² is used. If the voltage is sinusoidal and the current is distorted, only the fundamental current component contributes to the average active power:

P = Vrms I₁,rms cosφ₁

PF = (I₁,rms / Irms) cosφ₁

THDᵢ = √[Σₙ≥₂ Iₙ,rms²] / I₁,rms

Thus, correcting the phase shift alone does not eliminate the power factor loss caused by harmonics. In the calculations in the presentation, the conduction intervals of the waveform are set up first, followed by the average and RMS integrals.

## Inductor and capacitor

For an inductor, vL = L di/dt and the stored energy is WL = ½Li²; for a capacitor, iC = C dv/dt and the energy is WC = ½Cv². In periodic steady state, the stored energy returns to its initial value at the end of a period. Therefore, the average voltage of an ideal inductor and the average current of an ideal capacitor are zero.

*Note: Differently arranged copies of the presentations were merged into a single post. The assumptions of ideal switches and lossless elements do not mean that a real circuit is one hundred percent efficient.*
