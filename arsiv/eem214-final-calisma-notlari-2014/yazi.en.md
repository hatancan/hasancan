---
baslik: EEM214 Electronics I: Final Exam Study Notes (2014) – Diode Models, Rectifiers, Clippers, BJT/FET Analysis, Resistor and Capacitor Types
ozet: Handwritten summary notes kept for preparing for the EEM214 Electronics I final: diode models and DC/AC analysis steps, half-wave and full-wave rectifiers, series and parallel clippers, clamper circuits, transistor classification, DC and AC analysis of BJTs and FETs; for the homework, diode, resistor and capacitor types along with the resistor color code table.
---

This post presents the handwritten summary notes taken while preparing for the **spring 2014** final exam of the EEM214 Electronics I course (29 May 2014), as well as the notes prepared for the homework (on diode, resistor and capacitor types) that was stated to be covered in the final that semester. The text was transcribed from phone photographs of the pages; the photographs were not published. Figures are described in words. For the computer-typed answers to the homework, see [Homework Answers (2012–2014)](/arsiv/eem214-odev-cevaplari-2012-2014/); for the answer key of the final exam, see the [2014 Quiz 2 and final](/arsiv/eem214-quiz-2-final-2014/) post.

## Final notes

### Semiconductors and diodes

- **n-type material:** excess free electrons.
- **p-type material:** excess free bonds.
- **Diodes:** elements that conduct current in their own direction under forward bias.

*Note: In p-type material, the excess is not "bonds" but a lack of electrons, i.e. **holes**.*

### Diode models

- **1) Ideal diode:** behaves like a short circuit when conducting. It does not conduct in the reverse direction; V_i > 0 is sufficient for it to operate.
- **2) Constant voltage drop model (Constant Voltage Drop, CVD):** a voltage source of V_B when conducting. It does not conduct in the reverse direction; V_i > V_B is required for it to operate.
- **3) Piecewise linear model (Piece-Wise Linear, PWL):** a voltage source V_B in series with a resistance r_d when conducting. It does not conduct in the reverse direction; V_i > V_B is required for it to operate.

### DC and AC analysis of diodes

**DC analysis:**

1. Is the current direction the same as the diode direction?
2. If V_input > V_barrier,
3. draw the model as requested,
4. perform the circuit analysis.

**AC analysis:** Both AC and DC are applied to the input. The AC and DC models are drawn separately and the desired quantity is found for each; the result is obtained by adding the two values. In the AC model, the diode is represented by the resistance r_ac.

### Rectifier diode circuits

- **Half-wave rectifier:** source, series diode and R load. Only the positive half-cycles of the input sine pass to the output; during the negative half-cycles the output is zero.
- **Full-wave rectifier (bridge):** a four-diode bridge connected to the transformer secondary and an R load. Both half-cycles appear in the positive direction at the output.
- **Full-wave rectifier (center-tapped):** a center-tapped transformer and two diodes, R load; the output has the same shape as that of the bridge rectifier.

### Clipper diode circuits

**a) Series clipper:** the diode and a 3 V battery are in series with the source, and the output is taken across R. With the battery connected in the opposite direction to the diode, the diode does not conduct unless the input exceeds 3 V; at the output only the part of the input above 3 V is seen.

*Note (from the notebook):* Since the 3 V is stronger until V_g = 3 V, it clips up to 3 V. The diode direction (positive or negative) sets this.

In the second series clipper, the battery is connected in the same direction as the diode; the output waveform is drawn shifted upward relative to the input.

*Note (from the notebook):* Since the diode and battery are in the same direction, 3 V → +3 V goes through.

**b) Parallel clipper:** the source is through a series R, with a diode + 3 V battery in parallel with the output. The output is limited to 3 V, with the part of the input exceeding 3 V cut off; the negative half-cycle passes unchanged.

### Clamper circuits

1. Analysis starts with the half-cycle in which the diode conducts.
2. When the circuit is operating, the capacitor charges to the first voltage it sees.
3. In the opposite half-cycle, the capacitor is assumed not to discharge.
4. When it operates again, the capacitor supports the voltage source.

Example: a series capacitor, with a diode and R in parallel with the output. When the input is a +10 V / −10 V square wave, the output is a square wave varying between 0 and −20 V.

### Classification of transistors

- **BJTs:** NPN (forward), PNP (reverse).
- **FETs → JFETs:** n-channel, p-channel.
- **FETs → MOSFETs → Depletion-type MOS:** n-channel, p-channel.
- **FETs → MOSFETs → Enhancement-type MOS:** n-channel, p-channel.
- **MESFET** was also mentioned alongside the MOSFETs.

### BJTs

The npn and pnp symbols (B, C, E terminals) are drawn. If current enters through the base, current flows from C to E; the input (base) current and the C–E current vary in direct proportion.

- I_E = I_B + I_C
- I_C = β·I_B
- I_E = (β + 1)·I_B
- If β ≫ 1, I_C ≅ I_E can be taken.

**DC analysis of BJTs:** when drawing the circuit, capacitors are made open circuits.

**AC analysis of BJTs:** capacitors are short circuits, (DC) sources are killed (turned off).

- **r_e model:** a resistance β·r_e between B and E, and a dependent current source I_b·β between C and E.
- **r_π model:** a resistance r_π between B and E, and a dependent current source g_m·V_BE (or I_b·β) between C and E.

### DC analysis of FETs

- If V_T > V_GS, cutoff.
- If V_G > V_T, active:
- a) Triode (linear) region, if V_DS < V_GS − V_T: I_D = k_n′(W/L)·[(V_GS − V_T)·V_DS − ½·V_DS²]
- b) Saturation, if V_DS > V_GS − V_T: I_D = ½·k_n′(W/L)·(V_GS − V_T)²

*Note: The condition for being active is written in the notebook as "V_G > V_T"; the correct form is V_GS > V_T.*

### AC analysis of FETs

Open circuit between G and S (input voltage v_gs), a dependent current source g_m·v_gs between D and S.

**When performing AC analysis:**

1. Capacitors are short circuits,
2. DC sources are killed,
3. draw the model,
4. find A_v, A_i.

## Homework notes: Diode, resistor and capacitor types

### Diode options

- **a) Tunnel diode:** Made by adding a large amount of doping material to pure silicon or germanium. The current level increases up to a certain voltage value, and after a certain voltage the current decreases; it operates in the region where the decrease occurs. Used in high-frequency circuits and oscillators.
- **b) Varicap diode:** A diode that works like a capacitor adjustable by the voltage applied to its terminals; it operates under reverse bias. If the voltage increases, the insulating (depletion) region increases (or the opposite).
- **c) Schottky diode:** Normal diodes cannot respond quickly to the change of direction of the applied voltage at high frequency; to respond quickly, it is coated with platinum.
- **d) Photodiode:** Under reverse bias, like a light sensor, according to the intensity of the light; under normal bias, an ordinary diode.
- **e) LED diode:** A diode that emits light under forward bias; gallium arsenide; RGBY.

*Note: A Schottky diode is not a P-N diode "coated with platinum" but a diode with a metal–semiconductor junction; its speed is owed to the absence of minority carrier storage.*

### Resistor types

- **a) Carbon resistor:** Coded with color codes. Manufactured in ¼, ½, 1, 2, 3 W values; from 1 Ω to 22 MΩ. Resistance values change as they age.
- **b) Wire-wound resistor (ceramic/stone resistor):** Between 10 Ω and 100 kΩ, up to 30 W. The larger ones, those dissipating large power, heat up.
- **Integrated resistor:** use of multiple resistors as a single package.
- **SMD resistor:** easy use on PCB circuit boards.

**Adjustable resistors:**

- **1) Trimpot:** Low power, used in electronic circuits. Adjusted with a screwdriver; these are resistors that are left fixed after their resistance has been adjusted.
- **2) Potentiometer:** Generally used for voltage division and adjusting the output voltage; changed frequently in the circuit; generally used for volume adjustment. Types: linear, logarithmic and multi-turn potentiometer.
- **3) Rheostat:** Useful at high voltage, high current passes through it; controlled by hand.

**Variable resistors:**

- **Thermistor (NTC–PTC):** A resistor whose resistance value changes with temperature.
- **Varistor:** Its resistance value changes in inverse proportion to the voltage applied to its terminals. Generally used to prevent frequency drift, or in circuits that perform voltage clamping to protect against overvoltage.
- **Photoresistor (LDR):** Resistors that show high or low resistance according to the light falling on them: high resistance in the dark, low resistance in the light.

**Reading resistors:** The first two colors give the resistance value, the third gives the number of zeros, and the fourth gives the tolerance. Black 0, brown 1, red 2 … violet 7, gray 8, white 9.

### Resistor color code table

The table from a screenshot of a web page, taken together with the notes (source not stated, most likely the Turkish Wikipedia):

| Color | 1st band | 2nd band | 3rd band (multiplier) | 4th band (tolerance) | Temperature coefficient |
|---|---|---|---|---|---|
| Black | 0 | 0 | ×10⁰ | | |
| Brown | 1 | 1 | ×10¹ | ±1% (F) | 100 ppm |
| Red | 2 | 2 | ×10² | ±2% (G) | 50 ppm |
| Orange | 3 | 3 | ×10³ | | 15 ppm |
| Yellow | 4 | 4 | ×10⁴ | | 25 ppm |
| Green | 5 | 5 | ×10⁵ | ±0.5% (D) | |
| Blue | 6 | 6 | ×10⁶ | ±0.25% (C) | |
| Violet | 7 | 7 | ×10⁷ | ±0.1% (B) | |
| Gray | 8 | 8 | ×10⁸ | ±0.05% (A) | |
| White | 9 | 9 | ×10⁹ | | |
| Gold | | | ×10⁻¹ | ±5% (J) | |
| Silver | | | ×10⁻² | ±10% (K) | |
| None | | | | ±20% (M) | |

*Note: In the table in the screenshot, the header of the last column reads "Geçici Katsayı" ("transient coefficient"); the content is the temperature coefficient of the resistor.*

### Capacitor types

Classification: by dielectric type; by capacitance value (fixed and adjustable capacitors); by polarity (polarized and non-polarized).

- **By dielectric type:** vacuum, air, plastic film, mica, paper, glass, ceramic, aluminum electrolytic, tantalum, OS-CON, super and "gimmick" capacitors.
- **By capacitance value:** fixed capacitor and adjustable capacitor (variable, trimmer, varactor).
- **Variable capacitor:** high voltage, high frequency.
- **Trimmer:** low power; used in telecommunications.
- **Varactor:** high frequency; also used in telecommunications and frequency control.
