---
baslik: EEM322 Control Systems: Supplementary Notebook Notes: Modeling, Laplace, and Discrete-Time State Equations
ozet: Modeling and Laplace notes transcribed from photographs; an outline of the state-space solution, the discrete-time response, and a summary of reachability.
---

The supplementary topics left over from the EEM322 archive's notebook, solution sheet, and whiteboard records were **transcribed to text from photographed pages**. The names of the students who prepared the notes were not given; the documents do not share a common class date. The archive record date of 9 April 2015 was used. This post is text only; the photographs were not made available for download.

## System and modeling

A system is represented by an input–system–output relationship. When systems are combined, a block diagram results. In the notebook, the input and output voltage are drawn for a potentiometer, and **y = dx/dt** is drawn as an example for a differentiator.

Systems are classified as linear/nonlinear, dynamic/static, time-varying/time-invariant, and continuous-time/discrete-time. When building a model, parameters and variables are separated; Kirchhoff's laws are used for electrical systems and physical force equations for mechanical systems.

For the RL circuit, V_L + V_R = E is written, that is, **L di/dt + Ri = E**. For the RLC example:

L di/dt + Ri + (1/C)∫i dt = E

For constant E, differentiating gives **L d²i/dt² + R di/dt + i/C = 0**. The suspension model at the bottom of the page was started with only mass and damping terms and is incomplete.

## Complex variable and Laplace transform

The notebook writes s = σ + jω, j = √(−1), and F(s) = F_x + jF_y. The purpose of the Laplace transform is to convert differential equations into algebraic relations; the inverse Laplace transform is used to return to the time response.

With input R(s), transfer function G(s), and output C(s), **C(s) = R(s)G(s)**. The general transfer function is shown as the ratio of numerator and denominator polynomials.

## Outline of the state-space solution of a circuit

In the solution sheet, the states x₁ and x₂, the input u, and the parameters r, c, ℓ are used. The original circuit drawing of the source is not on this page; the following are only the equations written in the solution:

- i_c = cẋ₁
- v_ℓ = ℓẋ₂
- u = rcẋ₁ + x₁ = ℓẋ₂ + rx₂
- y = x₂ + cẋ₁

Accordingly:

A = [−1/(rc) 0; 0 −r/ℓ], B = [1/(rc); 1/ℓ], C = [−1/r 1]

The source uses the notation y = Cx + Du. Following the definition "minimal system = both observable and controllable," the observability matrix O = [C; CA] and the controllability matrix E = [B AB] are constructed.

*Note: On the sheet, the matrix ranks are written as "2 ≤ n" and then the conclusion "the system is not minimal" is reached. For a two-state system, if both ranks are 2, the system is minimal. For the written A, B, and C, provided r, c, ℓ are nonzero, both matrices have full rank when ℓ ≠ r²c; the special case ℓ = r²c must be examined separately.*

The transfer function step is started in the source with **H(s) = C(sI − A)⁻¹B**. Because A is diagonal, the diagonal elements of the resolvent are 1/[s + 1/(rc)] and 1/(s + r/ℓ).

*Note: From the y = x₂ + cẋ₁ equation on the same page, y = −x₁/r + x₂ + u/r follows. Therefore the direct feedthrough is D = 1/r; for a single output it must be a scalar. The source's transfer function calculation omits this +D term. The simplifications at the bottom of the page should not be used as a verified result.*

## Solution of the state equation in discrete time

x(k + 1) = Ax(k) + Bu(k), y(k) = Cx(k) + Du(k).

Successive substitution:

- x(1) = Ax(0) + Bu(0)
- x(2) = A²x(0) + ABu(0) + Bu(1)
- x(3) = A³x(0) + A²Bu(0) + ABu(1) + Bu(2)

General result:

**x(k) = Aᵏx(0) + Σ_(j=0)^(k−1) A^(k−1−j)Bu(j)**

Aᵏ is the discrete-time state transition matrix. Taking D = 0:

**y(k) = CAᵏx(0) + Σ_(j=0)^(k−1) CA^(k−1−j)Bu(j)**

The first term is the zero-input response, and the summation term is the zero-state response.

## Solution in the z-domain

With the one-sided z-transform:

zX(z) − zx(0) = AX(z) + BU(z)

X(z) = z(zI − A)⁻¹x(0) + (zI − A)⁻¹BU(z)

For D = 0:

Y(z) = Cz(zI − A)⁻¹x(0) + C(zI − A)⁻¹BU(z)

**Φ(k) = Aᵏ = Z⁻¹{z(zI − A)⁻¹}**.

## Whiteboard summary: reachability and time reversal

On the whiteboard, under the heading "DT C/O," the concepts of reachability, controllability, observability, and constructibility are shown together with the dual relationships among them. The reachability of a system is related to the observability of the dual system. The existence of A⁻¹ is stated as a separate condition for reconstructing the state backward in time.

For the input-free system x(k + 1) = Ax(k), when A is invertible:

**x(k) = A⁻¹x(k + 1), x(−1) = A⁻¹x(0)**.

On the whiteboard, a batch relation of the form "y − Tu = O(C,A)x(0)" is also written for recovering x(0) from observation data. Since the full matrix definitions are not given in the photograph, no additional numerical example was created.
