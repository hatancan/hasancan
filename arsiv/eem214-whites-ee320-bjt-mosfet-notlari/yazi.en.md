---
baslik: EEM214 Electronics I: BJT and MOSFET Lecture Notes – NPN Operation, MOSFET DC Analysis, Small-Signal Models, Current Mirrors (Keith W. Whites, EE 320, 2009)
ozet: Six lecture notes from Keith W. Whites' EE 320 Electronics I course: BJT construction and the physical operation of the NPN, MOSFET symbols and i_D–v_DS regions, MOSFET DC circuit design examples, the MOSFET amplifier and small-signal π model, worked amplifier examples, biasing in discrete and integrated circuits, and the MOSFET current mirror.
---

This post presents six transistor-related lecture notes (Lecture 10 and 26–30) from the EEM214 Electronics I course folder, taken from the English-language lecture notes that **Keith W. Whites** (South Dakota School of Mines and Technology) prepared for his **EE 320 Electronics I** course in fall 2009. The notes follow Sedra & Smith's *Microelectronic Circuits*. Below, the main ideas of each lecture and the results of the worked examples are summarized in English; the PDFs can be downloaded as a ZIP at the end of the post. For the same author's diode notes, see: [Whites EE 320 diode notes](/arsiv/eem214-whites-ee320-diyot-notlari/).

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed upon request by the rights holder.*

## Lecture 10: BJT Construction, NPN Physical Operation

A transistor is a three-terminal device; the current or voltage at one terminal controls the current between the other two terminals (an "electronic valve"). There are two main families: BJT and FET (the course devotes about 13 lectures to BJTs and 12 lectures to FETs). A BJT consists of three doped regions on silicon (npn or pnp) and contains two back-to-back pn junctions: the **emitter–base junction (EBJ)** and the **collector–base junction (CBJ)**. This construction goes back to William Shockley's US patent (2,569,347). Although the structure looks symmetric, it is not (the junction areas and doping levels differ), so the reverse active mode is not the same as simply swapping the collector and emitter. Depending on the state of the junctions there are four modes: cutoff, active, saturation, and reverse active. In digital circuits the transistor is switched between cutoff and saturation, while in linear amplifiers it operates in the active region. The note ends with a description of the physical operation of the npn transistor in active mode.

## Lecture 26: MOSFET Circuit Symbols, i_D–v_DS Characteristics

In the symbol of the enhancement-mode n-channel MOSFET, the terminal with the arrow is the source, and the direction of the arrow indicates n-type; the gap at the gate represents the oxide layer. The body is usually connected to the source, so a simpler symbol is common. The three operating regions:

1. **Cutoff:** v_GS < V_t, no channel, i_D = 0.
1. **Triode:** v_GS > V_t and the channel is continuous at the drain end as well (v_GD > V_t, i.e., v_DS < v_GS − V_t): i_D = k_n′(W/L)[(v_GS − V_t)v_DS − v_DS²/2]; for small v_DS, i_D ≈ k_n′(W/L)(v_GS − V_t)v_DS = v_DS / r_DS, i.e., a voltage-controlled resistor.
1. **Saturation:** the channel is pinched off at the drain end (v_GD ≤ V_t): i_D = ½k_n′(W/L)(v_GS − V_t)²; the device behaves like an ideal voltage-controlled current source.

## Lecture 27: MOSFET Circuits at DC

- **Example N27.1:** Design for I_D = 0.4 mA and V_D = 1 V (V_t = 2 V, µ_nC_ox = 20 µA/V², W/L = 400/10). Since V_GD = −1 V < V_t, saturation is assumed; the appropriate root of (V_GS − 2)² = 1 gives **V_GS = 3 V**, V_S = −3 V, and with respect to the −5 V supply R_S = (−3 + 5)/0.4 mA = 5 kΩ.
- **Example N27.2:** For a MOSFET whose gate is connected to its drain, V_GD = 0 < V_t, so it is in saturation: (V_GS − 2)² = 4 ⇒ **V_GS = 4 V**, V_D = 4 V.
- **Example N27.3:** Design for V_D = 0.1 V (V_t = 1 V, k_n′W/L = 1 mA/V²); with V_GS = 5 V the channel is not pinched off at the drain, so the device is in the triode region; r_DS is calculated.

## Lecture 28: MOSFET as an Amplifier, Small-Signal Equivalent Circuit Models

In the "conceptual" MOSFET amplifier (biased with V_GS and R_D), the device is biased in saturation, and v_GD ≤ V_t must hold over the entire signal swing. When v_gs is added at the gate, the v_gs² term in the expansion i_D = ½k_n′(W/L)[(V_GS − V_t) + v_gs]² is nonlinear and therefore must remain small: v_gs << 2(V_GS − V_t). Under this condition, the AC component of the current is i_d = g_m·v_gs, with **g_m = k_n′(W/L)(V_GS − V_t)** (in terms of the overdrive voltage V_OV, g_m = 2I_D/V_OV), and the gain is A_v ∝ g_m. In saturation the MOSFET is a voltage-controlled current source; the small-signal π model (open-circuit gate, a g_m·v_gs current source at the drain in parallel with r_o = V_A/I_D) and the T model are introduced.

## Lecture 29: MOSFET Small-Signal Amplifier Examples

**Example N29.1:** An amplifier with 10 MΩ feedback from drain to gate (V_t = 1.5 V, k_n′W/L = 0.25 mA/V², V_A = 50 V, V_DD = 15 V, R_D = 10 kΩ). Since V_GS = V_DS, I_D = 1.25×10⁻⁴(15 − 10000·I_D − 1.5)²; of the two roots, the physical one is **I_D = 1.06 mA, V_GS = V_DS = 4.4 V**. g_m = 0.25 mA/V² × (4.4 − 1.5) = 0.725 mS; with r_o ∥ R_D ∥ R_L ≈ 4521 Ω, **A_v ≈ −3.28 V/V**; the input resistance is then calculated by finding i_i in terms of v_i, rather than by setting v_gs = 0.

## Lecture 30: Biasing MOSFET Amplifiers, MOSFET Current Mirrors

In discrete circuits, biasing is done with methods similar to those used for BJTs; in integrated circuits, DC current sources are used because resistors and large capacitors are expensive.

- **Example N30.1:** I_D = 1 mA, ±2 V drain swing, and 1 MΩ input resistance (k_n′W/L = 0.5 mA/V², V_t = 2 V). To maximize gain, V_D = 0 is chosen; since V_GD,min = −2 V < V_t, saturation is maintained throughout the swing. V_G = 0, V_GS = 4 V, V_S = −4 V, and R_G = 1 MΩ.
- **MOSFET current mirror:** Q1, whose gate is connected to its drain, operates in saturation; I_REF determines its V_GS. The current of Q2, which shares the same V_GS, is I_O = I_REF·(W/L)₂/(W/L)₁; in integrated circuits, a single "golden current" is copied to many stages in this way.

## Download

The ZIP file contains the original PDFs of the six lecture notes (320Lecture10 and 320Lecture26–30).
