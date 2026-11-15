---
baslik: EEM323 Electromagnetics II: Solved Transmission Line Examples (Standing Wave Ratio, Load Impedance, Line Input)
ozet: EEM323 handwritten solved transmission line examples: finding the reflection coefficient and load impedance from the standing wave ratio and successive voltage minima, λ/4 matching; λ/8 line, input impedance, load voltage and power calculation.
---

This post is a text transcription of a 4-page handwritten set of **transmission line examples** from the EEM323 Electromagnetics II course (the author and date are not given in the document); the pages were transcribed from photographed/scanned paper, and the images are not published. The measured Zin values were recalculated and verified.

## Example 1: Unknown Load, Standing Wave Ratio

**Problem.** On a lossless 50 Ω transmission line terminated with an unknown load, the standing wave voltage ratio is measured as 3. The distance between successive voltage minima is 20 cm, and the first voltage minimum is 5 cm from the load. (a) Find the reflection coefficient Γ, (b) find the load impedance Z_L. (c) Find the load resistance and line length that make the input impedance of the line equal to Z_L.

**(a)** The distance between two minima is half a wavelength: λ = 2 × 0.2 = 0.4 m, β = 2π/λ = 5π rad/m. Since S = 3, |Γ| = (S−1)/(S+1) = 2/4 = 1/2. At the first voltage minimum, θ_L − 2β·d_min = −π must hold; hence θ_L = 2 × 5π × 0.05 − π = −0.5π rad. Therefore Γ = 0.5 e^(−j0.5π) = −j0.5.

**(b)** Z_L = 50 (1 − j0.5)/(1 + j0.5) = 50 (0.60 − j0.80) = **30 − j40 Ω**.

**(c)** Required: Z_in = 30 − j40 seen at the input of the line. The line is built, starting from a voltage minimum point, from a line of Z₀ = 50 Ω and length l_m, terminated by a resistor R_m:

30 − j40 = 50 (R_m + j50 tan βl_m) / (50 + jR_m tan βl_m)

If a voltage minimum is assumed at the load, then d_min + l_m = λ/2 and R_m = R₀/S: l_m = λ/2 − d_min = 0.2 − 0.05 = **0.15 m**, R_m = 50/3 ≈ **16.7 Ω**.

If a voltage maximum is assumed at the load (d_min + l_m = λ/4 = 0.1): R_m = R₀·S = 50·3 = **150 Ω**, l_m = 0.1 − 0.05 = **0.05 m**. Check: βl_m = 5π × 0.05 = π/4, tan π/4 = 1,

Z_in = 50 (150 + j50)/(50 + j150) = 50 (3 + j)/(1 + j3) = 50 (3 + j)(1 − j3)/10 = 50 (6 − j8)/10 = 30 − j40 Ω.

The required value is obtained. The solution is not unique: if n·λ/2 is added to the lengths, the impedance repeats itself. (If the length comes out as zero, a positive length can be obtained by taking λ/4 + λ/2.)

## Example 2: λ/8 Line, R ∥ L Load

**Problem.** A source with V_s = 1·cos ωt (ω = 2π × 10⁶ rad/s) and internal impedance Z_s = 100 Ω feeds a transmission line with characteristic impedance Z₀ = 100 Ω and length l = λ/8. The line is terminated with a parallel R = 100 Ω and L = 16 µH. What are (a) Z_in, (b) V_in, (c) V_L, (d) the power dissipated in R?

**Solution.** jX_L = jωL = j(2π·10⁶)(16·10⁻⁶) ≈ j100 Ω. Load: Z_L = 100·(j100)/(100 + j100) = 50(1 + j) = 50 + j50 Ω. βl = (2π/λ)(λ/8) = π/4.

**(a)** Z_in = Z₀ (Z_L + jZ₀ tan βl)/(Z₀ + jZ_L tan βl) = 100 [(1+j) + j2] / [2 + j(1+j)] = 100 (1 + j3)/(1 + j) = **100 (2 + j) Ω**.

**(b)** V_in = Z_in/(Z_in + Z_s) · V_s = 100(2+j) / (100(2+j) + 100) ≈ 0.7 + j0.1 = 0.71 e^(j0.14); that is, V_in(t) = **0.71 cos(ωt + 0.14)**.

**(c)** Γ_L = (Z_L − Z₀)/(Z_L + Z₀) = (50(1+j) − 100)/(50(1+j) + 100) = −0.2 + j0.4. Since V_L = V_L⁺(1 + Γ_L) and V_in = V_L⁺(e^(jβl) + Γ_L e^(−jβl)),

V_L = V_in (1 + Γ_L) / (e^(jβl) + Γ_L e^(−jβl)) = (0.7 + j0.1)(0.8 + j0.4) / [(1+j)/√2 + (−0.2 + j0.4)(1−j)/√2] = 0.42 − j0.14 = 0.45 e^(−j0.32)

(Used e^(−jβl) = e^(−jπ/4) = (1−j)/√2.) Returning to the time domain, **V_L(t) = 0.45 cos(ωt − 0.32)**.

**(d)** P_d = ½ Re{|V_L|²/Z_L*} = ½ (0.45)² Re{1/(50(1−j))} ≈ **10⁻³ W**. Since the line is lossless, the same power is also found at the input: P_d = ½ Re{|V_in|²/Z_in*} = ½ (0.71)² Re{1/(100(2−j))} ≈ 10⁻³ W.
