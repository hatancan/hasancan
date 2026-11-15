---
baslik: EEM474 Power Electronics: Final Exam Questions of 31 May 2006
ozet: The 11 questions of the 31 May 2006 EEM474 final exam: R-L load with freewheeling diode, ON-OFF AC control, buck-boost, 120° inverters, DC motor and stepper motor.
---

The questions of the EEM474 Power Electronics final exam dated 31 May 2006 were transcribed to text from photographed pages of the paper; the photographs have not been published. A handwritten photo in the same folder contains an attempted solution of questions 1 and 5 of the exam. Personal information on the exam paper has not been transcribed.

## Questions

1. For the R-L load in the given figure (R is the internal resistance of the inductor), switch S1 stays closed for a duration t1 and open for a duration t2 (Vs, DC source, diode D1, and a freewheeling diode Dm in parallel with the load). For one period: a) Sketch the waveforms of Io (load current) and If (diode current) and write their general expressions. b) Redraw the waveforms for R = 0. (10 pts)
2. Considering the characteristics of switching devices, mark in the table the characteristics appropriate to each device. Devices: GTO, transistor, thyristor, IGBT, triac. Characteristics: fully controlled, semi-controlled, uncontrolled, unidirectional current, bidirectional current conduction, pulse controlled, requires continuous control signal. (8 pts)
3. In the given AC voltage control circuit controlled by the ON-OFF method (two antiparallel thyristors, load R), both thyristors conduct for n cycles and are off for m cycles. Given that the input voltage is vs = Vm sin ωt, a) obtain the RMS value of the output voltage (given relation: 2 sin² ωt = 1 − cos 2ωt). b) Obtain the power factor (PF) in terms of n and m. (10 pts)
4. In the given circuit (D1–D4 bridge, thyristor T1 in the middle, load R, input vs = Vm sin ωt) a) sketch the output current waveforms i1 (thyristor current) and io (current of resistor R) as functions of the input voltage and firing angle α. b) Draw the circuit that can perform the same function using two thyristors. (10 pts)
5. For the buck-boost converter in steady state, obtain Vo/Vin according to the principle that "the average value of the voltage across the inductor due to periodic current is zero" (other solutions will not be accepted). (10 pts)
6. In the given three-phase DC/AC circuit, each switch conducts for only 120° during one period. Conduction starts at instant (0) with the conduction of G1, and continues with a 60° shift with G2, G3, G4, G5, G6 in sequence. For a Y (star) load, write the values of Van, Vbn, Vcn in the given table (Modes 1–6; each mode represents 60° of conduction). (The chart given on the back page may be used.) (12 pts)
7. In the given single-phase full-bridge circuit (Q1–Q4 IGBTs and D1–D4 diodes, R-L load), to obtain a quasi-square wave AC voltage: a) Sketch the control pulses to be applied to the switches by the control circuit, and the voltage and current waveforms across the load. b) According to the voltage waveform across the load, indicate which switches operate in which interval. c) What adjustments can be made to the output voltage with this method? (10 pts)
8. Explain with a formula what the response of the motor will be as the load decreases while the voltage U is constant in a shunt-wound DC motor (Ra, La, E represent the rotor (armature); Rf, Lf represent the shunt winding (field winding)). (10 pts)
9. A stepper motor with a resolution of 200 has a rotor speed of 60 r/s (revolutions per second). a) Find the step angle of the motor. b) Find the number of pulses per second that must be supplied to control the motor. c) Find the number of pulses required for the rotor to turn through an angle of 23.4°. (9 pts)
10. Propose different methods for operating a hair dryer that runs on the city mains from a battery (the terms UPS and uninterruptible power supply are not valid). For each proposal, draw an engineering block diagram and state roughly, as bullet points with values, what you expect from each block (gain, frequency, switching frequency, etc.). Specifications of the machine: 220 V AC (rms), 50 Hz, R = 5 Ω, L = 10 mH, and battery = 12 V DC. (10 pts)
11. Briefly compare a stepper motor with an AC motor. (5 pts)

## Attempted Solution (Handwritten Photo)

**Question 1.** On the photographed page, the R-L load and the freewheeling diode (Dm) are drawn; for the source voltage Vs, a +Vdc level during the interval 0–t1 and a −Vdc level during the interval t1–t2 are shown, and for the current, triangular-shaped If and IL curves that rise and fall linearly, with a peak at t1 and an ILmin value at t2, are shown. For R ≠ 0, these curves are drawn in exponential (R-L) form; the solution stops at the sketching stage, without the general expressions being written.

**Question 5.** The solution is only at the initial stage; the principle "the average of the voltage across the inductor due to periodic current is zero" is written on the paper, and the circuit equations are not completed. Expected result: Vo/Vin = −D/(1 − D).

## Computable Results

- Question 9: step angle 360°/200 = 1.8°; since the rotor turns at 60 r/s, 60 × 200 = 12,000 pulses per second are required; for 23.4°, 23.4/1.8 = 13 pulses are applied.
- Question 3: for n cycles of conduction and m cycles of off-time, Vrms = Vm·√(n/(2(n + m))) = Vs,rms·√(n/(n + m)), and for a resistive load PF = √(n/(n + m)).
- Question 8: in a shunt motor with constant U, when the load torque decreases, the armature current Ia = T/(KΦ) decreases; since E = U − Ia·Ra increases, the speed ω = E/(KΦ) rises, approaching the no-load speed.

*Note: Since the photograph of the exam paper had another student's handwritten answer marks on it, those answers have not been transcribed. In a 120° conduction three-phase inverter, the star-load phase voltages are at the levels ±Vs/3 and ±2Vs/3 depending on each mode; the table is unsolved in the source.*
