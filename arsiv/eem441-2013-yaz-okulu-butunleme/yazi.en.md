---
baslik: EEM441 Communications I: 2013 Summer School Make-up Exam and Solutions
ozet: EEM 441 summer school make-up exam: FDM channel guard band, FM frequency multiplier, down-converter placement for an FM signal, and AM tone calculations; with handwritten solutions.
---

Başkent University EEM 441 Communication Systems I, 2013 summer school make-up exam (duration 90 minutes; the date on the paper reads "…/8/2013", the day is unclear) and handwritten solutions. The exam paper and solutions were transcribed to text from photographed pages; the photographs have not been published. For this reason there is no downloadable original file. Personal information (student number, name) has been removed.

## Questions

1. 12 voice signals, each with bandwidth f_m, are multiplexed by SSB subcarrier modulation and frequency-division multiplexing to form a group. The guard band between channels is B_g. The center frequency f₀ of the BPFs, whose frequency response is |H(f)| = exp{−[1.2(f − f₀)/f_m]²}, is adjusted for each subcarrier. Calculate B_g so that the adjacent-channel response satisfies |H(f)| ≤ 0.1. Find the transmission bandwidth of the frequency-division multiplexing system.
2. An FM signal is applied to the input of a frequency multiplier. The center frequency of the BPF inside the frequency multiplier is set to 2f_c. Sketch the spectrum at the input and output of the BPF. Write the condition on Δf for successful operation in terms of f_c and W.
3. The audio section of a television transmitter is an indirect FM system with W = 10 kHz, D = 2.5 and f_c = 4.5 MHz. For a frequency deviation φ_Δ/2πT < 20 Hz and f_c = 200 kHz, draw the block diagram of this system. Using the shortest chain consisting of frequency doublers and triplers, and ensuring that the frequency does not exceed 100 MHz, determine the location of the down-converter.
4. The envelope amplitude of an amplitude-modulated signal varies between 5 and 15 V. The frequency of the information signal is 1 kHz and the carrier frequency is 100 kHz. a) Calculate the time-domain expression of the amplitude-modulated signal, stating the values. b) Sketch the two-sided frequency spectrum. c) Calculate the power dissipated in a 100 Ω resistor by the carrier, the lower sideband and the upper sideband. d) Calculate the bandwidth of the system. e) State what must be done to increase the power of the sidebands.

## Solution 1

The condition |H(f)| ≤ 0.1 is sought for |f − f₀| ≥ W/2 + B_g (W = f_m). exp{−[1.2x]²} ≤ 0.1 ⇒ 1.2x ≥ √(ln 10) ⇒ x = (W/2 + B_g)/W ≥ (1/1.2)√(ln(1/0.1)) ≈ 1.26.

Hence B_g ≥ 0.76 W. Transmission bandwidth: B_T = 12 W + 11 B_g ≥ 21 W (11 × 0.76 W ≈ 9 W). The figure shows the guard bands B_g between adjacent channels.

## Solution 2

β = k_f A_m / f_m = Δf / f_m (k_f = Δf / A_m). At the output of the n-th multiplier, nφ(t) = 2π (nΔf) ∫x(λ)dλ and B_n ≈ 2(nβ + 1) W. Three spectral regions (B₁, B₂, B₃) are seen around f_c, 2f_c, 3f_c in the output spectrum.

So that the upper regions do not overlap, the conditions f_c + B₁/2 < 2f_c − B₂/2 and 2f_c + B₂/2 < 3f_c − B₃/2 are written. From this f_c > ½(B₂ + B₃) = [(2β + 1) + (3β + 1)]W = 5Δf + 2W; that is, Δf < (f_c − 2W)/5.

## Solution 3: Indirect (Armstrong) FM

Δf = W × D = 10 × 2.5 = 25 kHz. The deviation at the narrowband FM output must satisfy φ_Δ/2πT < 20 Hz: n = 25000 / 20 = 1250. One doubler and six triplers give n = 2 × 3⁶ = 1458; φ_Δ/2πT = 25 kHz / 1458 = 17.1 Hz < 20 Hz.

Carrier: 200 kHz × 1458 = 291.6 MHz > 100 MHz. Therefore a down-converter is used before the last tripler; there the frequency is 291.6/3 = 97.2 MHz < 100 MHz. Down-converter: f_LO = 97.2 − (4.5/3) = 95.7 MHz; the BPF output is 1.5 MHz; then ×3 gives f_c = 4.5 MHz and Δf = 25 kHz.

Diagram: x(t) → NBFM (f_c = 200 kHz) → multiplier chain (×2 and triplers, total n = 1458/3 = 486) → 97.2 MHz → mixer (f_LO = 95.7 MHz) → BPF (1.5 MHz) → ×3 → f_c = 4.5 MHz, Δf = 25 kHz.

*Note: The value n = 2×3⁶ = 1458 in the text requires one doubler and six triplers; in the diagram on the paper, however, 2×3×3×3×3 (four triplers) appears before the down-converter, followed by a single ×3. There is an inconsistency between the diagram and the text; the calculation is given according to the values in the text.*

## Solution 4: Amplitude modulation

a) A_c = (A_max + A_min)/2 = (15 + 5)/2 = 10; μ = (A_max − A_min)/(A_max + A_min) = (15 − 5)/(15 + 5) = 0.5. f_m = 1 kHz (ω_m = 2π·10³ rad/s), f_c = 100 kHz (ω_c = 2π·10⁵ rad/s).

f_AM(t) = 10 [1 + 0.5 cos(2π·10³ t)] cos(2π·100·10³ t) = 10 cos(2π·100·10³ t) + 2.5 cos(2π·99·10³ t) + 2.5 cos(2π·101·10³ t).

b) Two-sided spectrum: lines of amplitude 5 at ±100 kHz, lines of amplitude 1.25 at ±99 and ±101 kHz (each line is half the peak amplitude).

c) For 100 Ω: P_carrier = (10/√2)² / 100 = 0.5 W; for each sideband P = (2.5/√2)² / 100 = 0.03125 W ≈ 31.25 mW.

d) B = 2 f_m = 2 × 1000 = 2000 Hz = 2 kHz.

e) To increase the power of the sidebands, the modulation index must be increased (within the limit μ ≤ 1).

*Note: In the handwritten solution the sideband amplitudes are shown as 1 and as 1/2 in the spectrum, and the power is written as 10 mW; the numbers above are the transcriber's own calculation (sideband amplitude μA_c/2 = 2.5 V). On the paper, the carrier power is found as 1/2 W with R = 2×50 = 100 Ω.*
