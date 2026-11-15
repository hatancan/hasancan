---
baslik: EEM214 Electronics I: Diode, Semiconductor, FET and BJT Homework Questions
ozet: Two handwritten homework sets: ideal diode circuits, carrier concentrations and current density; MOSFET sizing, BJT biasing and the hybrid-π small-signal model.
---

This post contains two handwritten homework sets from the EEM214 Electronics I folder. The authors are not named. The first set was transcribed from four images; the images are kept in a private archive. The second set is a four-page PDF titled **Homework 2 – Field-Effect Transistors / Bipolar Junction Transistors**, scanned on 29 April 2010, and it can be downloaded at the end of the post. The documents are problem sheets; they do not include a solution key.

## First homework: Diode circuits

### Question 1: Battery and ideal diode

An AA flashlight cell has a Thévenin equivalent of a 1.5 V source and a 1 Ω resistance. It is connected to an ideal diode. Describe the two possible cases and determine diode current and terminal voltage when the positive battery terminal is connected to (a) the cathode, (b) the anode.

### Question 2: Four series connections

For each circuit between +5 V and −5 V, determine the indicated current I and midpoint voltage V. The current reference is downward.

| Circuit | Upper element | Lower element |
|---|---|---|
| 1 | 10 kΩ resistor | Diode with anode at V, cathode at −5 V |
| 2 | 10 kΩ resistor | Diode with cathode at V, anode at −5 V |
| 3 | Diode with anode at +5 V, cathode at V | 10 kΩ resistor |
| 4 | Diode with cathode at +5 V, anode at V | Resistor; value not repeated in the drawing |

*Note: Although the source says "ideal diode," the accompanying characteristic is drawn with a 0.7 V turn-on threshold. These are different models; the assumption used should be stated when solving the problem.*

### Question 3: Diode logic gate

Three inputs V_a, V_b and V_c feed the common output V_y through three diodes; each anode is at its input and each cathode at the output. A resistor R connects V_y to ground. Assume ideal diodes and input levels of 0 and 5 V. Find a suitable R so that the current required from each input source does not exceed **0.2 mA**.

### Question 4: DC circuits with two diodes

Find the labelled current I and voltage V. A common upper node is connected through a resistor to +10 V. One diode leads downward from that node to ground; a second downward diode leads to V, which connects through a resistor to −10 V.

- First circuit: upper resistor 5 kΩ, lower resistor 10 kΩ.
- Second circuit: upper resistor 10 kΩ, lower resistor 5 kΩ.
- I is the downward current in the diode ending at ground.

The source again labels the diodes "ideal" while drawing a 0.7 V turn-on characteristic.

### Question 5: Solution using Thévenin's theorem

Assuming ideal diodes, use Thévenin's theorem to simplify each circuit and find the labelled current and voltage.

- First circuit: a 15 V supply feeds a 10 kΩ/20 kΩ divider. Its midpoint drives a forward-pointing diode to output V, which has a 20 kΩ load to ground. I is directed from the divider to the output.
- Second circuit: the left divider is 10 kΩ/10 kΩ across 15 V; the right divider is 10 kΩ/10 kΩ across 10 V. A diode connects their midpoints with its anode on the right, cathode on the left. I points left; diode voltage V is positive on the right.

### Question 6: Definition of a diode

What is a "diode"?

## First homework: Carriers and current density

### Question 7: Drift field

A current density of **10,000 A/cm²** exists in n-type silicon with resistivity **0.01 Ω·cm**. What electric field supports this drift current density?

### Question 8: Maximum drift current

The maximum carrier drift velocity in silicon is approximately **10⁷ cm/s**. Find the maximum drift current density for n-type silicon doped at **10¹⁶ cm⁻³**.

### Question 9: Compensated semiconductor

A semiconductor has N_D = 10¹⁶ cm⁻³, N_A = 4×10¹⁶ cm⁻³ and n_i = 10¹¹ cm⁻³. Find the electron and hole concentrations.

### Question 10: Boron doping

Silicon is doped with **5×10¹⁸ boron atoms/cm³**. Determine whether it is n-type or p-type; find hole and electron concentrations at room temperature and at **200 K**.

### Question 11: Equal donor and acceptor doping

A silicon sample is doped with **5.0×10¹⁹ donor atoms/cm³** and **5.0×10¹⁹ acceptor atoms/cm³**. Find its resistivity. Is it intrinsic material? Explain.

### Question 12: Indium doping

Silicon is doped with an indium concentration of **7×10¹⁹ cm⁻³**. Is indium a donor or acceptor impurity? At **300 K**, find electron and hole concentrations, electron and hole mobilities and resistivity. Identify the conductivity type.

### Question 13: Electron diffusion

The electron concentration falls from **n(0) = 10¹⁸ cm⁻³** to zero at **W_B = 2 µm**. The graph joins these endpoints with a descending line. If μ_n = **350 cm²/(V·s)**, determine electron diffusion current density at room temperature.

### Question 14: Drift and diffusion components

In a **3 µm** silicon region, concentrations vary along the drawn straight lines:

- p(0) = 1.01×10¹⁸ cm⁻³, p(3 µm) = 10¹⁸ cm⁻³.
- n(0) = 10¹⁶ cm⁻³, n(3 µm) = 10¹⁴ cm⁻³.
- Electric field magnitude is **25 V/cm**, directed toward decreasing x.
- μ_n = 350 cm²/(V·s), μ_p = 150 cm²/(V·s).

Find total current density at x = 0. Find each electron and hole drift and diffusion component at x = 1.5 µm.

## Second homework: Field-Effect Transistors

### Question 1: Two-terminal characteristic of a depletion NMOS

Neglect channel-length modulation. For the drawn depletion NMOS connection, show that:

- i = ½ k′_n(W/L)(v² − 2V_t v), for v ≥ V_t.
- i = −½ k′_n(W/L)V_t², for v < V_t.

Recall that V_t is negative. Sketch i–v for **V_t = −2 V** and **k′_n(W/L) = 2 mA/V²**.

### Question 2: PMOS sizing

The PMOS has **V_t = −2 V**, **μ_p C_ox = 8 µA/V²**, **L = 10 µm** and **λ = 0**. The source is at +10 V; the gate and drain are joined at output V_D, which connects through R to ground. Find **W and R** to establish **I = 0.1 mA** and **V_D = 7 V**.

![Depletion NMOS characteristic and diode-connected PMOS sizing questions](odev2-1.jpg "Homework 2: Questions 1–2")

### Question 3: Level setting with two NMOS devices

The devices have **V_t = 2 V**, **μ_n C_ox = 20 µA/V²**, **λ = 0**, and **L₁ = L₂ = 10 µm**. Two diode-connected NMOS devices are stacked between ground and a resistor from +10 V. Their nodes are **+3 V** and **+7 V**; current through R is **0.2 mA**. Find each gate width and R.

### Question 4: Current-mirror circuits

For the devices in the two circuits, **|V_t| = 1 V**, **λ = 0**, **γ = 0**, **μ_n C_ox = 20 µA/V²**, **L = 1 µm**, **W = 20 µm**. Find labelled currents and voltages in the two **+5 V** circuits.

![Level setting with two diode-connected NMOS devices and two current-mirror circuits](odev2-2.jpg "Homework 2: Questions 3–4; connections are as in the source drawing")

## Second homework: Bipolar Junction Transistors

### Question 5: V_BE and current

An npn transistor has **V_BE = 0.8 V** at **I_C = 1 A**. What V_BE is expected at I_C = 10 mA and I_C = 5 A?

### Question 6: Voltage divider design

The base voltage is obtained from a divider across **9 V**. Initially assume very large β and ignore base current. Design **V_B = 3 V** with **0.2 mA** in the divider. Then, for **β = 100**, analyze the circuit to find collector current and collector voltage. Both collector and emitter resistors are **1 kΩ**.

### Question 7: Biasing with a current source

An amplifier has a very high β and a **1 mA emitter current source**, a **2 kΩ collector resistor** and **+5 V supply**. Find the DC collector voltage and g_m. Replace the transistor with its simplified hybrid-π model; replace the DC current source with an open circuit for small-signal analysis. Find v_c/v_i.

![Variation of V_BE with BJT current, divider biasing and current-source amplifier](odev2-3.jpg "Homework 2: Questions 5–7")

### Question 8: Common-emitter with source and load effects

Given **V_CC = 9 V, R₁ = 27 kΩ, R₂ = 15 kΩ, R_E = 1.2 kΩ, R_C = 2.2 kΩ, β = 100 and V_A = 100 V**, calculate the DC base current I_B. The amplifier operates between a source with **R_S = 10 kΩ** and a **2 kΩ load**. Replace the transistor with its hybrid-π model and find input resistance R_i, voltage gain v_o/v_s and current gain i_o/i_i. The emitter by-pass and input/output coupling capacitors are marked as very large.

![Common-emitter amplifier with source resistance and load, 9 volt supply](odev2-4.jpg "Homework 2: Question 8")
