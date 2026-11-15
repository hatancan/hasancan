---
baslik: EEM214 Electronics I: Diode Lecture Notes – From the Ideal Diode to Rectifiers and Clampers (Keith W. Whites, EE 320, 2009)
ozet: Eight lecture notes on diodes from Keith W. Whites's EE 320 Electronics I course: the ideal diode, the physical operation of the pn junction, DC analysis and the CVD/PWL models, the small-signal model r_d = nV_T/I_D, Zener diodes, rectifiers, peak rectifiers and ripple, limiting and clamping circuits, and special diodes.
---

This post presents eight of the diode-related lecture notes (Lectures 1–4 and 6–9) found in the EEM214 Electronics I course folder, taken from the English lecture notes that **Keith W. Whites** (South Dakota School of Mines and Technology) prepared in fall 2009 for his course **EE 320 Electronics I**. The notes follow Sedra & Smith's *Microelectronic Circuits*, and some of the figures are taken from that textbook. Below, the main ideas and formulas of each lecture are summarized in English; the PDFs can be downloaded as a ZIP at the end of the post. The same author's BJT and MOSFET notes are in a separate post: [Whites EE 320 BJT and MOSFET notes](/arsiv/eem214-whites-ee320-bjt-mosfet-notlari/).

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed at the request of the rights holder.*

## Lecture 1: Ideal Diode

Resistors, inductors, and capacitors are linear elements: for y = f(x), m·y = f(m·x) holds (v = Ri, i = C·dv/dt). A diode, by contrast, is a junction formed by two different semiconductors and is **nonlinear**. The ideal diode has two operating regions: v < 0 ⇒ i = 0 (off) and i > 0 ⇒ v = 0 (on). A diode is like an electronic "valve" that passes current only in the direction of the arrow in its symbol; for example, it is used to protect a circuit when a battery is connected backwards. As applications, the signal rectifier (the diode conducts when v_I > 0, with v_O = v_I) and diode logic gates are introduced.

## Lecture 2: Physical Operation of Diodes

The real silicon diode has three regions: **forward bias** (about 0.6–0.7 V when conducting), **reverse bias** (i = −I_S; I_S is on the order of fA in small-signal diodes), and **breakdown** (v ≈ −V_ZK). In the forward direction, i = I_S·(e^(v/nV_T) − 1), where n is the emission coefficient (1–2) and V_T = kT/q ≈ 25 mV. The rest of the note covers the silicon crystal, thermally generated electron–hole pairs, the contribution of holes to conduction, acceptor (boron, p-type) and donor (phosphorus, n-type) doping, and the formation of the pn junction.

## Lecture 3: DC Analysis of Diode Circuits

In a circuit consisting of V_DD, R, and a diode, combining KVL, V_DD = I·R + V_D, with the diode equation yields a transcendental equation for V_D that has no analytical solution. There are five solution approaches:

1. **Graphical solution:** the intersection of the diode curve with the load line I = V_DD/R − V_D/R (useful for qualitative understanding).
1. **Simulation** (SPICE, ADS): for 2 V, 1 kΩ, and a 1N4148, V_D = 565 mV and I = 1.43 mA.
1. **Numerical methods** (Mathematica, MATLAB, Mathcad).
1. **Iterative analysis.**
1. **Approximate analysis:** the most common approach. In the **constant voltage drop (CVD)** model, a conducting diode is a 0.7 V source; in the **piecewise linear (PWL)** model, a series resistance r_D is added to this ("battery + internal resistance").

## Lecture 4: Small-Signal Diode Model and Its Application

A small time-varying signal rides on top of a DC value: v_D(t) = V_D + v_d(t). The diode current becomes i_D(t) = I_D·e^(v_d/nV_T); for v_d << 2nV_T, approximating the exponential by its first two terms gives i_D(t) ≈ I_D + (I_D/nV_T)·v_d(t). This defines the **small-signal resistance** r_d = nV_T / I_D; it is the reciprocal of the slope of the tangent at the Q point and depends on the bias (it is a different quantity from r_D in the PWL model). The analysis is done by superposition: after the DC solution, "all DC sources are zeroed and the diode is replaced by r_d".

## Lecture 6: Zener Diodes

In the steep reverse breakdown region, the voltage remains almost constant. There are two physical mechanisms: the **Zener effect** (the large field in the depletion region pulls electrons out of their bonds) and the **avalanche effect** (accelerated carriers collide with lattice atoms and knock loose new carriers). As long as the power limit is not exceeded, the diode is not damaged. The manufacturer specifies V_Z at a test current I_ZT (in the example datasheet, 8.2 V, 31 mA, 1 W); as the current varies, ΔV_Z = r_z·ΔI_Z (r_z is a few ohms to tens of ohms), and the model is V_Z = V_Z0 + r_z·I_Z. Applications: overvoltage protection and voltage regulation.

**Example N6.1:** 6.8 V (at 5 mA), r_z = 20 Ω, I_ZK = 0.2 mA, a 10 V ± 1 V source, and a 500 Ω series resistor. V_Z0 = 6.8 − 20 × 5 mA = 6.7 V; the no-load V_O = 6.83 V; a ±1 V variation in the source produces a ±38.5 mV variation at the output (**line regulation**); when a load is connected, I_Z decreases by 3.4 mA and ΔV_O = 20 × (−3.4 mA) = −68 mV (**load regulation**).

## Lecture 7: Diode Rectifier Circuits (Half Cycle, Full Cycle, Bridge)

The blocks of a DC power supply: transformer (V_2/V_1 = N_2/N_1; 8:1 for about 15 V from the 120 V_rms mains), rectifier, filter, and regulator. Three rectification methods: **half-wave**, **center-tapped full-wave**, and the most common one, the **bridge**. With the PWL model, the half-wave output is v_O = [v_S − V_D0]·R/(R + r_D) (when v_S > V_D0) and zero otherwise. Two parameters matter when selecting a rectifier diode: **current-carrying capability** and **peak inverse voltage (PIV)**; in a half-wave rectifier, PIV = V_s.

## Lecture 8: Peak Rectifiers

A capacitor in parallel with the load charges to the peak value during the positive half-cycles and discharges slowly through the load while the diode is off; τ = RC >> T must be chosen. The discharge follows v_O(t) = V_p·e^(−t/τ) (V_p − 0.7 for a non-ideal diode). For τ >> T, the ripple is approximately **V_r ≈ V_p·T/(RC) = V_p/(f·R·C)** (half-wave; in full-wave, T is halved). The note shows that the diode conducts only during a short **conduction interval** Δt, that the conduction angle is ωΔt ≈ √(2V_r/V_p), and that large peak currents flow through the diode in this short time; it then gives an example calculating C for 2 V_pp ripple.

## Lecture 9: Limiting and Clamping Diode Circuits, Voltage Doubler, Special Diode Types

- **Limiters (clippers):** keep the voltage between predetermined limits; used for protection and signal conditioning. The note shows how to realize a desired transfer function with ideal diodes.
- **Clamped capacitor circuit:** the diode keeps v_O ≥ 0, and the capacitor charges only when v_I < 0; in steady state, the capacitor charges to the negative peak of the input (6 V in the example) and the lowest value of the output is clamped to zero. Applications: a pulse-width modulation (PWM) detector and, combined with a peak rectifier, a **voltage doubler** (output ≈ 2V_p).
- **Special diodes:** the Schottky diode (metal–n-type semiconductor, about 0.2 V forward drop, fast because there is no minority carrier storage), the varactor (reverse-biased, voltage-controlled capacitance), the photodiode (current generated by light in a reverse-biased junction), and the LED (light emitted by carriers recombining in a forward-biased junction).

## Download

The ZIP file contains the original PDFs of the eight lecture notes (320Lecture1–4 and 320Lecture6–9).
