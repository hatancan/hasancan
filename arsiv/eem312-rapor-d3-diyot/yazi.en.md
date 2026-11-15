---
baslik: EEM312 Digital Electronics: D3 Diode Experiment Reports and Diode Simulation with SPICE (2011–2017)
ozet: EEM312 Digital Electronics diode experiment reports: I-V measurement with the 1N4001, variation of the reverse recovery time trr with frequency, Cj measurement; in SPICE, the I-V curve with the D1N4148 model, the BV reverse breakdown voltage, trr simulation, and a diode clipper circuit.
---

This post collects the reports written for the diode experiments of the Başkent University **EEM312 Digital Electronics** laboratory: two reports (2011 and 2014) for the hardware experiment **D3: Diode characteristics and models**, plus a 2014 preliminary study, a report, and a 2017 simulation study for the SPICE software experiment on the same topic. All of them are the work of fellow students; **personal information has been removed**. The hardware handout and background (the C_j formula, t_rr = t_s + t_t) are in the post [EEM312 hardware experiment handouts](/arsiv/eem312-donanim-deney-foyleri/). The reports with personal information redacted, the SPICE netlists of the 2017 study, and screenshots are in the ZIP at the end of the post.

## Hardware experiment (D3)

### 1. Forward voltage

A ±10 V, 1 kHz triangular wave was applied to the diode measurement circuit (D1N4001, R1 = 100 Ω):

- **Report A (2011):** the diode's forward voltage is **V_ON ≈ 0.6 V**.
- **Report B (2014):** the output voltage is **V_out = 3.54 V** (input ±10 V, 1 kHz).

### 2. Current–voltage measurement

| Diode voltage | A (2011) | B (2014) |
|---|---|---|
| −5 V | 0 | 0.09 mA |
| 0.5 V | 0.26 mA | 0.31 mA |
| 0.55 V | 0.605 mA | 0.44 mA |
| 0.6 V | 1.146 mA | 0.76 mA |
| 0.65 V | 4.513 mA | 0.97 mA |
| 0.7 V | 13.301 mA | 1.74 mA |
| 0.75 V | 47.02 mA | 1.83 mA |
| 0.8 V | not measured | 2.15 mA |

Report A did not measure 0.8 V to avoid burning out the diode; it interprets the roughly fourfold increase in current between 0.6 V and 0.65 V as confirmation of V_ON ≈ 0.6 V. The curve in A agrees with the exponential diode characteristic.

*Note: The values in Report B increase almost linearly between 0.5 and 0.8 V, and a reverse current of 0.09 mA appears at −5 V; this does not match the exponential behavior expected of a silicon diode (the reverse current should be on the order of nA). A series resistance or an ammeter range effect may be present in the measurement; the report nevertheless says "the graph matches the expected I-V curve".*

### 3. Reverse recovery time

A 0–5 V square wave was applied to the input and t_rr was measured:

| Frequency | A: t_rr | B: t_rr |
|---|---|---|
| 5 kHz | 20 µs | 14.40 µs |
| 10 kHz | 19 µs | 14.40 µs |
| 20 kHz | 17 µs | 13.90 µs |
| 40 kHz | 12.1 µs | 12.40 µs |
| 100 kHz | 5.2 µs | 4.6 µs |
| 200 kHz | 2.5 µs | 2.2 µs |
| 500 kHz | 1 µs | 1 µs |
| 1 MHz | 0.53 µs | 440 ns |

In both reports the measured t_rr decreases as the frequency increases. Report B writes that beyond 40 kHz the recovery could not be fully observed because the diode returned to conduction before the junction capacitance could discharge; it also explains the role of R1 as allowing the charge stored in this capacitance to discharge. Report A says the results resemble the datasheet but are not identical because the conditions differ, and that the time would get longer if R1 were increased (τ = RC).

*Note: The fact that the measured time is limited by the half period at high frequency (at 1 MHz the half period is 0.5 µs) explains most of the "decrease"; that is, at these frequencies the measured value is not the diode's actual t_rr but the waveform itself. In a general-purpose rectifier diode such as the 1N4001, t_rr is on the order of µs.*

### 4. Junction capacitance C_j

In the Figure 4 circuit of the handout (R2 = 10 kΩ), the diode current was found from the voltage across R2 (I_D = V_R/R2). Report A computed C_j with the formula C_j(V_R) = C_j0/(1 + V_R/V_j)^m, using the datasheet values C_j0 = 2 pF and m = 0.33.

| V_dc offset | Frequency | A: V_D | A: V_R | A: I_D | A: C_j | B: V_D | B: I_D | B: C_j |
|---|---|---|---|---|---|---|---|---|
| 2 V | 10 kHz | 1.95 V | 30 mV | 3.02 mA | 2.09 pF | 2.45 V | 0.011 mA | 3.02E−14 |
| 3 V | 20 kHz | 3.16 V | 11.11 mV | 1.01 mA | 2.03 pF | 3.20 V | 0.011 mA | 1.67E−13 |
| 5 V | 40 kHz | 5.17 V | 0.07 mV | 0.007 mA | 2 pF | 4.9 V | 0.010 mA | 1.21E−13 |
| 8 V | 100 kHz | 7.99 V | 0.12 mV | 0.010 mA | 2 pF | 7.52 V | 0.012 mA | 1.22E−13 |
| 10 V | 200 kHz | 9.36 V | 0.15 mV | 0.016 mA | 2 pF | 9.12 V | 0.012 mA | 1.22E−13 |

The reports' interpretation: R2 directly determines the voltage across the diode; as R2 increases, the diode voltage and, accordingly, C_j decrease.

*Note: In Report A, with I_D = V_R/R2, 30 mV/10 kΩ = 3 µA and 11.11 mV/10 kΩ ≈ 1.1 µA; the "mA" units in the table should be µA. Also, under reverse bias C_j cannot exceed C_j0; it should decrease as the reverse voltage increases. For example, for V_R ≈ 1.95 V and V_j = 0.75 V, C_j ≈ 2 pF/(1 + 2.6)^0.33 ≈ 1.3 pF; the 2.09 pF in the table and the constant 2 pF values do not agree with the formula. How the C_j values in Report B (in F) were calculated is not stated in the report.*

## Diode simulation with SPICE

### Preliminary study (B, 2014)

In SPICE, a diode is defined as `DXXXXXXX N+ N- MNAME <AREA> <OFF> <IC=VD> <TEMP=T>`: N+ and N− are the connection nodes, MNAME is the model name, AREA is the area factor, and OFF is an optional initial condition for DC analysis. The netlist prepared for the I-V curve of the D1N4148:

```
*D1N4148 Diyot Akım - Voltaj Grafiği
.model D1N4148 D(IS=5.84n N=1.94 RS=.7017 XTI=3 EG=1.11 CJO=.95p
+ M=.55 VJ=.75 FC=.5 BV=100 IBV=100u TT=11.07n)
VIN 1 0 DC 5
R1 2 0 10K
D1 1 2 D1N4148
.CONTROL
DC VIN -300 200 0.1
PLOT -VIN#branch vs V(1)-V(2)
.ENDC
.END
```

### Report (C, 2014)

- **Reverse breakdown:** In the simulation of the circuit from the handout, the reverse breakdown voltage was read as approximately **−100.3 V**, which corresponds to the **BV = 100** parameter in the model. When BV = 50 was set, the breakdown shifted to around 50 V, thereby showing that BV is the reverse breakdown voltage parameter. The report also adds that the parameters in the model are not sufficient to fully describe the static and dynamic behavior of the diode.
- **Reverse recovery:** t_rr measured with a 0–5 V square wave:

| Frequency | t_rr (R = 10 kΩ) | t_rr (R = 1 kΩ) |
|---|---|---|
| 1 kHz | 0.070 µs | 0.042 µs |
| 50 kHz | 0.065 µs | 0.039 µs |
| 100 kHz | 0.063 µs | 0.033 µs |

The effect of frequency on t_rr is very small; when the resistance drops from 10 kΩ to 1 kΩ, the time falls to roughly half.

- **Diode circuit (question 4):** In the circuit with two diodes driven by a square wave, the diodes operate as a rectifier/clipper, the negative portion is clipped, and the capacitor acts as a filter. The report also introduces **Schottky diodes**: diodes that can operate at very high frequencies, have low noise, and have a forward voltage of 0.15–0.45 V (around 0.7 V for ordinary diodes), and therefore improve efficiency in low-voltage power supplies.

### 2017 simulation study

In the 2017 study (Question 3), reverse recovery was examined for R1 = 1 kΩ and 10 kΩ with a 0–5 V pulse input using the same D1N4148 model:

```
.MODEL D1N4148 D(IS=5.84n N=1.94 RS=.7017 XTI=3 EG=1.11 CJO=.95p
+ M=.55 VJ=.75 FC=.5 BV=100 IBV=100u TT=11.07n)
D1 1 2 D1N4148
R1 2 0 1K
Vin 1 0 PULSE (0 5 0NS 2NS 2NS 1ms 0.01ms)
.control
tran 1ns 0.1ms
plot V(2)
.endc
.end
```

| Frequency | t_rr (R1 = 1 kΩ) | t_rr (R1 = 10 kΩ) |
|---|---|---|
| 1 kHz | 425 ns | 210 ns |
| 50 kHz | 420 ns | 220 ns |
| 100 kHz | 450 ns | 210 ns |

Comment: as the resistance increases, the current I = V_in/R1 decreases, the output approaches 5 V more closely, and the recovery time changes; the effect of frequency is again small. In Question 4, a ±10 V square wave was applied to a clipper circuit with two diodes (D1 to ground, D2 to 5 V) and a 5 nF capacitor; the output is clipped between approximately −0.7 V and 5.7 V.

*Note: The 2014 report (C) finds t_rr at R = 10 kΩ longer than at 1 kΩ, whereas the 2017 study finds it shorter. With a pulse input the forward current is I_F ≈ 5 V/R, so at small R the stored charge (Q = τ_T·I_F), and hence the storage time, increases; in this respect the trend in the 2017 study is as expected.*

## Appendix: Handwritten notes on the p-n junction

The folder contains two photographed notebook pages from 2014 (the photographs were not published; they were transcribed into text). A summary of the notes:

- The current formed by the carriers in the depletion region is divided into the **diffusion current I_D** and the **drift current I_S**; when V_D = 0, I_D = I_S, equilibrium.
- **Reverse bias:** the p side is connected to the − terminal of the source and the n side to the + terminal. Electrons move away from n and holes from p; the depletion region widens, the barrier voltage increases, and it becomes harder for current to flow. I = I_S − I_D; the current flowing externally is the very small saturation current.
- **Forward bias:** the p side is connected to the + terminal; the depletion region narrows, the diode can carry a high current, and I_D is supplied by the external circuit. I = I_D − I_S. Electrons and holes recombine in the junction region.
- In a junction fed by a current source, the current stays constant regardless of the connected load; in a junction fed by a voltage source, the voltage across the terminals is held constant.
