---
baslik: EEM214 Electronics I: Experiment 2 Diode Characteristics, Student Preliminary Work and Reports (2006–2012)
ozet: Student work from the EEM214 Electronics I laboratory experiment on diode characteristics: i–v values for the 1N4148 calculated with the Shockley equation, diode testing with a DMM, forward-bias measurement tables from 0.35–0.90 V, bulk resistance, and reverse-current measurements with 1 MΩ.
---

This post brings together student preliminary work and reports prepared in different years (2006, 2008, 2012) for the **Experiment 2: Diode Characteristics** experiment of the Başkent University **EEM 214 Electronics I** laboratory. All of it is the work of friends; names and student numbers have been redacted. The experiment handout can be found in the archive in the post "Laboratory Experiment 2 – Diode Characteristics". PDF copies with personal information redacted can be downloaded as a ZIP at the end of the post.

## Preliminary work: i–v values with the Shockley equation

In the preliminary work of the handout, values for the 1N4148 are calculated with the equation i_D = I_S·(e^(v_D/nV_T) − 1) and compared with PSpice. In the 2006 preliminary work, taking I_S = 10⁻¹⁵ A and nV_T ≈ 26 mV, the values found were:

| v_D (V) | 0.4 | 0.5 | 0.6 | 0.65 | 0.7 | 0.75 | 0.8 | 0.85 |
|---|---|---|---|---|---|---|---|---|
| i_D | 4.80 nA | 0.224 µA | 10.5 µA | 72.0 µA | 0.492 mA | 3.37 mA | 23 mA | 157.7 mA |

In the 2008 preliminary work, using a different I_S, 1.14 mA was calculated for 0.7 V and 79 mA for 0.8 V; it was noted that the circuit passes only the positive half-cycle, like a half-wave rectifier. The 2012 preliminary work consists only of PSpice plots (1N4148, 1 kΩ, 5 V peak, 100 Hz).

## Experimental results

### Diode test with a DMM

If a silicon diode is good, the DMM's diode range shows a value between 0.500 and 0.900 V in the forward direction, and "1" (out of range, open circuit) in the reverse direction. The measured forward values were: 0.6648 V, 0.619 V (ohmmeter 6443 Ω), 0.6775 V (2006); 0.5913 V and 0.6089 V (2008). In all of them it was concluded that the diode was good.

### Forward characteristic (R = 220 Ω)

| v_D (V) | Report A (mA) | Report B (mA) | Report C (mA) | 2008 (mA) |
|---|---|---|---|---|
| 0.35 | 0.0024 | 0.0035 | 0.0026 | 0 |
| 0.45 | 0.0252 | 0.0192 | 0.0259 | 0 |
| 0.55 | 0.255 | 0.072 | 0.196 | 0 |
| 0.60 | 0.628 | 0.153 | 0.571 | 0.45 |
| 0.65 | 1.230 | 1.133 | 1.663 | 0.90 |
| 0.70 | 6.204 | 4.942 | 4.498 | 4.61 |
| 0.75 | 11.89 | 11.43 | 10.95 | 23.23 |
| 0.80 | 25.34 | 24.38 | 24.31 | 22.85 |
| 0.85 | 48.87 | 48.93 | 48.11 | 50.56 |
| 0.90 | 88.38 | 95.29 | 79.60 | 65.02 |

The reports state that the current increases rapidly beyond approximately 0.70 V, and that below this the diode can be considered "off" although a very small current still flows. In the 2008 report it is noted that some values were changed afterwards because the measuring instrument and the diode did not give the theoretical result, so there may be errors.

### Bulk resistance

From the forward voltages at 40 mA and 50 mA, using r = ΔV/ΔI: 0.8344 → 0.8504 V gives **1.6 Ω**; 0.835 → 0.853 V gives **1.8 Ω**; 0.869 → 0.905 V gives **3.6 Ω**.

### Reverse direction (R = 1 MΩ)

The source was varied between 0 and −25 V, and the diode current I = V_R / 1 MΩ was calculated by measuring the voltage across the 1 MΩ resistor. In one report, −2.97 mV at −1 V and −5.83 mV at −25 V were measured, and the reverse current was found to be between −2.97 nA and −5.83 nA; in the other, 1.40–3.89 mV was measured.

*Note: A voltage of 1.40–3.89 mV across 1 MΩ corresponds to a current of 1.40–3.89 nA; in one report these values were written as mA. In the 2008 report as well, the reverse-direction current was calculated from the diode voltage as "0.99 mA ... 24.9 mA"; these currents are not possible with a voltage of a few mV across 1 MΩ, and the currents are on the order of nA.*

### Rectification

In the half-wave circuit, the output is zero when the input is negative, and when it is positive the output is about 0.7–0.8 V below the input (the turn-on voltage of the silicon diode).

## Download

The ZIP file contains PDF copies, with personal information redacted, of eight preliminary works/reports organized in folders by year (2006: the preliminary work of the same student with two report versions, and another student's report; 2008: preliminary work and two report versions; 2012: preliminary work).
