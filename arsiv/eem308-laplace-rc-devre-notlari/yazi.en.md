---
baslik: EEM308 Signals and Systems II: RC Circuit Solutions with the Laplace Transform and s-Domain Circuit Models (Handwritten Notes)
ozet: Handwritten study notes for EEM308, dated June 2014: transfer function and impulse response of an RC circuit, an RC circuit with an initial condition solved by the unilateral Laplace transform, and unilateral s-domain models of the resistor, capacitor, and inductor.
---

This post presents a three-page **handwritten study note** from the final exam period (15 June 2014) of Başkent University's **EEM 308 Signals and Systems II** course. It covers the transfer function and impulse response of an RC circuit for two different outputs, the solution of an RC circuit with an initial condition using the unilateral Laplace transform, and the s-domain models of circuit elements. The pages carry no name or student number. The notes were transcribed to text from photographed pages; the photographs themselves are kept in the archive and are not published.

## Example 1: Transfer function and impulse response of a series RC circuit

A voltage source v_s(t), a resistor R, and a capacitor C are connected in series. Two cases are asked for:

- **a)** For x(t) = v_s(t), y(t) = v_c(t) (capacitor voltage), find h(t).
- **b)** For x(t) = v_s(t), y(t) = i(t) (circuit current), find h(t).

### a) Output is the capacitor voltage

The differential equation of the circuit is:

dy(t)/dt + (1/RC) y(t) = (1/RC) x(t)

Taking the Laplace transform gives sY(s) + (1/RC) Y(s) = (1/RC) X(s), so

H(s) = Y(s)/X(s) = (1/RC) / (s + 1/RC)

**h(t) = ℒ⁻¹{H(s)} = (1/RC) e^(−t/RC) u(t)**

### b) Output is the circuit current

i(t) = C dv_c(t)/dt, and from Kirchhoff's voltage law

−v_s(t) + R i(t) + (1/C) ∫₋∞ᵗ i(τ) dτ = 0

Here x(t) = v_s(t), y(t) = i(t):

y(t) + (1/RC) ∫₋∞ᵗ y(τ) dτ = (1/R) x(t)

Differentiating gives dy(t)/dt + (1/RC) y(t) = (1/R) dx(t)/dt, and with the Laplace transform sY(s) + (1/RC) Y(s) = (1/R) s X(s):

H(s) = (s/R) / (s + 1/RC) = (1/R) · s / (s + 1/RC) = 1/R − (1/(R²C)) · 1/(s + 1/RC)

**h(t) = (1/R) δ(t) − (1/(R²C)) e^(−t/RC) u(t)**

## Example 2: Unilateral Laplace transform, RC circuit with an initial condition

In a series RC circuit where the switch closes at t = 0, v_c(0) = V₀ and v_s(t) = V·u(t). Find: **a)** i(t) = ? **b)** v_c(t) = ?

### a) Current

R i(t) + (1/C) ∫₋∞ᵗ i(τ) dτ = v_s(t)

In the unilateral Laplace transform, the part of the integral before 0⁻ gives the initial condition: ∫₋∞⁰ i(τ) dτ = C v_c(0) = C V₀. Thus

R I(s) + (1/C) [ (1/s) I(s) + (1/s) C V₀ ] = V/s
R I(s) + (1/(sC)) I(s) + V₀/s = V/s
(R + 1/(sC)) I(s) = (V − V₀)/s

I(s) = ((V − V₀)/s) · 1/(R + 1/(sC)) = ((V − V₀)/R) · 1/(s + 1/RC)

**i(t) = ((V − V₀)/R) e^(−t/RC) u(t)**

### b) Capacitor voltage

C dv_c(t)/dt + v_c(t)/R = v_s(t)/R, that is, dv_c(t)/dt + (1/RC) v_c(t) = (1/RC) v_s(t). With the unilateral Laplace transform,

s V_c(s) − v_c(0) + (1/RC) V_c(s) = (1/RC)(V/s)
V_c(s) (s + 1/RC) = (1/RC)(V/s) + V₀

*Note: The note page ends at this line. The rest of the solution: V_c(s) = V/(s(RCs + 1)) + V₀/(s + 1/RC) = V/s − V/(s + 1/RC) + V₀/(s + 1/RC), so v_c(t) = [V + (V₀ − V) e^(−t/RC)] u(t). Check: v_c(0) = V₀, v_c(∞) = V, and C dv_c/dt = ((V − V₀)/R) e^(−t/RC), which is the same as the current in part a.*

## Unilateral s-domain models of circuit elements

| Element | t domain | s domain |
| --- | --- | --- |
| Voltage source | v(t) | V(s) |
| Current source | i(t) | I(s) |
| Resistor | v(t) = R i(t) | V(s) = R I(s) |
| Capacitor | i(t) = C dv(t)/dt | I(s) = sC V(s) − C v(0) |
| | | V(s) = (1/sC) I(s) + (1/s) v(0) |
| Inductor | v(t) = L di(t)/dt | V(s) = sL I(s) − L i(0) |
| | | I(s) = (1/sL) V(s) + (1/s) i(0) |

These relations correspond to two equivalent circuits:

- **Capacitor:** a C·v(0) current source in **parallel** with an impedance of 1/sC (Norton form), or a v(0)/s voltage source in **series** with an impedance of 1/sC (Thevenin form).
- **Inductor:** an L·i(0) voltage source in **series** with an impedance of sL, or an i(0)/s current source in **parallel** with an impedance of sL.

The last line of the note gives the title of the next topic: *Obtaining the frequency response from the pole-zero diagram.*

*Note: In the note, the current source in the parallel model of the inductor reads as v(0)/s; as the relation I(s) = (1/sL)V(s) + (1/s)i(0) in the second row shows, it should be i(0)/s.*
