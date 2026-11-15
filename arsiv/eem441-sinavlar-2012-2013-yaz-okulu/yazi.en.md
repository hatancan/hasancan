---
baslik: EEM441 Communications I: Summer School Exams of 2012 and 2013 (Questions and Solutions)
ozet: The August 2012 midterm, final and quiz, and the August 2013 final of EEM441 Communications Systems I: phasor diagram, FM band limiting, FDM filter design, AM spectrum and power.
---

The summer school exams of 2012 and 2013 for the Başkent University EEM 441 Communications Systems I course: the final of 7 August 2012, the midterm of 10 August 2012, Quiz 2 of 13 August 2012, and the final of 14 August 2013. The sources are phone photographs of the exam papers and handwritten solutions; the content was transcribed from the photographed pages, and the photographs were not published. The solutions are from a friend's handwritten notes; personal information (name, number) was removed.

## Midterm, 10 August 2012 (duration 90 min)

**Question 1.** Draw the phasor diagram for the amplitude-modulated signal v(t) = v₁(t)cos(ω_ct) + v₂(t)cos(ω_ct + α). Using the phasor diagram, find the components v_I(t) and v_Q(t), the envelope A(t), and the phase angle φ(t). Repeat the calculations for |v₂(t)| ≪ |v₁(t)|.

*Solution.* v_I = v₁ + v₂cos α, v_Q = v₂sin α; A(t) = √(v₁² + 2v₁v₂cos α + v₂²) ≈ v₁ + v₂cos α; φ(t) = arctan[v₂sin α/(v₁ + v₂cos α)] ≈ v₂sin α/v₁.

**Question 2.** An FM signal modulated by a voice signal with a bandwidth of 4 kHz and a modulation index of β = 2 is applied to a BPF with center frequency f_c and bandwidth 8500 Hz. Draw the frequency spectrum and the phasor diagram of the FM signal; calculate and sketch the envelope of the output signal.

*Solution.* f_m = 4 kHz; J₀(2) ≈ 0.22, J₁(2) ≈ 0.58. The BPF passes only the carrier and the first sidebands (f_c ± 4 kHz): the spectrum has lines of 0.22A_c at f_c, +0.58A_c at f_c + 4 kHz, and −0.58A_c at f_c − 4 kHz (the second sidebands are at 8 kHz, outside the band). In the phasor diagram, two 0.58A_c phasors rotating in opposite directions are added to the carrier phasor; the resultant vertical component is 2 × 0.58 = 1.16A_c. The envelope has A_min = 0.22A_c and A_max = √(0.22² + 1.16²)A_c ≈ 1.18A_c; A(t) fluctuates at twice the rate of f_m (period 1/2f_m).

**Question 3.** An FM signal is applied to the input of a frequency multiplier; the BPF inside the multiplier is tuned to a center of 2f_c. Sketch the spectrum at the input and output of the BPF; write the condition on Δf for successful operation in terms of f_c and W.

*Solution.* β = k_fA_m/f_m = Δf/f_m; the bandwidth of the signal multiplied by n is B_n ≈ 2(nβ + 1)W. The spectra lie around f_c, 2f_c, 3f_c with widths B₁, B₂, B₃. For no overlap, f_c + B₁/2 < 2f_c − B₂/2 and 2f_c + B₂/2 < 3f_c − B₃/2; from this f_c > (B₂ + B₃)/2 = 5Δf + 2W and **Δf < (f_c − 2W)/5**.

**Question 4.** The envelope amplitude of an amplitude-modulated signal varies between 5 and 15 V; the frequency of the information signal is 1 kHz and the carrier frequency is 100 kHz. a) The time-domain expression, b) the two-sided frequency spectrum, c) the power dissipated in a 100 Ω resistor by the carrier, the lower sideband and the upper sideband, d) the bandwidth, e) what should be done to increase the sideband power?

*Solution.* A_c = (15 + 5)/2 = 10 V; μ = (15 − 5)/(15 + 5) = 0.5. s(t) = 10[1 + 0.5cos(2π·10³t)]cos(2π·100·10³t) = 10cos(2π·100k·t) + 2.5cos(2π·99k·t) + 2.5cos(2π·101k·t). B = 2f_m = 2 kHz. In R = 100 Ω, P_c = (10²/2)/100 = 0.5 W, and for each sideband (2.5²/2)/100 ≈ 31 mW. To increase the sideband power, the modulation index (μ) must be increased.

*Note: In the handwritten solution, the sideband amplitudes are given as 1 V (the spectrum is written as 5, ½, ½) and the sideband power as 5 mW; since the sideband amplitude in the expansion s(t) = A_c[1 + μ cos ω_mt]cos ω_ct is μA_c/2 = 2.5 V, the values above are given in corrected form.*

## Quiz 2, 13 August 2012 (duration 1 hour)

**Question 1.** At a radio transmitter station, f_m = 20 kHz, β = 1.0, A_c = 100 and f_c = 30 kHz are given. Derive the appropriate formula for the frequency-modulated signal s(t), sketch its frequency spectrum, and show that S_T < A_c²/2; calculate the bandwidth of the system.

*Solution summary.* f_i(t) = f_c + βf_m cos(2πf_mt) = 30 + 20cos(40πt) kHz. Bessel coefficients J₀(1) = 0.77, J₁(1) = 0.44, J₂(1) = 0.11, J₃(1) = 0.02: the lines have amplitudes 77, 44, 11, 2 (77 at f_c = 30 kHz, ±44 at 50 and 10 kHz, ±11 at 70 and −10 kHz, ±2 at 90 and −30 kHz); lines falling at negative frequencies are folded over. The bandwidth is marked in the handwritten notes as 80 kHz (Carson ≈ 2(β + 1)f_m = 80 kHz) and 120 kHz.

*Note: The total power calculation in the handwritten notes gives a result of 4390 and compares it with A_c²/2 = 5000; there is a numerical inconsistency in the sum of the folded lines (−33, 75, 11, 2), so the number should be verified separately.*

## Final, 7 August 2012 (duration 110 min)

1. In a circuit whose input signal is tone-modulated SSB, the local oscillator has a phase error φ' (envelope detector, with A_LO cos(ω_ct ± φ') added to the signal). Using the phasor diagram, derive the signal envelope equation; show that for A_LO ≫ A_cA_m, A(t) ≈ A_LO + ½A_cA_m cos(ω_mt ± φ').
2. For m(t) = cos(ω_mt) − (1/3)cos(3ω_mt), derive the SSB formula. Using the square-wave approximation, calculate the envelope A(t) of the SSB signal; for A_c = 2, sketch A(t) and m(t) and compare them.
3. 12 voice signals, whose components outside 300 < |f| < 3300 Hz are neglected, are multiplexed by SSB subcarrier modulation with a guard band B_gb left between channels. At the receiver, the transfer function of the BPFs tuned to center frequency f₀ for each subcarrier is |H(f)| = exp{−[1.2(f − f₀)/W]²}; find the value of B_gb that satisfies the adjacent-channel response |H(f)| ≤ 0.1, and the transmission bandwidth of the FDM system.
4. For a tone-modulated FM signal with A_c = 1 and β = 1, sketch the phasor diagrams at the instants ω_mt = 0, π/4, π/2; calculate the envelope A(t) and the phase φ(t) for each.

*The photographs of this exam contain only the question paper.*

## Final, 14 August 2013 (duration 110 min)

**Question 1.** In a telephone exchange, voice channels are separated at the receiver by bandpass filters with transfer function |H(f)| = 1/√(1 + [2(f − f₀)/B]^(2n)). Neglecting the components of the baseband voice signal outside 300 < |f| < 3300 Hz, sketch the spectrum of three adjacent channels in the group spectrum; find B, f₀ and n such that |H(f)| ≤ 0.1 outside the desired passband.

*Solution.* The subcarriers are spaced 4 kHz apart; each channel is 3 kHz wide and is placed with a 300 Hz upper-sideband margin between neighbors. Take B = 3 kHz and f₀ = f_i − 0.3 kHz − B/2 = f_i − 1.8 kHz; the nearest component of the adjacent channel is B/2 + 1 kHz = 2.5 kHz away from the edge of the passband. For |H|² ≤ 0.01: 1 + (2 × 2.5/3)^(2n) ≥ 100 ⇒ (5/3)^(2n) ≥ 99 ⇒ 2n·log(5/3) ≥ log 99 ⇒ n ≥ 4.5, so **n = 5**.

**Question 2.** A tone-modulated FM signal with modulation index β = 2 and a highest information-signal component of f_m = 200 Hz is applied to a BPF with center frequency f_c and bandwidth 750 Hz. Sketch the FM spectrum and the phasor diagram; calculate and sketch the envelope of the output signal.

*Solution.* This has the same structure as Question 2 of the 2012 midterm: only the carrier (0.22A_c) and the f_c ± 200 Hz sidebands (±0.58A_c) pass through the filter; A_min = 0.22A_c, A_max ≈ 1.18A_c.

**Question 3.** Video signals of unit amplitude are transmitted by DSB-SC modulation. Draw the phasor diagram for a tone-modulated DSB-SC signal. If the width of the lower sideband is halved, calculate the envelope A(t) and the phase angle φ(t) of the DSB-SC modulated signal using the phasor diagram.

*Solution.* For a tone, x_c(t) = A_c cos ω_ct·cos ω_mt = (A_c/2)cos(ω_c − ω_m)t + (A_c/2)cos(ω_c + ω_m)t. When the lower sideband is halved (A_c/4): v_I = (A_c/2)cos ω_mt + (A_c/4)cos ω_mt = (3/4)A_c cos ω_mt, v_Q = (A_c/2)sin ω_mt − (A_c/4)sin ω_mt = (A_c/4)sin ω_mt. A(t) = (A_c/4)√(9cos²ω_mt + sin²ω_mt) = (A_c/4)√(5 + 4cos 2ω_mt); φ(t) = arctan[(tan ω_mt)/3].

**Question 4.** a) With f_m ≪ f_c and m(t) = cos(2πf_mt)u(t), for amplitude modulation: sketch the envelopes for DSB and for AM with μ < 1 and μ > 1; indicate the amplitude values. b) Repeat the same question for T ≫ 1/f_c with m(t) = 0.5u(t) − 1.5u(t − T).

*The solution page contains envelope sketches (AM near μ = 1, and DSB); there is no numerical expression that can be transcribed into text.*
