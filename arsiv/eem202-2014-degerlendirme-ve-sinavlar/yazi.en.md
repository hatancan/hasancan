---
baslik: EEM202 Circuit Theory II: 2013-2014 Spring Grading Criteria, Quiz III and Final Exam Solutions
ozet: EEM202 Circuit Theory II, 2013-2014 spring semester: grade distribution (quizzes, homework, midterm, final), the Quiz III questions of 16 May 2014, and solutions from a graded final exam answer sheet (rms power, Thevenin–Norton and maximum power, ideal transformer, three-phase system, circuit analysis with Laplace transforms).
---

This post brings together three documents from the 2013-2014 spring semester of the Başkent University Electrical-Electronics Engineering course **EEM202 Circuit Theory II**: the **grading** slide shown in class (18 February 2014), the **Quiz III** question sheet by Asst. Prof. Dr. Selda Güney (16 May 2014), and a **four-page exam answer sheet**, photographed at the end of the semester (13 June 2014), which the instructor graded in red pen. All were transcribed from photographed pages; the photographs themselves are not published, and the name and student-number information on the sheets was not carried into the text. There is no downloadable file for this post.

## Grading

The grade distribution on the slide shown in the first week of the semester:

| Component | Weight |
| --- | --- |
| Attendance | 3% |
| Quizzes | 15% |
| Homework | 7% |
| Midterm | 35% |
| Final | 40% |

Attendance requirement: **70%**.

## Quiz III (16.05.2014)

1. For the circuit in the figure below, calculate the value that the impedance Z₀ must have for maximum power to be transferred to it. (Circuit: a 30∠0° V (rms) source, a 15 Ω resistor, two inductors of j30 Ω and j15 Ω, with a mutual inductance of j18 Ω between them.)
1. In the following Y-Δ connected, positive-sequence (abc) circuit (source phases 1365∠0°, 1365∠−120° and 1365∠120° V; each line j2 Ω + 1.5 Ω; each branch of the delta load 85.5 Ω + j114 Ω), find the following:

- a) Calculate the line currents (I_aA, I_bB, I_cC) and the phase currents (I_AB, I_BC, I_CA).
- b) Calculate the complex power produced by the source per phase.
- c) Calculate what percentage of the real power produced by the source is dissipated in the load.

The answer key for this quiz, with its solutions, is in the archive post [Quiz Questions and Answer Keys](/arsiv/eem202-kisa-sinav-cozumleri/).

## Final exam: graded answer sheet

The sheet does not include the question texts; below, what each question asks has been inferred from the solution and written out, followed by the calculations and results on the answer sheet. The points in parentheses are those the instructor wrote on the sheet.

### Question 1: RMS value and power of a periodic voltage (20 points)

A voltage with period T = 10 s: v = −5t for 0 ≤ t ≤ 2 s, −10 V for 2–4 s, 0 for 4–5 s, and 10 V for 5–10 s. The average power dissipated in a resistor R = 2 Ω is P = V_rms²/R:

- V_rms = [ (1/10) ( ∫₀² 25t² dt + ∫₂⁴ 100 dt + ∫₅¹⁰ 100 dt ) ]^(1/2)
- = [ (1/10)(66.67 + 200 + 500) ]^(1/2) = √76.67 ≈ 8.76 V
- **P = 76.67/2 = 38.33 W**

### Question 2: Thevenin–Norton equivalent and maximum power (8 + 7 + 5 points)

A circuit consisting of a 100∠0° V (rms) source, two 5 Ω resistors, a −j5 Ω capacitor, a j5 Ω inductor, and a 0.1V_φ dependent current source:

- Open circuit: (V_φ − 100)/5 + V_φ/(j5) − 0.1V_φ = 0 → V_φ(0.5 − j) = 100 → V_φ = 40 + j80 V
- **V_Th** = 0.1V_φ(−j5) + V_φ = V_φ(1 − j0.5) = **80 + j60 V (rms)**
- Short circuit: V_φ = 100 V, I_N = 0.1V_φ + V_φ/(−j5) = (0.1 + j0.2)V_φ = **10 + j20 A (rms)**
- **Z_Th** = V_Th/I_N = (80 + j60)/(10 + j20) = **4 − j2 Ω**
- For maximum power, Z_L = Z_Th* = **4 + j2 Ω**

Continuing with the power in the load: I = (80 + j60)/8 = 10 + j7.5 A (rms), S = Z·|I|² = (4 + j2)(10 + j7.5)(10 − j7.5) = **625 + j312.5 VA**, that is, **P = 625 W**, **Q = 312.5 VAr**.

### Question 3: Circuit with an ideal transformer (10 + 5 + 5 points)

A 300 V source, 60 Ω in the primary, a 20 Ω resistor common to the primary and secondary loops, and 40 Ω in the secondary; for the ideal transformer V₂ = V₁/4 and I₂ = −4I₁:

- 300 = 60I₁ + V₁ + 20(I₁ − I₂), 0 = 20(I₂ − I₁) + V₂ + 40I₂
- Substituting: 300 = 160I₁ + V₁ and V₁ = 1040I₁
- **I₁ = 0.25 A, V₁ = 260 V, I₂ = −1 A, V₂ = 65 V**
- P₂₀ = (I₁ − I₂)²·20 = 1.25²·20 = **31.25 W**, P₄₀ = 1²·40 = **40 W**

### Question 4: Three-phase system (2 + 3 + 3 + 6 + 3 + 3 points)

Line voltage V_AB = 7200 V, line impedance 0.5 + j4 Ω, two balanced loads in parallel at the load (Z₁ and Z₂ = 207.36 + j60.48 Ω):

- V_AN = 7200/(√3∠−30°) = **4156.92∠30° V** (as written on the sheet)
- First load: S₁ (three-phase) = 691.2 − j201.6 kVA → per phase 230.4 − j67.2 kVA; θ = arctan(−201.6/691.2) = −16.26°, power factor 0.96 (leading). P₁ = V_AN·I₁·cos θ → 230.4·10³ = 4156.92·I₁·0.96 → **I₁ = 57.73∠46.26° A**
- Second load: I₂ = V_AN/Z₂ = 4156.92∠30° / 216∠16.26° = **19.2∠13.74° A**
- **I_aA** = I₁ + I₂ = 58.65 + j46.26 = **74.7∠38.26° A**; on the sheet I_bB = 74.7∠158.26° A, I_cC = 74.7∠−81.73° A
- V_an = (0.5 + j4)(58.65 + j46.26) + V_AN = 3444.28 + j2336.24 = **4161.72∠34.14° V**
- On the sheet V_ab = 7208.3∠64.14° V, V_bc = 7208.3∠124.14° V, V_ca = 7208.3∠−115.86° V

*Note: Since the question text is not available, the phase sequence is unknown. The relation V_AN = V_AB/√3∠+30° on the sheet and I_bB leading I_aA by 120° are consistent with a negative (acb) sequence; in that case V_ab = √3·V_an∠−30° = 7208.3∠4.14° V would be expected. If V_ab = 7208.3∠64.14° V on the sheet was obtained with the positive-sequence ∠+30° relation, the angles of V_bc and V_ca (124.14° and −115.86°) are also not consistent with either phase sequence (the line voltages should be 120° apart). The magnitudes of the currents and voltages are correct.*

### Question 5: Circuit analysis with the Laplace transform (5 + 5 + 5 + 5 points)

The circuit in the s-domain: a 1/s capacitor (C = 1 F) and a 2 Ω resistor, a 2/s A current source, an s inductor (L = 1 H), a 12/s V voltage source, and a 2 Ω output resistor. With mesh currents I₁ and I₂:

- I₁(2 + 1/s) = V₁, V₁ + (2 + s)I₂ + 12/s = 0, and from the current source I₁ − I₂ = 2/s
- I₁(s² + 4s + 1) = 2s + 16 → I₁ = (2s + 16)/(s² + 4s + 1); roots s = −0.27 and s = −3.73
- I₂ = I₁ − 2/s = K₁/(s + 0.27) + K₂/(s + 3.73) − 2/s; K₁ = 15.46/3.46 = 4.46, K₂ = 8.54/(−3.46) = −2.46
- V_o = 2I₂ = 8.92/(s + 0.27) − 4.92/(s + 3.73) − 4/s
- **v_o(t) = [−4 + 8.92e^(−0.27t) − 4.92e^(−3.73t)] u(t) V**

Check: v_o(0⁺) = −4 + 8.92 − 4.92 = 0 and v_o(∞) = −4 V.
