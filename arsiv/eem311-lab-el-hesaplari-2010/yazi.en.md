---
baslik: EEM311 Electronics II: Hand Calculations and Measurements from the 2010 Laboratory (BJT and MOSFET)
ozet: BJT small-signal calculations, CD4007 common-source amplifier measurements, and the DC and AC preliminary work of a two-stage JFET–BJT amplifier, from photographed student work.
---

This post contains additional preliminary work and report pages prepared by classmates in the **EEM311 Electronics II** laboratory at Başkent University. Personal information has been removed; the content was **transcribed to text from photographed pages**. The photographs were taken on 14 October and 10 November 2010. This post has no downloadable file. Other reports from the same period can be found in the [2010 Experiments 1–4 post](/arsiv/eem311-lab-raporlari-2010-deney-1-4/).

## Experiment 1: Common-Emitter BJT, Hand Calculation

The circuit is a common-emitter amplifier powered by V_CC = 15 V. R_B1 = 470 kΩ, R_B2 = 1.8 kΩ and R_C = 1 kΩ. The input and output are connected through coupling capacitors; the emitter is grounded.

The DC loop equation is written in the photograph as follows:

15 V = I_B(R_B1 + R_B2) + I_C R_C

Taking I_C = 320I_B for β = 320:

15 V = (791.8 kΩ)I_B

I_B = **18.94 µA**, I_C = **6.061 mA**

The page gives V_CQ = I_C R_C = 6.061 V and V_CEQ = 6.061 V. With the same base current, I_C = 4.735 mA is calculated for β = 250 and approximately 3.788 mA for β = 200. The DC load line and characteristic curves for three different β values are drawn.

*Note: In the drawn circuit the base resistor is connected to the supply; the base loop equation should include V_BE, and the collector resistor should not appear in this loop. Also, the collector voltage is V_CC − I_C R_C, not I_C R_C. The numbers in the photograph are preserved as the results of the solution draft; they are not a verified operating point.*

### Small-Signal Calculation and Simulation Output

The relations used in the hand calculation:

r_π = nV_T/I_BQ

g_m = I_CQ/(nV_T)

r_o = (V_A + V_CE)/I_CQ

The page gives r_π ≈ 1.32 kΩ, g_m = 242.4 µS and r_o ≈ 17.51 kΩ; at the end of the gain calculation the ratio 7.81 V / 25 mV ≈ 312.4 is obtained. The gain calculation on this line mixes DC and AC quantities.

*Note: 6.061 mA / 25 mV = 0.2424 S = 242.4 mS; the µS unit on the page is a thousand times too small. The r_π value of about 1.32 kΩ is consistent with the calculation, but the unit error in g_m and the DC operating point errors carry over into the gain calculation.*

On a separate PSpice output page, the note **2 mV peak-to-peak, A_v = −92.968** is written. The output shows the input and output sinusoids and the gain trace over a 0–10 ms time interval; the output is displayed at roughly a 200 mV scale and the input at a 2 mV scale.

## Experiment 3: Common-Source MOSFET Report

The report states that DC and AC analysis of a common-source NMOS stage was performed, and that PSpice was used because the Proteus 7.1 model of the CD4007 could not be found. Measured voltages:

| Quantity | Value in the report |
| --- | --- |
| V_G | 3.276 V |
| V_D | 7.384 V |
| V_S | 1.46 V |

Four waveforms were drawn by hand for a 50 mV, 1 kHz input: the input, the normal output, the output without C_d and R_L, and the output without C_S. The recorded gains:

- With the normal connection, A_v = **−3.84**.
- Open-circuit output gain A_v,open = **−38.6**; the output is 1.93 V peak-to-peak.
- With C_S removed, A_v = **−3.654**.

When the input amplitude was increased until the output began to distort, **V_out,max = 1.09 V peak-to-peak** was recorded.

For the input resistance measurement, a 50 kΩ potentiometer and a 1 kHz source were used. The text states that the source was 50 mV peak-to-peak, and that the measured v_in = 940 mV and R_in = 24.48 kΩ. For the output resistance, v_out = 1.06 V peak-to-peak and **R_out = 16.9 kΩ** are given.

*Note: A passive input voltage divider cannot produce 940 mV from a 50 mV source. Because the source/measurement amplitudes in the text are inconsistent, the R_in and R_out results cannot be verified with this information; the values are reported as given in the report.*

The results page also contains another simulation drawing: the **IRF9520** is used instead of the CD4007, and the operating point is given as Q(2.976 mA, 6 V). The resistors on this page are R_D = 2.52 kΩ and R_S = 500 Ω; the input is 50 mV, 1 kHz, and the supply is 15 V. This is not the same operating point as on the first measurement page.

## Experiment 4: Two-Stage JFET–BJT Amplifier Preliminary Work

The first stage is a common-source JFET and the second stage is a common-emitter BJT. A coupling capacitor connects the JFET drain to the BJT base; the source/emitter resistors of both stages are bypassed for AC.

| Component / parameter | Value |
| --- | --- |
| V_CC | 12 V |
| R_G, R_D, R_S | 1 MΩ, 1 kΩ, 330 Ω |
| BJT base divider | 30 kΩ and 47 kΩ |
| R_C, R_E, R_L | 1 kΩ, 2.2 kΩ, 100 kΩ |
| β, V_BE(on), V_A | 100, 0.7 V, 100 V |
| I_DSS, V_P | 50 mA, −3 V |

### JFET DC Calculation

I_D = I_DSS(1 − V_GS/V_P)²

V_G = 0, V_S = 330I_D and V_GS = −330I_D were used:

I_D = 0.05(1 − 110I_D)²

605I_D² − 12I_D + 0.05 = 0

The selected root is **I_D = 5.954 mA**. The drain-source loop:

12 = I_D(1.33 kΩ) + V_DS

**V_DS = 4.0813 V**, Q_JFET = (5.954 mA, 4.0813 V).

### BJT DC Calculation

V_BB = 12·47/77 = 7.324 V, R_B = 30 kΩ ∥ 47 kΩ = 18.31 kΩ.

In the photograph, I_B ≈ 30 µA and **I_C = 3.045 mA** were found using the equation V_BB = I_B[R_B + (β + 1)R_E]. In the final lines:

12 = (1 kΩ)(3.045 mA) + V_CE + (2.2 kΩ)(3.045 mA)

**V_CE = 1.9515 V** is written.

*Note: The 0.7 V V_BE term in the base loop is omitted in this line. Also, in the final equation shown, 12 − 3.045·3.2 = 2.256 V; the result of 1.9515 V cannot be obtained with the same arithmetic. In the exact calculation, the emitter current should also be taken as (β + 1)I_B instead of I_C.*

### AC Calculation

In the preliminary work, r_π = βV_T/I_C ≈ 7.41 kΩ is written; for the JFET, r_o1 = 1/(λI_D) ≈ 1.68 kΩ and g_m1 ≈ 0.0115 S. Multiplying the gains of the first and second stages gives approximately **A_v = 19.951**.

*Note: With β = 100, V_T = 25 mV and I_C = 3.045 mA, r_π ≈ 821 Ω; the 7.41 kΩ on the page is inconsistent with these data. Because the stages load each other, the input resistance of the second stage must also be included in the output load of the first stage. Since the photograph is blurry, uncertain intermediate coefficients were not transcribed; the result is preserved as written in the source.*
