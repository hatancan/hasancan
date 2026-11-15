---
baslik: EEM202 Circuit Theory II: 2004-2005 Spring Midterm Exam Questions and Answers
ozet: EEM202 Circuit Theory II 2004-2005 spring midterm exam and the instructors' answer key: Thevenin equivalent for maximum power in a circuit with an ideal transformer, power in a transmission line and power compensation, Y-Δ three-phase system, superposition in a circuit with mutual inductance.
---

This post contains the question sheets and the answer key titled "ANSWERS" for the **2004-2005 Spring semester midterm exam** of **EEM 202 Circuit Theory-II** at Başkent University, Department of Electrical and Electronics Engineering. The exam was prepared by Prof. Dr. Turhan Çiftçibaşı and Lecturer Mustafa Doğan. The documents in the archive are photographs of the papers; under each question, the question text and the main results from the answer key have been transcribed. Grading: Questions 1 and 2 are worth twenty points each, Questions 3 and 4 thirty points each (100 in total). The photographs themselves are kept in the archive and are not published.

## Question 1: Thevenin equivalent and maximum power with an ideal transformer (20 points)

Find the **Thévenin** equivalent seen from terminals a-b of the amplifier circuit below. When an **ideal transformer** is connected to the output of this equivalent circuit as shown in the figure, what must Z_y be so that **maximum power** is drawn from the amplifier circuit? V_s(t) = 10 cos(10000t + 53.13°) is given. (Take cos 53.13° ≅ 0.6 and sin 53.13° ≅ 0.8.)

The circuit contains a 200 µH inductor, a 25 µF capacitor, a 2 Ω resistor, a (3/2)i dependent current source, and a 1:5 ideal transformer.

- V_s = 10e^(j53.13°) = 10(0.6 + j0.8) = **6 + j8**; inductor j2 Ω, capacitor −j4 Ω
- Nodal equation at node d for V_oc (V_d = V_oc): V_oc/(−j4) + (V_oc − V_s)/(j2) − (3/2)[(V_oc − V_s)/(j2)] = 0 → **V_oc = 3 + j4 = 5e^(j53.13°) V**
- For I_sc (since the circuit contains a dependent source): V_d/2 + V_d/(−j4) + (V_d − V_s)/(j2) − (3/2)[(V_d − V_s)/(j2)] = 0 → V_d = (3 + j4)/(1 − j), I_sc = V_d/2 = (3 + j4)/(2 − j2)
- **Z_th = V_oc/I_sc = 2 − j2 Ω**
- For maximum power transfer: Z_y′ = Z_th* = 2 + j2 = (1/5)²·Z_y → **Z_y = 50 + j50 Ω**

## Question 2: Transmission line and power compensation (20 points)

For the circuit below (f = 60 Hz, 465 V-rms generator, Z_line = 4 + j3 Ω, Z_load = 120 + j90 Ω):

1. Find the output voltage (V_load), the transmission line current (I_line), and the corresponding complex powers (S_line, S_load).
1. Find the capacitance that must be connected in parallel with the load to make the phase angle at the load zero (power compensation), C = ? (Hint: Z′_load = Z_C ∥ Z_load; when the capacitor is included, Z′_load must be a real number.)
1. With the capacitor found connected, find again the new load impedance (Z′_load), and accordingly the transmission line current (I′_line) and the output voltage (V′_load).

a)

- V_load = (120 + j90)/(124 + j93)·465 = 150e^(j36.9°)/155e^(j36.9°)·465 = **450 V-rms**
- I_line = 465/155e^(j36.9°) = **3e^(−j36.9°) A-rms**
- S_line = |I_line|²·Z_line = 3²(4 + j3) = **36 + j27 VA**
- S_load = V_load·I_line* = 450·3e^(j36.9°) = 1350e^(j36.9°) = **1080 + j810 VA**

b) Z′_load = Z_C ∥ Z_load, Y′_load = Y_C + Y_load. Since Z′_load and Y′_load are real, |Y_C| = |Im{Y_load}| must hold:

- Y_load = 1/(120 + j90) = 1/(30(4 + j3)) = (4 − j3)/750 = 4/750 − j·3/750
- 2πfC = |Im{Y_load}| = 3/750 → C = 3/(750·2π·60) → **C = 10.61 µF**

c)

- Z′_load = 1/Y′_load = 750/4 = **187.5 Ω**
- I′_line = 465/(191.5 + j3) = 465/191.5e^(j0.9°) = **2.43e^(−j0.9°) A-rms**
- V′_load = I′_line·Z′_load = 2.43e^(−j0.9°)·187.5 = **455.6e^(−j0.9°) V**

*Note: 465·187.5/191.52 ≈ 455.3 V; the 455.6 V in the answer is a small difference caused by rounding the current to 2.43.*

## Question 3: Y-Δ three-phase system (30 points)

The 3-phase, positive-sequence, Y (wye)-connected generator (source) below is connected through a transmission line to a Δ (delta)-connected balanced load. In the single-phase equivalent, V_a = 120 V-rms and Z_line = 0.5 + j1.4 Ω.

1. Find the Y (wye) equivalent of the balanced Δ (delta) load, Z_Y = ?
1. Find the line currents (I_aA, I_bB, I_cC).
1. Find the phase voltages (V_AB, V_BC, V_CA) and currents (I_AB, I_BC, I_CA) across the load (V_AN will be found first).
1. Find the line voltages at the generator (V_ab, V_bc, V_ca) (V_an will be found first).
1. Find the total real power dissipated by the load (P_T).

- a) Z_Y = Z_Δ/3 = **39.5 + j28.6 = 48.77e^(j35.91°) Ω**
- b) I_aA = 120/(Z_line + Z_Y) = 120/(40 + j30) = **2.4e^(−j36.87°) A-rms**; I_bB = 2.4e^(−j156.87°), I_cC = 2.4e^(j83.13°) A-rms
- c) V_AN = I_aA·Z_Y = 2.4e^(−j36.87°)(39.5 + j28.6) = **117.04e^(−j0.96°) V-rms**
- V_AB = √3e^(j30°)·V_AN = **202.72e^(j29.04°) V-rms**, V_BC = 202.72e^(−j90.96°), V_CA = 202.72e^(j149.04°) V-rms
- I_AB = (1/√3)e^(j30°)·I_aA = **1.39e^(−j6.87°) A-rms**, I_BC = 1.39e^(−j126.87°), I_CA = 1.39e^(j113.13°) A-rms
- Check: I_AB = V_AB/Z_Δ = 202.72e^(j29.04°)/(118.5 + j85.8) = 202.72e^(j29.04°)/146.3e^(j35.91°) = 1.39e^(−j6.87°).

- d) V_an = 120 V-rms; V_ab = √3e^(j30°)·V_an = 120√3e^(j30°) = **207.85e^(j30°)**, V_bc = 207.85e^(−j90°), V_ca = 207.85e^(j150°)
- e) For the load, S_T = P_T + jQ_T and Q_T = P_T·tan θ (θ = θ_VAN − θ_IaA)
- P_T = 3|V_AN||I_aA| cos(θ_VAN − θ_IaA) = 3·117.04·2.4·cos(−0.96° + 36.87°) = 3·117.04·2.4·cos(35.91°)
- **P_T = 682.53 W**, Q = P_T·tan(35.91°) = 494.25 VAR → **S = (682.53 + j494.25) VA**

## Question 4: Superposition (30 points)

Find the instantaneous value of the voltage across the capacitor (V_c(t)) in the circuit below using the superposition method. The circuit contains 5 cos(2t) and 3 sin(0.5t) sources, a 0.5 F capacitor, 4 H and 6 H inductors, and 2 H of mutual inductance between them.

For ω = 2 (capacitor −j Ω, inductors j8 and j12 Ω, mutual inductance j4 Ω):

- V_L1 = j8(I₁ − I₂) − j4I₂, V_L2 = j12I₂ − j4(I₁ − I₂)
- Mesh 1: −5 + (−j)I₁ + V_L1 = 0; mesh 2: −V_L1 + V_L2 = 0 → I₂ = (3/7)I₁
- I₁ = −j(35/13), I₂ = −j(15/13)
- V_C1 = (−j)·I₁ = −35/13 → **v_C1(t) = (35/13) cos(2t + 180°)**

For ω = 0.5 (capacitor −j4 Ω, inductors j2 and j3 Ω, mutual inductance j1 Ω):

- V_L1 = j2(I₁ − I₂) − jI₂, V_L2 = j3I₂ − j(I₁ − I₂)
- Mesh 1: (−j4)I₁ + V_L1 = 0 → I₂ = −(2/3)I₁; mesh 2: −V_L1 + V_L2 − 3j = 0
- I₁ = −9/23, I₂ = 6/23
- V_C2 = (−j4)I₁ = j(36/23) = (36/23)e^(j90°) → **v_C2(t) = (36/23) cos(0.5t + 90°)**

Result:

**V_c(t) = v_C1(t) + v_C2(t) = (35/13) cos(2t + 180°) + (36/23) cos(0.5t + 90°)**
