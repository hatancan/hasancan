---
baslik: EEM214 Electronics I: Folder Supplement, EEM311 Op-Amp and Instrumentation Amplifier Lab Handout
ozet: Inverting amplifier, integrator and differentiator with the 741; gain, CMRR, frequency response, slew rate, offset and noise measurements on 741 and AD620 instrumentation amplifiers.
---

This post is the handout for **Başkent University EEM311 Electronics II, Experiment 9 – Operational Amplifiers**, kept in the EEM214 Electronics I folder. The PDF was created on 9 October 2012; it does not name its author. The first part covers the inverting amplifier, integrator and differentiator; the second part covers op-amp characteristics and instrumentation amplifiers. The English instructions have been transcribed into the text; the 12-page PDF, with its metadata cleaned, is available for download at the end of the post.

## Inverting amplifier, integrator and differentiator

**Objectives:** Demonstrate an inverting amplifier and the use of operational amplifiers for integration and differentiation.

An ideal op-amp has infinite open-loop gain and input resistance. Negative feedback sets the closed-loop gain. For an inverting amplifier with input resistance R₁ and feedback resistance R_F:

A_v = −R_F/R₁.

An integrator uses a feedback capacitor. A resistor in parallel with the capacitor limits DC gain and prevents a small DC input or offset from driving the output to a supply limit. The handout writes:

V_out = −[1/(R_in C_F)]∫V_in dt.

For a sine input A sin(ωt), it prints −A cos(ωt)/(ωR_in C_F).

*Note: The sign of the last equation is wrong in the source. If the integral is taken together with the leading minus sign, the result, apart from the constant term, is +A cos(ωt)/(ωR_in C_F).*

Integration requires frequencies well above **f_B = 1/(2πR_F C_F)**. A differentiator uses an input capacitor:

V_out = −R_F C_in·dV_in/dt = −ωR_F C_in A cos(ωt).

A series input resistor limits high-frequency differentiation at **f_B = 1/(2πR_in C_in)**. A parallel feedback capacitor provides another high-frequency limit and reduces the tendency to oscillate. A square-wave input produces approximately a triangle at an integrator and edge pulses at a differentiator.

## Procedure: Inverting amplifier

Use a 741 with ±15 V supplies and **R₁ = 1 kΩ**. If oscillation occurs, the handout suggests adding 0.1 µF supply bypass capacitors from each supply pin to ground.

1. For R_F = 4.7 kΩ, apply a **100 mV peak, 1 kHz sine**. Observe and sketch input and output; record their phase difference.
1. Replace the generator with **1 V DC** and set R_F = 10 kΩ. Record the output voltage and polarity to verify DC amplification.
1. Set R_F = 1 MΩ, sketch the input and output and comment on the result.

![Inverting amplifier with a 741, 1 kilohm input resistor and feedback resistor](opamp-3.jpg "Inverting amplifier connection")

## Procedure: Integration and differentiation

### Integrator

Use R_in = **47 kΩ**, R_F = **470 kΩ**, C_F = **0.22 µF** and ±15 V supplies.

1. Apply a **±5 V peak, 100 Hz square wave**. Draw both signals and label amplitudes and times.
1. Calculate the break frequency.
1. Change the frequency first to **20 Hz**, then **1 kHz**; describe what happens.

![741 integrator, 47 kilohm input and 470 kilohm feedback resistor in parallel with 0.22 microfarad](opamp-4.jpg "Integrator experiment")

### Differentiator

Use R_in = **470 Ω**, C_in = **0.22 µF**, R_F = **10 kΩ**, C_F = **1 nF** and ±15 V supplies.

1. Apply a **±1 V peak, 200 Hz square wave** and sketch input/output with their values.
1. Calculate the break frequency; change to **500 Hz**, then “100” as written in the source.
1. Discuss whether the integrator and differentiator actually perform the intended operations. State the input/output phase difference of the inverting amplifier.

![741 differentiator and high-frequency limiting resistor-capacitors](opamp-5.jpg "Differentiator experiment")

*Note: The unit of the last frequency is missing in the handout; the context suggests Hz. With the given components, the integrator's break frequency is about 1.54 Hz, the differentiator's input RC limit is 1.54 kHz, and its feedback RC limit is 15.9 kHz.*

### Equipment and reporting

741 or equivalent, ±15 V and variable DC supplies, signal generator, dual-trace oscilloscope; resistors 1 MΩ, 4.7 kΩ, 10 kΩ, 1 kΩ, 47 kΩ, 470 kΩ and 470 Ω; capacitors 1 nF and 0.22 µF. A blank report page provides axes for every waveform and spaces for observations. The handout cites *Electronic Devices and Circuits*, fifth edition, Section 10-1.

## Op-amp characteristics and instrumentation amplifiers

The second experiment examines **bandwidth, slew rate, common-mode rejection ratio, offset voltage and noise**. Equipment is to be declared to the teaching assistant at least one hour before the experiment; the source allows groups of at most three and refers students to the LM741 and AD620 specifications.

### Bandwidth and slew rate

The closed-loop bandwidth decreases as gain increases. The given relationships are:

- f_T = BW_CL/β, with β = R₁/(R₁ + R_F).
- Slew rate S = ΔV/Δt.
- Maximum sinusoidal frequency without slew-rate distortion: f_S,max = S/(2πK), where K is output peak amplitude.

### Output offset

Input offset voltage and mismatched input bias currents cause output offset. A resistor at the noninverting input helps compensate the bias-current contribution:

R_C = R₁ ∥ R_F.

With this compensation, the handout writes **|V_OS| = (I⁺ − I⁻)R_F = I_io R_F**, and notes that the sign depends on which bias current is greater. The 741's pins 1 and 5 permit offset nulling with a potentiometer. The example uses R₁ = R_F = 1 MΩ, R₊ = 470 kΩ and a 10 kΩ potentiometer.

*Note: In the offset magnitude written with absolute value, the right-hand side should also be taken as |I⁺ − I⁻|R_F; the source gives the equation with the signed current difference.*

![Offset compensation resistor and 741 offset-null potentiometer](opamp-9.jpg "Offset voltage and compensation connections")

## Instrumentation amplifier design

1. Build a three-op-amp instrumentation amplifier using 741s, designed for **gain 10**, and adjust for maximum CMRR.
1. Build an **AD620** instrumentation amplifier, also with gain 10.
1. Measure gain, CMRR, frequency response, slew rate and noise for both circuits.

The classic three-amplifier network gives:

- V_o = (R₃/R₂)(V_b − V_a).
- V_b − V_a = (V₂ − V₁)(1 + 2R₁/R).
- **V_o = (V₂ − V₁)(R₃/R₂)(1 + 2R₁/R).**

Use practical resistances in the **10–100 kΩ** range. Match resistor pairs carefully: ordinary tolerance may be 5%; measure several resistors and use small series corrections when needed.

![Instrumentation amplifier with three 741s and the gain relation](opamp-10.jpg "Connection consisting of two input stages and a difference amplifier")

## CMRR measurement

The handout defines:

- V_id = V₁ − V₂.
- V_ic = (V₁ + V₂)/2.
- V_o = A_d V_id + A_c V_ic.
- CMRR = A_d/A_c, or **20 log₁₀(A_d/A_c)** in dB.

Apply the same **4–5 V common-mode signal** to both inputs and measure the output. Then apply a small differential signal, using a divider if necessary, and adjust until the output amplitude is equal to that in the common-mode test. The source then writes **CMRR = 20 log(V_d/V_cm)**.

*Note: Under the equal-output condition A_dV_d = A_cV_cm, so the ratio is written inverted. The correct form is CMRR(dB) = 20 log₁₀|V_cm/V_d|. In addition, the earlier gain derivation uses V₂−V₁ while the later differential-input definition uses V₁−V₂, which introduces a sign discrepancy.*

## Frequency response, slew rate, noise and grading

- **Frequency response:** Find the frequency where output falls to 1/√2 ≈ 0.707 of its low-frequency value, the −3 dB point.
- **Slew rate:** Apply a square wave, observe input and output together and measure the output transition ΔV/Δt. Compare with the device specification.
- **Noise:** Devise and justify a measurement method. The handout points to RMS quantities, resistor thermal noise and noise figure.
- **Targets:** Gain **10 ±5%**; for the 741 version, CMRR at least **40 dB**. The source relates this to approximately 1% resistor matching.
- **Report:** Compare all measured parameters for the 741 and AD620 versions and explain unexpected results. Do not dismantle the circuit before the assistant's check. The source permits either reporting language.

The supply note in the source asks that ±15 V levels and polarities be checked before connecting an op-amp, since reverse supply polarity can destroy it.
