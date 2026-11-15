---
baslik: EEM312 Digital Electronics: CMOS Threshold Voltage, Noise, and Inverter Chain, Handwritten Notes
ozet: The ideal inverter, fan-out, derivation of the CMOS switching threshold, junction capacitance calculation, and the optimal number of stages in an inverter chain. Formulas and results from the handwritten notes.
---

This post contains study sheets on CMOS inverters prepared by a friend, taken from the **EEM312 Digital Electronics** folder. They were transcribed to text from photographed pages; personal information has been removed. The pages carry no date, and the files bear an April 2014 archive date. The source photographs are kept in a private archive; the post has no download file.

## The ideal inverter and noise measures

The voltage transfer characteristic of the ideal inverter drops from V_DD to zero at the point V_in = V_DD/2:

- V_OL = 0; V_OH = V_DD; V_SW = V_DD.
- V_IL = V_IH = V_DD/2.
- V_NMH = V_OH − V_IH = V_DD/2.
- V_NML = V_IL − V_OL = V_DD/2.

In a real inverter the transition has finite width. In the page's notation, the undefined region lies between V_IL and V_IH; V_M is the point where the input equals the output.

Noise sensitivities:

**V_NSH = V_OH − V_M**, **V_NSL = V_M − V_OL**.

Normalized noise immunities:

**V_NIH = V_NSH/V_SW**, **V_NIL = V_NSL/V_SW**.

In the ideal symmetric case, both sensitivities are V_DD/2 and both normalized immunities are 1/2.

## Fan-in and fan-out

The note defines fan-in as the number of inputs of a gate. For the inputs the output must drive, it writes **I_out = N I′_in**. In the ideal case, R_in → ∞ reduces input loading; R_out → 0 shortens the charging time of the load.

The separate limits at the high and low logic levels:

N_high = I_out(high)/I′_in(high),

N_low = I_out(low)/I′_in(low).

The maximum fan-out is the integer not exceeding the smaller of these two values.

*Note: In one place the source abbreviates fan-out as "number of outputs." The quantity being computed is not the number of physical output terminals, but the number of gate inputs that a single output can drive.*

## CMOS switching threshold

At the point V_in = V_out = V_M, the saturation currents of the two transistors are equal. The initial equation the source writes using signed PMOS voltages:

k_n V_DSATn[V_M − V_Tn − V_DSATn/2]

+ k_p V_DSATp[V_M − V_DD − V_Tp − V_DSATp/2] = 0.

Collecting the terms containing V_M:

V_M(k_nV_DSATn + k_pV_DSATp)

= k_nV_DSATn(V_Tn + V_DSATn/2)

+ k_pV_DSATp(V_DD + V_Tp + V_DSATp/2).

With the definition **r = k_pV_DSATp/(k_nV_DSATn)**:

**V_M = [(V_Tn + V_DSATn/2) + r(V_DD + V_Tp + V_DSATp/2)]/(1 + r)**.

In the note, using k = μC_ox(W/L):

r = [μ_p C_ox,p(W_p/L_p)V_DSATp] / [μ_n C_ox,n(W_n/L_n)V_DSATn].

### Large-overdrive approximation

The expression V_DSAT = E_cL V_GT/(E_cL + V_GT) approaches E_cL for large V_GT. On this page E_cL = Lv_sat/μ is written. Taking C_ox,n = C_ox,p for equal oxide thicknesses, the ratio the note arrives at is:

r ≈ v_sat,p W_p/(v_sat,n W_n).

Assuming V_DD is large compared with the threshold and saturation voltages:

V_M ≈ rV_DD/(1 + r).

Choosing r = 1 gives V_M ≈ V_DD/2. The corresponding sizing:

(W_p/L_p) = (W_n/L_n)[V_DSATn k′_n/(V_DSATp k′_p)].

*Note: The other page of the MOS velocity saturation derivation uses E_c = 2v_sat/μ; the approximation on this page is not the same as that critical-field definition. The signed PMOS quantities should also not be confused with the absolute-value formulas.*

### General W/L ratio

The result found on a separate page for a target V_M:

**(W/L)_p/(W/L)_n = k′_n V_DSATn(V_M − V_Tn − V_DSATn/2) / [k′_p V_DSATp(V_DD − V_M + V_Tp + V_DSATp/2)]**.

This is the initial current-equality equation rearranged for the transistor sizes.

## Average value of the junction capacitance

The example with V_DD = 2.5 V considers the first half-transition of the output. While the reverse-bias voltage changes from 2.5 V to 1.25 V, m = 0.5 and Φ₀ = 0.9 V are used for the bulk junction. The equivalent coefficient on the page:

K_eq = −Φ₀^m [(Φ₀ + 2.5)^(1−m) − (Φ₀ + 1.25)^(1−m)] / [(-2.5 + 1.25)(1−m)] ≈ **0.57**.

For the half-transition corresponding to a reverse bias from 0 V to 1.25 V:

K_eq = −Φ₀^m [(Φ₀ + 1.25)^(1−m) − Φ₀^(1−m)] / [(-1.25)(1−m)] ≈ **0.79**.

For the 0.25 µm process, 2λ = 0.25 µm, λ = 0.125 µm, and 19λ² ≈ 0.3 µm² are written. The gate-drain overlap contributions:

- NMOS: 2 × 0.31 × 0.375 ≈ 0.23 fF.
- PMOS: 2 × 0.27 × 1.125 ≈ 0.61 fF.

On the back page, K_eq,n = 0.57, K_eq,sw,n = 0.61, A_D = 0.3 µm², P_D = 1.875 µm are taken:

C_db1 = K_eq,n A_D C_j + K_eq,sw,n P_D C_jsw

= 0.57 × 0.3 × 2 + 0.61 × 1.875 × 0.28 ≈ **0.66 fF**.

In the small sketch in the perimeter calculation, 5λ + 4λ + 4λ + λ + λ = 15λ; 15 × 0.125 = 1.875 µm. The rest of the note says that this load capacitance and R_eq, which scales with W/L, will be used in the inverter transient example; the page does not contain the final delay calculation.

## Equal stage ratio in an inverter chain

In the three-stage sketch, the input capacitances are labeled a, b, c and the final load d:

d/c = c/b = b/a = f.

Thus b = af, c = af², d = af³; **f = (d/a)^(1/3)**. For the intermediate capacitances, b = √(ac), c = √(bd) are written.

For a general N stages, F = C_L/C_in and f = F^(1/N). The note's total delay model:

**t_p = Nt_p0[1 + F^(1/N)/γ]**.

Differentiating with respect to N and setting the result to zero:

γ + F^(1/N) − F^(1/N)ln(F)/N = 0.

Substituting F = f^N gives γ + f − f ln f = 0, and therefore:

**f = e^(1 + γ/f)**.

In the note, the result N = ln F and f = e for the limit γ = 0 is additionally boxed.

*Note: The γ = 0 result belongs to the ideal limit of the derivative condition; setting zero directly in the delay expression containing 1/γ is undefined.*

### Example with F = 64, γ = 1

| Number of stages N | Stage ratio F^(1/N) | t_p/t_p0 in the source |
|---|---|---|
| 1 | 64 | 65 |
| 2 | 8 | 18 |
| 3 | 4 | 15 |
| 4 | About 2.8 | 15.3 |

Among these options, three stages give the smallest total delay. For four stages, the exact calculation is 4(1 + 64^(1/4)) ≈ 15.314, which agrees with the source's result of 15.3.
