---
baslik: EEM441 Communications I: 2013 summer school EEM 442 Communications II final exam and solutions
ozet: EEM 442 summer school final: QPSK symbol sequence with a raised-cosine filter, choice of M and R for PCM and receiver power, slope overload in delta modulation, TDM-PCM bit rate and bandwidth.
---

This document belongs to the EEM 442 Communications II course; it is published here because it was found in the EEM 441 folder. It is the Başkent University EEM 442 Communications II summer school final exam (the date on the paper reads "…/8/2013", duration 110 minutes; the day is illegible) and its handwritten solutions. The exam paper and solutions were transcribed to text from photographed pages; the photographs are not published. For this reason there is no original file to download. Personal information (student number, name) has been removed. Since the exam papers were sideways-rotated photographs, the transcription was done carefully. The content of a printed solution page from a textbook is summarized in this post by its result only.

## Questions

1. Consider a communication system with a raised-cosine filter with roll-off factor α = 0, operating at a bit rate of 2 Mbps. The modulation is M = 4 phase modulation, using the mapping {00, 01, 11, 10} ⇒ {1+j, −1+j, −1−j, 1−j}. The symbol sequence applied to the input of the raised-cosine filter is s(0), s(T_s), s(2T_s), s(3T_s) = [1+j, −1−j, −1+j, −1+j]. a) Write the impulse response function. b) Calculate the average energy per symbol. c) Calculate the bit duration, the symbol rate, and the symbol duration. d) Using the impulse response function found in part a), and assuming the sampler samples synchronously, find the output at the sampling instants (t = 0, T_s, 2T_s, 3T_s, 4T_s, …) and sketch its graph.
2. A signal with bandwidth W = 15 kHz is transmitted as an M-ary PCM signal over a channel with noise power spectral density N₀ = 0.01 µW/Hz and transmission bandwidth B_T = 40 kHz. a) Calculate the smallest M and R values for SNR₀ ≥ 40 dB. b) Assuming the PCM signal uses the entire transmission bandwidth, with P_e < 10⁻⁵ and P_peak/P = 2, what should the minimum received power be in order to operate above the threshold signal-to-noise ratio?
3. A ramp signal x(t) = a·t is applied to a delta modulator (DM) with sampling period T_s and step size Δ. a) Determine the conditions under which slope-overload distortion occurs. b) For three step-size values, Δ = 0.75 a T_s, Δ = a T_s, and Δ = 1.25 a T_s, sketch the DM modulator output starting from zero.
4. A digital communication system transmits eight message signals, each with a bandwidth of 4 kHz, time-division multiplexed, using a binary uniformly quantized PCM system. The sampling rate must be at least 50 percent above the Nyquist rate; the sampling error must not exceed 1 percent of the peak amplitude. a) Calculate the sampling rate. b) Calculate the number of quantization levels and the number of bits per sample. c) Calculate the total bit rate for the multiplexed message signal. d) Calculate the transmission bandwidth of the digital communication system.

The exam paper also has a "Useful formulas" page: for the observation vector r(T) = ±A + n(T), P_b = p₁Q((A − λ)/σ) + (1 − p₁)Q((A + λ)/σ); Q(3.09023) = 10⁻³, Q(√20) = 3.87×10⁻⁶; B_T = (R_s/2)(1 + α); SNR₀ = 3×2^(2R)/α, α = peak power/average power; for binary correlated signaling, P_b = Q(√(E_s(1 − ρ)/N₀)); for M-PSK, P_s = 2Q(√(2E_s/N₀) sin(π/M)); sinc(2Wt) ⇔ (1/2W)Π(f/2W); (1/(M/2))Σ(2i − 1)² = (M² − 1)/3; for M-PAM, P_E(M) = [2(M − 1)/M] Q(√(6E_s,av/((M² − 1)N₀))).

## Solution 1: Raised-cosine, α = 0

Symbol sequence {00, 01, 11, 10} ⇒ {1+j, −1+j, −1−j, 1−j}; in the solution on the paper, s(0), s(T_s), s(2T_s), s(3T_s) = {1+j, −1+j, −1−j, 1−j} is taken in order (for α = 0, W = 1/(2T_s)).

a) p(t) = sinc(2Wt) = sinc(t/T_s) (α = 0).
b) Average energy per symbol: E_s = |1 ± j|² = 2.
c) Bit rate R_b = 2 Mbps ⇒ bit duration T_b = 0.5 µs; symbol rate R_s = R_b/2 = 1 Msymbol/s ⇒ symbol duration T_s = 1/R_s = 1 µs.
d) Sampling instant = symbol duration: T_s = 1 µs. The output is the sum of shifted sinc pulses, one for each symbol; since at exactly t = kT_s only the pulse of the corresponding symbol is nonzero (no ISI), the output takes the values 00 → 1+j, 01 → −1+j, 11 → −1−j, 10 → 1−j at the instants 0, T_s, 2T_s, 3T_s, respectively.

## Solution 2: M, R, and receiver power for PCM

SNR₀ = 3L²/α, α = 2 ⇒ (3/2) L² > 10⁴ ⇒ L² = (2/3)10⁴ ⇒ L > 81.6.

On the paper, the symbol rate is written as R_s = f_s R/log₂M = 2WR/log₂M and B ≥ 1/(2T_s) = R_s/2; from this, B ≈ W R is obtained. With B_T = 40 kHz, R < B_T/W = 40 kHz/15 kHz ⇒ R = 2 (written as 2.5 on the paper). L = M^R > 81.6 ⇒ M² > 81.6 ⇒ M = 10 and L = M² = 100.

Threshold SNR: SNR_th = (6B/W)(M² − 1) = (6×40 kHz/15 kHz)(100 − 1) = 16 × 99 ≈ 1600.
Received power: P_r = N₀ W SNR_th = 10⁻⁸ × 15×10³ × 1.6×10³ = 0.24 W = 240 mW.

*Note: The paper writes "R < B/W = 2.5"; 40/15 = 2.67. The result (R = 2) does not change.*

## Solution 3: Delta modulation and slope overload

a) In one period T_s, the input signal increases by aT_s, whereas the output of the delta modulator can change by at most Δ. Slope-overload distortion occurs when Δ < aT_s, i.e., when Δ/T_s < a.

b) Δ = 0.75 aT_s: the output continually lags behind the input (slope overload); Δ = aT_s: the output follows the input step by step (boundary case); Δ = 1.25 aT_s: the output follows the input and exhibits small oscillation between steps, with no slope overload (granular noise).

*Note: The photograph for this part is a printed page from the textbook solution manual; therefore only its result is summarized, and the printed drawings have not been transcribed. The printed statement on the paper is read in one place as something like "Δ ≳ aT_s"; the correct condition for slope overload is Δ < aT_s.*

## Solution 4: 8-signal TDM-PCM

W = 4 kHz.

a) f_s = 1.5 × 2 × W = 1.5 × 2 × 4 kHz = 12000 samples/s.
b) Sampling (quantization) error: Δ/2 = m_peak/L ≤ 0.01 m_peak ⇒ L ≥ 100; L = 2^R ≥ 100 ⇒ R = 7 bits/sample, L = 128.
c) Each sample is coded with R = 7 bits. The bit rate per signal is R_b = R f_s = 7 × 12000 = 84000 bps; when 8 signals are multiplexed, the total is R_B = 8 × 84000 = 672000 bps = 672 kbps.
d) The minimum required transmission bandwidth is B_T = 1/(2T_b) = R_b/2 = 336 kHz.
