---
baslik: EEM474 Power Electronics: Handwritten Course Notes (From Switches to Motors)
ozet: 53 pages of handwritten course notes with numerical examples on switching devices, rectifiers, DC/DC converters, SPWM, AC voltage control, UPS, and DC motors.
---

A scanned copy of the handwritten EEM474 Power Electronics course notes (53 pages) that a friend kept in a grid-paper notebook. Personal information has been removed. Below, the page headings, formulas, and solved examples have been transcribed into text; all the pages, in their original handwritten form, are available in the PDF at the end of the post. The notes follow the order of the course slides: switches, rectifiers, DC/DC converters, inverter, AC voltage control, UPS, and motors.

## Switching Devices (pages 1–9)

**Energy recovery.** When the switch is on, energy is stored in the inductor (vL = L·di/dt). When the switch is turned off, the energy in the inductor is returned to the source through diodes.

**Ideal power switch.** When conducting, the internal resistance should be 0; when off, the current should be 0; ton = 0 and toff = 0 are expected; no energy should be required when going from conduction to cutoff. A real switch is not ideal.

**Switches (in terms of control).** 1) Uncontrolled switches (diode). 2) Semi-controlled switches: only turn-on or only turn-off can be controlled (thyristor). 3) Fully controlled switches (transistor). Semiconductor switches: those that require a continuous gate signal (BJT, MOSFET: voltage controlled), those that require a pulse gate signal (once an instantaneous pulse arrives, the device remains on), bipolar voltage, unipolar voltage, bidirectional current, and unidirectional current are among the classes.

- **Thyristor:** it is semi-controlled; it controls only its turn-on. Triac: formed by connecting two thyristors in anti-parallel; it conducts current in both directions. GTO: controls both turn-on and turn-off.
- **Diode characteristic** and **thyristor characteristic:** common point with the diode: for the thyristor to turn on, forward polarity (anode relative to cathode) is required; difference from the diode: for it to turn on, current must flow from the gate to the cathode for a certain time.

**Comparison of switches.** The device is selected according to voltage, current, and frequency. Thyristors operate at the highest voltage and current; the fastest are MOSFETs (highest frequency). Frequency and operating speed are directly proportional. Thyristor and GTO are pulse controlled: the thyristor turns on with a pulse applied to its gate, and the load voltage continues after the pulse; therefore it controls only turn-on. The GTO controls both turn-on and turn-off, and there is energy saving. Transistor and MOSFET require continuous control. The IGBT is made by combining the good properties of the thyristor, transistor, and MOSFET. If a transistor is to carry current in both directions, an anti-parallel diode is connected next to it.

**Operating region of switches (in the i–v plane).** Diode: in conduction only the positive half of the i axis, in cutoff the negative half of the v axis. BJT: in conduction on the i axis, in cutoff on the positive v axis. Transistor with anti-parallel diode: in conduction (transistor) positive i, (diode) negative i; in cutoff the v axis. If the two are connected in series, voltage is seen in both directions only in the cutoff state.

## Harmonic Power Examples (pages 10–12)

**Example 1.** v(t) = 4 + 8 sin(ω₁t + 10°) + 5 sin(ω₂t + 50°); Vrms = √(4² + (8/√2)² + (5/√2)²) = 7.78 V.

**Example 2.** v(t) = 100 cos(377t) V; i(t) = 8 + 15 cos(377t + 30°) + 6 cos(2·377t + 45°) + 2 cos(3·377t + 60°) A.

- a) Power drawn by the load: P = 0·8 + (100/√2)(15/√2) cos30° + 0 + 0 = 650 W (since the DC component of the voltage is 0, there is no DC power).
- b) PF: Vrms = 100/√2 = 70.7 V; Irms = √(8² + (15/√2)² + (6/√2)² + (2/√2)²) = 14 A; PF = P/S = 650/(70.7·14) ≈ 0.66.
- c) DF = I₁,rms/Irms = (15/√2)/14 ≈ 0.76.
- d) THD = √((Irms² − I₁,rms²)/I₁,rms²) = √((14² − (15/√2)²)/(15/√2)²) ≈ 0.86 (86%). THD is expected to approach 0 and DF to approach 1.

*Note: 650 W is a rounded value of 100·15/2·cos 30° = 649.5 W. Since Irms² = 8² + 112.5 + 18 + 2 = 196.5, Irms ≈ 14.02 A, PF = 649.5/(70.71·14.02) ≈ 0.655, and THD ≈ 0.86; the results on the paper are correct.*

## Half-Wave and Full-Wave Rectifiers (pages 12–17)

- If a thyristor is used, the firing point is α (it must be fired at a point before π). If two diodes are used, a (center-tapped) transformer is required; if four diodes (bridge) are used, no transformer is needed. In the two-diode circuit, the inverse voltages are different.
- See the RF, FF, η calculations: efficiency η = Pdc/Pac (half-wave: one diode, full-wave: 2 or 4 diodes; efficiency increases). FF = Vrms/Vdc (form factor), RF = Vac/Vdc (ripple factor); the full-wave rectifier has less ripple than the half-wave, so RF decreases.
- **Full-wave bridge:** as in the half-wave case, thyristors can be used instead of diodes; the diagonal thyristors must be fired at the same time. If fired at 90° and 150°, whichever fires later dominates (output between 150° and 180°).
- **Half-wave rectifier with RL load.** If the load is R and L, L stores energy while the diode is conducting: vL = L·di/dt. When the current decreases, the polarity changes; that is, the inductor begins to behave like a current path or a voltage source. This effect is the energy stored by the inductor, and the current continues to flow after π (until π + β). The value of α varies with the size of L; as L increases or the source frequency increases, continuity increases. To eliminate this partially negative voltage portion, a freewheeling diode is connected in parallel with R-L; when it is connected, the circuit operates as if connected directly to R, the load voltage always remains positive, and the current becomes continuous.
- Summary: when converting AC to DC, if there is an R-L load, energy accumulates in it; to prevent this from being returned to the source, a parallel diode is connected.
- A DC motor is mathematically composed of R, L, and E: as long as the motor is not rotating, there are only R and L; as the motor begins to rotate, E (back EMF) comes into play. In the four-thyristor rectifier with an RLE (DC motor) circuit, the output carries current between α and α + π.

## Three-Phase Rectifiers (pages 18–20)

Unlike a single-phase alternator, a three-phase alternator generates sinusoids in three phases, with 120° between the phases. Characteristics: 1) when single-phase is rectified, there is a lot of ripple; 2) in single-phase the power factor is low; 3) higher power can be drawn in three-phase.

- **Half-wave three-phase rectifier:** one diode is connected to each phase; the phases in the source follow one another. While diode 1 is conducting, 2 and 3 are off; then diode 2, with 1 and 3 off; then it returns to the start. Three diodes share one period, and each diode conducts for 120°. The output looks more like DC.
- **Three-phase full-wave rectifier:** two diodes for each phase, six diodes in total; the conduction time of each diode is 60°; two diodes are conducting at every instant. The output is even closer to DC.

## DC-to-DC Converters (pages 21–31)

**Linear and switching.** Linear converter: a transistor or MOSFET operates in the linear region (series or parallel); voltage step-down, e.g., LM7805 (12 V to 5 V). Line regulation: the output voltage remains constant even if the input voltage varies within certain limits; load regulation: the output remains constant even if the load changes. Where there is regulation, feedback is involved.

**Switching type (SMPS).** In the linear type there is no transformer at no load, but in the switching type there is a transformer at no load: AC → DC → AC (high frequency) → DC. Step-up/step-down can be done; volume and size are small (because of the size of the transformer), the capacitors are small; the frequency is around 25 kHz (50 Hz in linear). The ripple is written as ΔV = 1/(2·e·f·C).

**Chopper DC/DC.** Linear: like a variable resistor, the voltage is controlled instantaneously. Switching: the instantaneous value is not considered, the average value is; with a chopper, the voltage can be changed in a DC/DC converter. Vavg = K·Vs, K = ton/(ton + toff) = ton/T (duty cycle or pulse ratio); Vrms = √K·Vs. Vavg and Vrms depend on K; the output voltage changes with K. There are two ways of changing K: 1) PWM: ton is changed, T is constant; 2) frequency modulation: ton is constant, T increases or decreases.

**Example.** 48 V source, 25 kHz switching, 24 Ω load, ton = 1 ms (this value is given on the paper): T = 1/f = 4 ms (the paper writes "T = 1 ms") and K = 1/4 was taken; Vo = (1/4)·48 = 12 V, Vrms = √(1/4)·48 = 24 V.

*Note: On the paper the frequency is written as "25 kHz", but the calculation was done with T = 4 ms (250 Hz); for ton = 1 ms and K = 1/4, T = 4 ms is required. At 25 kHz, T = 40 µs. The results (12 V and 24 V) are correct for K = 1/4.*

**Buck (step-down) converter.** When the switch is closed, the inductor voltage is VL = Vd − Vo = Vin − Vo; when the switch is open, VL = −Vo. With an RL load the current is exponential; ΔImax = Vs/(4fL); a high switching frequency is desired; Vo = K·Vin, 0 ≤ K ≤ 1, Vo ≤ Vin.

**Boost (step-up) converter ("Principle of step-up operation").** When the switch is closed (conducting), VL = Vs, ΔiL = Vs·DT/L; when the switch is open (not conducting), the inductor changes polarity, Vo = Vs + VL: Vo = Vs[1 + t1/t2] = Vs/(1 − K). For K = 0.5, Vo = 2Vs; as K → 1, Vo → ∞ (the way of stepping up voltage). With ΔiL(closed) + ΔiL(open) = 0, Vo = Vd/(1 − D); Vo ≥ Vd. Input power = output power: Vd·Id = Vo²/R. The inductor current is triangular: Imax = IL + ΔiL/2, Imin = IL − ΔiL/2.

**Classification of converters.** 1st-quadrant chopper (only the 1st quadrant in the Vo–Io plane; asolton converter); 2nd-quadrant chopper (motor; with diode); 1st- and 2nd-quadrant chopper.

**Continuous conduction limit.** For Imin ≥ 0, Lmin = D(1 − D)²·T·R/2; "Lmin so that iLmin does not fall to zero". Ripple = ΔVo/Vo, ΔVo/Vo = D/(R·C·f); as the switching frequency increases, the ripple decreases. ΔiL(on) + ΔiL(off) = 0 and the average VL is 0; these two conditions are used in all converters to find Vo/Vd.

**Example (boost).** Vo = 30 V, Vin = 12 V, ripple 1%, R = 50 Ω, f = 25 kHz. D = 1 − Vs/Vo = 1 − 12/30 = 0.6. Lmin = D(1 − D)²R/(2f) = 0.6·(0.4)²·50/(2·25000) = 96 µH. IL = Vs/((1 − D)²R) = 12/(0.16·50) = 1.5 A; ΔiL/2 = Vs·DT/(2L) = 1.2 A; Imax = 2.7 A, Imin = 0.3 A. C > D/(R·f·(ΔVo/Vo)) = 0.6/(50·25·10³·0.01) = 48 µF.

**Buck-boost converter.** For D > 0 it can act as a boost (Vo > Vs) and also as a buck; the polarity of the output voltage is opposite to that of the input. With the switch conducting, VL = Vd, ΔiL(on) = Vd·DT/L; with the switch in cutoff, VL = Vo (in magnitude), ΔiL(off) = Vo(1 − D)T/L; the result is Vo = −Vs·D/(1 − D) (for D = 0.5, Vo = −Vs: only the polarity changes; at D = 0, Vo = 0, as D → 1, Vo → ∞). Selection: if the voltage drops and the polarity changes, buck-boost; if only the voltage drops, buck; if the voltage rises and the polarity is the same, boost; if only a polarity change is desired, buck-boost.

**Ćuk converter.** It works exactly like the buck-boost: Vo = −Vs·D/(1 − D). (See the figures of the buck-boost, buck, and boost converters; it may be asked in the exam.)

## Control of DC/DC Converters (pages 32–36)

Source → power electronics circuit → load; feedback from the output to the control block (comparison with the reference, regulator). Line regulation: the voltage X remains constant even though the input varies within certain limits; load regulation: the voltage remains constant even if the load changes. Voltage-mode control (VL is monitored) and current-mode control (iL is monitored). To increase Vo, D is increased: Vo = D·Vs (buck). PWM is used to change D: a sawtooth signal is compared with Vc (V₂); if V₂ increases the pulse width increases, if it decreases the pulse narrows; D = ton/T, Vo = D·Vs.

Control loop: if Vo increases or decreases, V₂ changes → V₃ changes → D changes → Vo = D·Vs. If a transistor is used instead of the switch, it changes BE and CE. In voltage mode, a sample is taken from the voltage across Vo; in current mode, from the current (a low-value resistor is used for the current sample; high wattage, small resistance value).

**Example (buck).** L = 100 µH, Vin = 40 V, D = 0.3, Po = 24 W, fs = 100 kHz, Ts = 10 µs. Vo = D·Vin = 12 V; Io = Po/Vo = 2 A; R = Vo/Io = 6 Ω; IL = Io = 2 A; ΔiL = (Vin − Vo)/L · D·Ts = 0.84 A (peak to peak); Imax = IL + Δi/2 = 2.42 A, Imin = 1.58 A. The inductor voltage is +28 V for 3 µs and −12 V for 7 µs.

**Example (boost).** L = 100 µH, Vin = 12 V, D = 0.4, Po = 30 W, fs = 100 kHz. Vo = Vin/(1 − D) = 20 V; Io = 30/20 = 1.5 A; IL = Iin = 30/12 = 2.5 A; ΔiL = Vs·DT/L = (12/100 µ)·4 µ = 0.48 A; Imax = 2.74 A, Imin = 2.26 A; the inductor voltage is +12 V for 4 µs and −8 V for 6 µs.

**Example (buck-boost).** L = 100 µH, Vin = 12 V, D = 0.6, Po = 36 W, fs = 100 kHz. The inductor voltage is +12 V for 0.6T and −18 V for 0.4T; the average inductor current is 5 A (ΔiL = 0.72 A; Imax = 5.36 A, Imin = 4.64 A).

**PWM and feedback loop.** D = ton/Ts = Vcontrol/Vst; Vcontrol = D·Vst. A portion of Vo (R2/(R1 + R2) = K) is taken from the output through a voltage divider and compared with Vref; the error amplifier (A·(Vref − Vin·D·K)) feeds the PWM; the change in Vo is the change in D (the frequency is constant, the duty cycle changes). Where Vo is concerned, if the load R changes, Vo changes. **Programs that can be used:** PSPICE, PSIM, MATLAB, PSCAD; in PSIM, the connections are made and "run simulation" is used.

## Inverter and SPWM (pages 37–39)

Single-phase full bridge (switches S1–S4, Vdc source, AC load); the SPWM block is given the inputs ma, mf, and fsin. V₁ = ma·Vdc: 1) the amplitude of the sinusoid, 2) the frequency can be controlled, 3) the harmonics that are present. ma = Vsin/Vtri (modulation index, between 0 and 1); mf = ftri/fsin ≫ 1 (frequency index). The change in ma is related to the change in Vsin.

SPWM is divided into bipolar and unipolar; they differ in their control sections, but their outputs after the filter are the same. Bipolar SPWM: the triangular wave and the sinusoid are fed to a comparator; the output is applied directly to Q1, Q4 and inverted to Q2, Q3. Unipolar SPWM: two comparators, the sinusoid is sent with a 180° phase difference; the Q1, Q2 and Q3, Q4 pairs. The fundamental difference between these two circuits is the harmonics produced.

## AC–AC Conversion and Voltage Control (pages 39–47)

AC to AC is done in two ways: 1) without using an inverter (amplitude adjustment: the RMS value of the AC voltage is changed, on-off and phase control; frequency adjustment), 2) using an inverter (AC/DC → DC/AC). If amplitude adjustment is desired, a transformer is used.

**RMS control: 1) On-off.** Two anti-parallel thyristors (TR1, TR2); coefficients m and n: n cycles ON (fired at α = 0, acts like a diode), m cycles OFF. Vrms = Vs·√(n/(m + n)) = Vs·√k. As the off time (m) decreases, the PF improves.

**2) Phase control.** The value of α is variable. In the unidirectional (thyristor + diode) circuit, the thyristor is fired at α; if it is fired at the instant π... The maximum value at the output is the value of the source (firing at α = 0); the minimum value is at the instant the thyristor is fired at π, that is, for the negative sinusoid value (diode), −Vm/2 (as written on the paper). The waveform across the thyristor: we cannot see anything after π, because it is a diode, so we cannot see it. If two thyristors are connected in parallel (SCR1, SCR2), the average value of the output is 0, and the same waveform is also obtained with a two-diode bridge: unidirectional current passes through the thyristor, bidirectional current through R. In RL circuits, because of the effect of L, the thyristor remains on for longer than π (π + β). When there was R, it was fired once; when R + L is present, it needs to be fired several times.

**Cycloconverter.** AC/AC with two anti-parallel rectifier groups (1 and 2); if group 1 does this and then group 2 does it, a periodic wave from + to − is formed; the frequency ends up below the source frequency. The disadvantage is the increase in harmonics.

**Triac.** Its greatest advantage is that it conducts current in both directions. Dimmer: a triac (A1, A2, G) with a load (lamp); Vrms is adjusted by changing the firing angle α; as α increases, less voltage than 220 V is obtained and the lamp burns dimmer. The diac behaves like a Zener diode (for AC); it does not allow conduction up to a certain value. The operating region of the thyristor (in the i–v plane) and the operating region of the triac are drawn (the triac in the 1st and 3rd quadrants).

**Question.** Half bridge (two different circuits with thyristor + diodes; D1–D4 and T1): a) the outputs of the two circuits are the same; b) Vout = Vm/π (for α = 90°, cos90° = 0); Vo = (1/π)∫α→π Vm sin(ωt) dωt = (Vm/π)(1 + cos α). In circuit 1, the current through T1 is always in the same direction; in circuit 2, since the triac conducts current in both directions, the current flows in both directions.

## UPS (page 49)

A DC-to-AC converter is used. UPS systems are divided into two groups: 1) online (the inverter runs continuously), 2) offline (the inverter does not run continuously). When the mains is present, the battery is charged; when the mains is absent, energy is supplied from the battery.

## Motors (pages 50–53)

**Motor selection:** 1) cost, 2) thermal capacity, 3) efficiency, 4) torque-speed profile. AC motors: induction, synchronous, universal. DC motors: wound-field DC motors, permanent magnet, brushless (an electronic circuit must be present for it to operate).

**Machine efficiency:** η = Po/Pin; expressed in three forms: η = Po/Pi × 100 %, η = Po/(Po + Ploss) × 100 %, η = (Pi − Ploss)/Pi × 100 %.

**Motor and generator.** Electrical energy ↔ mechanical energy. Mechanical → electrical: E = K·Φ·ω (ω angular speed, Φ magnetic flux). Electrical → mechanical: T = K·Φ·I (I current). The same machine can operate as either a motor or a generator depending on the energy supplied. P = E·IA = T·ω. In a motor U > EA, in a generator EA > U. If the motor does not rotate, E = 0. Circuit: V = Ia·Ra + Ea, Ea = KΦω; at DC voltage, L acts as a short circuit.

**Permanent magnet DC motor.** When the angular speed is 0, the torque is at its maximum; when the angular speed is at its maximum, the torque is 0 (there is an inverse relationship). U = E + Ia·Ra, I = T/(KΦ). ω = Vs/(KΦ) − Ra·T/(KΦ)² (the slope is negative); as Vs changes, the slope does not change, but the characteristic shifts in parallel.

**Wound-field DC motor — shunt motor.** The field winding is connected in parallel with the rotor; even if we change the direction of U, the direction of the field and the rotor will change, so the direction of the motor does not change. The speed variation with load is low. **Separately excited motor:** when we change either U_E or U_A, the direction of the motor changes. **Series motor:** the rotor and the winding are connected in series; the direction of the motor does not change, and its torque is very high. **Compound-wound motor:** the direction of the motor changes. The loss dissipated in it is greater in the wound-field DC motor (because of internal resistances).
