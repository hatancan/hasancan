---
baslik: EEM474 Power Electronics: Quizzes 1–6 and Answer Notes
ozet: A/B forms of six quizzes on power factor, switches, buck/boost converters, PWM inverters, and DC motors.
---

The six quizzes of the EEM474 Power Electronics course and the answer notes on them have been compiled together. In many questions, the answer refers to a page number in the course slides; these parts are not presented as completed solutions. The PDFs, with metadata that could contain personal information removed, are in the ZIP at the end of the post.

## Quiz 1: Basic Concepts

The questions cover converter types (AC/DC, DC/DC, DC/AC, AC/AC), the RMS value measured by an AC voltmeter, harmonics, and power quality. For sinusoidal v(t) = Vm cos(ωt + θ) and i(t) = Im cos(ωt + φ), PF = cos(θ − φ) is written. The harmonics of a signal with a 100 Hz fundamental are integer multiples of this frequency.

Given the relations DF = I₁,rms / Irms and THD = √(Irms² − I₁,rms²)/I₁,rms, good power quality is expected to have DF approaching 1 and THD approaching 0. An in-phase sinusoidal current, a phase-shifted sinusoidal current, and a pulse-shaped rectifier current are compared.

In periodic steady state, the average current of a capacitor is zero. A fuse's overcurrent protection and overvoltage protection are not the same function. The current of a freewheeling diode is examined according to whether the load is resistive or inductive.

*Note: In the answer notes, the statement that an ideal switch uses "very little energy" for switching is marked as correct. In the fully ideal model, switching loss is zero; a small but nonzero loss belongs to the real switch.*

## Quiz 2: Switches and Losses

The differences between a triac and a GTO, the properties of an ideal switch, and the voltage–current–frequency criteria for switch selection are asked. Conduction loss is separated from turn-on/turn-off loss. From the BJT drive pulse, the base current, collector current, and VCE waveforms are drawn; a suitable switch structure is selected from the current–voltage regions.

An SCR is gate-controlled only in the direction of turning on. A GTO can be taken to cutoff with a negative gate pulse. A triac can carry current in both directions; it should not be concluded that a GTO carries current in both directions.

## Quiz 3: DC–DC and Feedback

Linear and switching power supplies are compared in terms of size, loss, output ripple, and control. For the H-bridge, which switches are conducting is asked for positive/negative output and for unidirectional voltage. In a boost converter, when the switch is conducting, diL/dt = Vin/L.

The example feedback buck circuit has a 20 V source, a 150 µH inductor, a 100 µF capacitor, and a 32 Ω initial load. A sample is taken from the output through an equal-resistor divider; a 5 V output is obtained with a 2.5 V reference. The answer in the source states that the reference should be set to 3 V for a 6 V target. The roles of the error amplifier and the comparator, and the effect of connecting an additional load after 3 ms, are asked.

## Quiz 4: Inverter and Harmonics

The meaning of THD is explained; the ratio of the RMS components other than the fundamental component to the fundamental RMS is used. Three structures are requested for producing adjustable AC from the mains:

- Controlled rectifier + square-wave inverter: amplitude from the rectifier, frequency from the inverter.
- Uncontrolled rectifier + buck + square-wave inverter: amplitude from the buck, frequency from the inverter.
- Uncontrolled rectifier + SPWM inverter: both adjustments from the inverter.

In the example with 100 V DC, R = 10 Ω, L = 25 mH, and a 60 Hz square wave, the output RMS, the odd harmonic currents, and the THD are requested. The last question is an estimate of the surface area of the paper without using a measuring instrument.

## Quiz 5: PWM and AC Voltage Control

In the half-bridge with two capacitors, the sign of the output is first drawn according to whether the upper or lower switch closes. For the H-bridge, bipolar and unipolar SPWM gate signals are generated. From the voltage graph, the ma and mf ratios are determined, and from the normalized spectrum, the switching method.

It is emphasized that a DC/DC converter is not an AC frequency converter that raises or lowers frequency; it changes the DC voltage level. For phase-controlled AC output, the RMS integral is taken only over the conduction intervals.

## Quiz 6: DC Machines

For motors and generators, the relations E = KΦω, T = KΦIa, and Pconversion = EIa = Tω are used. The equivalent circuit includes the armature resistance, inductance, and back EMF. At the motor's initial start, since E = 0, current limiting is necessary.

The questions cover adjustable supply of a 220 V DC motor from the mains, the torque–speed curve, efficiency with losses, shunt motor starting current, and speed control in wound-field motors. The source arrangement, in which many answers refer only to the course slides, has been preserved.

*Note: The parts of the A/B forms that give the same questions in a different order have been merged here. The "Answer Key" text is not a student name. The PDF Title/Author fields were regenerated and cleaned.*
