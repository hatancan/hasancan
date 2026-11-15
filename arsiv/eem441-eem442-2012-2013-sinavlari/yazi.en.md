---
baslik: EEM441 Communications I: EEM442 Communications II 2012 and 2013 Exams (Questions and Solutions)
ozet: EEM442 Communications II May 30, 2012 final, March 30, 2013 midterm, and May 22, 2013 final: 8-PAM, ISI, M-PSK design, PCM, PDM/PPM, and matched filter problems.
---

The May 30, 2012 final, March 30, 2013 midterm, and May 22, 2013 final of the Başkent University EEM 442 Communications II course. The sources are phone photographs of the exam papers and handwritten solutions (since they were kept in the EEM441 folder, they are listed here under EEM441); the content was transcribed to text from the photographed pages, and the photographs were not published. The solutions were read from a friend's handwritten notes; personal information was removed.

## Final, May 30, 2012 (duration 110 min)

**Question 1.** A rectangular-pulse 8-level bipolar signal is applied to the receiver with AWGN of noise power spectral density N₀ = 2×10⁻⁶ W/Hz. i) R_b = 150 kbit/s, ii) the spacing between transmission levels is ±1 V, ±3 V, ±5 V, ±7 V (spacing 2 V), iii) there is no ISI at the output of the α = 0.4 raised cosine filter. a) The values of the signal points at the matched filter output, b) the signal-to-noise ratio at the sampling instant, c) the symbol error probability, d) the transmission bandwidth.

*Solution.* R_s = R_b/3 = 50 ksymbol/s, T_s = 20 µs; for A = 1 V, E_g = A²T_s = 20×10⁻⁶, √E_g ≈ 4.47×10⁻³; the matched filter output is ±√E_g, ±3√E_g, ±5√E_g, ±7√E_g. The adjacent-level crossover probability is p = Q(√(2E_g/N₀)) = Q(√20) ≈ 3.87×10⁻⁶. The symbol error probability is P_s = (2(M−1)/M)·p = (7/4)(3.87×10⁻⁶) ≈ 6.77×10⁻⁶; with Gray coding, BER = P_s/3 ≈ 2.26×10⁻⁶. Average SNR: E_s/N₀ = (E_g + 9E_g + 25E_g + 49E_g)/(4N₀) = 21E_g/N₀ = 210 (23.22 dB). Bandwidth B = (1/2T_s)(1 + 0.4) = 0.7R_s = 35 kHz.

**Question 2.** In a baseband system, g(t) = A Σ a_n p(t − nT), with a_n = ±1 equiprobable. At the output of an LTI filter with impulse response h(t), v(T₀) = +7, v(T₀−T) = +2, v(T₀+T) = −1, and v(T₀+nT) = 0 for |n| > 1; the noise variance is σ² = 4, and a₀ = 1 is assumed. a) The pulse values at t = T₀ that make the error probability due to ISI minimum and maximum, b) the error probabilities for these two cases and the average error probability, c) repeat for a₀ = −1.

*Solution.* At the sampling instant, ψ(T₀)/A = −a₋₁ + 7a₀ + 2a₁ (a₀ = +1):

| a₋₁ | a₁ | ψ(T₀)/A |
|---|---|---|
| +1 | +1 | 8 |
| +1 | −1 | 4 |
| −1 | +1 | 10 |
| −1 | −1 | 6 |

The smallest value (4) makes the error probability maximum, and the largest value (10) makes it minimum: P_e,max = Q(4A/σ) = Q(2A), P_e,min = Q(10A/σ) = Q(5A). Average: P_e,avg = ¼[Q(4A) + Q(2A) + Q(5A) + Q(3A)]. For a₀ = −1, by symmetry the values are −6, −10, −4, −8; −10 has the largest magnitude (smallest error), and −4 makes the error probability maximum.

**Question 3.** A real-time (zero-delay) communication system is to be designed using M-PSK (coherent) and M-FSK (noncoherent) over an AWGN channel such that the BER does not exceed 10⁻³, the data rate is 9600 bit/s, the transmission bandwidth (Nyquist) is at most 5000 Hz, and the received E_b/N₀ = 12 dB. a) Under these conditions, the symbol rate, symbol energy, bandwidth efficiency, and suitable M, b) the M that satisfies the BER.

*Solution.* For coherent M-PSK, W = R_s = R_b/log₂M, η = log₂M; for noncoherent M-FSK, W = MR_b/log₂M, η = log₂M/M. For M = 2, 4, 8, 16 the PSK efficiencies are 1, 2, 3, 4; the FSK efficiencies are 0.5, 0.5, 0.375, 0.25, so PSK is more efficient for every M; PSK is tried first. E_b/N₀ = 12 dB (15.85):

| M | W = R_s | Suitable (W ≤ 5000 Hz) | P_b |
|---|---|---|---|
| 2 | 9600 Hz | no | — |
| 4 | 4800 Hz | yes | ≈ 8×10⁻⁹ |
| 8 | 3200 Hz | yes | ≈ 6.3×10⁻⁵ |
| 16 | 2400 Hz | yes | ≈ 7×10⁻³ (exceeds 10⁻³) |

Only 4-PSK and 8-PSK satisfy the conditions; 8-PSK is chosen because it has the higher bandwidth efficiency.

**Question 4.** (This part of the paper is not in the photograph.) From the solution sheet: ISI arises from the filtering effect of the system; the equivalent transfer function is H(f) = H_t(f)H_c(f)H_r(f), and when square-root raised cosine filters are used at the transmitter and receiver, one deals with H(f) = H_RC(f)H_c(f). When the band over which the channel is flat is 250 kHz (assuming baseband transmission), (R_s/2)(1 + α) ≤ 250 kHz, and for α = 0.2, R_s ≤ 500/1.2 = 416.67 ksymbol/s and for M = 8, R_b = 3R_s ≤ 1250 kbit/s. At higher rates the bandwidth extends beyond the flat region of the channel and ISI appears.

## Midterm, March 30, 2013 (duration 110 min)

1. An analog speech signal band-limited to W = 3000 Hz is to be transmitted using binary PCM and M-PAM, SNR₀ > 60 dB. a) Transmitter block diagram, b) the minimum number of bits per sample and the actual SNR₀, c) the sampling frequency and the data rate, d) bipolar NRZ with pulse duration 62.5 µs: transmission bandwidth and symbol rate.
2. The bit rate of a PCM system with an 8-bit binary encoder after a uniform quantizer is 100×10⁶ bit/s. a) The maximum bandwidth of the message sampled at the Nyquist rate, b) the output SNR when operating at the peak value of a sinusoid with a frequency of 1 MHz.
3. A random signal uniformly distributed over the range ±12 V is passed through a 256-level uniform quantizer; what is the ratio of the signal power to the quantization noise at the quantizer output?
4. The signal s(t) = e^(−αt), 0 ≤ t ≤ T is corrupted by zero-mean white Gaussian noise with power spectral density N₀/2. a) The impulse response of the matched filter and its graph, b) find the maximum output SNR in terms of α, T, and N₀; sketch the filter input and output spectra, c) the error probability if s₀(t) = s(t) and s₁(t) = −s(t) are sent with equal probability.

*Solution summary.*

3. Δ = 2m_max/L = 24/256 = 12/128; σ_Q² = Δ²/12.
4. h(t) = s(T − t) = e^(−α(T−t)), 0 ≤ t ≤ T. The output f(t) = s(t)⊗h(t): for 0 ≤ t ≤ T, (1/2α)[e^(−α(T−t)) − e^(−α(T+t))]; for T ≤ t ≤ 2T, (1/2α)[e^(−α(T−t)) − e^(−α(3T−t))]; the maximum value at t = T is E_s = (1 − e^(−2αT))/(2α). The output noise power is (N₀/2)E_s, hence SNR_out = E_s²/((N₀/2)E_s) = 2E_s/N₀ = (1/(αN₀))(1 − e^(−2αT)). The decision threshold is λ = 0, and the error probability is P_e = Q(√(2E_s/N₀)).

*Note: In Question 3, the handwritten solution took the signal power with a density of 1/2, found 576, and gave the SNR as 12×2¹⁶ (58.95 dB). For a uniform distribution on [−12, 12] the density is 1/24; P = 12²/3 = 48, and P/σ_Q² = L² = 2¹⁶ = 65 536 (about 48.2 dB). There are no solution photographs for Questions 1 and 2.*

## Final, May 22, 2013 (duration 110 min)

**Question 1.** The signal x(t) = cos(2πt/T_m) is uniformly sampled at t = kT_s (T_s = T_m/3) to produce the pulse-modulated signal x_p(t). Sketch the waveforms for a) PDM (pulse duration modulation) with μ = 0.8, τ₀ = 0.4T_s, b) PPM (pulse position modulation) with t_d = 0.57T_s and t₀ = τ = 0.2T_s.

*Solution.* PDM: τ_k = 0.4T_s[1 + 0.8cos(2πk/3)] (for k = 0, 1, 2, 3 the pulse widths are 0.72, 0.24, 0.24, 0.72 T_s). PPM: t_k = T_s[k + 0.5 + 0.2cos(2πk/3)], width 0.2T_s.

**Question 2.** A signal with bandwidth W = 15 kHz is transmitted by M-ary PCM over a channel with noise power spectral density N₀ = 0.01 µW/Hz and transmission bandwidth B_T = 40 kHz. a) The minimum M and R for SNR₀ ≥ 40 dB, b) the minimum received power for operating above the threshold SNR, with P_e < 10⁻⁵ and P_peak/P = 2, while using the entire PCM transmission bandwidth.

*Solution.* SNR₀ = 3L²/α = (3/2)L² > 10⁴ ⇒ L ≥ 81.6. From the bandwidth condition, the number of M-ary symbols per sample is R ≤ B/W = 40/15 ≈ 2.67 ⇒ R = 2. L = M^R > 81.6 ⇒ M = 10, L = 100. The source solution takes the threshold SNR as 16(100 − 1) ≈ 1600; the received power is P_r = N₀W·SNR_threshold = 10⁻⁸ × 15×10³ × 1600 = 0.24 W = 240 mW.

**Question 3.** Signals S₀, S₁, S₂ with transmission probabilities P(S₀) = 0.5, P(S₁) = P(S₂) = 0.25 are sent over an AWGN channel with amplitudes 0, −√E, √E, respectively. a) Place the symbols in signal space, and compute the decision regions and threshold values. b) The error probability and decision regions of the optimum receiver.

*Solution.* Intermediate values: λ = d/2 + (N₀/2d)ln 2 (d = √E); the decision regions are r < −λ, |r| < λ, r > λ; P_e = Q(λ/σ) + ½Q((d − λ)/σ) + ½Q((d + λ)/σ), and for λ = d/2, (3/2)Q(d/2σ) + ½Q(3d/2σ).

**Question 4.** A digital communication system produces 3000 symbols per second and has 128 distinct symbols. a) The bandwidth required to transmit the output as a binary PAM signal, b) the M required to transmit it as an M-ary signal over a B = 3 kHz telephone line. (There is no solution photograph.)

*Note: The threshold SNR expression in Question 2 is only partly legible in the handwriting; the result values are transcribed as in the source. Of Questions 3 and 4, only the solution to Question 3 appears in the photographs.*
