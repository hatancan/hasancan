---
baslik: EEM401 Digital Signal Processing: z-Transform, Region of Convergence, Inverse z-Transform, and Decimation-in-Time FFT (Notebook Notes)
ozet: Notes from my EEM401 notebook, 27 November 2014: definition of the z-transform and its region of convergence (ROC), stability and causality, inverse z-transform examples, the decimation-in-time (DIT) fast Fourier transform algorithm, and an 8-point example.
---

This post is a text transcription of 16 pages of handwritten notes that I took in my notebook during the **EEM401 Digital Signal Processing** course (Asst. Prof. Dr. Selda Güney) in the 2014–2015 fall semester, and photographed on 27 November 2014. The photographs have not been published; the content has been rewritten. For the course slides, see the posts "Discrete-Time Signals and Systems" and "Digital Filters".

## 1. Fast Fourier transform (decimation in time, DIT)

**Definition.** X(k) = Σ_{n=0}^{N−1} x[n]·W_N^{kn}, W_N = e^{−j2π/N}; W_N^k is periodic: W_N^{k+N} = W_N^k.

**Splitting into even- and odd-indexed samples (N even).**
X(k) = Σ_{m=0}^{N/2−1} x[2m]·W_N^{2mk} + Σ_{m=0}^{N/2−1} x[2m+1]·W_N^{(2m+1)k}. Since W_N² = e^{−j(2π/N)·2} = e^{−j4π/N} = W_{N/2}:

X(k) = F(k) + W_N^k·G(k), k = 0, 1, …, N/2 − 1
X(k + N/2) = F(k) − W_N^k·G(k), k = 0, 1, …, N/2 − 1

Here F(k) is the N/2-point DFT of the even-indexed samples and G(k) is the N/2-point DFT of the odd-indexed samples; W_N^{k+N/2} = W_N^k·W_N^{N/2} = −W_N^k (because W_N^{N/2} = e^{−jπ} = −1). F(k) and G(k) repeat with period N/2 (F(0) = F(4), F(1) = F(5), … for N = 8).

**N = 4 example and the flow for N = 8.** The same method is applied inside the 4-point DFT: the sequence x[0], x[2], x[4], x[6] enters the F block; the sequence x[1], x[3], x[5], x[7] enters the G block. The 4-point blocks are in turn split into 2-point DFTs: F_a[0] = x[0] + W₈⁰·x[4] = x[0] + x[4], F_a[1] = x[0] − x[4], F_t[0] = x[2] + x[6], F_t[1] = x[2] − x[6]; G_a[0] = x[1] + x[5], G_a[1] = x[1] − x[5], G_t[0] = x[3] + x[7], G_t[1] = x[3] − x[7]. Then, with the factor W₈²:
- F(0) = F_a(0) + F_t(0), F(1) = F_a(1) + W₈²·F_t(1), F(2) = F_a(0) − F_t(0), F(3) = F_a(1) − W₈²·F_t(1);
- G(0), G(1), G(2), G(3) are obtained in the same way; in the last step X(0) … X(3) are found from X(k) = F(k) + W₈^k·G(k) (k = 0 … 3), and X(4) … X(7) from X(k + 4) = F(k) − W₈^k·G(k). In the butterfly diagrams the weights are W₈⁰, W₈¹, W₈², W₈³, and −1 on the opposing branches.

**Numerical example.** x[n] = {1, 1, −1, −1, −1, 1, 1, −1}, N = 8: find X(k) using the decimation-in-time FFT. The rows of the 4-point DFT matrix are taken as (1, 1, 1, 1), (1, −j, −1, j), (1, −1, 1, −1), (1, j, −1, −j) (W₄⁰ = 1, W₄² = −1). The even-indexed samples are f[n] = {1, −1, −1, 1} and the odd-indexed samples are g[n] = {1, −1, 1, −1}. With the 4×4 DFT matrix, F(k) = {0, 2 + j2, 0, 2 − j2}, G(k) = {0, 0, 4, 0}. Result:
X(0) = 0, X(1) = 2 + j2, X(2) = W₈²·4 = −j4, X(3) = 2 − j2, X(4) = 0, X(5) = 2 + j2, X(6) = +j4, X(7) = 2 − j2.

On the unit circle, the points n = 0, 4 → 1; n = 1, 5 → −j; n = 2, 6 → −1; n = 3, 7 → j are drawn, along with the 90° (W₄) and 180° rotations of the columns of the W₈ matrix (the rows of the W₄ matrix). There is also a short power spectrum sketch (P_k: 0.25; 0.5; 0.25; 0.5).

## 2. z-transform

The z-transform is a generalization of the Fourier transform. If the sum of a signal diverges (for example x[n] = (0.5)ⁿu[−n] or a growing signal), we cannot take its Fourier transform; that is why we use the z-transform. **The z-transform has a region of convergence (ROC).**

**Region of convergence.**
- Writing Z = r·e^{jω}, X_r(e^{jω}) = Σ x[n]·r^{−n}·e^{−jωn}; the sum can be made finite by choosing r. Example: for x[n] = 2ⁿu[n], Σ|x[n]| = ∞, i.e. the DTFT does not exist; but with r = 3 (r > 2), Σ 2ⁿ·3^{−n}·e^{−jωn} = Σ (2/3)ⁿ e^{−jωn} converges.
- Geometric series: Σ_{n=0}^{∞} αⁿ = 1/(1 − α), |α| < 1.
- If the unit circle is inside the ROC, the discrete-time Fourier transform exists; if not, it does not.
- If the signal is **right-sided**, the ROC is the exterior of a circle; if it is **left-sided**, the ROC is the interior of a circle. A right-sided signal is causal; a left-sided signal is not causal.
- **Properties:** The ROC contains no poles; for stability the ROC must include the unit circle; for the system to be both causal and stable, the poles must lie inside the unit circle (with magnitude less than 1); for the ROC to contain no poles, it must lie inside the smallest pole, outside the largest pole, or between poles. Example: if the poles are at 0.5, 2, 3, 5, the ROC is |z| < 0.5, 0.5 < |z| < 2, 2 < |z| < 3, 3 < |z| < 5, or |z| > 5 (between 2 and 5 "is not allowed", between 2 and 3 is fine, and between 3 and 5 is fine).
- If the degree of the numerator is greater than that of the denominator, the system is not causal (example: H(z) = (z³ − 2z² + z)/(z² + z/4 + 1/8) is not causal).

**Example 1 (left-sided).** x[n] = −(7/8)ⁿ·u[−n−1]. X(z) = Σ_{n=−∞}^{−1} −(7/8)ⁿ z^{−n} = … = 1/(1 − (7/8)z⁻¹), ROC: |z| < 7/8 (for the sum to converge, |(7/8)^{−1}·z| < 1). The notebook also has the note "if the equation were x[n] = (7/8)ⁿu[n], X(z) would be the same, but the ROC would be |z| > 7/8".

**Example 2.** x[n] = 7(1/3)ⁿu[n] − 6(1/2)ⁿu[n]: X(z) = 7/(1 − (1/3)z⁻¹) − 6/(1 − (1/2)z⁻¹) = (1 − (3/2)z⁻¹) / [(1 − (1/3)z⁻¹)(1 − (1/2)z⁻¹)], |z| > 1/2.

**Example 3 (sinusoidal).** x[n] = (1/3)ⁿ·sin(πn/4)·u[n] → X(z) = ((1/3)·(√2/2)·z) / [(z − (1/3)e^{jπ/4})(z − (1/3)e^{−jπ/4})] (|z| > 1/3; the poles lie on the circle of radius 1/3 at ±45°).

In an example with poles at 1/3 and 1/2, three regions are drawn: |z| > 1/2 is right-sided (causal and stable, contains the unit circle); 1/3 < |z| < 1/2 is two-sided; |z| < 1/3 is left-sided (of the form x[n] = 7(1/3)ⁿu[−n−1] + 6(1/2)ⁿu[−n−1]).

## 3. Inverse z-transform

Some inverse z-transform pairs:

| X(z) | |z| > |α| | |z| < |α| |
|---|---|---|
| 1 / (1 − αz⁻¹) | αⁿ·u[n] | −αⁿ·u[−n−1] |
| 1 / (1 − αz⁻¹)² | (n+1)·αⁿ·u[n] | −(n+1)·αⁿ·u[−n−1] |
| 1 / (1 − αz⁻¹)^m | [(n+1)(n+2)…(n+m−1)/(m−1)!]·αⁿ·u[n] | −[(n+1)…(n+m−1)/(m−1)!]·αⁿ·u[−n−1] |

Notes: αz⁻¹/(1 − αz⁻¹)² = αz/(z − α)²; if the numerator and denominator degrees are equal, they are divided to extract the constant coefficient; for pole/zero locations such as z = 0 and z = −1 and for repeated poles, one more value is given ("we multiplied by 2 and divided by 2" is used to adjust the numerator). A partial-fraction example: X(z) = z⁻¹ / [(1 − az⁻¹)(1 − bz⁻¹)²] = A/(1 − az⁻¹) + B1/(1 − bz⁻¹) + B2/(1 − bz⁻¹)².

**Numerical example (three regions).** The partial-fraction expansion of X(z) yields three different sequences for three different ROCs:
- |z| < 1/2: x[n] = 2δ[n] + 9(1/2)ⁿu[−n−1] − 8u[−n−1],
- 1/2 < |z| < 1: x[n] = 2δ[n] − 9(1/2)ⁿu[n] − 8u[−n−1],
- |z| > 1: x[n] = 2δ[n] − 9(1/2)ⁿu[n] + 8u[n].

Of these three cases, only |z| > 1 is right-sided and causal; 1/2 < |z| < 1, which contains the unit circle, is two-sided and has a Fourier transform.

*Note: Because some parts of the notebook (especially the partial-fraction coefficients and the sketches) were written in a hurry, there may be small discrepancies when reading them from the handwriting.*
