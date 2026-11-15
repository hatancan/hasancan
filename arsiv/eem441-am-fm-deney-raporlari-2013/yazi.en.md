---
baslik: EEM441 Communications I: 2013 AM and FM Lab Reports
ozet: Text of the AM modulation index, 455 kHz intermediate frequency, and FM lab observations, with personal information removed.
---

The AM and FM lab reports dated 26 December 2013, together with short reports containing the same measurements, have been transcribed into text with personal information removed. The lab photographs are kept in a private archive; this post has no downloadable file.

## Amplitude modulation

The report defines the carrier as Vc = Ec cos(ωc t) and the single-tone message as Vm = Em cos(ωm t). The full AM signal is:

VAM = [Ec + Em cos(ωm t)] cos(ωc t) = Ec[1 + m cos(ωm t)] cos(ωc t), m = Em/Ec.

Expanding this yields the carrier together with the sideband frequencies fc − fm and fc + fm. The amplitude of each sideband is mEc/2. If the message bandwidth is B, double-sideband AM and DSB-SC require 2B, while SSB requires B. In SSB, one of the two sidebands is selected. In DSB-SC, the carrier is suppressed; a sign change in the message produces a 180° phase shift in the modulated wave.

The index measured from the envelope is m = (A − B)/(A + B). For A = 152 mV and B = 57 mV in the report, m = 95/209 ≈ 0.455; the result is given as 0.45. The dB ratio of the carrier to the sideband amplitude is written as 20 log₁₀(2/m); approximately 6 dB corresponds to m ≈ 1.

## Measurements in the AM experiment

1. The tone selected from the audio oscillator is fed to the AM DSB modulator; t.p.1 and t.p.9 are observed.
2. With t.p.1 selected as the trigger source, the modulated signal is examined at t.p.3. It is recorded that the output changes with the Balance knob.
3. The amplitude and frequency of the tone are varied, and the changes in the envelope and in the wave density are observed.
4. The transmitted broadcast is located using the receiver's tuning dial. A phase difference is observed between the RF amplifier output and its input.
5. The stage that mixes the local oscillator and the RF signal is examined. The local oscillator frequency is 455 kHz higher than the received frequency; the difference component forms the intermediate frequency.
6. The outputs of the IF stages, the diode detector, and the audio amplifier are observed in sequence. Apart from the photographs, the last sections contain no separate numerical measurement table.

The receiver example in the report gives a 455 ± 6 kHz passband, that is, the 449–461 kHz range. For 300 Hz–3 kHz audio, the SSB bandwidth is written as 2.7 kHz.

*Note: The statements in the report that "in SSB, two-thirds of the power is in the carrier" and "in DSB-SC, the sidebands carry two-thirds of the power" are not correct for suppressed-carrier signals. The two-thirds/one-third split belongs to the example of full AM with a single tone at 100% modulation. In the phrase "sending from the receiver and receiving from the transmitter," the receiver and transmitter are swapped. The description of the sum/difference frequencies for the mixer should not be read as the numerical product of two frequencies.*

## Basic relations of FM and PM

The FM report defines the phase of the carrier as θ(t) and the instantaneous angular frequency as dθ/dt. For single-tone FM:

VFM(t) = Ec cos[ωc t + β sin(ωm t)]

β = Δω/ωm = Δf/fm.

For a 75 kHz deviation and a 300 Hz message, β = 250; for the same deviation and a 15 kHz message, β = 5. For small β, the narrowband approximation is used; for larger indices, the sideband expansion in terms of Bessel functions is used. The Carson approximation is given as BT ≈ 2(Δf + fm) = 2(β + 1)fm.

In the report's β = 1 example, J₀ ≈ 0.765; J₁ ≈ 0.440; J₂ ≈ 0.115. The carrier and the first two pairs of sidebands contain approximately 99.47% of the total power. The source gives the power result as approximately 0.4997Ec².

*Note: With the written coefficients, [0.765² + 2×0.440² + 2×0.115²]/2 = 0.4974375. The source's result of 0.4997 does not agree with these rounded numbers. In some lines of the report, the Carson bandwidth is written with the letter β; bandwidth and the dimensionless modulation index are different quantities. For a fixed deviation, β is inversely proportional to the message frequency.*

## FM experimental setup and observations

The audio oscillator, reactance/varactor modulator, mixer-amplifier, resonant circuit, amplitude limiter, and low-pass filter are examined. In the setup, the audio oscillator range is stated as 16 Hz–20 kHz.

1. The audio oscillator is connected to the modulator input; the switch is in the Reactance position, and the carrier adjustment is kept at the middle position.
2. At the mixer-amplifier output, an amplitude of 520 mV and a frequency of 93.98 Hz are recorded.
3. It is stated that when the audio amplitude is increased, the wave density at the output changes.
4. For the detection experiment, a 455 kHz sine wave is applied to the resonant circuit; a measurement is also taken for 475 kHz.
5. At the next output, a sine wave, a DC level, and a small ripple are observed. It is written that the t.p.73 output is the same as t.p.40.
6. In the noise test, the limiter's suppression of amplitude variations is discussed.

*Note: The 520 mV and 93.98 Hz values are transcribed from the report exactly as written; it is not sufficiently explained whether the measurement point was the carrier, difference, or audio output. A reactance modulator cannot be described merely as a circuit that "changes the resistance," nor can an untuned resonant circuit be described merely as a power amplifier. The claims in the source that AM does not require an antenna and that FM is better at every signal level are not generally valid.*

## Separate lab photographs

The oscilloscope photographs in the same folder include a single-channel sine wave, a comparison of two channels, a modulation envelope, a low-amplitude/noisy signal, and flat output traces. The ANACOM 1/1 transmitter and ANACOM 1/2 receiver boards, the carrier adjustment knobs, and the experiment connections are visible. Because the photographs are not matched to a measurement sequence number, no new results table was derived from the screens; the measurements explicitly written in the report have been preserved above.
