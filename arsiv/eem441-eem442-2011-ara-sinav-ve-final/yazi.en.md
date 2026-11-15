---
baslik: EEM441 Communications I: EEM442 Communications II 2011 Midterm and Final Exams (Questions and Solutions)
ozet: The 3 August 2011 midterm and 1 June 2011 final of the EEM442 Communications II course: signal constellation, matched filter, 16-PAM, ISI and PCM problems, with solution summaries.
---

Two exams from the summer of 2011 for the EEM 442 Communications II course in the Department of Electrical and Electronics Engineering at Başkent University: the 3 August 2011 midterm and the 1 June 2011 final. The source is phone photographs of the exam papers and handwritten solutions (since it sits in the EEM441 folder, it appears under EEM441 in this archive); the content was transcribed to text from the photographed pages, and the photographs themselves have not been published. The solutions were read from a friend's handwritten notes; they contain no personal information.

## Final, 1 June 2011 (duration 2 hours)

**Question 1.** The figure shows an 8-point signal constellation consisting of two circles, an inner and an outer one (r₁/r₂ = 1/2, r₁ = √E₀; E₀ is the smallest symbol energy).

- a) Find the average symbol energy in terms of E₀.
- b) Write the upper bounds on the error probability of the symbols on the inner and outer circles in terms of E_s,avg/N₀.
- c) Taking the Euclidean distances into account, encode the constellation with a Gray code; compute the average BER.
- d) Propose a simple modification that improves performance and calculate its effect.

*Solution summary.* r₁ = √E₀, r₂ = 2√E₀; E_s,avg = (r₁² + r₂²)/2 = (5/2)E₀ = 3E_b,avg, i.e. E₀ = (2/5)E_s,avg = (6/5)E_b,avg. The nearest-neighbor distances are d₁ = √(2E₀), d₂² = r₁² + r₂² − √2 r₁r₂ = (5 − 2√2)E₀, d₃ = 2√(2E₀). For the inner ring, P_e,i ≈ 2Q(d₁/√(2N₀)) + 2Q(d₂/√(2N₀)); for the outer ring, P_e,o ≈ 2Q(d₂/√(2N₀)) + 2Q(d₃/√(2N₀)). With Gray coding, P_b ≲ (1/6)(P_e,i + P_e,o) = (1/3)[Q(d₁/√(2N₀)) + 2Q(d₂/√(2N₀)) + Q(d₃/√(2N₀))]. Proposal: change the ratio r₂/r₁ so that d₁ = d₂: 2r₁² = r₁² + r₂² − √2 r₁r₂ ⇒ x² − √2x − 1 = 0, x = r₂/r₁.

*Note: The handwritten solution obtains x = 1.905, E_s,avg = 2.314E₀ and a gain of 0.336 dB. The positive root of the equation x² − √2x − 1 = 0 is (√2 + √6)/2 ≈ 1.932; from this, E_s,avg = (1 + x²)E₀/2 ≈ 2.366E₀ and 10 log(2.5/2.366) ≈ 0.24 dB.*

**Question 2.** s₁(t) = A, 0 ≤ t ≤ T; s₂(t) = A (0 ≤ t ≤ 3T/4) and −A (3T/4 ≤ t ≤ T). Equiprobable binary transmission over an AWGN channel.

- a) Signal energies, b) correlation coefficient, c) block diagram of the matched-filter receiver and the outputs at the sampling instant, decision criterion, d) bit error probability with a coherent matched filter.

*Solution summary.* E₁ = E₂ = A²T. ρ = (1/E)∫s₁s₂dt = (A²/E)(3T/4 − T/4) = 1/2. The receiver takes the difference of the outputs of two matched filters (1/√E)s₁(T−t) and (1/√E)s₂(T−t) and compares it with a threshold of 0. The sampled output is r(T) = ±(1 − ρ)√E + n(T), with noise variance N₀(1 − ρ). The error probability is P_e = Q(√((E/N₀)(1 − ρ))) = Q(√(E/(2N₀))).

**Question 3.** AWGN, N₀ = 10⁻⁶ W/Hz, equiprobable binary signal s(t) = ±2t/T_b, 0 ≤ t ≤ T_b.

- a) Sketch the impulse response of the matched filter, b) compute and sketch the waveform at the filter output, c) find the smallest bit duration and the bit rate for which the error probability is less than 10⁻⁴.

*Solution summary.* h(t) = s(T_b − t) = 2(T_b − t)/T_b; E_b = ∫s²dt = (4/3)T_b. For 0 ≤ t ≤ T_b the output is r(t) = 2(t/T_b)²(T_b − t/3), r(T_b) = (4/3)T_b, and for T_b ≤ t ≤ 2T_b it decreases to 0. P_b = Q(√(2E_b/N₀)) = Q(√(8T_b/(3N₀))) < 10⁻⁴ requires √(8T_b/(3N₀)) ≈ 3.7; T_b ≈ 5.13 µs, R_b ≈ 195 kbit/s.

**Question 4.** A line-driver circuit uses M = 16-level 16-PAM: maximum average power 10 dBm, maximum instantaneous peak power 30 dBm, maximum symbol rate 12 Msymbols/s.

- a) The maximum voltage spacing for 16 equally spaced levels, b) whether this spacing is limited by the peak or the average power, c) the achievable bit rate and its dependence on the average power, d) the symbol and bit error probabilities for N₀ = 10⁻¹² W/Hz.

Useful formulas from the exam paper: for binary transmission P(s₁→s₂) = Q(d₁₂/√(2N₀)); for correlated signals P_b = Q(√((E_s/N₀)(1 − ρ))); for coherent M-PSK P_s = 2Q(√(2E_s/N₀) sin(π/M)); for M-PAM P_E = (2(M−1)/M) Q(√(6E_s,avg/((M²−1)N₀))); quantization noise variance σ_Q² = Δ²/12 = (2m_max/L)²/12, L = 2ᴿ.

*Solution summary.* E_avg = a²(M²−1)/3 = 85a², E_peak = (15a)² = 225a²; T = 1/12 µs. From the conditions P_avg = 85a²/T ≤ 10 mW and P_peak = 225a²/T ≤ 1 W, we get a ≤ 3.13 µV (average) and a ≤ 19.2 µV (peak); the average power is the limiting one, and the maximum voltage spacing is 2a ≈ 6.3 µV. The bit rate is R_b = 4 × 12 = 48 Mbit/s; the system's bit rate is independent of power, and the average power is related to E_avg·R_b/log₂M. The source solution gives the symbol error probability as P_e ≈ 8.9×10⁻⁶ and P_b = P_e/4 ≈ 2.2×10⁻⁶.

*Note: The numerical result in the source solution was obtained by taking E_avg/N₀ ≈ 833; with the problem data (P_avg = 10 mW, T = 1/12 µs, N₀ = 10⁻¹² W/Hz), E_avg/N₀ is much larger. Here the numbers from the source are carried over as they are.*

## Midterm, 3 August 2011 (duration 110 min)

**Question 1.** In a binary PAM system y_m = a_m + n_m + i_m; a_m = ±1, n_m is zero-mean Gaussian with variance σ_n², and the ISI term i_m takes the values −0.5, 0, 0.5 with probabilities 0.25, 0.5, 0.25 respectively. Find the average error probability as a function of σ_n.

*Solution.* When a_m = −1 is sent: P_e = ¼P(n > 1/2) + ¼P(n > 3/2) + ½P(n > 1) = ¼Q(1/(2σ_n)) + ¼Q(3/(2σ_n)) + ½Q(1/σ_n).

**Question 2.** The bit rate of a PCM system with a 7-bit binary encoder after a uniform quantizer is 50×10⁶ bit/s. a) The maximum message bandwidth when sampling at the Nyquist rate, b) the signal-to-quantization-noise ratio at the output when operating at the peak value of a sinusoid with a frequency of 1 MHz.

**Question 3.** A step/ramp signal x(t) = a·t is applied to a delta modulator with sampling interval T_s and step size Δ. a) The slope overload condition, b) sketch the modulator output for Δ = 0.75aT_s, aT_s and 1.25aT_s.

**Question 4.** The signal s(t) consists of seven symbols with spacing T (a₀ = a₁ = a₂ = a₄ = 1, a₃ = a₅ = a₆ = −1) and is carried by a triangular pulse g(t) (base width 2T). a) The characteristic function of the matched filter and the energy of g(t), b) the impulse response of the matched filter and the output sampled at t = nT, c) the peak value of the output.

*Solution summary.* s(t) = Σ a_k g(t − kT), E_g = T; h_opt(t) = g(T − t)/√T; the sampled output is +√E_g at the instants T, 2T, 3T, 5T and −√E_g at the instants 4T, 6T, 7T; the peak value is √E_g = √T.

*Note: There are no solutions on the photographed pages for Questions 2 and 3; only the questions were transcribed.*
