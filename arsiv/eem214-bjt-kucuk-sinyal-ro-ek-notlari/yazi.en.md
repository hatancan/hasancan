---
baslik: EEM214 Electronics I: BJT Small-Signal Model and the Effect of rₒ on Input Resistance
ozet: Common-base and common-emitter configurations, the hybrid-π model, a 12 V BJT amplifier example; the effect of finite output resistance in the emitter-resistor configuration and in the emitter follower.
---

This post contains a friend's lecture notes from the EEM214 Electronics I folder, dated **April 8, 2013**, along with two handwritten supplementary derivations. It was transcribed from photographed pages; personal information has been removed. Because the source images are kept in a private archive, this post contains no images or downloadable files.

## Common-base configuration and the hybrid-π model

In the common-base configuration, the input is between the emitter and the base, and the output is between the collector and the base. In the small-signal equivalent, the emitter input resistance is r_e, and the collector current source is represented by αi_e:

Z_E = v_i/i_e = r_e.

In the hybrid-π model of the BJT, r_π lies between the base and the emitter, and the g_m v_be dependent current source and r_o lie between the collector and the emitter. The r_μ between the base and the collector is assumed to be very large and is neglected.

- g_m = I_C/V_T, in siemens.
- V_T is approximately 25–26 mV.
- r_π = v_be/i_b = β/g_m = V_T/I_B.
- i_b = i_c/β = (g_m/β)v_be.
- r_e = V_T/I_E.
- With the approximation I_C ≈ I_E, r_e ≈ 1/g_m and r_π ≈ βr_e.

*Note: The equality r_π = βr_e is used in the notes under the approximation I_C ≈ I_E. If the definition r_e = V_T/I_E is applied exactly, then r_π = (β + 1)r_e.*

## Common-emitter amplifier example

In the given circuit, **V_CC = 12 V, R_B = 470 kΩ, R_C = 3 kΩ, β = 100, r_o = 50 kΩ**; the emitter is grounded. The quantities requested are the input/output resistances and the voltage/current gains.

### DC operating point

I_B = (12 − 0.7)/470 kΩ = **24.04 µA**.

I_E = (β + 1)I_B ≈ **2.428 mA**.

r_e = 26 mV/2.428 mA ≈ **10.71 Ω**.

The note, using I_C ≈ 2.4 mA, finds:

V_CEQ = 12 − 2.4 mA·3 kΩ = **4.8 V**.

The endpoints of the load line are I_C,sat = 4 mA and V_CE,cutoff = 12 V. Since the smaller swing margin of the Q point is 4.8 V, the largest symmetric output swing drawn with ideal limits is given as **9.6 V_pp**.

*Note: The 9.6 V_pp calculation assumes V_CE at saturation is zero; the actual saturation voltage and the limits of linear operation reduce the usable swing.*

### Input and output resistance

In the AC equivalent, the supply is at ground and the coupling capacitors are short circuits:

- Z_i = R_B ∥ βr_e = 470 kΩ ∥ 1071 Ω ≈ **1.07 kΩ**.
- Z_o = R_C ∥ r_o = 3 kΩ ∥ 50 kΩ ≈ **2.83 kΩ**.
- If r_o is neglected, Z_o ≈ R_C.

In calculating the output resistance, the independent signal source at the input is set to zero. If a load is connected, the total parallel resistance at the output node is R_C ∥ r_o ∥ R_L.

### Voltage gain

In the notes, using current division:

- i_RC = βi_b·r_o/(r_o + R_C).
- i_ro = βi_b·R_C/(r_o + R_C).
- v_o = −βi_b(R_C ∥ r_o).

From this:

A_v ≈ −(R_C ∥ r_o)/r_e.

For r_o → ∞, A_v ≈ −R_C/r_e = −3000/10.71 ≈ **−280.11**. The negative sign indicates phase inversion. With a load, A_v ≈ −(R_C ∥ r_o ∥ R_L)/r_e.

### Current gain

The division of the input current between the base resistor and the transistor input:

i_b/i_i = R_B/(R_B + βr_e).

Taking the output current direction according to the arrows in the notes:

A_i = [βr_o/(r_o + R_C)]·[R_B/(R_B + βr_e)].

For r_o → ∞, A_i = βR_B/(R_B + βr_e).

## Supplement 1: Finite rₒ in the common emitter with emitter resistor

In the circuit, the resistance from the base to ground is R_B, the resistance from the emitter to ground is R_E, and the resistance from the collector to ground is R_C. The base-emitter resistance of the transistor is taken as βr_e, and the collector-emitter resistance as r_o.

Using dependent source transformations, the note first defines:

R′ = R_E ∥ (r_o + R_C) = R_E(r_o + R_C)/(R_E + r_o + R_C).

The base voltage is:

v_b = i_b(βr_e + R′) + [βi_b r_o/(r_o + R_C)]R′.

Thus:

Z_b = v_b/i_b = βr_e + R′ + βr_oR′/(r_o + R_C)

= βr_e + R_E[(β + 1)r_o + R_C]/(R_E + r_o + R_C)

= **βr_e + R_E[(β + 1) + R_C/r_o]/[1 + (R_E + R_C)/r_o]**.

The input resistance of the amplifier is **Z_i = R_B ∥ Z_b**. Finite r_o changes the contribution of the emitter resistor reflected to the base.

## Supplement 2: Finite rₒ in the emitter follower

Since the collector is at AC ground, the resistance seen by the emitter is R_E ∥ r_o. From the equivalent in the note:

v_b = i_b[βr_e + (R_E ∥ r_o)] + βi_b(R_E ∥ r_o).

Z_b = βr_e + (β + 1)(R_E ∥ r_o)

= **βr_e + R_E(β + 1)/(1 + R_E/r_o)**.

The total input is again **Z_i = R_B ∥ Z_b**. The drawings on the two supplementary pages show step by step the source transformations that lead to these results; here, the description of the connections and the intermediate relations are preserved in text.
