---
baslik: EEM474 Power Electronics: August 17, 2011 Summer Final
ozet: Question and answer copies of the summer final; harmonic power, converter blocks, bridge drive, SPWM and RMS calculation.
---

The question and answer copies of the EEM474 summer final dated August 17, 2011. Both PDFs of the twelve-question exam can be downloaded from the ZIP at the end of the post. The answer copy also includes questions that were left blank.

## Active Power from Harmonics

The first question gives v(t) = 1.2 cosωt + 0.33 cos3ωt + 0.2 cos5ωt; i(t) = 0.6 cos(ωt + 30°) + 0.1 cos(5ωt + 45°) + 0.1 cos(7ωt + 60°). Only the common frequencies contribute:

P = (1.2 × 0.6/2) cos30° + (0.2 × 0.1/2) cos45° ≈ 0.319 W.

The source rounds the result to 0.32 W. Since the third voltage harmonic and the seventh current harmonic have no counterpart component, their contribution to the average power is zero.

## Converter Chains

To obtain AC with adjustable amplitude and frequency from the mains, the answers are: controlled rectifier + square-wave inverter; uncontrolled rectifier + buck + square-wave inverter; uncontrolled rectifier + SPWM inverter. In the first two structures the amplitude is adjusted in the DC stage, and in the third by the inverter's ma ratio. The output frequency is determined by the inverter's reference.

## Switch, Rectifier and Regulator Questions

The second question asks for the voltage waveform across the switch. The fourth question asks under which condition the efficiency of the series and shunt linear regulators is greatest. In the fifth question, the resistive load voltages of three different AC/DC circuits are plotted for the firing angles α and π + α. The sixth question is a snubber circuit that protects the thyristor against di/dt stress at turn-on and dv/dt stress at turn-off.

## Bridge and Buck–Boost

In the seventh question, the VA, VB and VAB waveforms are obtained from the given gate pulses. In the tenth question, taking the current direction of the inductive load into account, the switches/diodes conducting in each interval of the output waveform are determined. The eighth question is written in the source as "ΔL" for the buck–boost.

*Note: The ΔL expression in the eighth question is ambiguous; the source notation was kept so as not to confuse it with the ΔiL current ripple used in most converter derivations.*

## RMS and SPWM

In the ninth question, if the width of the ±Vs pulses in each half period is γ, then Vrms = Vs√(γ/π). The eleventh question asks for an op-amp arrangement that generates gate pulses from a sinusoidal reference and a triangular carrier. For ma = 0.4, fsin = 75 Hz, mf = 21 and Vdc = 100 V, the answer gives a fundamental voltage peak of 40 V at a frequency of 75 Hz; the carrier frequency is 1575 Hz.

The last question asks for the RMS expression of AC phase control and the special case α = π/2. For an ideal resistive load the result is Vs,rms/√2.

*Note: 40 V is the peak value of the fundamental component used in the answer; the RMS value of the same sinusoid is 40/√2 V. The cropping at the top of the question copy has been completed using the answer copy.*
