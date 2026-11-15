---
baslik: EEM312 Digital Electronics: D2 Lab Reports, Integrated Inverter (SN7404 and CD4049) Measurements
ozet: Two students' reports for experiment D2 of the EEM312 Digital Electronics hardware laboratory: measurements of VOL, VOH, VIL, VIH, noise margins, and tr, tf, tpHL, tpLH for the TTL SN7404 and CMOS CD4049 inverters, compared with manufacturer data.
---

This post compares two reports written for the **D2: Integrated circuit inverter measurements** experiment of the Başkent University **EEM312 Digital Electronics** hardware laboratory: a report (A) from the spring 2011 semester using the **TTL SN7404**, and a preliminary study and report (B) from 2014 using the **CMOS CD4049**. Both are reports by friends; **personal information has been removed**. The lab handout itself is in the post [EEM312 hardware lab handouts](/arsiv/eem312-donanim-deney-foyleri/). PDFs of the reports with personal information redacted are in the ZIP at the end of the post.

## Preliminary study: characteristics of the ICs (B)

According to B's preliminary study, the CD4049/CD4050 ICs given in the attachment belong to the **CMOS** family and have the following notable features:

- They can perform logic level conversion with a single supply (V_DD).
- When used as level converters, the input high level (V_IH) can go up to V_DD.
- They can directly drive two DTL/TTL loads.
- They are designed as hex buffers (CMOS → DTL/TTL or CMOS current driver).

According to the recommended operating conditions, the CD4049/CD4050 operates at 3–15 V, while the SN5404/SN7404 operates at a nominal 5 V supply; both can be used at 5 V. At 5 V, the transition times in the datasheet are t_r = t_f = 20 ns for the CD4049/CD4050 and t_r, t_f < 7 ns for the SN7404. In the circuit in the handout, the CD4049/CD4050 is used as a hex buffer in between, to connect the output of a CMOS-based IC to a TTL or another CMOS IC.

Report A, on the other hand, introduces the SN7404: a 14-pin **hex inverter** containing six inverters (1 pin ground, 1 pin V_CC), with an operating temperature of 0–70 °C; recommended conditions are V_CC = 4.75–5.25 V, V_IH ≥ 2 V, V_IL ≤ 0.8 V.

## Static measurements (VTC)

The inverter was set up and a 0–5 V triangular wave was applied to the input (A: 1 kHz, 10 pF at the output; B: 1 pF at the output), and the V_out–V_in curve was observed on the oscilloscope in X-Y mode.

| Quantity | A: SN7404 measured | A: SN7404 datasheet | B: CD4049 measured |
|---|---|---|---|
| V_OL | 0 V | 0.2 V (typical) | 20 mV |
| V_OH | 5.2 V | 3.4 V (typical) | 5.4 V |
| V_IL | 0 V | at most 0.8 V | 2.8 V |
| V_IH | 5 V | at least 2 V | 2.9 V |
| NM_H = V_OH − V_IH | 0.2 V | 1.4 V | 2.4 V |
| NM_L = V_IL − V_OL | 0 V | 0.6 V | 2.58 V |

Both reports attribute the differences to the inability to achieve ideal conditions (noise-free 5 V supply, 25 °C room temperature), the internal resistances of the components, the connecting cables, and the components used in the experiment being worse than the samples measured by the manufacturer.

*Note: In report A, the student writes that they could not observe a curve in X-Y mode; the values V_IL = 0 V and V_IH = 5 V are therefore not an actual VTC reading. In the report, NM_L is written as "V_OL − V_IL"; the correct expression is V_IL − V_OL.*

*Note: With the values given in report B, NM_H = 5.4 − 2.9 = 2.5 V and NM_L = 2.8 − 0.02 = 2.78 V (the report gives 2.4 V and 2.58 V). The measured V_OH = 5.4 V at a 5 V supply also indicates that the supply was set slightly higher than 5 V.*

## Dynamic measurements (100 kHz square wave)

A 0–5 V, 100 kHz square wave was applied to the input, and the transition and delay times were measured at the output.

| Quantity | A: SN7404 measured | A: datasheet (C_L = 15 pF) | B: CD4049 measured | B: manufacturer data |
|---|---|---|---|---|
| t_r | 36 ns | 7 ns | 116 ns | 60 ns |
| t_f | 28 ns | 7 ns | 64 ns | 30 ns |
| t_pHL | 17 ns | at most 15 ns | 69 ns | 65 ns |
| t_pLH | 18 ns | at most 22 ns | 43 ns | 85 ns |
| t_d | 17.5 ns | – | 58 ns | – |

The TTL inverter is noticeably faster than the CMOS CD4049. The reports again explain the measured times being larger than the manufacturer values by the non-ideal nature of the experimental setup (load capacitor, probe and cable capacitances, internal resistances).

*Note: With B's values, t_d = (69 + 43)/2 = 56 ns; the report gives 58 ns.*
