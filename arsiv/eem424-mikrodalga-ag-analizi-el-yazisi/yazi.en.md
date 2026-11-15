---
baslik: EEM424 Microwave Theory: Microwave Network Analysis Lecture Notes (Z, Y, S and ABCD Matrices, 3 dB Attenuator Example)
ozet: Transcription of handwritten notes from the EEM424 course: impedance and admittance matrices, lossless networks, the scattering (S) matrix, an example of a T-type 3 dB attenuator with 8.56 ohm - 141.8 ohm - 8.56 ohm, and the transmission (ABCD) matrix.
---

This post is a text transcription of 19 pages of handwritten notes I took in May 2015 in the **EEM424 Microwave Theory** course (Prof. Dr. S. Gökhun Tanyer, topic: *microwave network analysis*). The notes were mostly written in English; the explanations have been translated into Turkish here. The photographed pages have not been published.

## 1. Impedance matrix: V = Z·I

With the vectors V = [V1, V2, …]ᵀ and I = [I1, I2, …]ᵀ, V = Z·I (and I = Y·V).

**Question:** Only I_j is given as a source, and there are no sources at the other ports (I_k = 0, k ≠ j). The observation is V_i:

Z_ij = V_i / I_j |_{I_k = 0, k ≠ j}   (source: I_j, observation: V_i)

**Example (T network).** For a two-port network with series arms Z_A and Z_B and a common (shunt) arm Z_C:
- Z11 = V1/I1 |_{I2=0} = Z_A + Z_C,
- Z22 = Z_B + Z_C,
- Z21 = V2/I1 |_{I2=0}: V2 = I1·Z_C ⇒ Z21 = Z_C (the same result is also obtained with V2 = V1·Z_C/(Z_B + Z_C) and I1 = V1/(Z_A + Z_C)),
- Z12 = V1/I2 |_{I1=0} = Z_C.

Therefore Z12 = Z21: a **reciprocal network**; similarly Y_ij = Y_ji. In matrix form:

[V1; V2] = [[Z_A + Z_C, Z_C]; [Z_C, Z_B + Z_C]] · [I1; I2]

**Lossless network:** Re{Z_mn} = 0 (for all m, n); that is, the Z_ij are purely imaginary.

## 2. Admittance matrix

Y_ij = I_i / V_j |_{V_k = 0, k ≠ j} (source/input: V_j, observation: I_i). Example: in the same T network, Y12 = I1/V2 |_{V1=0}: I1 = V2 · (Z_A ∥ Z_C)/(Z_B + (Z_A ∥ Z_C)); hence Y12 = (Z_A ∥ Z_C)/(Z_B + (Z_A ∥ Z_C)) (this is how it is written in the notebook; in terms of units, an additional 1/Z factor is needed for this expression to correspond to an admittance). The relationship between the Z and Y matrices, [Y] = [Z]⁻¹, was left as homework.

## 3. Scattering matrix

[V⁻] = S·[V⁺]: observation V_i⁻ (outgoing wave), input V_j⁺ (incident wave):

S_ij = V_i⁻ / V_j⁺ |_{V_k⁺ = 0, k ≠ j}

*Question:* How is V_k⁺ = 0 (k ≠ j) achieved? *Answer:* By connecting a **matched load** to the ports with k ≠ j.

### Example: T-type attenuator (R_A, R_B, R_C, 50 Ω line)

Between port 1 and port 2 there are R_A (series), R_B (series), and R_C (shunt) in the middle; the lines connected to the ports are 50 Ω.

- **S11** = V1⁻/V1⁺ |_{V2⁺=0}: with a 50 Ω load at port 2, the input impedance is Z_in^(1) = R_A + R_C ∥ (R_B + 50) = R_A + R_C(R_B + 50)/(R_C + R_B + 50). S11 = Γ^(1) = (Z_in^(1) − Z0)/(Z_in^(1) + Z0). If Z_in^(1) = 50 Ω, then **S11 = 0**.
- Given values: **R_A = R_B = 8.56 Ω, R_C = 141.8 Ω**; with these values Z_in = 8.56 + 141.8 ∥ 58.56 = 8.56 + 41.44 ≈ 50 Ω, i.e. S11 = 0 (S22 = 0 by symmetry).
- **S12 = ?** S12 = V1⁻/V2⁺ |_{V1⁺=0}; due to symmetry (reciprocal network), S12 = S21.
- **S21** = V2⁻/V1⁺ |_{V2⁺=0}. Since S11 = S22 = 0 and port 2 is terminated with a matched load, V1 = V1⁺ (V1⁻ = 0) and V2 = V2⁻ (V2⁺ = 0). With the divider relation:

V2⁻ = V2 = V1 · [R_C ∥ (R_B + 50) / (R_A + R_C ∥ (R_B + 50))] · [50/(50 + R_B)]

With numerical values = V1⁺ · [141.8 ∥ (8.56 + 50) / (8.56 + 141.8 ∥ (8.56 + 50))] · [50/(50 + 8.56)] = **0.707·V1⁺** ⇒ **S21 = S12 = 0.707**.

**Power calculation.** For the V1⁺ input only, P_in = ½·|V1⁺|²/Z0 and P_out = ½·|V2⁻|²/Z0; since V2⁻ = S21·V1⁺, P_out = ½·S21²·|V1⁺|²/Z0. Hence

P_out / P_in = S21² = 1/2 ⇒ **S21 = −3 dB**.

That is, this network is a **3 dB attenuator (pad)**: half of the input power is transmitted to the output, and it is matched at both ports.

## 4. Transmission (ABCD) matrix

For a two-port network: V1 = A·V2 + B·I2 and I1 = C·V2 + D·I2, i.e. [V1; I1] = [[A, B]; [C, D]] · [V2; I2].

**Question:** If two networks are connected successively as 1–2–3, what is the relationship between 1 and 3? Answer: since [V1; I1] = M1·[V2; I2] and [V2; I2] = M2·[V3; I3], we have **[V1; I1] = M1·M2·[V3; I3]**: in a cascade (chain) connection of networks, the ABCD matrices are multiplied.

**Examples.**
- *Series impedance Z:* For A, I2 = 0 (open circuit): V1 = V2 ⇒ A = 1. For B, V2 = 0 (short circuit): V1 = Z·I2 ⇒ B = Z. For C, I2 = 0: I1 = 0 ⇒ C = 0. For D, V2 = 0: I1 = I2 ⇒ D = 1. Result: [[1, Z], [0, 1]].
- *Homework:* the ABCD matrix for a shunt admittance Y.
- *Homework:* the ABCD matrix of a transmission line section of length ℓ, characteristic impedance Z0, and propagation constant β.

*Note: In the handwritten notes, the formulas of the Y matrix example were written in abbreviated form; the Z and Y relations above have been rearranged according to the standard definitions in the textbook.*
