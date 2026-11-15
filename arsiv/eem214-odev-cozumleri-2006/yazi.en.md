---
baslik: EEM214 Electronics I: 2006 Homework Solutions, Excess Carrier Diffusion, and a Semiconductor Bar Illuminated by Light
ozet: The handwritten portions of the EEM214 Electronics I homework solutions from spring 2006: the diffusion equation for excess holes under continuous injection and its solution δp(x) = Δp·e^(−x/L_p); the decay of excess carriers after the light is switched off, the dark resistance, and the time-dependent resistance R(t).
---

This post presents only the handwritten portions of the Homework I and Homework II solution files (password-protected PDFs) from the spring 2006 term of the Başkent University **EEM214 Electronics I** course. The rest of the solution files and the Homework 3 solutions were not published, because they consist of pages taken from the textbook's (Jaeger, *Microelectronic Circuit Design*) solutions manual. The handwritten pages appear to have been prepared by the course's teaching assistant. These three pages can be downloaded as a PDF at the end of the post. The quiz and midterm solutions from the same term are in separate posts in the archive.

## Homework I – Problem 6: Excess holes under continuous injection

**Given:** δp(0) = Δp, the excess hole density at the injection point; δp(W) = 0, the excess hole density at x = W; τ_p, the hole recombination lifetime; W >> L_p. Find: δp(x).

**Solution:** The continuity equation is

∂p(x,t)/∂t = −(1/q)·∂J_p/∂x − δp/τ_p

The hole diffusion current is J_p = −q·D_p·∂p/∂x; since p = p₀ + δp(x), we have ∂p/∂x = ∂δp(x)/∂x and J_p = −q·D_p·∂δp(x)/∂x. Thus

∂p(x,t)/∂t = D_p·∂²δp/∂x² − δp/τ_p

In steady state the left-hand side is zero:

∂²δp/∂x² = δp/(D_p·τ_p) = δp/L_p², L_p = √(D_p·τ_p)

The solution has the form δp(x) = C₁·e^(x/L_p) + C₂·e^(−x/L_p). Boundary conditions: at x = 0, δp(0) = Δp = C₁ + C₂; at x = W, δp(W) = 0 = C₁·e^(W/L_p) + C₂·e^(−W/L_p). Since W >> L_p, e^(−W/L_p) → 0 and C₁·e^(W/L_p) = 0 is required, so C₁ = 0 and C₂ = Δp:

**δp(x) = Δp·e^(−x/L_p)**

The excess hole density decays exponentially away from the injection point; at x = L_p it falls to Δp·0.3679. Here L_p is the **mean diffusion length** of the holes.

## Homework II – Problem 5: Semiconductor bar illuminated by light

**a)** Since the bar is illuminated uniformly, ∂J_p/∂x = 0: there is no diffusion current; since the electric field is zero, there is no drift current either. The continuity equation is

∂δp(t)/∂t = −δp(t)/τ_p ⇒ δp(t) = δp(0)·e^(−t/τ_p)

and with δp(0) = Δp, **δp(t) = Δp·e^(−t/τ_p)** (cm⁻³).

**b)** The conductivity is σ = q(n·µ_n + p·µ_p). At t = 5τ_p, δp(t) drops to nearly zero and is negligible; in that case σ = q(n₀µ_n + p₀µ_p), ρ = 1/σ. Since n₀ ≅ N_D and p₀ = n_i²/N_D, the dark resistance is

R_dark = ρL/(w·d) = L / [q·w·d·(N_D·µ_n + (n_i²/N_D)·µ_p)]

**c)** The time-dependent resistance is R(t) = ρL/(w·d) = L / [q(n·µ_n + p·µ_p)·w·d]; here n = n₀ + δn, p = p₀ + δp, and taking Δp = Δn and τ_p = τ_n gives n = N_D + Δp·e^(−t/τ_p), p = n_i²/N_D + Δp·e^(−t/τ_p), and

**R(t) = L / {q·w·d·[(N_D + Δp·e^(−t/τ_p))·µ_n + (n_i²/N_D + Δp·e^(−t/τ_p))·µ_p]}**

## Download

The PDF file contains two handwritten solution pages from Homework I and one from Homework II (the parts taken from the textbook solutions manual have been removed).
