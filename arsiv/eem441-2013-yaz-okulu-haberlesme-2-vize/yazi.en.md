---
baslik: EEM441 Communications I: 2013 Summer School EEM 442 Communications II Midterm Exam (5 August 2013) and Solutions
ozet: EEM 442 Communications II summer school midterm exam: matched filter, binary signaling in impulse noise, quantization SNR, and 16-PAM telemetry design; with handwritten solutions.
---

This document belongs to the EEM 442 Communications II course; it is published here because it was found in the EEM 441 folder. Başkent University EEM 442 Communications II summer school midterm exam (5 August 2013, duration 110 minutes) and handwritten solutions. The exam paper and solutions were transcribed to text from photographed pages; the photographs have not been published. For this reason, there is no downloadable original file. Personal information (student number, name) has been removed.

## Questions

1. Consider the given signal s(t) (s(t) = 1 for 0–3T; −1 for 3T–4T; +1 for 4T–5T; −1 for 5T–7T). a) For the signal s(t) at the matched filter input, derive the required expression for the transmit filter in terms of the characteristic function g(t); compute the energy of the pulse g(t). b) Compute the impulse response of the matched filter for s(t); plot the impulse response and the matched filter output sampled at t = nT as a function of time. c) Compute the peak value of the matched filter output.
2. Some switching circuits produce impulse noise, modeled as filtered white noise with average power σ² and exponential pdf p_n(n) = (1/√(2σ²)) e^(−√2|n|/σ). a) Derive an expression for the error probability P_e for bipolar signaling in impulse noise in terms of A and σ. b) For P_e ≤ 0.001, compare the effect of Gaussian noise and impulse noise.
3. In a digital communication system, a random signal with a uniform distribution over the range ±2 V is passed through a 256-level uniform quantizer. Compute the ratio of the signal power to the quantization noise power at the quantizer output.
4. The telemetry circuit of a satellite system uses a 16-PAM transmission system with M = 16 symbol levels. The characteristics of the telemetry circuit are: i) maximum average power 10 dBm, ii) maximum instantaneous peak power 30 dBm, iii) maximum data rate 12 M symbols/s. a) Given that the 16 transmission levels are equally likely, what is the largest voltage spacing between the usable transmission levels? b) Is the largest voltage spacing limited by the peak or the average power requirements of the telemetry system? c) What is the total bit rate that can be achieved? Does the bit rate of the system depend on the average power? d) Compute the symbol and bit error probabilities for N₀ = 10⁻¹² W/Hz.

The formula sheet provided with the exam contains: P_b = p₁Q((A − λ)/σ) + (1 − p₁)Q((A + λ)/σ); Q(3.09023) = 10⁻³, Q(√20) = 3.87×10⁻⁶; B_T = (R_s/2)(1 + α); SNR₀ = 3×2^(2R)/α; for binary correlated signaling P_b = Q(√(E_s(1 − ρ)/N₀)); for M-PSK P_s = 2Q(√(2E_s/N₀) sin(π/M)); (1/(M/2)) Σ(2i − 1)² = (M² − 1)/3; for M-PAM P_E(M) = [2(M − 1)/M] Q(√(6E_s,av/((M² − 1)N₀))).

## Solution 1: Matched Filter

a) s(t) = Σ_{k=0}^{6} a_k g(t − kT); a₀ = a₁ = a₂ = a₄ = 1, a₃ = a₅ = a₆ = −1. The basic pulse g(t) is a rectangle of duration T and amplitude 1; its energy is E_g = ∫₀ᵀ g²(t) dt = T. At the matched filter output, the autocorrelation of g is obtained, i.e., a triangle extending from 0 to 2T with a peak value of √E_g at T.

b) h_opt(t) = (1/√T) g(T − t). The output sampled at times nT consists of bars of height √E_g weighted by the sequence a_k: +√E_g at T, 2T, and 3T; −√E_g at 4T; +√E_g at 5T; and −√E_g at 6T and 7T.

c) The peak value of the output is √E_g = √T.

## Solution 2: Impulse Noise

The conditional densities P_Y(y|0) (mean −A/2) and P_Y(y|1) (mean +A/2) are symmetric; the optimum threshold is λ_opt = 0.

a) P_e = P_e0 = ∫₀^∞ p_n(y + A/2) dy = (1/√(2σ²)) ∫₀^∞ e^(−√2 (y + A/2)/σ) dy = ½ exp(−A/√(2σ²)).

b) For P_e ≤ 10⁻³, A/√(2σ²) ≥ ln(1/(2×10⁻³)) ⇒ A ≥ 8.86σ (impulse noise). For Gaussian noise, P_e = Q(A/2σ) ≤ 10⁻³ ⇒ A ≥ 6.2σ. For the same P_e, impulse noise requires more signal power.

*Note: Since ln(500) = 6.215 and √2 × 6.215 = 8.79, our own calculation gives A ≥ 8.79σ; the 8.86σ on the paper is a close rounding. For Gaussian, 3.09 × 2 = 6.18σ.*

## Solution 3: Quantization SNR

Step size Δ = 2m_max/L = 2×2/256 = 2/128 = 1/64. Quantization noise power σ_q² = Δ²/12 = 1/(12 × 64²). The power of a signal uniformly distributed over [−2, 2] is P = ∫ x² (1/4) dx = (1/4)(x³/3) |₋₂² = (1/12)(2×2³) = 4/3. Hence

SNR₀ = P/σ_q² = (4/3)/(Δ²/12) = 16/Δ² = 16 × 64² = 2¹⁶ = (256)² = 65536 (48.16 dB).

## Solution 4: 16-PAM Telemetry

The average power is at most 10 dBm = 10 mW, the peak power is at most 30 dBm = 1 W (into 50 Ω); the symbol rate is R_s ≤ 12 Msymbols/s, so T_s ≥ 1/12 µs. The levels are taken as 0, a, 3a, 5a, …, 15a (a = √E₀).

a) E_av = (1/(M/2)) Σ a²(2i − 1)² = a² (M² − 1)/3 = a² × 255/3 = 85a²; E_peak = (15a)² = 225a².
Average power limit: P_av = E_av/T = 85a²/T ≤ 10 mW ⇒ a ≤ √(P_av T/85) = 3.13 µV. Peak power limit: P_peak = 225a²/T ≤ 1 W ⇒ a ≤ √(P_peak T/225) = 1.92×10⁻⁵ = 19.25 µV. The largest voltage spacing is 2a = 6.16 µV (this value is written on the paper).

b) The largest voltage spacing is limited by the average power requirement (the average power limit on a is smaller).

c) M = 16 ⇒ k = 4 bits/symbol; R_b = k R_s = 4 × 12 = 48 Mbit/s. The bit rate depends on the average power: P_av = E_av/T = E_av R_b/log₂M.

d) For N₀ = 10⁻¹² W/Hz, E_av/N₀ = 10 mW × T/N₀ = 10⁻² × (1/12)10⁻⁶ / 10⁻¹² = 10⁴/12 = 2500/3. Symbol error probability P_E(16) = (2×15/16) Q(√(6/255 × 2500/3)) = (15/8) Q(√19.61) ≈ 8.9×10⁻⁶. Bit error probability P_b ≈ P_E/4 = 2.23×10⁻⁶.

*Note: 2a is 6.26 µV with a = 3.13 µV (the 6.16 µV on the paper is a typographical slip). Also, T = (1/12) µs was used in the P_av T/85 calculation; the results are consistent with this assumption.*
