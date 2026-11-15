---
baslik: EEM401 Digital Signal Processing: Digital Filters (Network Structures, IIR Design, FIR Design)
ozet: Selda Güney's EEM401 Digital Filters I–III presentations: IIR and FIR realizations (direct, canonical, cascade, parallel, transposed), Butterworth/Chebyshev/elliptic analog filters, impulse invariance and the bilinear transformation, windowing, and frequency sampling.
---

The three December presentations from the EEM401 Digital Signal Processing course (Asst. Prof. Dr. Selda Güney, Fall 2014–2015): *Digital Filters I* (realization), *II* (IIR design), and *III* (FIR design). The original presentations can be downloaded as a ZIP at the end of the post. The course title on the slides is "EEM 401 Digital Signal Processing".

## I. Realization of digital filters

**Advantages:** the transfer function can be changed by changing the coefficients; high reliability and accuracy; transfer functions that cannot be realized with analog filters can be realized. **Disadvantages:** cost, need for a continuous power supply.

By design, there are two types:

1. **Recursive**: the output is a function of both the input and the output; the phase response is not linear; for stability, the poles of the transfer function must lie inside the unit circle in the z-plane.
2. **Non-recursive**: the output depends only on the input and the past values of the input; it has a linear phase response and is stable; a large number of delay elements is required for a transfer function with a sharp transition.

Linear time-invariant (LTI) systems are divided into **FIR** (finite impulse response: y[n] = Σ_{k=0}^{M−1} h(k) x(n − k), generally non-recursive) and **IIR** (infinite impulse response, generally recursive).

Realization methods: direct, canonical form, series (cascade), parallel, ladder, and lattice realization.

Constant-coefficient difference equation: y[n] = −Σ_{k=1}^{N} a_k y[n − k] + Σ_{k=0}^{M} b_k x[n − k] and H(z) = Σ b_k z^(−k) / (1 + Σ a_k z^(−k)). Basic elements: adder, multiplier, and unit delay. Example: y[n] = a1·y[n−1] + a2·y[n−2] + b0·x[n].

### Network structures for IIR systems

- **Direct form I:** H(z) = H2(z)·H1(z); first v[n] = Σ b_k x[n − k], then y[n] = Σ a_k y[n − k] + v[n].
- **Direct form II (canonical):** by swapping the order of H1 and H2, w[n] = Σ a_k w[n − k] + x[n] and y[n] = Σ b_k w[n − k]; the number of delay elements is minimal. For example, for a single-pole system, w1[n] = a·w1[n−1] + x[n], y[n] = b0·w1[n] + b1·w1[n−1]. An example shows how to write the wave variables (w1[n], w2[n], …) from the signal flow graph and obtain the unit impulse response using the z-transform.
- **Cascade form:** H(z) is the product of first- or second-order sections; second-order sections are practical. Example:
  H(z) = (1 + 2z⁻¹ + z⁻²) / (1 − 0.75z⁻¹ + 0.125z⁻²) = (1 + z⁻¹)(1 + z⁻¹) / ((1 − 0.5z⁻¹)(1 − 0.25z⁻¹)); realizations in direct form I and II and in cascade form are shown.
- **Parallel form:** partial fraction expansion. In the same example, H(z) = 8 + 18/(1 − 0.5z⁻¹) − 25/(1 − 0.25z⁻¹), and with second-order sections H(z) = 8 + (−7 + 8z⁻¹)/(1 − 0.75z⁻¹ + 0.125z⁻²).
- **Transposed form:** if the directions of all branches of the signal flow graph are reversed and the input and output are interchanged, the input-output relationship does not change.

### Network structures for FIR systems

Direct form I; direct form II (the transpose of I); cascade form H(z) = Π (b0k + b1k z⁻¹ + b2k z⁻²); the **lattice form** for linear-phase FIR systems (the sequence h[n] must be symmetric; the cases of M even and odd are treated separately).

## II. Design of IIR filters

The goal is to obtain a realizable G(z) that approximates a given frequency response; the course covers only magnitude approximation.

The impulse responses of the four ideal filters cannot be realized because they are non-causal and infinitely long. In practice, the magnitude response is specified with acceptable tolerances in the passband and stopband; between them lies the **transition band**. For a low-pass filter: ωp is the passband edge, ωs is the stopband edge, δp is the maximum ripple in the passband, and δs is the minimum ripple in the stopband. Loss function A(ω) = −20·log10|G(e^jω)|; αp = −20·log10(1 − δp) and αs = −20·log10(δs). Edge frequencies given in Hz are converted to radians using the sampling frequency F_T (ω = 2πF/F_T).

The most commonly used method: (1) the digital filter specifications are converted to the specifications of a prototype analog low-pass filter; (2) the analog Ha(s) is determined; (3) Ha(s) is transformed into the digital G(z). The reason: analog filter design is highly developed and has tables.

### Types of analog filters

1. **Butterworth:** |Ha(jΩ)|² = 1 / (1 + (jΩ/jΩc)^(2N)); poles s_k = Ωc·e^(jπ(2k + N + 1)/2N).
2. **Chebyshev:** |Ha(jΩ)|² = 1 / (1 + ε²·V_N²(Ω/Ωc)), V_N(x) = cos(N·cos⁻¹x).
3. **Elliptic.**

### Transformation from analog to digital filter

- **Impulse invariance method:** h[n] = Td·ha(nTd). If Ha(s) = Σ A_k/(s − s_k), then H(z) = Σ Td·A_k / (1 − e^(s_k·Td)·z⁻¹); the poles s_k in the s-plane map to the poles e^(s_k·Td) in the z-plane. Example: for 0.89125 ≤ |H(e^jω)| ≤ 1 (0 ≤ ω ≤ 0.2π) and |H(e^jω)| ≤ 0.17783 (0.3π ≤ ω ≤ π), with Td = 1, the Butterworth design gives N = 5.8858 ≈ **6** and Ωc = 0.70474; the 6th-order Ha(s) = 0.12093 / [(s² + 0.364s + 0.4945)(s² + 0.9945s + 0.4945)(s² + 1.3585s + 0.4945)]; the result is an H(z) consisting of three second-order sections.
- **Bilinear transformation (BLT):** it is used more often because of the factors affecting aliasing and stability: s = (2/T)·(1 − z⁻¹)/(1 + z⁻¹). The left half of the s-plane maps to the inside of the unit circle, the right half to the outside, and the jΩ axis to the unit circle; that is, a stable analog function maps to a stable digital function. The frequency relationship Ω = (2/T)·tan(ω/2) is nonlinear and produces **frequency warping**. Design steps: (1) apply prewarping to the edge frequencies (find Ωp, Ωs); (2) design the analog filter; (3) obtain G(z) with the BLT. The BLT can be used only for filters with piecewise-constant magnitude responses and does not preserve the phase response of the analog filter. In the same example, with the BLT, N = 5.305 ≈ 6 and Ωc = 0.766 are found and H(z) = 0.0007378(1 + z⁻¹)⁶ / [(1 − 1.2686z⁻¹ + 0.7051z⁻²)(1 − 1.0106z⁻¹ + 0.3583z⁻²)(1 − 0.9044z⁻¹ + 0.2155z⁻²)] is obtained.
- **The matched z-transform** is mentioned as a third method. The presentation ends with a low-pass Butterworth design with ωp = 0.25π, ωs = 0.55π, αp = 0.5 dB, αs = 15 dB.

## III. Design of FIR filters

FIR design is based on direct approximation of the specified magnitude response; linear phase is generally desired. Designing an Nth-order FIR filter means finding the (N + 1)-length impulse response coefficients {h[n]} or (N + 1) samples of the frequency response. Methods: windowed Fourier series, frequency sampling, computer-based optimization (Parks–McClellan).

- FIR design is a discrete-time process; it has no equivalent in the analog domain; definitions are mostly in the time domain.
- Two advantages: **stability** and **linear phase**; the number of coefficients (order) is much larger than for an IIR filter with the same specifications.
- The simplest FIR filter is the **moving average** filter: it is a rather poor low-pass filter in terms of magnitude response, and its bandwidth is controlled only by the order.
- Filter equation y[n] = Σ_{k=0}^{N−1} b_k x[n − k]; if an impulse is applied to the input, the coefficients equal the samples of the impulse response (b_k = h[k]). Causal FIR filters with a symmetric impulse response have linear phase (even symmetry N = 2n + 2, odd symmetry N = 2n + 1).

**Five-step design:** (1) the specifications are determined (passband edge, stopband edge, cutoff frequency, ripples); (2) the coefficients are computed; (3) the structure is determined; (4) (optional) simulation; (5) implementation.

### Windowing method

h[n] = h_d[n]·w[n]. First the coefficients of the ideal filter h_d[n] = sin(nω_c)/(nπ) are computed (2f_c for n = 0); the result is the circular convolution of h_d with the window response in the frequency domain. Then the window is chosen:

| Window | Main lobe width | Peak side lobe |
|---|---|---|
| Rectangular | 4π/M | −13 dB |
| Bartlett | 8π/M | −25 dB |
| Hanning | 8π/M | −31 dB |
| Hamming | 8π/M | −41 dB |
| Blackman | 12π/M | −57 dB |

The rectangular window is the simplest (w[n] = 1, 0 ≤ n ≤ M); it has a sharp main lobe but wide side lobes and large oscillation around the discontinuity. Hamming is better than Hanning and Bartlett and simpler than Blackman; Blackman's side lobes are the best but its equation is complex.

### Frequency sampling method

N equally spaced samples H_k are taken from the 0–2π range of the frequency response H(e^jω), and the inverse DFT is taken: h[n] = (1/N) Σ_{k=0}^{N−1} H_k·W_N^(−nk), n = 0, 1, …, N − 1. The presentation works through this method with examples.
