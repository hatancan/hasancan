---
baslik: EEM214 Electronics I: 2014 Laboratory Measurement and Waveform Notes
ozet: Measurement notes transcribed from photographs of the oscilloscope usage, 1N4148 diode measurements, rectification, clipping, and clamping experiments.
---

The laboratory sheets dated 25 February, 4 March, and 18 March 2014 were transcribed to text from photographed pages. Personal information has been removed. The photographs are not shared and there is no download file. Numbers that were blurry or fell outside the frame were not guessed; the measurements below are only the entries that could be read.

## Experiment 1: Oscilloscope and Signal Generator

The 25 February pages ask for observing a sine wave with DC coupling, checking the probe multiplier, and drawing the waveform with the voltage/time scales. Next to the sine drawings, a note of V_pp = 2 V can be read. A line reading V_min = −1 V can be made out; all other voltage and frequency values cannot be read reliably.

In another drawing, a square wave and a sine wave of the same period are shown superimposed. On the next set of axes, a horizontal trace is drawn; the scale note is unclear. No exact frequency or phase difference has been derived from these graphs.

The potentiometer table has columns for R_1, R_2, and unloaded V_out. The entries that could be read:

| Position | R_1 | R_2 | V_out |
| --- | --- | --- | --- |
| First position | Appears to be 1.2 Ω | Approximately 4.68 kΩ | 0 V |
| Middle position | Unclear | 2.5 kΩ | 3.5 V |
| Last position | Approximately 4.69 kΩ | Appears to be 147 Ω | Unclear |

The handout also asks for the measurement to be repeated with a load connected, and mentions a 150 Ω load; the loaded-result column is outside the frame.

*Note: The numbers in this section are transcribed as far as they could be read from the blurry photograph; they should not be used as an exact calibration record.*

## Experiment 2: 1N4148 Diode Test

On the 4 March sheet, the multimeter diode test recorded 0.5638 V in the forward direction and 0.000 in the reverse direction. The handout gives the typical silicon diode forward reading as in the range 0.500–0.900 V.

*Note: The 0.000 in the reverse direction is the source instrument's display record. Depending on the multimeter, the open-circuit indication may be OL or some other form; a zero voltage value alone is not a "good diode" criterion for all instruments.*

Filled-in rows for the forward i–v characteristic with a 220 Ω series resistor:

| Target diode voltage in handout | Measured diode voltage | Recorded current |
| --- | --- | --- |
| 0.40 V | Approximately 0.4542 V | 20.61 µA |
| 0.50 V | 0.5212 V | 74.26 µA |
| 0.60 V | Approximately 0.60 V; last digits unclear | 138.29 µA |
| 0.70 V | 0.6075 V | 144.84 µA |
| 0.80 V | Reads as 0.6257 V | 276.33 µA |

The rows for 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, and 0.90 V are blank or crossed out.

*Note: The target voltage and the measured voltage are different columns. The records in the photograph do not match the targets exactly; the target numbers were not entered in place of measurements.*

## Reverse Bias Table

For small currents, the handout asks for the voltage across a 1 MΩ resistor to be measured instead of measuring current directly. The readable transcription of the source columns:

| Source voltage | Voltage measured across resistor | Diode voltage written at source | Current written at source |
| --- | --- | --- | --- |
| 0 V | 0 V | 0.3 V | 0 |
| −1 V | 0.0030 V | 1.43 V | 0 |
| −2 V | 0.0040 V | 2.12 V | 0 |
| −3 V | 0.0042 V | Reads as 2.88 V | 0 |
| −4 V | 0.0040 V | 3.66 V | 0 |
| −5 V | 0.0040 V | 4.62 V | 0 |
| −10 V | 0.0063 V | 9.28 V | 0 |
| −15 V | 0.0064 V | 13.69 V | 0 |
| −20 V | 0.0052 V | 18.13 V | 0 |
| −25 V | 0.0053 V | Approximately 22.98 V; last digit unclear | 0 |

*Note: 3.0–6.4 mV across 1 MΩ corresponds to approximately 3.0–6.4 nA; the source rounded the current column to zero. The diode voltage column does not exactly agree with the difference between the nominal source and resistor voltages. These values are the experiment record in the photograph, not the result of a corrected calculation.*

## Half-Wave Rectification Observation

The two photographs from the same day are different framings of the same drawing. The handout asks for the input and output to be drawn with a 100 Hz sine, 5 V peak-to-peak input, and R_L = 1 kΩ. The input consists of positive and negative half-cycles; the second curve shows conduction in only one half-cycle. In the other half-cycle, the output is drawn near zero.

*Note: Which curve the handwritten arrows belong to is unclear in places; no exact peak value or diode drop was calculated from the photograph.*

## Experiment 4: Clipper Circuits

On the 18 March pages, the input conditions of the first experiment are a 100 Hz, 20 V peak-to-peak sine. For the circuit, R = 1 kΩ and R_L = 47 kΩ are given. DC coupling is used on the oscilloscope; there are 5 V scale notes next to the channels.

In the first output drawing, the top of the sine is flattened and clipped. When the diode is reversed and the positive DC source is replaced by a negative source, the bottom is flattened in the second drawing. These two drawings show that the clipping direction changes.

In the next section, where the circuit designed in the preliminary work is to be tried, the input is 100 Hz and 10 V peak-to-peak. The drawn circuit has a 1 kΩ series resistor at the input, a 47 kΩ load at the output, and 3 V and 2 V DC sources associated with oppositely oriented diode branches. The input/output graph boxes in this section have been left blank; there is no measured waveform.

## Clamper Circuits

In the next section of the handout, C = 1 µF is used with a 100 Hz, 20 V peak-to-peak input; the output sine is drawn shifted downward. In the second circuit, C = 47 µF. In the drawing, a magnitude of 5.3 V is written next to the upper level and 14.7 V next to the lower level. Relative to the zero line, these are at approximately +5.3 V and −14.7 V.

When the direction of the diode and the DC source is reversed, the next drawing has magnitudes of 14.7 V above and 5.3 V below; relative to the axis, these are shown as approximately +14.7 V and −5.3 V.

*Note: The source does not explicitly show the minus sign in the lower-level annotations. The signs are explained here relative to the zero line in the graph; in both cases the total span is 20 V.*

The last page compares the input, output, and X–Y transfer curves for the cases with and without the capacitor connected. The DC sources are to be changed separately. The student's short comment: "There is a capacitor difference between a and b. In b, it will clamp by the amount of the difference between the two volts." The output drawing is shown as shifted and limited in one direction; since the exact scale could not be read, no numerical clamping level is given.
