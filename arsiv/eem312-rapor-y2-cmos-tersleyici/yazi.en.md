---
baslik: EEM312 Digital Electronics: Lab Report Y2, Comparison of VTC and Delay for Four Inverter Structures (2014)
ozet: EEM312 Digital Electronics software lab experiment Y2 report: SPICE VTC curves of resistor-load NMOS, pseudo-NMOS, resistor-load PMOS, and CMOS inverters, VOH, VOL, VIH, VIL, VM, noise margins, tr, tf, tpHL, tpLH, and the effect of PMOS width.
---

This post presents a report prepared in 2014 for the **Y2: CMOS inverter characteristics** experiment of the Başkent University **EEM312 Digital Electronics** software lab. It is a friend's report; **personal information has been removed**. The schematics and questions for the four circuits in the handout are in the post [EEM312 software lab handouts Y1–Y3](/arsiv/eem312-yazilim-deneyleri-y1-y3/). The report with personal information redacted and the SPICE netlists are in the ZIP at the end of the post.

The four circuits were simulated with the same Level 2 MOSN/MOSP models, a 3.1 V supply, and a 1 fF load:

- **(a)** NMOS with a 100 kΩ resistor load,
- **(b)** NMOS with a PMOS load whose gate is tied to ground (pseudo-NMOS),
- **(c)** PMOS with a 100 kΩ resistor as its load (resistor-load PMOS),
- **(d)** CMOS inverter.

As an example, the DC analysis of circuit (d) (model parameters abbreviated):

```
*D)
.MODEL MOSN NMOS LEVEL=2 LD=0.15U TOX=200.0E-10 ...
.MODEL MOSP PMOS LEVEL=2 LD=0.15U TOX=200.0E-10 ...
VIN 3 0 PULSE(0 5 0NS 2NS 2NS 500NS 1US)
VDC 1 0 DC 3.1
C1 2 0 1ff
M1 2 3 1 1 MOSP W=1.8U L=1.2U NRS=0.333 NRD=0.333
M2 2 3 0 0 MOSN W=1.8U L=1.2U NRS=0.333 NRD=0.333
.CONTROL
DC VIN 0 5 0.1
PLOT V(2) vs V(3)
.ENDC
```

## Question 1: Values read from the VTC

| Circuit | V_OH | V_OL | V_IH | V_IL | V_M | NM_H | NM_L |
|---|---|---|---|---|---|---|---|
| (a) NMOS + R | 3.10 V | 118.1 mV | 1.40 V | 700 mV | 1.23 V | 1.70 V | 581.9 mV |
| (b) pseudo-NMOS | 3.10 V | 296 mV | 2.0 V | 1.80 V | 1.83 V | 1.10 V | 1.504 V |
| (c) PMOS + R | 2.70 V | 0 V | 2.30 V | 1.20 V | 1.540 V | 400 mV | 1.20 V |
| (d) CMOS | 3.10 V | 0 V | 1.40 V | 1.20 V | 1.29 V | 1.70 V | 1.20 V |

The noise margins are consistent with the definitions NM_H = V_OH − V_IH and NM_L = V_IL − V_OL. Only in the CMOS inverter are both V_OL = 0 and V_OH = V_DD; in the ratioed circuits (a, b) V_OL does not reach zero, and in (c) V_OH cannot reach the supply.

## Question 2: Transient measurements

Times measured (in ns) with a 0–3.1 V pulse of 10 ns period applied to the input (`PULSE(0 3.1 0 1ns 1ns 4ns 10ns)`):

| Circuit | t_r | t_f | t_pHL | t_pLH | t_d |
|---|---|---|---|---|---|
| (a) | 2 | 0.4 | 0.2 | 0.8 | 0.5 |
| (b) | 0.5 | 0.3 | 0.3 | 0.2 | 0.2 |
| (c) | 1.6 | 3 | 0.4 | 0.2 | 0.4 |
| (d) | 0.4 | 0.3 | 0.2 | 0.5 | 0.3 |

In the resistive loads (the rise in (a), the fall in (c)), the load charges and discharges through 100 kΩ, so the corresponding transition time is noticeably longer.

*Note: With t_d = (t_pHL + t_pLH)/2, (b) comes out as 0.25 ns, (c) as 0.3 ns, and (d) as 0.35 ns; the report lists 0.2, 0.4, and 0.3 ns, respectively.*

## Questions 3–4: Comments

- **Best inverter:** circuit (d), the CMOS inverter: its VTC has the transition region closest to vertical, i.e., its gain in the transition region is closest to that of an ideal inverter.
- **Symmetry:** According to the report, the circuits are not symmetric; to achieve symmetry, the capacitance and resistance values in the MOSN and MOSP definitions need to be adjusted.
- **PMOS width:** Since the saturation current is I_D = (k'/2)(W/L)(V_GS − V_T)², increasing the PMOS W lowers its internal resistance and increases its current-sourcing capability. In circuit (d), when W_p is increased, the transition region of the VTC becomes steeper and the output stays "high" up to higher input values (V_M shifts to the right).

*Note: For a symmetric CMOS inverter (V_M ≈ V_DD/2, t_pHL ≈ t_pLH), the actual adjustment is the W/L ratios: the KP values in the model are 8.0E−5 (NMOS) and 2.7E−5 (PMOS), and since their ratio is about 3, W_p ≈ 3·W_n should be used. The choice of W_p = 5.4 µm, W_n = 1.8 µm used in the handout's later experiments comes from this; in this report, however, both transistors are 1.8 µm, so V_M (1.29 V) falls below V_DD/2 (1.55 V).*

The file `y2_2017_cmos_gecici.cir` in the ZIP is the CMOS inverter (W_p = 5.4 µm, W_n = 1.8 µm) transient netlist from the 2017 version of the same experiment.
