---
baslik: EEM441 Communications I: Angle Modulation and FM Lecture Slides (FM-1 … FM-29)
ozet: Scanned lecture slides covering phase and frequency modulation, narrowband and wideband FM, Carson's rule, Bessel functions, FM generation, demodulation, and PLLs.
---

Scans of the English-language slide printouts numbered FM-1 through FM-29 from the EEM441 Communications I course; 31 pages. The pages do not name the author of the slides. All of the scanned pages are in the PDF at the end of the post; the content is summarized below in page order.

## Angle Modulation and Basic Definitions (FM-1 … FM-4)

In angle modulation, the angle of the carrier is varied according to the message while the amplitude remains constant. The angle-modulated wave is s(t) = Ac cos[θi(t)]; the instantaneous frequency is fi(t) = (1/2π) dθi/dt. For an unmodulated carrier, θi = 2π fc t + φc and fi = fc.

- Phase modulation (PM): θi(t) = 2π fc t + kp m(t); fi(t) = fc + (kp/2π) dm/dt.
- Frequency modulation (FM): fi(t) = fc + kf m(t); θi(t) = 2π fc t + 2π kf ∫ m(τ)dτ.

In PM the phase is proportional to the message, and in FM the frequency is proportional to the message. Using integrator and differentiator circuits, a phase modulator can produce FM and vice versa: m(t) → integrator → phase modulator → FM; m(t) → differentiator → frequency modulator → PM.

**Example (instantaneous frequency).** The instantaneous frequency of the signal s(t) = 10 cos[2π·1000 t + 2π sin(10π t)] is found to be fi(t) = 1000 + 10 cos(10π t), and the peak frequency deviation is plotted; the second example shows that for a signal whose phase is a quadratic function of t, the instantaneous frequency increases linearly.

Comparison of AM and angle modulation: in angle modulation the envelope is constant (in AM it depends linearly on the message); the average transmitted power is Ac²/2; the zero crossings are not at a constant rate and carry message information; the modulated wave does not resemble the message waveform.

Single-tone FM: m(t) = Am cos(2π fm t), fi(t) = fc + kf Am cos(2π fm t), Δf = kf Am (maximum frequency deviation), modulation index β = Δf/fm; the FM signal is s(t) = Ac cos[2π fc t + β sin(2π fm t)]; narrowband FM has β ≪ 1 radian, wideband has β ≫ 1.

## Narrowband FM (FM-5, FM-6)

s(t) = Ac cos(2π fc t + β sin 2π fm t) = Ac cos φ cos(ωc t) − Ac sin φ sin(ωc t), φ(t) = β sin(2π fm t). When φ(t) ≪ 1 radian (≈ 57°), cos φ ≈ 1 and sin φ ≈ φ: s(t) ≈ Ac cos(ωc t) − Ac β sin(2π fm t) sin(ωc t) = Ac cos(ωc t) + (Ac β/2)[cos(ωc + ωm)t − cos(ωc − ωm)t].

Tone-modulated AM: s(t) = Ac cos(ωc t) + (μAc/2)[cos(ωc + ωm)t + cos(ωc − ωm)t]. The only difference is the sign of the lower sideband; therefore tone-modulated AM and narrowband FM have similar characteristics and the same transmission bandwidth. In the phasor comparison, the sidebands in AM change the amplitude along the same direction as the carrier, whereas in narrowband FM the sidebands are perpendicular to the carrier and change the phase.

Narrowband FM generation: φ(t) = 2π Δf ∫ m(t)dt is obtained with a block diagram consisting of an integrator, sine and cosine branches, a product modulator, and a summer.

## Wideband FM and Bessel Functions (FM-7 … FM-13)

The complex envelope of single-tone FM, s̃(t) = Ac e^{jβ sin(2π fm t)}, is periodic and can be expanded in a Fourier series: the coefficients are cn = Ac Jn(β), where Jn(β) = (1/2π) ∫ exp[j(β sin x − n x)] dx is the Bessel function of the first kind of order n. Thus

s(t) = Ac Σ Jn(β) cos[2π(fc + n fm)t], S(f) = (Ac/2) Σ Jn(β)[δ(f − fc − n fm) + δ(f + fc + n fm)].

Properties of Bessel functions: Jn(β) = (−1)ⁿ J−n(β); as β → 0, J0 → 1, J1 ≈ β/2, J2 ≈ β²/8; as β → ∞ they behave like damped sinusoids; ΣJn²(β) = 1.

Observations on the spectrum: it contains the carrier and an infinite number of lines at fc ± n fm. The carrier amplitude J0(β) depends on the modulation index; unlike in AM, the carrier amplitude is not constant and carries part of the message information. The total power is Ac²/2.

**Example (line spectrum of tone FM).** Ac = 100, fm = 4 kHz, Δf = 8 kHz, β = 2. J0..J5 = 0.22; 0.58; 0.35; 0.13; 0.03; < 0.01. For fc = 30 kHz, the sidebands are at |fc ± n fm| = |30 ± 4n| kHz; BT = 2 nmax fm = 2·4·4 = 32 kHz. For fc = 11 kHz, some of the sidebands fold over into negative frequencies (folded terms) and BT = 26 kHz. The effect of fm and Am on the spectrum (Δf fixed, fm varying; fm fixed, Am varying) is shown with normalized FM spectra.

## FM Transmission Bandwidth (FM-10, FM-11)

An FM signal contains an infinite number of sidebands; in practice the bandwidth is limited to a certain number of significant sidebands. Effective bandwidth (Carson's rule): BT ≈ 2Δf + 2fm = 2Δf(1 + 1/β) = 2fm(1 + β). A more accurate definition: the bandwidth extending to the farthest sideband whose amplitude is greater than 1% of the carrier; BT = 2 nmax fm, where nmax is the largest integer satisfying |Jn(β)| > 0.01.

| β | 0.1 | 0.3 | 0.5 | 1 | 2 | 5 | 10 | 20 | 30 |
|---|---|---|---|---|---|---|---|---|---|
| 2 nmax | 2 | 4 | 4 | 6 | 8 | 16 | 28 | 50 | 70 |

For an arbitrary modulating signal, the deviation ratio is D = Δf/W (W: the highest frequency of m(t)); D plays the role that β plays in the tone case. Example: Δf = 75 kHz, W = 15 kHz → D = 5; by Carson's rule BT = 2(75 + 15) = 180 kHz; with the universal 1% curve, BT ≥ 3.2 Δf = 240 kHz.

## FM Generation (FM-14 … FM-18)

There are two basic methods.

**Indirect FM (Armstrong).** The message is first integrated, and narrowband FM is generated in a narrowband phase modulator (with a crystal-controlled oscillator) while keeping β small; then the desired deviation is obtained with a frequency multiplier (memoryless nonlinear element + BPF). Frequency stability comes from the crystal oscillator. The output of the nonlinear element is v(t) = a1 s(t) + a2 s²(t) + … + an sⁿ(t); for an FM input signal, the nth harmonic at the output has fi'(t) = n fc + n kf m(t); the BPF bandwidth is n times that of the input, and β must be increased n-fold.

**Wideband FM modulator example.** Target: fc = 100 MHz, Δf = 75 kHz. In the phase modulator β1 ≈ 0.2 radian; for modulating frequencies of 100 Hz–15 kHz, Δf1 = 20 Hz and 3 kHz (low message frequencies are more critical). The total multiplication is 3750; two-stage multipliers n1 = 75 and n2 = 50, with an 8.5 MHz shift in the intermediate mixer (carrier frequency 0.1 MHz → 7.5 MHz → 2 MHz → 100 MHz; deviation 20 Hz → 1.5 kHz → 1.5 kHz → 75 kHz).

**Direct FM.** The instantaneous frequency of the carrier is varied directly by the message: voltage-controlled oscillator (VCO). Above 1 GHz, a klystron tube; at lower frequencies, an LC resonator tuned by a varactor (the capacitance of a reverse-biased p-n junction) (for example, a Hartley oscillator). For C(t) = C0 − ΔC m(t) and ΔC ≪ C0, fi(t) = f0 [1 + ΔC/(2C0) m(t)] = f0 + kf m(t), kf = f0 ΔC/(2C0).

Advantages: good oscillator stability is obtained (with frequency multipliers and a crystal), a constant proportionality between output frequency and input voltage, and a large frequency deviation can be achieved. Disadvantage: additional circuitry is required for frequency stability (a stable feedback structure: VCO, low-pass filter, mixer, crystal oscillator, frequency discriminator).

## FM Demodulation (FM-19 … FM-23)

Frequency demodulation is the recovery of the message from the FM wave. The output voltage of a frequency discriminator varies linearly with the instantaneous frequency. There are four approaches: FM-to-AM conversion (frequency discrimination), phase-shift discrimination, zero-crossing detector, and frequency feedback.

**Frequency discrimination.** Limiter → differentiator (d/dt) → envelope detector → DC block. At point A, s(t) = Ac cos[ωc t + 2π kf ∫m]; after the differentiator, s'(t) = −2π Ac [fc + kf m(t)] sin[...]; the envelope is proportional to 2π Ac[fc + kf m(t)]; removing the DC component yields m(t). **Balanced frequency discriminator:** two tuned circuits (fres > fc and fres < fc) widen the linear range; the transfer function approximates the desired linear amplitude response over a small frequency range (slope detection).

**Phase-shift discriminator.** It uses a circuit with a linear phase response (as opposed to the linear amplitude response in slope detection). Group delay and a phase shift of ωc T = π/2: output voltage ∝ dφ/dt ∝ kf m(t). It provides better linearity than the balanced discriminator.

**Zero-crossing detector.** Hard limiter + monostable pulse generator + low-pass filter (integrator) + DC block. At each upward or downward zero crossing of the FM signal, a short pulse of constant amplitude and duration is generated. The instantaneous frequency is fi = nT/T, where nT is the number of pulses in the interval T. The integrator output equals A·τ·fi(t); after the DC block it is ∝ m(t). Commercial zero-crossing detectors can operate with linearity better than 0.1% and up to 100 MHz.

**FM stereo multiplexing.** It is a form of frequency-division multiplexing; two separate channels are transmitted over the same carrier. It is used in FM radio broadcasting; it is compatible with mono receivers and operates within the allocated FM broadcast channel.

## Phase-Locked Loop, PLL (FM-24 … FM-26)

The PLL is a negative feedback system and is closely related to frequency modulation. Applications: synchronization, frequency division/multiplication, indirect frequency demodulation. Blocks: phase detector (multiplier), low-pass loop filter h(t), VCO. The VCO is a sinusoidal signal generator whose output frequency is determined by an externally applied voltage: s(t) = Ac sin[2π fc t + φ1(t)], φ1(t) = 2π kv ∫ m(t)dt; r(t) = Av cos[2π fc t + φ2(t)], φ2(t) = 2π kv ∫ v(t)dt. The goal is for the VCO output r(t) to have the same phase as the FM signal at the input, i.e., v(t) ∝ m(t).

Nonlinear model: e(t) = km Ac Av [sin(φe(t)) + high-frequency component]; φe = φ1 − φ2; v(t) = ∫ e(τ)h(t − τ)dτ; dφe/dt = dφ1/dt − 2π K0 ∫ sin φe(τ) h(t − τ)dτ, K0 = km kv Ac Av (loop gain parameter, Hz). The sinusoidal nonlinearity makes the analysis of PLL behavior difficult.

Linear model: when the phase error is small (φe ≪ 1 radian), sin φe ≈ φe: Φe(f) = Φ1(f)/(1 + L(f)), where L(f) = K0 H(f)/(jf) is the open-loop transfer function. If |L(f)| ≫ 1, then V(f) ≈ (jf/kv) Φ1(f)... and v(t) ≈ (kf/kv) m(t): the PLL is equivalent to a system that differentiates φ1 and operates like an FM demodulator.

## Nonlinear Effects (FM-27, FM-28)

Strong nonlinearity is introduced intentionally (frequency multiplier); weak nonlinearity, on the other hand, arises from imperfections of the components (amplitude nonlinearity). With v0 = a1 vi + a2 vi² + a3 vi³ and an FM signal at the input, second and third harmonics appear. The condition required to separate the desired FM signal is 2fc − (2Δf + W) > fc + Δf + W, and with a BPF at fc: fc > 3Δf + 2W.

FM signals are very sensitive to phase nonlinearity and insensitive to amplitude nonlinearity. The most common phase nonlinearity is AM-to-PM conversion; it is characterized by a constant K in degrees per dB (the peak phase change at the output for a 1 dB change in the input envelope). In a good microwave repeater, K < 2°/dB.

## Superheterodyne FM Receiver (FM-29)

The superheterodyne receiver performs carrier-frequency tuning (selecting the radio or TV signal), filtering (separating unwanted modulated signals), and amplification (compensating for the power loss during transmission), followed by demodulation. It overcomes the difficulty of building a tunable, high and variable Q filter by using an IF filter with a fixed center frequency and bandwidth; all radio and TV receivers are of the superheterodyne type. In an FM receiver the sequence is: antenna → RF section → mixer (local oscillator, common tuning) → IF section → limiter → frequency discriminator → audio amplifier → loudspeaker.

| Parameter | AM radio | FM radio |
|---|---|---|
| RF frequency | 535–1605 kHz | 88–108 MHz |
| IF midband frequency | 455 kHz | 10.7 MHz |
| IF bandwidth | 10 kHz | 200 kHz |

*Note: The slide transcription was written from a quick reading; a few values (especially the intermediate results of the example calculations) should be verified against the scanned pages. See the page scans for the figures and circuit diagrams.*

*This content belongs to slides distributed as part of the course; since it was distributed without attribution, it is shared for archival and nostalgic purposes. It will be removed at the request of the rights holder.*
