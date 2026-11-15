---
baslik: EEM214 Electronics I: Experiment 9 – MOSFET Basics, I_DS–V_DS Curves with the CD4007, MOSFET Resistor and Diode Connection
ozet: The MOSFET handout of the EEM214 Electronics I laboratory (2006 Experiment 9, 2012 Experiment 7): ohmic and saturation regions, I_DS equations, r_ohmic, diode-connected MOSFET; I_DS–V_DS tables measured with the CD4007, threshold voltage, r_ohmic and V_MOSDIODE values.
---

This post contains the **MOSFET Transistor Basics** handout of the Başkent University **EEM 214 Electronics I** laboratory and two student reports prepared for this experiment. The handout was prepared in May 2006 as **Experiment 9**; in 2012 the same text was used under the title **Experiment 7** (both versions are in the ZIP). The reports are the work of friends; names and student numbers have been redacted. Since the handout is in English, its text is reproduced in English. For the theory, see the post [Lecture 6 – FET and MOSFET Transistors](/arsiv/eem214-ders-06-fet/).

## Handout: MOSFET Transistor Basics

**Aim:** To familiarize the student with the basic regions of operation of a MOSFET transistor.

### Theory

The MOSFET is a four-terminal device (drain, gate, source, body), but the more common three-terminal symbol is used here; the devices in this lab have the body internally connected to the source. N-channel MOSFETs are studied. Two external sources provide V_DS and V_GS. A sufficiently high V_GS establishes an internal channel between drain and source; the higher V_GS, the easier the drain-source current I_DS flows. The only DC current in the MOSFET is I_DS, since the gate is insulated from the channel.

The MOSFET operates in the **ohmic (linear)** and **saturation (active)** regions. In the I_DS–V_DS curves for constant V_GS, the ohmic region exists where V_DS is small and the curve is nearly linear; as V_DS increases the curve flattens, and at V_D(SAT) = V_GS − V_T the device enters saturation. For 0 ≤ V_DS ≤ V_D(SAT) it is ohmic, for V_DS ≥ V_D(SAT) it is saturated.

1. Ohmic region: I_DS = µ₀C_ox (W/L) [(V_GS − V_T) − V_DS/2] V_DS. Here the MOSFET acts as a voltage-controlled resistor.
1. Its resistance: 1/r_ohmic = ∂I_DS/∂V_DS = µ₀C_ox (W/L) [V_GS − V_T − V_DS].
1. Saturation region (λ = 0): I_DS = ½ µ₀C_ox (W/L) (V_GS − V_T)². Here the device acts as a voltage-controlled current source (used for amplification), shunted by a small-signal resistance r_ds.
1. Diode-connected MOSFET (gate tied to drain, V_GS = V_DS, saturation virtually guaranteed): V_MOSDIODE = V_T + √[ I_DS / (½ µ₀C_ox (W/L)) ].

### Preliminary work

Review Section 4.10 of the textbook. The lab uses the **CD4007** MOSFET array; its NMOS has µ₀C_ox = 166.67 µA/V², W/L = 3, V_T = 1.45 V; assume V_A = 1/λ = 100 V. (The parameter values were obtained from measurements on the CD4007 and provided courtesy of Dr. David M. Binkley and colleagues at the University of North Carolina at Charlotte.)

1. For the MOSFET with V_GS and V_DS applied, find I_DS, the region of operation and, if necessary, r_ohmic for: a) V_GS = 3 V, V_DS = 0.5 V; b) V_GS = 5 V, V_DS = 0.5 V; c) V_GS = 2 V, V_DS = 3 V.
1. Plot the I_DS–V_DS curves in MATLAB for V_GS = 0–4 V in 0.5 V steps (V_DS = 0–5 V in 0.01 V steps), using: if V_GS < V_T, cut-off (I_D = 0); otherwise if V_DS ≤ V_GS − V_T, I_D = µC_ox (W/L)(V_GS − V_T − V_DS/2)V_DS, else I_D = ½µC_ox (W/L)(V_GS − V_T)².
1. Find the V_GS needed for a MOSFET resistor of 100 kΩ at V_DS = 0 V.
1. For the diode-connected MOSFET fed through R (Fig. 7), find V_DS = V_MOSDIODE and R (write KCL at the drain and use Eqs. 3 and 4).
1. Read the experimental work.

### Experimental work

The CD4007 contains three NMOS and three PMOS transistors; NMOS substrates are connected to V_SS (pin 7) and PMOS substrates to V_DD (pin 14). Pin 7 must go to the most negative voltage and pin 14 to the most positive voltage, and the chip must not be connected with the power on. Characteristics vary considerably from chip to chip. MOSFETs are very susceptible to electrostatic discharge: ground yourself before handling the chip and do not touch the pins. Verify the resistors within 2%, set V_GS to +4 V and V_DS to 0 V before connecting.

1. Connect the circuit of Fig. 8 and record I_DS as V_DS varies from 0 to 5 V (0.4 V steps, then 0.2 V) for V_GS = 4, 3 and 2 V; plot the family of curves (Excel) and mark the ohmic and saturation regions.
1. With V_DS = 5 V, find the V_GS at which I_DS becomes negligible (5 µA); this is close to V_T.
1. Connect Fig. 9 with an ohmmeter across drain and source; record r_ohmic for V_GS = 1.5, 2, 3, 4, 5 V and compare with Eq. 2.
1. Using the R found in the preliminary work, set a 100 µA current into the diode-connected MOSFET (Fig. 10), adjusting the potentiometer; record R_POT and V_DS; repeat for 75 µA and 50 µA and compare with Eq. 4.
1. Why would it be necessary to create a resistor from a MOSFET? Name some advantages.
1. Why would a MOSFET be connected like a diode? Would the voltage set by it be helpful in circuit design?

**Components:** CD4007 chip, 100 kΩ potentiometer.

## Student Reports

### I_DS–V_DS measurements (mA)

| V_DS (V) | V_GS = 2 V (2006) | 3 V (2006) | 4 V (2006) | 2 V (2008) | 3 V (2008) | 4 V (2008) |
|---|---|---|---|---|---|---|
| 0.4 | 0.250 | 0.738 | 1.393 | 0.20 | 0.752 | 0.941 |
| 0.8 | 0.262 | 1.170 | 2.129 | 0.20 | 1.171 | 1.712 |
| 1.2 | 0.265 | 1.270 | 2.680 | 0.21 | 1.280 | 2.496 |
| 1.6 | 0.267 | 1.294 | 2.969 | 0.21 | 1.342 | 2.852 |
| 2.0 | 0.268 | 1.304 | 3.049 | 0.21 | 1.354 | 2.931 |
| 3.0 | 0.271 | 1.321 | 3.108 | 0.21 | 1.372 | 2.991 |
| 4.0 | 0.273 | 1.332 | 3.136 | 0.22 | 1.384 | 3.017 |
| 5.0 | 0.276 | 1.342 | 3.154 | 0.22 | 1.140 | 3.040 |

The curves are linear (ohmic) at small V_DS and flatten (saturation) after V_DS ≈ V_GS − V_T. In the 2006 report, the voltage at which I_DS dropped to 5 µA was found to be **V_GS = 1.2 V** (close to the threshold voltage).

### MOSFET resistance (V_DS = 0)

| V_GS | Measured r_ohmic (2006) | Measured r_ohmic (2008) | Calculated from Eq. 2 |
|---|---|---|---|
| 1.5 V | 2.634 kΩ | 2.9 kΩ | 40 kΩ |
| 2 V | 960 Ω | 1 kΩ | 3.636 kΩ |
| 3 V | 447 Ω | 986 Ω | 1.290 kΩ |
| 4 V | 302 Ω | 330 Ω | 784 Ω |
| 5 V | 241 Ω | 280 Ω | 563 Ω |

The report states that the measured and calculated values are "almost the same"; as the table shows, however, the measured resistances are roughly between one half and one third of the calculated ones. This indicates that the V_T and µ₀C_ox values of the chip used differ from those in the handout (as the handout also notes, characteristics vary from chip to chip).

*Note: In the 2006 report, the calculated value for V_GS = 1.5 V is written as "4.000"; with µ₀C_ox(W/L) = 500 µA/V² and V_T = 1.45 V, r_ohmic = 1/(500 µA/V² × 0.05 V) = 40 kΩ. The other calculated values (3.636, 1.290, 0.784, 0.563 in kΩ) are correct.*

### Diode-connected MOSFET

| I_DS | R_POT (2006) | V_DS (2006) | R_POT (2008) | V_DS (2008) | Calculated from Eq. 4 |
|---|---|---|---|---|---|
| 100 µA | 29.18 kΩ | 1.744 V | 31 kΩ | 1.74 V | 2.08 V |
| 75 µA | 40.92 kΩ | 1.658 V | 46 kΩ | 1.66 V | 2.00 V |
| 50 µA | 70.5 kΩ | 1.556 V | 69 kΩ | 1.58 V | 1.90 V |

The 2008 report comments that the MOSFET resistance keeps the drain-source current at the desired value and protects the FET from overcurrent; that the diode connection behaves like a diode; and that I_D is controlled by the electric field between gate and source, and since no current flows through the gate, there is no loading at the input.

## Download

The ZIP file contains the 2006 (Experiment 9, password removed) and 2012 (titled Experiment 7) handouts, together with redacted PDF copies of the 2006 and 2008 reports.
