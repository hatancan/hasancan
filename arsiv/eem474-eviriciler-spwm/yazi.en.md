---
baslik: EEM474 Power Electronics: Single-Phase and Three-Phase Inverters, SPWM
ozet: Square-wave and quasi-square-wave inverters, RL load, harmonics, sinusoidal PWM, and three-phase switching.
---

The explanations and formulas from the English-language presentations in the EEM474 course folder have been transcribed into text. The author's name is not explicitly stated in the documents. Because photographs and images taken from books were not transcribed, this post has no download file.

## DC-to-AC Conversion

Half-bridge and full-bridge inverters produce an alternating-polarity output voltage from a DC source. In the full bridge, diagonal switch pairs are turned on in sequence. If the upper and lower switches of the same leg are turned on at the same time, the DC source is short-circuited. With an inductive load, current continuity is provided by the anti-parallel diodes.

## Square Wave and RL Load

The ±Vdc full-bridge square wave consists of odd harmonics only. For odd n, the peak value of the nth voltage harmonic is 4Vdc/(nπ). For an RL load, Zₙ = √[R² + (nωL)²], Iₙ = Vₙ/Zₙ and φₙ = atan(nωL/R) are used for each harmonic. The inductance limits high-frequency current components more strongly.

THD is the ratio of the total rms value of the harmonics other than the fundamental to the rms value of the fundamental component. The voltage THD and the current THD are not necessarily the same.

## Quasi-Square Wave

The pulse width is varied by applying zero voltage during part of the output period. The presentation examines the effect of the delay angle on the harmonics and the choice of eliminating particular harmonics. The fundamental component of the voltage and the distortion of the load current are evaluated together.

In the example with R = 10 Ω, L = 25 mH and f = 60 Hz, for a square wave with a 100 V DC supply, the peak value of the fundamental current is shown as approximately 9.27 A and the current THD as 16.7%. In the quasi-square-wave example with α = 30° and Vdc = 116 V, the THD drops to approximately 6.6%.

## Sinusoidal PWM

A sinusoidal reference is compared with a high-frequency triangular carrier. The amplitude modulation ratio is defined as ma = Vreference,peak / Vcarrier,peak, and the frequency ratio as mf = fcarrier / ffundamental. In the linear region, the peak value of the full-bridge fundamental output is proportional to ma Vdc.

In bipolar PWM, the output switches between two polarities. In the unipolar method, the legs of the bridge are driven with opposite references; a zero level also appears in the output. Shifting the harmonics to around the carrier frequency makes filtering easier. In overmodulation, the linear amplitude relationship ceases to be valid.

In the presentation's example with Vdc = 100 V, ma = 0.8, mf = 21, f = 60 Hz, R = 10 Ω and L = 20 mH, the fundamental voltage peak is 80 V, the fundamental current peak is approximately 6.39 A, the total power is approximately 205.5 W and the current THD is given as 8.7%. The final design problem targets a 75 Vrms, 60 Hz output from a 150 V DC source, with R = 12 Ω, L = 60 mH and a current THD of less than 10%.

## Three-Phase Inverter

In the three-leg bridge, the phases are shifted by 120°. The six switching states of the 180° conduction scheme are shown in the presentation in the order 123, 234, 345, 456, 561 and 612. The states change at 60° intervals. For wye and delta load connections, the phase and line voltages are evaluated separately.

In the six-step output, the rms value of the line voltage is √(2/3)Vdc. In three-phase SPWM, three sinusoids shifted by 120° are compared with the same carrier; the line voltage is the difference between the outputs of two legs.

*Note: The numerical THD results belong to the presentation's harmonic calculations and roundings; they are not a fixed ratio for every switching method.*
