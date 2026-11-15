---
baslik: MAT340 Probability and Statistics: Quiz Questions and Solutions, 2007–2010
ozet: Başkent University MAT340 Probability course quiz keys (2007-2010): conditional probability, combinations, continuous and joint distributions, binomial and normal distribution applications, expected value, variance, and random variable transformations; with solutions.
---

Quiz papers and **answer keys** from 2007–2010 for the **MAT 340 Probability** course in the Electrical-Electronics Engineering Department at Başkent University. The course instructors were Lecturer Pelin Toktaş and (in 2010) Prof. Dr. Fulya Altıparmak (two sections). The questions and solutions were transcribed from handwritten scanned keys, and the calculations were checked. The original scans are in the ZIP file at the end of the post (the 2010 Quiz 2 and Quiz 3 solutions came as photo/scan files, so they are outside the ZIP; they were only transcribed).

## Quiz 1 – October 19, 2007: Nuclear Power Plant (Conditional Probability)

A nuclear power plant consists of 3 systems, A, B, and C. The plant is shut down if systems A and B fail, or if systems A and C fail. Systems A, B, and C fail independently with probabilities 0.01, 0.03, and 0.02, respectively. (a) What is the probability that the plant is operating? (b) Given that system A has failed, what is the probability that the plant is operating? (c) Given that the plant has been reported as not operating, what is the probability that system B is working?

**Solution.** The probabilities of the eight cases (multiply by 0.99, 0.97, 0.98 if A, B, C are working, respectively): ✓✓✓ 0.941094; ✓✓✗ 0.019206; ✓✗✓ 0.029106; ✓✗✗ 0.000594; ✗✓✓ 0.009506; ✗✓✗ 0.000194; ✗✗✓ 0.000294; ✗✗✗ 0.000006. The plant operates in the first five cases.

- (a) P(plant operating) = 0.941094 + 0.019206 + 0.029106 + 0.000594 + 0.009506 = **0.999506**
- (b) P(operating | A failed) = 0.009506 / 0.01 = **0.9506**
- (c) P(B working | plant not operating) = 0.000194 / (1 − 0.999506) = 0.000194 / 0.000494 = **0.3927**

## Quiz 2 – October 30, 2008: Continuous Distribution

f(x) = x/4 (0 < x ≤ 2), 3 − x (2 < x ≤ 3), 0 (otherwise). (a) P(1 < X ≤ 5/2)? (b) Find the cumulative distribution function and compute P(X > 2.1). (c) E(X)? (d) P(X = 2)?

- (a) ∫₁² x/4 dx + ∫₂^2.5 (3 − x) dx = 3/8 + 3/8 = **0.75**
- (b) F(x) = 0 (x ≤ 0); x²/8 (0 < x ≤ 2); −7/2 + 3x − x²/2 (2 < x ≤ 3); 1 (x > 3). P(X > 2.1) = 1 − F(2.1) = **0.405**
- (d) P(X = 2) = **0** (for a continuous random variable, the probability at a single point is zero).
- (c) The calculation in the key gave E(X) = 3/2; however, ∫₀² x·(x/4) dx = x³/12 |₀² = 2/3 (the key wrote "1/3").

*Note: The correct value is E(X) = 2/3 + ∫₂³ (3x − x²) dx = 2/3 + 7/6 = **11/6**; the value 3/2 in the key is incorrect.*

## Quiz 1 – October 12, 2010: Combinations and Relay Chain

1. In a class of 10 male and 5 female students: (a) In how many ways can a 6-person committee be chosen? **C(15,6) = 5005**. (b) If every committee must include at least one female student? 5005 − C(10,6)·C(5,0) = 5005 − 210 = **4795**. (c) If a particular male student and a particular female student do not want to be on the same committee? 5005 − C(13,4)·C(2,2) = 5005 − 715 = **4290**.
2. A transmitter sends a message in binary code; each datum passes through 3 relays before reaching the receiver, and each relay makes an error with probability 0.20 (relays are independent). (a) The probability that "1" comes out of all three relays when "1" is sent from the transmitter: 0.8³ = **0.512**. (b) The probability that "1" is received at the receiver (tree diagram): there must be an even number of errors: 0.8·0.8·0.8 + 3 · 0.2 · 0.2 · 0.8 = 0.512 + 0.096 = **0.608**.

## Quiz 3 – November 9, 2010: Expected Value and Variance

1. If E(X) = 19, E(Y) = 25, Var(X) = 25, Var(Y) = 144, ρ_XY = −1/2, then: Cov(X,Y) = −30. (a) Var(X − Y) = 25 + 144 − 2(−30) = **229**. (b) E(XY) = −30 + 19·25 = 445, E(−2XY + 3) = **−887**. (c) Z = −X − 5Y: E(Z) = **−144**, Var(Z) = 25 + 25·144 + 10·(−30) = **3325**.
2. X takes the values −3, 6, 9 with probabilities 1/6, 1/2, 1/3; g(X) = −3X − 1. E(X) = 5.5; E(X²) = 46.5; Var(X) = 16.25. E[g(X)] = **−17.5**, Var[g(X)] = 9 · 16.25 = **146.25**.

## Quiz 2 (October 26, 2010 section) – Cumulative Distribution and Joint Distribution

1. For the same density as in the 2008 quiz: (a) P(1 < X ≤ 5/2) = 0.75, (b) F(x) and P(X > 2.1) = 0.405, (c) P(X = 2) = 0.
2. f(x, y) = c(x + y), 0 < x < y < 1. (a) ∫∫ = c/2 = 1 → **c = 2**. (b) Marginal h(y) = ∫₀^y 2(x + y) dx = 3y²; f(x|y) = 2(x + y)/(3y²). P(X > 0.6 | Y = 0.8) = (1/0.96) ∫₀.₆^0.₈ (x + 0.8) dx = 0.30/0.96 ≈ **0.3125**.

## Quiz 4 – November 23, 2010: Binomial Distribution (Repetition Code)

In a communication system, 00000 is sent in place of 0 and 11111 in place of 1; because of noise, each bit is transmitted incorrectly with probability 0.2, independently; the receiver decodes by majority (e.g., 01001 → 0). (a) What is the probability that an important message is received in error? X ~ Binom(5; 0.2), P(X ≥ 3) = 1 − P(X ≤ 2) = 1 − 0.94208 = **0.05792**. (b) What is the probability that 2 of 4 independently sent messages are received in error? p ≈ 0.06, Y ~ Binom(4; 0.06): C(4,2)(0.06)²(0.94)² ≈ **0.0191**.

(The paper also includes the probability function, mean, and variance formulas for the discrete uniform, Bernoulli, binomial, hypergeometric, negative binomial, and geometric distributions.)

## Quiz 5 – December 14, 2010: Normal Distribution

X ~ N(110, 10²) is the voltage passing through a computer's power supply. The computer fails with probability 0.01 below 100 V; 0.001 between 100–120 V; and 0.05 above 120 V. P(V₁) = P(X < 100) = 0.1587; P(V₂) = P(100 < X < 120) = 0.6826; P(V₃) = P(X > 120) = 0.1587.

- (a) P(failure) = 0.1587·0.01 + 0.6826·0.001 + 0.1587·0.05 ≈ **0.0102**
- (b) P(V₃ | failed) = (0.1587·0.05)/0.0102 ≈ **0.778**
- (c) Upper bound for the lowest 15% slice of the voltage: z = −1.04 → x* = 110 − 10.4 = **99.6 V**

## Quiz 6 – 2010: Random Variable Transformation

1. f(x) = 2x e^(−x²), 0 < x < ∞; if Y = X²: x = √y, |J| = 1/(2√y); g(y) = 2√y e^(−y) · 1/(2√y) = **e^(−y), 0 < y < ∞** (exponential distribution).
2. f(x₁, x₂) = x₁x₂/36, x₁, x₂ = 1, 2, 3; Y₁ = X₁X₂, Y₂ = X₂. (a) Joint distribution g(y₁, y₂) = y₁/36 (y₁ = 1, 2, 3, 4, 6, 9; y₂ = 1, 2, 3; y₁ = x₁y₂):

| g(y₁, y₂) | y₁ = 1 | 2 | 3 | 4 | 6 | 9 |
|---|---|---|---|---|---|---|
| y₂ = 1 | 1/36 | 2/36 | 3/36 | 0 | 0 | 0 |
| y₂ = 2 | 0 | 2/36 | 0 | 4/36 | 6/36 | 0 |
| y₂ = 3 | 0 | 0 | 3/36 | 0 | 6/36 | 9/36 |

(b) Marginal distribution of Y₁: f(1) = 1/36, f(2) = 4/36, f(3) = 6/36, f(4) = 4/36, f(6) = 12/36, f(9) = 9/36.
