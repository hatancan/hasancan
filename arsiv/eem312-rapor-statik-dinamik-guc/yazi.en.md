---
baslik: EEM312 Digital Electronics: Static and Dynamic Power Lab Reports, Power and Power-Delay Product in the CMOS Inverter (2005–2017)
ozet: A comparison of nine student reports from 2005–2017 on the static and dynamic power experiment of the EEM312 Digital Electronics software laboratory: short-circuit current in the CMOS inverter, Pdyn = C·VDD²·f, the effect of period, VDD and load capacitance, the power-delay product versus VDD, and the optimum supply voltage.
---

This post compares nine reports written for the **static and dynamic power** experiment of the Başkent University **EEM312 Digital Electronics** software laboratory. The experiment was carried out under different numbers over the years: **Y7** in 2005–2006, **Y5** in the 2011 handouts, "Experiment 9" in 2014, and again "Experiment 9" in 2017. The reports are: one dated 19 May 2005 (A), five from spring 2006 (B–F), and one each from 2011 (G), 2014 (H) and 2017 (I). They are all the work of friends; **personal information has been removed**. The handout is in the post [EEM312 software laboratory handouts Y4–Y8](/arsiv/eem312-yazilim-deneyleri-y4-y8/) (Y5 section). The reports with personal information redacted and the SPICE netlists are in the ZIP at the end of the post.

The circuit is the CMOS inverter with the Level 2 model from the handout: PMOS L/W = 1.2 µm/5.4 µm, NMOS L/W = 1.8 µm... 

Correction — let me give the full, accurate translation:

---
baslik: EEM312 Digital Electronics: Static and Dynamic Power Lab Reports, Power and Power-Delay Product in the CMOS Inverter (2005–2017)
ozet: A comparison of nine student reports from 2005–2017 on the static and dynamic power experiment of the EEM312 Digital Electronics software laboratory: short-circuit current in the CMOS inverter, Pdyn = C·VDD²·f, the effect of period, VDD and load capacitance, the power-delay product versus VDD, and the optimum supply voltage.
---

This post compares nine reports written for the **static and dynamic power** experiment of the Başkent University **EEM312 Digital Electronics** software laboratory. The experiment was carried out under different numbers over the years: **Y7** in 2005–2006, **Y5** in the 2011 handouts, "Experiment 9" in 2014, and again "Experiment 9" in 2017. The reports are: one dated 19 May 2005 (A), five from spring 2006 (B–F), and one each from 2011 (G), 2014 (H) and 2017 (I). They are all the work of friends; **personal information has been removed**. The handout is in the post [EEM312 software laboratory handouts Y4–Y8](/arsiv/eem312-yazilim-deneyleri-y4-y8/) (Y5 section). The reports with personal information redacted and the SPICE netlists are in the ZIP at the end of the post.

The circuit is the CMOS inverter with the Level 2 model from the handout: PMOS L/W = 1.2 µm/5.4 µm, NMOS L/W = 1.2 µm/1.8 µm. The instantaneous power is taken as the product of the supply current and voltage; the 2017 report's netlist also computes the average directly:

```
M1 3 1 0 0 MOSN W=1.8u L=1.2u NRS=0.333 NRD=0.333
M2 3 1 2 2 MOSP W=5.4u L=1.2u NRS=0.333 NRD=0.333
Vdd 2 0 5V
Cl 3 0 0.1p
Vin 1 0 pulse (0V 5V 0 10ns 10ns 100ns 200ns)
.control
tran 0.1ns 800ns
print mean (-Vdd#branch*V(2))
plot -Vdd#branch*V(2)
.endc
```

## 1a. DC analysis: short-circuit power

While V_in is swept from 0 to 5 V (with V_DD also stepped between 0 and 5 V), the power drawn from the supply reaches its maximum when the input is around V_DD/2: the reports read the peak at V_in ≈ 2.65–2.7 V. In this region the NMOS and PMOS conduct at the same time, so a direct path from V_DD to ground forms (short-circuit/direct-path current). As V_DD increases, this peak rises rapidly; report B explains this with P_stat = I_stat·V_DD.

## 1b–d. Dynamic power: effect of period, V_DD and C_L

The dynamic power is given by **P_dyn = P₀→₁·C_L·V_DD²·f**. The common observation in all reports: power is consumed only at the switching instants; the largest peak occurs at the **0-to-1 transition of the output**, when the load capacitor is charged from the supply through the PMOS, while no energy is drawn from the supply during discharge.

Theoretical values (from report C's calculation): for C_L = 0.1 pF and V_DD = 5 V, P_dyn = 12.5 µW at a 200 ns period (f = 5 MHz) and 25 µW at a 100 ns period (10 MHz); 50 µW for C_L = 0.2 pF. Simulation results:

| Condition (V_DD = 5 V) | A/G | B/H | E | F | I |
|---|---|---|---|---|---|
| C_L = 0.1 pF, T = 200 ns | 15.1 µW | 15.1 µW | – | 31.9 µW | 5.06 µW |
| C_L = 0.1 pF, T = 100 ns | 30.14 µW | 30.14 µW | 31.1 µW | 63.4 µW | 2.50 µW |
| C_L = 0.2 pF, T = 100 ns | – | 55.04 µW | 56.1 µW | 83.7 µW | 56.1 µW |

Effect of V_DD: in report E, for C_L = 0.2 pF and T = 100 ns, the power is 19.6 µW at V_DD = 3 V and 56.1 µW at 5 V (ratio ≈ 2.9, while the V_DD² ratio is 25/9 ≈ 2.8); in report F it is 21.9 µW at 3 V. Reports A, G and C show by calculation that when C_L is doubled the power doubles as well (25 µW → 50 µW).

*Note: In reports A, B, G and H, the average powers are written in watts, such as "15.1 W", "30.14 W", "55.04 W"; the values given by the simulation are on the order of microwatts (e.g. 0.1 pF·25 V²·10 MHz = 25 µW). The units in the table were corrected to µW.*

*Note: Reports B and H give 55.04 µW for C_L = 0.2 pF, T = 200 ns and 20 µW for T = 100 ns; power should increase when the frequency doubles, so the two values appear to have been swapped or measured incorrectly (placed in the table as 55.04 µW in the T = 100 ns row). Report I also finds 2.50 µW for the 100 ns period and 5.06 µW for 200 ns and states that "power is the same for both periods" and that "power increased as the transition time increased"; these results contradict the relation P_dyn ∝ f (power should increase with frequency).*

*Note: Report A states that the simulation shows "power did not change" when C_L is doubled, whereas the same report's theoretical calculation predicts a twofold increase; the simulations in reports E and F show the increase.*

## 2. Power-delay product versus V_DD

At C_L = 0.1 pF and T = 100 ns, V_DD was varied from 1 to 5 V, and the average power P_av, the propagation delay t_p and the **PDP = P_av·t_p** were found.

| V_DD | A/G: t_p | A/G: P_av | A/G: PDP | B/H: P_av | B/H: t_p | B/H: PDP | E: PDP | D: PDP |
|---|---|---|---|---|---|---|---|---|
| 1 V | 3550 ps | 1.19 µW | 4.23 fJ | 1.354 µW | 3540 ps | 4.79 fJ | 4.22 fJ | 4.19 fJ |
| 1.5 V | 1850 ps | 2.6 µW | 4.81 fJ | 2.91 µW | 1862 ps | 5.4 fJ | 4.83 fJ | 4.78 fJ |
| 2 V | 1350 ps | 4.7 µW | 6.34 fJ | 5.05 µW | 1339 ps | 6.76 fJ | 6.3 fJ | 6.37 fJ |
| 2.5 V | 1000 ps | 7.36 µW | 7.4 fJ | 7.78 µW | 1020 ps | 7.93 fJ | 7.43 fJ | 7.38 fJ |
| 3 V | 820 ps | 10.6 µW | 8.7 fJ | 11.1 µW | 860 ps | 9.55 fJ | 9.01 fJ | 8.72 fJ |
| 4 V | 850 ps | 19.3 µW | 16.41 fJ | 19.5 µW | 835 ps | 16.3 fJ | 16.21 fJ | 16.38 fJ |
| 5 V | 750 ps | 31.2 µW | 23.4 fJ | 30.14 µW | 764 ps | 23 fJ | 23.55 fJ | 23.44 fJ |

Report F found larger values in a separate simulation (e.g. 1.24 µW and 5.85 ns at 1 V, 8.29 µW and 2.38 ns at 2.5 V, 63.33 µW and 1.78 ns at 5 V). Report C calculated the PDP using the theoretical P_dyn = C_L·V_DD²·f values (1 µW at 1 V, 25 µW at 5 V).

Nearly all of them choose **V_DD = 2.5 V** as the best operating point: below this value the delay grows rapidly, and above it the power increases with V_DD² while the delay decreases very little. The common comment for short-channel MOSFETs: the channel resistance and t_p decrease, and if the average power does not change, the PDP decreases.

*Note: The PDP values in the tables are consistent with the product P_av·t_p (e.g. 1.19 µW × 3.55 ns = 4.22 fJ). However, the PDP increases continuously with V_DD; the smallest PDP is at 1 V. The choice of 2.5 V comes not from the minimum of the PDP but from considering energy and speed together: the energy-delay product PDP·t_p, using the A/G values, is ≈ 15·10⁻²⁴ J·s at 1 V, 8.6·10⁻²⁴ at 2 V, 7.4·10⁻²⁴ at 2.5 V, 7.1·10⁻²⁴ at 3 V and 17.6·10⁻²⁴ at 5 V; so the optimum region is indeed around 2.5–3 V.*

*Note: Reports D and E give the unit of PDP as "W" and report C as "pW"; the PDP is an energy, and its unit is the joule (here fJ). Report C's value of "3.03 pW" should also be 1 µW × 303 ps = 0.303 fJ. The PDP column of report F, on the other hand, does not agree with the product of its own P_av and t_p values (e.g. for 1 V, 1.24 µW × 5.85 ns ≈ 7.3 fJ, while the report gives 5.85 fJ).*

## Similarities among the reports

Some of the reports in the folder share the same simulation results: the PDP table and text of A and G, and the power and PDP values of B and H, are identical. They are shown together in the tables to make the comparison easier. Two reports that use A's table and text verbatim, and one report that uses E's text verbatim, were not included separately because they are copies.
