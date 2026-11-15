---
baslik: EEM312 Digital Electronics: MOS Operating Regions, Velocity Saturation, and Capacitances, Handwritten Notes
ozet: Channel formation in NMOS/PMOS, body effect, channel-length modulation, derivation of the velocity-saturation voltage, and calculation of MOS capacitances. A readable text transcription from handwritten study sheets.
---

**EEM312 Digital Electronics** archive: this study set consists of handwritten notes, in Turkish and English, on MOS transistors prepared by a friend. They were transcribed to text from photographed pages; personal information was removed. The document carries no date; the archive date of the sources is April 2014. The photographs are kept in a private archive, and no downloadable document is provided.

## Gate insulation and channel formation

The notes give the following illustrative dimensions and values:

- SiO₂ thickness: 20–100 nm = 0.02–0.1 µm.
- Insulated-gate current: approximately 10⁻¹⁵ A.
- Channel length L ≈ 1–10 µm and width W ≈ 2–500 µm.
- Short-channel example: L ≈ 0.25 µm, W ≈ 0.375 µm.
- Without gate bias, the drain-source path has resistance on the order of 10¹² Ω.

These are values written in the archived notes, associated with the technologies studied there.

An induced n-channel is an inversion layer. V_T is the threshold voltage at which inversion occurs; the notes use positive V_T for enhancement NMOS and negative V_T for enhancement PMOS. **V_GS − V_T** is the excess gate voltage or overdrive.

With V_DS applied, electrons move from source to drain. Channel potential rises from 0 at the source to V_DS at the drain. The gate-to-channel voltage falls from V_GS to V_GS − V_DS, so the channel tapers toward the drain.

## Triode and saturation regions

As V_DS increases, the channel narrows at the drain and its resistance increases. The I_D–V_DS curve bends away from its initial nearly linear part. At **V_DS = V_GS − V_T**, the drain end reaches pinch-off.

| Device | Channel induced | Continuous channel / triode | Saturation |
|---|---|---|---|
| NMOS | V_GS ≥ V_T | V_DS < V_GS − V_T | V_DS ≥ V_GS − V_T |
| PMOS, signed voltages | V_GS ≤ V_T | V_DS > V_GS − V_T | V_DS ≤ V_GS − V_T |

Using **V_GS = V_GD + V_DS**, the notes rewrite the saturation condition as V_GD ≤ V_T for NMOS and V_GD ≥ V_T for PMOS.

The algebra at the region boundary is:

(V_GS − V_T)(V_GS − V_T) − (V_GS − V_T)²/2 = (V_GS − V_T)²/2.

The ideal long-channel saturation picture has constant current beyond pinch-off. The next section adds the channel-length effect.

## Channel-length modulation

Increasing V_DS beyond pinch-off extends the depleted drain region and shortens the effective conducting channel. The notes write:

**I_D = ½k′_n(W/L)(V_GS − V_T)²(1 + λV_DS)**.

Extrapolated saturation curves intersect the V_DS axis at −V_A = −1/λ. V_A is compared to the Early voltage of a BJT. The slope is marked **1/r_o**.

For the intercept, define Z = ½k′_n(W/L)(V_GS − V_T)². Then 0 = Z(1 + λV_DS) gives V_DS = −1/λ.

## Body effect in stacked NMOS devices

The drawing contains two stacked NMOS transistors. The lower source is grounded, with V_SB1 = 0; the upper source is above ground, with V_SB2 ≠ 0. The notes indicate:

|V_SB2| > |V_SB1| ⇒ V_T2 > V_T1.

Increasing source-body reverse bias raises the threshold. A separate warning on the page says that V_SB should remain above approximately −0.6 V for the NMOS example; otherwise the source-body diode becomes forward biased.

*Note: A second image of the same body-effect drawing was also among the sources; it was transcribed only once.*

## Derivation of the velocity-saturation voltage

The note uses the definitions V_GT = V_GS − V_T and K(V) = 1/[1 + V/(E_cL)]. At the saturation point, the two current expressions are equated:

v_sat C_ox W(V_GT − V_DSAT)

= K(V_DSAT) μ_n C_ox(W/L)[V_GT V_DSAT − V_DSAT²/2].

Using the definition **E_c = 2v_sat/μ_n** on this page:

V_GT − V_DSAT = K(V_DSAT) V_DSAT(2V_GT − V_DSAT)/(LE_c).

Substituting K(V_DSAT) = E_cL/(E_cL + V_DSAT):

V_DSAT(2V_GT + E_cL) = V_GT(E_cL + V_DSAT),

V_DSAT(V_GT + E_cL) = V_GT E_cL.

Result:

**V_DSAT = V_GT E_cL/(V_GT + E_cL) = V_GT K(V_GT)**.

For large V_GT, V_DSAT ≈ E_cL.

*Note: The CMOS threshold calculation page of the same set of notes uses the approximation E_c = v_sat/μ, whereas here the definition is 2v_sat/μ. Since the critical-field definitions of the two pages differ, the coefficients should not be carried directly from one to the other.*

## Saturation current and equivalent resistance

The other approximation given in the note:

I_DSAT = v_sat C_ox W[V_GS − (V_T + V_DSAT/2)].

With V_GS = V_DD and the assumption V_DD ≫ V_T + V_DSAT/2:

I_DSAT ≈ v_sat C_ox W V_DD.

R_eq = (3/4)(V_DD/I_DSAT)[1 − (7/9)λV_DD].

Thus V_DD cancels in the first factor. The note states that in this approximation the resistance becomes largely independent of the supply voltage; the remaining small variation comes from channel-length modulation.

## Example of MOS capacitances at zero bias

Data given in the source:

| Parameter | Value |
|---|---|
| t_ox | 6 nm |
| L | 0.24 µm |
| W | 0.36 µm |
| L_D = L_S | 0.625 µm |
| C₀ | 3 × 10⁻¹⁰ F/m |
| C_j0 | 2 × 10⁻³ F/m² |
| C_jsw0 | 2.75 × 10⁻¹⁰ F/m |

C_ox = ε_ox/t_ox ≈ 5.7 fF/µm².

C_GC = WL C_ox ≈ 0.49 fF.

The source and drain overlap capacitances are each calculated as W C₀; the page gives 0.105 fF. The total gate capacitance on the page is **0.49 + 0.105 + 0.105 = 0.7 fF**.

Base and sidewall components of the diffusion capacitance:

- C_bottom = C_j0 L_D W = 0.45 fF.
- C_sidewall = C_jsw0(2L_D + W) ≈ 0.44 fF.
- Total diffusion capacitance ≈ **0.89 fF**.

*Note: With the written W = 0.36 µm and C₀ = 0.3 fF/µm, the overlap capacitance comes out to 0.108 fF; 0.105 fF is a rounded/different intermediate value used in the source. With this data, the total gate capacitance is approximately 0.708 fF.*

## Sheet and contact resistance

For a uniform conductive strip:

R = ρL/A, A = tw ⇒ **R = (ρ/t)(L/W) = R_□(L/W)**.

R_□ is the sheet resistance; its unit is written as Ω/square. If L and W are scaled up by the same ratio, the L/W ratio and the resistance do not change. The source/drain series resistance in the note is:

R_S,D = (L_S,D/W)R_□ + R_C.

R_C is the contact resistance. Series resistance reduces the drain current at the same control voltage. The source lists a low-resistivity surface treatment and widening the transistor as ways to reduce the resistance; after the surface treatment, it gives a value on the order of 1–4 Ω/square.
