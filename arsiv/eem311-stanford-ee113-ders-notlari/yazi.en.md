---
baslik: EEM311 Electronics II: Stanford EE113 Electronic Circuits Lecture Notes (Gregory T. A. Kovacs, 1997)
ozet: The 268-page English lecture notes for Stanford University's EE113 Electronic Circuits course by Gregory T. A. Kovacs: BJT review, op-amp circuits, common-emitter/base/collector amplifiers, frequency response, cascode and differential amplifiers, current sources, multi-stage amplifiers, and feedback.
---

This post presents the **lecture notes** for **EE113 Electronic Circuits** from the **Department of Electrical Engineering at Stanford University**, kept alongside the instructor slides for EEM 311 Electronics II. The notes were prepared by **Prof. Gregory T. A. Kovacs** ("© 1997 Gregory T. A. Kovacs, All Rights Reserved"; the PDF is the "Rev0" version dated April 12, 1998). Because the 268-page English text covers nearly all the topics of Electronics II (amplifier stages, frequency response, differential amplifiers, current sources, feedback), it was used as an additional resource during the course. The complete notes can be downloaded as a PDF at the end of the post.

*Note: This content belongs to a third party; it is shared for archival and nostalgic purposes, with the source credited. It will be removed at the request of the rights holder.*

## Course objectives and structure

The first chapter of the notes lists the goals of EE113 as follows:

- To gain practical knowledge of the design and analysis of basic analog circuits.
- To learn about operational amplifiers (op-amps) and the circuits that use them.
- To see how bipolar transistors actually behave in circuits.
- To learn to design, analyze, and test basic amplifiers.
- To learn differential pairs, current sources, and multi-stage amplifier design.
- To learn how feedback is applied to amplifiers.

The textbook is Sedra & Smith's *Microelectronic Circuits*; supplementary references are Horowitz & Hill (*The Art of Electronics*), Gray & Meyer (*Analysis and Design of Analog Integrated Circuits*), Neudeck, and Muller & Kamins. Grading: weekly homework 10%, midterm and quizzes 35%, final 55% (exams are open book). The introduction also includes Kovacs's humorous "Analog Boot Camp Drill Routine" chant ("One, two, three, four, / Gain and bandwidth, we want more. / Five, six, seven, eight, / We don't want to oscillate.").

## Table of contents

| Chapter | Topic | Page |
| --- | --- | --- |
| 1 | Introduction (objectives, course information, course schedule) | 1 |
| 2 | Basic Concepts: sources, signals, amplifier models, noise, distortion, power supplies and efficiency, large/small signal, transfer functions, Bode plots | 5 |
| 3 | BJT Review: DC (large-signal) analysis, biasing, DC load line, small-signal behavior, hybrid-π model, base–emitter resistance scaling, AC load line | 25 |
| 4 | Operational Amplifiers: voltage follower, inverting, logarithmic, exponential, non-inverting, summing, integrator, and differentiator circuits; "real" and ideal op-amps, op-amp frequency response, internal structure of op-amp chips, introduction to feedback | 38 |
| 5 | Single-Stage BJT Amplifiers and the Common Emitter Amplifier: classical biasing, base circuit design strategy, local feedback with an emitter resistor | 54 |
| 6 | BJT Frequency Response | 84 |
| 7 | General Amplifier Frequency Response (estimating general frequency response, time constants) | 97 |
| 8 | The Common Base Amplifier | 117 |
| 9 | The Common Collector Amplifier | 127 |
| 10 | Cascaded and Cascode Amplifiers | 135 |
| 11 | Differential Amplifiers | 153 |
| 12 | Current Sources | 188 |
| 13 | Multi-Stage Amplifiers (analysis of an example amplifier) | 197 |
| 14 | Feedback: properties of negative feedback, effect on bandwidth, types of mixers and samplers, the four feedback topologies, analysis in realistic circuits, stability and pole locations, compensation, the pole–zero "tent" model, linear oscillators | 203 |

## From the feedback chapter: the four topologies

Feedback, one of the most extensive chapters in the notes, classifies amplifiers into four types according to how they mix and sample:

| Topology | Input / output | Amplifier type |
| --- | --- | --- |
| Series-shunt (series mixing, voltage sampling) | voltage in, voltage out | Voltage amplifier |
| Shunt-series (shunt mixing, current sampling) | current in, current out | Current amplifier |
| Series-series (series mixing, current sampling) | voltage in, current out | Transconductance amplifier |
| Shunt-shunt (shunt mixing, voltage sampling) | current in, voltage out | Transresistance amplifier |

In real circuits the feedback network loads the basic amplifier, so the notes suggest the following steps:

1. Redraw the amplifier as an "A circuit" that includes the loading effect of the feedback network along with R_S and R_L; compute the open-loop gain from this circuit (A').
1. Find the feedback ratio β.
1. Compute the closed-loop gain using the corrected gain: A_f = A' / (1 + A'β).
1. If needed, compute the input and output impedances with the appropriate (1 + A'β) scaling.
1. If needed, find the impedances seen at the amplifier's own terminals by mathematically removing the effects of R_S and R_L.

> "In real situations, the feedback network is generally passive, and loads the basic amplifier in the loop and thus affects A, Ri and Ro... The trick is to lump these 'bad' effects into the previously mentioned 'A' circuits."
