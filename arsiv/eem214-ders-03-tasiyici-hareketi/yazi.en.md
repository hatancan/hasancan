---
baslik: EEM214 Electronics I: Lecture 3 – Carrier Action and the P-N Junction
ozet: The third lecture of EEM214 Electronics I: drift and diffusion currents, mobility, resistivity, the Einstein relationship, band bending, the depletion region, the built-in potential V_bi, and the band diagrams of forward- and reverse-biased P-N junctions.
---

This post is the content of the *Lecture 3: Carrier Action* presentation from the **EEM214 Electronics I** course at Başkent University. The presentation is among the lecture slides of the course instructor, Assist. Prof. Dr. Derya Yılmaz (last edited February 2012); the title slide credits Luis G. Sison (University of the Philippines – Diliman), so the slides appear to be adapted from his lecture notes. Topic: the motion of carriers by drift and diffusion, followed by the qualitative behavior of the P-N junction based on this knowledge. Since the slides are in English, the text is reproduced in English as well; the band diagrams are provided as slide images. The archive also contained a shorter 19-slide copy of this presentation; the full 24-slide version was used here. The original presentation file can be downloaded at the end of the post.

## Causes of carrier motion

- **Drift:** caused by electric field (or potential difference)
- **Diffusion:** caused by difference in concentration of carriers

![Drift: holes move in the direction of the field and electrons in the opposite direction under an external voltage; diffusion: motion arising from a concentration difference](s-02.jpg "Causes of carrier motion")

## Drift currents

Drift current density:

- J_P|drift = q·μ_p·p·ε for holes
- J_N|drift = q·μ_n·n·ε for electrons

Terminal velocity is reached for high E-fields.

### Mobilities

| Material (room temperature) | μ_p | μ_n |
|---|---|---|
| Si (almost pure) | ≈ 460 cm²/V·s (at N_A = 10¹⁴/cm³) | ≈ 1360 cm²/V·s (at N_D = 10¹⁴/cm³) |
| GaAs (high purity) | ≈ 400 cm²/V·s (at N_A ≤ 10¹⁵/cm³) | ≈ 8000 cm²/V·s (at N_D ≤ 10¹⁵/cm³) |

Electrons are faster than holes.

**Doping dependence:** mobility decreases as a result of increased scattering by ionized impurities. **Temperature dependence:** for N_D = 10¹⁴ … 10¹⁸ cm⁻³, μ_n falls as T rises from 10² K toward 10³ K; the effect is weaker at heavy doping.

![Variation of electron and hole mobility with doping concentration (10¹⁵–10¹⁹ cm⁻³)](s-05.jpg "Doping dependence of mobility")

### Resistivity and doping

- J = (1/ρ)·ε, ρ = 1 / (q·(μ_n·n + μ_p·p))
- Effect of doping: ρ = 1/(q·μ_n·N_D) for n-type, ρ = 1/(q·μ_p·N_A) for p-type

## Diffusion current density

Diffusion is driven by the concentration gradient:

- J_P|diff = −q·D_p·∇p
- J_N|diff = q·D_n·∇n

### Einstein relationship (summary)

- D_N/μ_n = kT/q for electrons
- D_P/μ_p = kT/q for holes

Units of diffusion constant: cm²/sec.

### Total currents

- J_P = q·μ_p·p·ε − q·D_p·∇p (drift + diffusion)
- J_N = q·μ_n·n·ε + q·D_n·∇n
- J = J_P + J_N

## Band bending

With no external voltage E_c and E_v are flat. With an applied voltage the bands tilt: the voltage increases in the direction opposite ε, since ε = −∇V.

![Tilting of the energy bands when an external voltage is applied](s-11.jpg "Band-bending")

### Energy-voltage relationship

The energy diagram is the flipped graph of voltage:

P.E. = −qV = E_c − E_ref

Therefore the electric field is proportional to the slope of the energy diagram:

ε = −∇V = (1/q)·dE_c/dx = (1/q)·dE_v/dx = (1/q)·dE_i/dx

Questions on the slide: sketch the ε of the material with a given band diagram; what is the direction of drift for each of the charge carriers shown?

## Depletion region formation

- Before equilibrium, carriers near the junction recombine.
- At equilibrium a depletion region forms; outside it are quasi-neutral regions with negligible ε-field.
- Q: Sketch V(x) using ε = −∇V.

![Depletion region and quasi-neutral regions in a P-N junction before equilibrium and at equilibrium](s-14.jpg "Depletion region formation")

### Non-uniform doping

- Electrons diffuse from the high N_D area to the low N_D area …
- The Fermi level equalizes across the material …
- But relative energy levels in each area (far from the junction) remain constant

… which results in band-bending. In equilibrium:

- J_P = q·μ_p·p·ε − q·D_p·∇p = 0
- J_N = q·μ_n·n·ε + q·D_n·∇n = 0

Band bending sets up an electric field stopping further diffusion. (Q: In which direction is the electric field caused by band bending?)

![Equalization of the Fermi level in non-uniform doping: band diagram before and after](s-15.jpg "Non-uniform doping: before and after")

## Built-in potential

The internal potential V_j is the sum of the built-in potential V_bi plus any externally applied potential V_d.

![Band bending of qV_bi in a P-N junction, with the V(x) and ε(x) profiles](s-17.jpg "Built-in potential")

Energy levels are related to charge concentrations by the following equations:

- N_A ≈ p = n_i·e^((E_i − E_F)/kT)
- N_D ≈ n = n_i·e^((E_F − E_i)/kT)

From qV_bi = a + b we get:

V_bi = (kT/q)·ln(N_A·N_D / n_i²)

![Derivation of the built-in potential from the E_F − E_i differences (a and b) in the p and n regions](s-18.jpg "Built-in potential V_bi")

> Q: Suppose N_A = N_D = 10¹⁴/cm³ for Si at 300 K. Compute V_bi. Sketch the energy band diagram of the diode. Compute the spacings between E_F and E_i at both ends of the diode.

## P-N junction under bias

At V_d = 0, drift and diffusion currents of electrons and holes balance each other.

![Band diagram of the P-N junction at V_d = 0; drift and diffusion currents in balance](s-20.jpg "P-N junction at V_d = 0")

**P-N junction electrostatics:** the built-in voltage has opposite polarity to V_d. (1) V_d > 0 (2) lowers V_bi to V_j (3) raises E_c to E_c′ by qV_d.

![Forward voltage lowering the built-in potential to V_j and raising E_c by qV_d](s-21.jpg "P-N junction electrostatics")

![Band diagrams of forward- and reverse-biased P-N junctions: in the forward direction the diffusion currents grow](s-22.jpg "Forward-biased P-N junction")

![Barrier rising and diffusion currents shrinking in a reverse-biased P-N junction](s-23.jpg "Reverse-biased P-N junction")

## Summary of qualitative diode behavior

- Fermi level no longer flat when net currents flow – use quasi-Fermi levels
- When the diode is forward-biased, "ON" current is mainly **diffusion** current: electrons diffuse from N to P region, where they become **minority carriers**; similarly, holes diffuse from P to N …
- Minority carrier diffusion dynamics are important! – leads to the ideal diode equation
