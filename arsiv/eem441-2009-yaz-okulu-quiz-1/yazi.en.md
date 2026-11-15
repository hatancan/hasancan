---
baslik: EEM441 Communications I: Summer School 2009 Quiz I (10 July 2009) and Its Solution
ozet: Mixing scheme with a nonlinear element, carrier amplitude, sideband power and carrier power for an amplitude-modulated signal; with handwritten solution.
---

Başkent University, Department of Electrical and Electronics Engineering, EEM 441 Communications I, Quiz I (10 July 2009, duration 1 hour): the questions and the handwritten solution. The exam paper and the solutions were transcribed to text from photographed pages; the photographs have not been published. For this reason there is no downloadable original file. Personal information (student number, name) has been removed.

## Questions

1. Given the voltage e₁ in the block diagram below: a) Find the voltage e₅. b) For A = 10, calculate the average power that the voltage e₅ produces across a 50 Ω resistor.

Block diagram: e₁(t) = cos ω₁t + cos 2ω₁t; e₁ splits into two branches. In the upper branch e₂ = A e₁²; in the lower branch a low-pass filter (cutoff 1.5 ω₁) gives e₃. e₄ = e₂ + e₃ passes through a band-pass filter (3.5 ω₁ – 5.5 ω₁) and becomes e₅.

2. Draw the block diagram of the product modulator used in generating amplitude-modulated signals. The modulating signal is given as f(t) = 12 cos(2π 3 10³ t) volts. To obtain an amplitude-modulated signal with a modulation percentage of 80%: a) What must the carrier amplitude be, in volts? Calculate it. How is the resulting amplitude-modulated signal affected if the carrier amplitude is smaller than 12 volts? What is this condition called? b) Taking the carrier frequency as 30 kHz, write the mathematical expression of the amplitude-modulated signal for the values given above, draw its double-sided frequency spectrum indicating the values, and find the bandwidth. c) Calculate the carrier power and the total sideband power that the resulting amplitude-modulated signal produces across a 50 Ω resistor.

## Solution 1

e₂ = A[cos ω₁t + cos 2ω₁t]² = A cos²ω₁t + 2A cos ω₁t cos 2ω₁t + A cos²2ω₁t
= A/2 (1 + cos 2ω₁t) + A[cos(2ω₁ − ω₁)t + cos(2ω₁ + ω₁)t] + A/2 (1 + cos 4ω₁t)
= A/2 + (A/2) cos 2ω₁t + A cos ω₁t + A cos 3ω₁t + A/2 + (A/2) cos 4ω₁t.

e₃ = cos ω₁t (the low-pass filter cuts everything above 1.5ω₁). e₄ = e₂ + e₃ (sum). The band-pass filter passes only the range 3.5ω₁–5.5ω₁; only 4ω₁ lies in it:

a) e₅ = (A/2) cos 4ω₁t.

b) P_avg = (A/2 / √2)² / 50 = A²/(8 × 50) = 10²/400 = 1/4 W (A = 10).

## Solution 2

Product modulator: m f(t) is first multiplied by the carrier f_c(t) = A_c cos 2π f_c t, and the result is added to the carrier: f_AM(t) = A_c[1 + m f(t)] cos ω_c t. Modulation m = 80% = 0.8.

a) m = A_m/A_c ⇒ A_c = A_m/m = 12/0.8 = 15 V. If A_c < 12 V, then m > 1; this is called overmodulation, and in the amplitude-modulated signal it causes phase reversal and envelope distortion.

b) For f_c = 30 kHz, f_c(t) = 15 cos 2π(30×10³)t. The expansion written on the paper: f_AM(t) = 15 cos 2π30×10³t + 72 cos 2π(27×10³)t + 72 cos 2π(33×10³)t (carrier, lower sideband, upper sideband); the plot: lines of 15/2 at ±30 kHz and 72/2 at ±27 and ±33 kHz; bandwidth BW = 6 kHz.

c) P_c = (15/√2)² / 50 = 2.25 W; the sideband power is written on the paper as (72/√2)²/50 + (72/√2)²/50 = 103.68 W.

*Note: The sideband amplitude of 72 V on the paper comes from multiplying the expression m·f(t) by 0.8 × 12 = 9.6 and then by 15 (15 × 9.6 / 2 = 72); however, m is already the modulation index, which relates the amplitude of f(t) to A_c. The correct expression is f_AM(t) = [A_c + f(t)] cos ω_c t = 15 cos ω_c t + 6 cos 2π27×10³t + 6 cos 2π33×10³t (sideband peak amplitude mA_c/2 = 6 V); in this case P_c = 2.25 W, each sideband is 6²/(2×50) = 0.36 W, and the total sideband power is 0.72 W (= m²/2 · P_c). The bandwidth is 6 kHz and does not change.*
