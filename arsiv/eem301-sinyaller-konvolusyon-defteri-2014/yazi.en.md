---
baslik: EEM301 Signals and Systems I: Signals, System Properties and Convolution Notebook (2014)
ozet: Signal transformations, impulse and step functions, energy and power, system properties, and convolution examples from 22 photographed notebook pages.
---

The **22 photographed pages** of a friend's EEM301 course notebook were transcribed to text. One of the pages bears the date 8 October 2014; the photo series is named 14 October 2014. Personal information was not transcribed. Because the photos are kept in a private archive, this post contains no photos or downloadable files. The short appendix at the end covers the legible part of a separate blurry solution photo.

## Complex numbers and signal representation

For z=x+jy, the real part is x, the imaginary part is y, and the magnitude is |z|=√(x²+y²). Since j²=−1, j³=−j, j⁴=1, the powers of j form a cycle of four. In polar form, z=r(cosθ+j sinθ)=re^(jθ) is written.

A continuous-time x(t) is defined for every real t, and a discrete-time x[n] for integer n. The graph of a sequence is shown with vertical lines drawn at the sample points. Discretization in time and quantization of amplitude are not the same operation.

## Shifting, reversal, and scaling

x(t−t₀) is a right shift, x(t+t₀) is a left shift, and x(−t) is time reversal. In discrete time, x[n−n₀], x[n+n₀], and x[−n] perform the same operations on the sample indices. In the notebook, the new breakpoints are marked on piecewise graphs.

For x(at), |a|>1 is time compression and 0<|a|<1 is time expansion. For a<0, there is additionally a reversal. In operations with several steps, the original breakpoints are carried over by setting them equal to the new argument.

Even and odd components:

- xₑ(t)=[x(t)+x(−t)]/2.
- xₒ(t)=[x(t)−x(−t)]/2.
- x=xₑ+xₒ; the even component is symmetric about the vertical axis, and the odd component is symmetric about the origin.

## Periodicity

In continuous time the condition x(t+T)=x(t) is sought, and in discrete time x[n+N]=x[n]. For discrete time, N must be a positive integer.

- For cos(ω₀t), the fundamental period is 2π/|ω₀|.
- e^(jω₀n) is periodic only if ω₀/(2π) is rational.
- For cos(πn/5), N=10 is the fundamental period; 20 is also a period.
- For cos(2t), the fundamental period is π.

The notebook also contains a short probabilistic remark about countable and uncountable sets: the probability of picking an integer from the real line is written as "0".

*Note: A uniform probability distribution cannot be defined over the entire real line. The probability of a countable set being zero holds, for example, when a continuous distribution is chosen over an interval; probability is not computed simply by dividing the cardinalities of sets.*

## Exponential and sinusoidal signals

Euler's relation e^(jωt)=cosωt+j sinωt connects the exponential representation to sine and cosine. For e^(at), the real part of a produces growth/decay, and the imaginary part produces oscillation. In discrete time, the sequence aⁿ decays to the right for |a|<1; a negative a causes sign alternation.

## Unit step and impulse

u[n] is 1 for n≥0 and 0 otherwise. δ[n] is 1 only at n=0. Hence δ[n]=u[n]−u[n−1]. In continuous time, the unit-area property of the impulse and the fact that it is the derivative of u(t) are used.

*Note: In the impulse drawing on one of the pages, the value at zero is marked as 1. This value is valid for the discrete-time δ[n]; the continuous-time δ(t) is not an ordinary function with finite height.*

Expansion of an example sequence in terms of impulses:

x[n]=δ[n+1]+0.5δ[n]+2δ[n−1]+3δ[n−2].

In general, x[n]=Σx[k]δ[n−k]. This representation is the starting point for constructing an LTI system output from impulse responses.

## Energy and power

Continuous-time energy is E=∫|x(t)|²dt, and discrete-time energy is E=Σ|x[n]|². Average power is the limit of the energy per unit time or per number of samples as the symmetric interval is enlarged.

For the complex exponential e^(jωt), |x|²=1, the average power is 1, and the total energy is infinite. A signal with finite, nonzero energy has zero average power.

In the notebook, the example x(t)=e^(−2t)u(t) is classified as an energy signal and E=1/2 is written.

*Note: The signal was not squared in this result. For the given x(t), E=∫₀∞e^(−4t)dt=1/4. The energy-signal classification and the result P=0 do not change.*

## System properties

The output of a memoryless system depends only on the input at the same instant. Delayed samples, future samples, derivatives, and integrals require memory. Causality, on the other hand, is the condition of not depending on future input values; a system with memory can be causal.

For linearity, additivity and scaling must hold together. The system y=2x+3 is not linear because zero input does not give zero output. y[n]=x[n]+x[n+1] is not causal because it depends on a future sample.

Time invariance requires that when the input is shifted, the output shifts by the same amount. The notebook compares the paths of shifting first and then applying the system versus applying the system first and then shifting. In BIBO stability, a bounded input is required to produce a bounded output.

In the moving-average examples, one checks whether the window used extends into the future; a symmetric window in general also uses future samples.

## Discrete-time convolution

For an LTI system, y[n]=Σx[k]h[n−k]. In the graphical computation, h[k] is reversed and shifted by n; the overlapping samples are multiplied and summed.

For x=[1,1,1] and h=[3,2,1], with both sequences starting at n=0:

| n | Overlapping products | y[n] |
|---|---|---|
| 0 | 1·3 | 3 |
| 1 | 1·2+1·3 | 5 |
| 2 | 1·1+1·2+1·3 | 6 |
| 3 | 1·1+1·2 | 3 |
| 4 | 1·1 | 1 |

The result is [3,5,6,3,1]. The convolution length of finite sequences is Nₓ+Nₕ−1; the starting indices are added.

## Convolution with geometric sums

For x[n]=2ⁿu[−n] and h[n]=u[n], the support conditions of the product are k≤0 and k≤n. Therefore the upper limit of the sum is min(n,0):

- n<0: y[n]=Σₖ₌₋∞ⁿ2ᵏ=2^(n+1).
- n≥0: y[n]=Σₖ₌₋∞⁰2ᵏ=2.

Geometric series formula: Σₖ₌₀ᴺaᵏ=(1−a^(N+1))/(1−a), a≠1; for the infinite series, the condition |a|<1 is additionally used.

## Continuous-time convolution example

The signals given on the last page:

x(t)=e^(−3t)[u(t)−u(t−2)], h(t)=e^(−t)u(t).

x(t) is active only in the interval 0≤t<2. The convolution is written as y(t)=∫x(τ)h(t−τ)dτ; the regions t<0, 0<t<2, and t>2 are drawn. In the integral lines on the page, the limits 0–2 and 2–∞ are used.

*Note: The active interval of the product is 0≤τ≤min(t,2). Therefore the correct piecewise results are 0 for t<0; e^(−t)(1−e^(−2t))/2 for 0≤t<2; and e^(−t)(1−e^(−4))/2 for t≥2. The 2–∞ integral in the source is not consistent with the finite-support x(t).*

## Additional material legible from the blurry solution photo

In the separate photo, the partial-fraction decomposition of rational expressions is being worked on. Denominators of the type (s+1)² and s+2 and terms of the form A/(s+1)² and B/(s+1) can be made out. There are intermediate lines in which the denominators are equated and the coefficients are compared.

*Note: The initial expression and all of the coefficients in this photo cannot be read reliably. No numerical solution was guessed; only the discernible method and terms were transcribed.*
