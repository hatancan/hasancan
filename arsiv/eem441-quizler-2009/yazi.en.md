---
baslik: EEM441 Communications I: 2009 Quizzes (Quiz 1 and Quiz 3, with Solutions)
ozet: EEM441 Communications I 2009 quizzes: product modulator and square-law receiver, amplitude modulated signal and power, SSB phase-shift method, FM frequency multiplier chain and FM demodulators.
---

The three quizzes given in 2009 for the EEM 441 Communications I course in the Department of Electrical and Electronics Engineering at Başkent University: Quiz 1 on 10 July 2009 (summer school), Quiz 1 on 19 November 2009, and Quiz 3 on 22 December 2009. The sources are phone photographs of the exam papers and handwritten solutions; the content was transcribed from the photographed pages into text, and the photographs were not published. The solutions come from a friend's handwritten notes; personal information has been removed.

## Quiz 1, 10 July 2009 (duration 1 hour)

**Question 1.** In the block diagram shown, e₁(t) = cos ω₁t + cos 2ω₁t goes in parallel to a square-law device e₂ = A·e₁² and to an LPF (cutoff 1.5ω₁); after the sum (e₄), the output of a BPF passing the 3.5ω₁–5.5ω₁ band is e₅. a) Find e₅. b) For A = 10, calculate the average power that e₅ produces in a 50 Ω resistor.

*Solution.* e₂ = A/2 + (A/2)cos 2ω₁t + A cos ω₁t + A cos 3ω₁t + A/2 + (A/2)cos 4ω₁t; e₃ = cos ω₁t; e₄ = e₂ + e₃. The BPF passes only the 4ω₁ component: e₅ = (A/2)cos 4ω₁t. P = (A/2)²/(2·50) = A²/400 = 100/400 = 1/4 W.

**Question 2.** Draw the block diagram of a product modulator. For an amplitude modulated signal with modulating signal f(t) = 12cos(2π·3×10³t) V and a modulation percentage of 80%: a) What must the carrier amplitude be in V? What happens (give its name) if the carrier amplitude is smaller than 12 V? b) For a carrier frequency of 30 kHz, give the expression of the amplitude modulated signal, its double-sided frequency spectrum, and its bandwidth. c) Find the carrier power and the total sideband power in a 50 Ω resistor.

*Solution.* m = A_m/A_c = 0.8 ⇒ A_c = 12/0.8 = 15 V. If A_c < 12 V, then m > 1: overmodulation; phase reversal and envelope distortion occur. s(t) = A_c[1 + m cos(2π·3×10³t)]cos(2π·30×10³t) = 15cos(2π·30k t) + 6cos(2π·27k t) + 6cos(2π·33k t): the carrier is 15 V (30 kHz), and the lower and upper sidebands are each 6 V (27 and 33 kHz). Bandwidth is 6 kHz. P_c = (15/√2)²/50 = 2.25 W; sideband power is 2 × (6/√2)²/50 = 0.72 W.

*Note: In the handwritten solution, the sideband amplitude was taken as "m·f(t)" with 0.8×12×15 = 144, giving 72 V and a total sideband power of 103.68 W; this is wrong because the product was formed with a non-normalized message. The correct result is μA_c/2 = 6 V per sideband and 0.72 W.*

## Quiz 1, 19 November 2009 (duration 1 hour)

**Question 1.** A periodic modulating signal f(t) is shown in the figure (peak value 5, minimum value −2, a sine-like wave with a period of a few ms). a) What is the minimum carrier amplitude required for amplitude modulation? What kinds of distortion occur if the carrier amplitude is smaller than this value? What is the mathematical expression of the amplitude modulated signal? b) Sketch the resulting AM signal, indicating values. c) If the carrier frequency is taken as 100 kHz, sketch the frequency spectrum of the AM signal, indicating values.

**Question 2.** In the block diagram that produces an SSB signal by the phase-shift method, there are blank boxes (f₁(t), f₂(t), f₃(t), f₄(t) and f_SSB(t)). a) Fill in the necessary information in the blank boxes. b) If f(t) = Σ cos(ω_i t + θ_i) and the carrier is f_c(t) = cos(ω_c t), show that v(t) = Σ[cos(ω_c t)cos(ω_i t + θ_i) − sin(ω_c t)sin(ω_i t + θ_i)] is an SSB signal (ω_c ≫ ω_N); does it represent the lower or the upper sideband? c) Give the expression for the other sideband. d) Give the total DSB signal. e) If the SSB signal in part (b) is multiplied by cos(ω_c t) and passed through a low-pass filter, the information-bearing signal is obtained; sketch the frequency spectrum of the signal at the multiplier output and state the range of the LPF cutoff frequency f₀ (in terms of ω_c, ω₁, … ω_N).

*The photographs of this quiz contain only the questions; there is no solution.*

## Quiz 3, 22 December 2009 (duration 1 hour)

**Question 1.** In the block diagram, the signal f₁(t) is a narrowband FM signal obtained by frequency modulating the modulating signal f(t) onto a carrier of f_c1 = 2 MHz; the maximum value of β₁ is 0.5. The modulating signal is f(t) = cos(2π10³t) + cos(2π·5·10³t) + cos(2π·8·10³t). The frequency multipliers are ×10 and ×n; between them there are a mixer and an oscillator f_LO; the output f₅(t) is to be a wideband FM signal with carrier frequency f_c5 = 96 MHz and maximum frequency deviation Δf₅ = 80 kHz. a) Find n and f_LO. b) Find the maximum frequency deviations at points 1, 2 and 4 (Δf₁, Δf₂, Δf₄). c) Find the bandwidths at points 1, 2, 4 and 5.

*Solution.* f_m,min = 1 kHz, f_m,max = 8 kHz. β₅ = Δf₅/f_m,min = 80 kHz/1 kHz = 80; β₁ must be 0.5 ⇒ 10n = 80/0.5 ⇒ **n = 16**. f_c2 = 10 × 2 = 20 MHz; f_c4 = 96/16 = 6 MHz; f_LO = f_c2 ± f_c4 = 26 MHz or 14 MHz. Δf₁ = 80 000/160 = 500 Hz, Δf₂ = 10Δf₁ = 5 kHz, Δf₄ = Δf₂ = 5 kHz (Δf₅ = 16 × 5 kHz = 80 kHz). Bandwidths: B₁ = 2f_m,max = 16 kHz; β₂ = 5000/8000 = 0.625 (narrowband) ⇒ B₂ = B₄ = 16 kHz; β₅ = 80 000/8000 = 10 (wideband) ⇒ B₅ = 2(1 + 10)·8 kHz = 176 kHz (≈ 2Δf = 160 kHz).

**Question 2.** a) The functions of the limiter and the discriminator used in FM receivers; the blocks that make up these circuits. b) Block diagrams of the following methods used for demodulating FM signals: i) zero-crossing demodulator, ii) phase-locked loop, iii) FM demodulator with feedback.

*Solution summary.* Limiter: consists of a high-gain amplifier (hard limiter) and a band-pass filter; it keeps the amplitude of the FM signal at the discriminator input constant. Discriminator: takes the derivative of the phase of the input signal; it consists of a differentiator and an envelope detector. Zero-crossing demodulator: FM signal → limiter → pulse generator → low-pass filter → information signal. Delay-line demodulator: the limiter output is added to its delayed version, and the information signal is obtained with a half-wave rectifier and a low-pass (LPF) envelope detector. (The solution page cites Haykin p. 374 and METU p. 266 as sources.)
