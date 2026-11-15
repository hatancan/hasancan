---
baslik: EEM312 Digital Electronics: Lab Reports for Experiment D1, RC Low-Pass Filter and Delay Measurements
ozet: A comparison of three student reports for the first experiment (D1) of the EEM312 Digital Electronics hardware laboratory: computing C from the measured R and cutoff frequency, the variation of gain and phase difference with frequency, and measurements of tr, tf, tpHL, tpLH, and td with a square-wave input.
---

This post presents together three reports written for the first experiment in the hardware laboratory of the Başkent University course **EEM312 Digital Electronics**, **D1: Use of Basic Laboratory Equipment** (RC low-pass filter). Two belong to the spring 2011 term and one to 2014; all three were prepared by classmates, and **personal information has been removed** (they are referred to as A, B, and C). The experiment handout and its questions are in the post [EEM312 hardware lab handouts](/arsiv/eem312-donanim-deney-foyleri/); here there are only the measurements, calculations, and comments from the reports. The reports with personal information redacted are available as PDFs in the ZIP at the end of the post.

## Part I: Computing C from the Cutoff Frequency

Each student was given a mixed resistor–capacitor pair; R was measured with a multimeter, the circuit was built on a breadboard, a 2 V_pp sine wave was applied to the input, and the frequency at which the output dropped to 1.4 V_pp (gain ≈ 0.7071) was recorded as the **cutoff frequency**. The capacitor is calculated from this frequency:

**ω_c = 1/(RC) → C = 1/(2π·R·f_c)**

| Report | Measured R | Measured f_c | Calculated C |
|---|---|---|---|
| A (2011) | 55 kΩ | 23 kHz | 0.125 nF |
| B (2011) | 150 kΩ | 4.673 kHz | 227 pF |
| C (2014) | 27.5 kΩ | 10.40 kHz | 556 pF |

All three C values are consistent with the formula (it gives 125.8 pF, 227.1 pF, and 556.5 pF). The common conclusion of the reports: although Equation 1 is sufficient for a single RC, it is inadequate for measuring the internal capacitance of a component once other elements whose parameters vary with frequency, and parasitic capacitances, come into play. Report B also describes the cutoff frequency as "the frequency at which the output loses half of its energy" (−3 dB, the half-power point).

## Part II: Variation of Gain and Phase Difference with Frequency

The phase difference was calculated from the time difference Δt between the input and output peaks on the oscilloscope, using **ϕ = 360°·f·Δt**.

**Report A (R = 55 kΩ, f_c = 23 kHz):**

| f | V_out | V_in | Gain | Phase difference |
|---|---|---|---|---|
| 10 kHz | 1.78 V | 2.04 V | 0.872 | 17.63° |
| 50 kHz | 0.960 V | 2.02 V | 0.475 | 50.90° |
| 100 kHz | 0.520 V | 2.00 V | 0.260 | 69.12° |
| 150 kHz | 0.360 V | 2.00 V | 0.180 | 73.07° |
| 200 kHz | 0.280 V | 2.00 V | 0.140 | 80.64° |
| 250 kHz | 0.232 V | 2.00 V | 0.116 | 112.5° |
| 300 kHz | 0.192 V | 2.00 V | 0.096 | 72.43° |
| 400 kHz | 0.160 V | 2.00 V | 0.080 | 81.29° |
| 500 kHz | 0.128 V | 2.00 V | 0.064 | 59.4° |
| 1 MHz | 0.080 V | 2.00 V | 0.040 | 79.2° |

**Report B (R = 150 kΩ, f_c = 4.673 kHz):**

| f | Gain | Phase difference |
|---|---|---|
| 10 kHz | 0.490 | 59.88° |
| 50 kHz | 0.130 | 76.60° |
| 100 kHz | 0.076 | 78.41° |
| 150 kHz | 0.044 | 79.62° |
| 200 kHz | 0.032 | 87.76° |
| 250 kHz | 0.027 | 94.33° |
| 300 kHz | 0.021 | 103.68° |
| 400 kHz | 0.016 | 117.21° |

**Report C (R = 27.5 kΩ, f_c = 10.4 kHz):**

| f | Gain | Δt | Phase in report |
|---|---|---|---|
| 1 kHz | 0.980 | 0 µs | 0° |
| 5 kHz | 0.911 | 17 µs | 6.12° |
| 10 kHz | 0.733 | 13 µs | 23.4° |
| 15 kHz | 0.56 | 10 µs | 36° |
| 20 kHz | 0.4615 | 7 µs | 37.8° |
| 25 kHz | 0.39 | 7.2 µs | 51.84° |
| 30 kHz | 0.34 | 6.8 µs | 73.44° |
| 40 kHz | 0.26 | 5.2 µs | 74.88° |
| 50 kHz | 0.21 | 4.8 µs | 86.4° |
| 100 kHz | 0.11 | 2.4 µs | 86.4° |

The three reports' interpretations point in the same direction: because the capacitor's impedance Z_C = 1/(jωC) decreases with frequency, the output voltage, and hence the gain, drops (low-pass filter); since the transfer function is H = 1/(1 + jωRC), the phase angle also grows with increasing frequency as −arctan(ωRC). Report C also built the circuit in Proteus and compared the input and output waveforms at 1 kHz, 25 kHz, and 100 kHz (at 25 kHz, gain ≈ 0.37 and peak difference ≈ 7.8 µs), finding them consistent with the table values.

*Note: In a first-order RC filter, the phase difference can approach 90° at most. The values of 112.5° at 250 kHz in Report A and 94°–117° at 250–400 kHz in Report B exceed this limit; they must be measurement errors arising from reading Δt by eye on the oscilloscope at high frequency and from probe/breadboard capacitances. For this reason, the comment in Report A that "the bandwidth ends after 250 kHz" is also not physical.*

*Note: In Report C, the phase values in the 5–25 kHz rows were calculated by multiplying the measured Δt by the frequency of the previous row (e.g., for 5 kHz, 360·1 kHz·17 µs = 6.12°). The correct calculation gives approximately 30.6°, 46.8°, 54°, 50.4°, and 64.8° for 5, 10, 15, 20, and 25 kHz respectively; these are also consistent with the theoretical arctan(f/f_c) values (25.7°, 43.9°, 55.3°, 62.5°, 67.4°). The values from 30 kHz onward were calculated correctly.*

## Part III: Delay Measurements with a Square-Wave Input

A square wave was applied to the input, and the 10%–90% rise/fall times (t_r, t_f), the propagation delays between the 50% points (t_pHL, t_pLH), and their average t_d = (t_pHL + t_pLH)/2 were measured.

| Report | Pulse shape | t_r | t_f | t_pHL | t_pLH | t_d |
|---|---|---|---|---|---|---|
| A | 50%, 60 kHz | 1.1 µs | 6.7 µs | 3 µs | 2.4 µs | 2.7 µs |
| A | 30%, 60 kHz | 1.0 µs | 6.4 µs | 2.4 µs | 3.4 µs | 2.9 µs |
| B | 50%, 60 kHz | 5.4 µs | 6.4 µs | 3.6 µs | 3.6 µs | 4.8 µs |
| B | 30%, 60 kHz | 8.0 µs | 8.2 µs | 4.8 µs | 4.8 µs | 4.8 µs |
| C | 50%, 6 kHz | 31 µs | 34 µs | 16 µs | 17 µs | 16.5 µs |
| C | 30%, 6 kHz | 37 µs | 36 µs | 14 µs | 14 µs | 14 µs |

In Report C, RC ≈ 27.5 kΩ × 556 pF ≈ 15.3 µs; for a first-order circuit the expected t_r ≈ 2.2·RC ≈ 34 µs and t_p ≈ 0.69·RC ≈ 10.6 µs, which are of the same order as the measured values.

Comments on the questions:

- **t_r ≠ t_f, t_pHL ≠ t_pLH:** Ideally they should be equal. The reports attribute the difference to the capacitor's charge and discharge paths being different (charging through R, discharging through the source's internal resistance) and to the 10%, 50%, and 90% points being read by eye on the oscilloscope.
- **Effect of pulse width:** As the pulse width decreases, the capacitor's charge–discharge times, and accordingly the measured times, decrease (A and B); Report C observes an effect directly proportional to the pulse width.
- **Input t_r:** No matter how fast the rise at the input is, the output t_r remains slower than the input because of the RC time constant.

*Note: In Report B's table, t_d is defined as the average of t_pHL and t_pLH, yet in the 50% row 4.8 µs is written instead of (3.6 + 3.6)/2 = 3.6 µs.*

## Part IV: Second-Order Effects

Report A says that when a pulse is applied to the input at high frequency, second-order effects (overshoot, ringing) may appear because of oscillations coming from the signal generator and the inductive/parasitic effects of the cables and components. Report B, on the other hand, writes that since there is only one energy-storing element (the capacitor) in the circuit, no second-order effect is seen, and that the inductive effect of the wires would appear only at very high frequencies that the generator cannot reach.
