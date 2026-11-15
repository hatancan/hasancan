---
baslik: EEM301 Signals and Systems I: Course Content Form, Homework, Exercise List and MATLAB Projects
ozet: The 2010–2011 and 2012–2013 course content forms for EEM301 Signals and Systems I (weekly topics, textbook, grading), Prof. Dr. Alper Uraz's HW-1 and HW-2 homework assignments (linearity, time invariance, impulse response, convolution, Fourier series and transform), the Oppenheim & Willsky exercise list, and the Buck–Daniel–Singer MATLAB projects.
---

This post collects the administrative documents for the **EEM301 Signals and Systems I** course in the Electrical-Electronics Engineering Department at Başkent University: the **course content forms** for two different semesters (Fall 2012–2013, Prof. Dr. Alper Uraz; Fall 2010–2011, section EEM 301-02, Assoc. Prof. Dr. İsmail Avcıbaş), the **HW-1 / HW-2 homework assignments** prepared by Prof. Dr. Alper Uraz, the **exercise list** from the Oppenheim & Willsky textbook, and the **MATLAB project** lists. The documents are Word files from 2006–2012; their contents are transcribed below as text. The original files can be downloaded as a ZIP at the end of the post.

## Course content form (Fall 2012–2013)

| | |
|---|---|
| Course code / name | EEM 301 Signals and Systems I |
| Instructor | Prof. Dr. Alper Uraz |
| Class hours | Tuesday 15.00–16.50, Friday 13.00–14.50 |
| Office hours | Monday 10.00–10.50, Wednesday 15.00–15.50 (Office: D410) |
| Textbook | Oppenheim, A. V., Willsky, A. S., *Signals and Systems*, Prentice-Hall, 2/e, 1997 |
| Supplementary books | Buck–Daniel–Singer, *Signals and Systems using MATLAB*, Prentice Hall, 2/e, 2002; Sinha, N. K., *Linear Systems*, Wiley, 1991 |

**Grading:**

| Attendance | Quiz | Homework | MATLAB project | Midterm | Final exam | Total |
|---|---|---|---|---|---|---|
| 3 | 14 | 4 | 4 | 35 | 40 | 100% |

**Weekly topics:**

| Week | Topics |
|---|---|
| 1 | Classification of systems, differential equation models, p-operator, complementary function, particular integral |
| 2 | Difference equation models, q-operator, complementary solution, particular solution, stability |
| 3 | Classification of signals, periodic signals, complex exponential signals |
| 4 | Some common signals, power and energy signals; impulse response of DT LTI systems |
| 5 | Convolution sum for DT LTI systems, properties of convolution sum |
| 6 | Impulse response of LTI system, convolution integral for CT LTI systems, properties of convolution integral |
| 7 | Eigenfunctions, eigenvalues, Fourier series for CT periodic signals (CTFS) |
| 8/9 | Midterm |
| 8/9 | CTFS properties, periodic convolution, symmetry of signals |
| 10 | Fourier series for DT periodic signals (DTFS), DTFS and LTI systems, frequency selective filters |
| 11 | CT Fourier transform (CTFT), FT properties |
| 12 | Frequency responses of LTI systems, duality |
| 13 | DT Fourier transform (DTFT), properties, DT LTI systems |
| 14 | Magnitude and phase of FT, review |

Form dated 01.10.2012.

### Fall 2010–2011, section EEM 301-02

The same form adapted for Assoc. Prof. Dr. İsmail Avcıbaş's section (24.09.2010). Class hours are Monday 13.00–14.50 and Thursday 11.00–12.50, and office hours are Thursday 09.00–10.50 (Office: D404). The weekly topics are the same as above (midterm in week 8); the only supplementary book is Buck–Daniel–Singer. Grading: attendance 3, quiz 12, homework 5, project 5, midterm 35, final exam 40.

## EEM301 Homework (HW-1 and HW-2)

Homework by Prof. Dr. Alper Uraz. Each student works with different coefficients according to their position (i) in the class list.

### HW-1

**1.** Consider the following systems with x as input and y as output:

- S1: d²y(t)/dt² + a dy(t)/dt + b y(t) = c dx(t)/dt + d x(t)
- S2: y(n) + e y(n−1) + f y(n−2) = g x(n) + h x(n−1)

| i | a | b | c | d | i | e | f | g | h |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 2 | 1 | 1 | 26 | ny | 1 | 2 | 1 |
| 2 | 1 | t | 1 | 1 | 27 | 3 | 2 | 1 | 1 |
| 3 | 1 | 1 | 1 | t | 28 | 1 | n | 1 | 1 |
| 4 | y | 1 | 0 | 1 | 29 | 1 | 1 | 1 | n |
| 5 | 1 | 1 | 1 | x | 30 | y | 1 | 0 | 1 |
| 6 | y | 1 | 0 | t | 31 | 1 | 1 | 1 | x |
| 7 | 2 | 1 | 0 | 2 | 32 | y | 1 | 0 | n |
| 8 | 2 | 1 | 2t | 3 | 33 | 2 | 1 | 0 | 2 |
| 9 | 2 | 2y | 0 | 1 | 34 | 2 | 1 | 2n | 3 |
| 10 | 3y | 1 | 1 | 1 | 35 | 2 | 2y | 0 | 1 |
| 11 | 0 | t | 2 | 1 | 36 | 3y | 1 | 1 | 1 |
| 12 | 0 | ty | 0 | 1 | 37 | 0 | n | 2 | 1 |
| 13 | 3 | 2 | x | 1 | 38 | 0 | ny | 0 | 1 |
| 14 | 3 | 2 | t | 0 | 39 | 3 | 2 | x | 1 |
| 15 | 0 | 0 | 0 | tx | 40 | 3 | 2 | n | 0 |
| 16 | y | 0 | 1 | t | 41 | 2 | 2 | 0 | x |
| 17 | 2 | 0 | 0 | 2 | 42 | 0 | y | 1 | n |
| 18 | 0 | 1 | 2t | 3 | 43 | 1 | n | 0 | 2 |
| 19 | 2 | 2y | 1 | 1 | 44 | 2 | 2 | 2n | 4 |
| 20 | 3y | t | 1 | 1 | 45 | 2 | ny | 0 | 1 |
| 21 | 0 | t | 2 | 0 | 46 | 3y | 1 | 1 | 0 |
| 22 | 0 | ty | 0 | 1 | 47 | 1 | n | 2 | 1 |
| 23 | 1 | 1 | y | 1 | 48 | 2 | ny | 2 | 1 |
| 24 | t | 2 | 1 | 0 | 49 | 3 | 3 | x | 2 |
| 25 | 1 | 0 | 0 | tx | 50 | 3 | n | 2 | 0 |

Mathematically determine whether S1 or S2 is a linear/nonlinear and time-invariant/time-varying system for the given coefficients. Note that the index i corresponds to the student's place in the register.

**2.** Consider S1 and S2 with the following coefficients:

| i | a | b | c | d | i | e | f | g | h |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 2 | 1 | 1 | 26 | -0.4 | 0.04 | 1 | 1 |
| 2 | 2 | 1 | 2 | 1 | 27 | -0.5 | 0.06 | 2 | 1 |
| 3 | 2 | 2 | 1 | 2 | 28 | -1 | 0.25 | 1 | 2 |
| 4 | 5 | 6 | 3 | 2 | 29 | -0.7 | 0.12 | 1 | 0 |
| 5 | 4 | 4 | 1 | 3 | 30 | -0.9 | 0.2 | 2 | 1 |
| 6 | 4 | 13 | 1 | 1 | 31 | -1.2 | 0.36 | 2 | 3 |
| 7 | 7 | 12 | 2 | 1 | 32 | -1.1 | 0.3 | 1 | 2 |
| 8 | 6 | 9 | 1 | 2 | 33 | -1.3 | 0.42 | 3 | 2 |
| 9 | 2 | 5 | 2 | 3 | 34 | -1.4 | 0.49 | 1 | 1 |
| 10 | 9 | 20 | 1 | 2 | 35 | -1.5 | 0.56 | 2 | 1 |
| 11 | 8 | 16 | 3 | 2 | 36 | -1.7 | 0.72 | 1 | 2 |
| 12 | 6 | 25 | 1 | 1 | 37 | -1.5 | 1.0 | 1 | 0 |
| 13 | 11 | 30 | 3 | 2 | 38 | -1.6 | 1.0 | 1 | 1 |
| 14 | 10 | 25 | 1 | 2 | 39 | -1.7 | 1.0 | 2 | 1 |
| 15 | 8 | 41 | 1 | 1 | 40 | -1.8 | 1.0 | 1 | 2 |
| 16 | 4 | 3 | 0 | 3 | 41 | -0.2 | 0.01 | 2 | 1 |
| 17 | 12 | 36 | 2 | 1 | 42 | -0.6 | 0.08 | 2 | 3 |
| 18 | 4 | 8 | 1 | 1 | 43 | -0.7 | 0.1 | 1 | 2 |
| 19 | 5 | 4 | 0 | 2 | 44 | -0.6 | 0.09 | 3 | 2 |
| 20 | 14 | 49 | 2 | 2 | 45 | -0.8 | 0.12 | 1 | 1 |
| 21 | 6 | 13 | 2 | 3 | 46 | -0.9 | 0.14 | 2 | 1 |
| 22 | 6 | 5 | 3 | 2 | 47 | -0.8 | 0.16 | 1 | 2 |
| 23 | 8 | 25 | 0 | 4 | 48 | -1 | 0.16 | 1 | 0 |
| 24 | 16 | 64 | 2 | 1 | 49 | -1.1 | 0.18 | 1 | 1 |
| 25 | 7 | 6 | 4 | 2 | 50 | -0.8 | 0.15 | 2 | 1 |

1. Find the impulse response h(t) or h(n) of the causal LTI system S1 or S2 with the corresponding coefficients given above.
1. Obtain the output y(t) or y(n) for the following causal input utilizing either the convolution integral or the convolution sum: x(t) = e^(−8t) u(t) or x(n) = (0.1)ⁿ u(n).
1. Verify your findings in (b) by utilizing either the p-operator or the q-operator wherever it is applicable.

*Note that HW-1: Problems 1 and 2 are due on Friday of the 8th week.*

### HW-2

**3.** Consider S1 with {c = 0 and d = 1} or S2 with {g = 1 and h = 0} LTI system and the corresponding {a, b} or {e, f} coefficients given in Pr. 2 above. Find the Fourier series (FS) representation of the output y(t) or y(n) for the following input: x(t) = cos 2πt or x(n) = sin(3πn/4).

*Note that for Problem 3, the student's new index is taken as 26 ≤ (i + 25) ≤ 50 or 1 ≤ (i − 25) ≤ 25.*

**4.** Consider S1 with {c = 0 and d = 1} or S2 with {g = 1 and h = 0} LTI system and the corresponding {a, b} or {e, f} coefficients given in Pr. 2 above.

1. Determine the frequency response H(jω) of S1 or H(e^(jω)) of S2 utilizing the Fourier (or DTFT) transform.
1. Obtain the output response y(t) or y(n) for the following input using FT or DTFT: x(t) = t e^(−2t) u(t) or x(n) = (−1/2)ⁿ u(n).

**5.** Consider S1 with {c = 0 and d = 1} or S2 with {g = 1 and h = 0} LTI system and the corresponding {a, b} or {e, f} coefficients given in Pr. 2 above. Obtain the output response y(t) or y(n) for the following input using FT or DTFT: x(t) = 5e^(−3t) u(t) or x(n) = δ(n) + (1/2) δ(n−1).

*Note that for Problem 5, the student's new index is taken as 26 ≤ (i + 25) ≤ 50 or 1 ≤ (i − 25) ≤ 25.*

*Note that HW-2: Problems 3, 4 and 5 are due on Friday of the 14th week.*

## Exercise list (Oppenheim & Willsky)

In the Fall 2006 document "EEM301 – HW + Exercises," the homework assignments are given as follows:

- **HW-1:** Problems 2.11, 2.21, 2.55f, 2.56f (due 17.11.2006)
- **HW-2:** Problems 3.33, 3.36, 4.31, 4.32, 4.33 (due 22.12.2006)

Problems recommended for solving (the 2007 "EEM301 – Exercises" list is the same):

- **Chapter 1:** 1.1, 1.2, 1.3a, b, c, f, 1.4, 1.5a, 1.6a, b, 1.7, 1.8, 1.9b, c, 1.10, 1.11, 1.19a, 1.20, 1.21, 1.22, 1.23a, 1.24a, 1.25a, b, c, 1.26, 1.27, 1.28, 1.48, 1.49, 1.51, 1.54, 1.55, 1.56
- **Chapter 2:** 2.1, 2.2, 2.3, 2.4, 2.7, 2.8, 2.9, 2.10a, 2.13, 2.14, 2.18, 2.22a, c, 2.24, 2.25b, 2.26, 2.29, 2.30, 2.32, 2.33, 2.38, 2.39, 2.42, 2.53, 2.54, 2.55, 2.56
- **Chapter 3:** 3.2, 3.4, 3.7, 3.9, 3.10, 3.12, 3.13, 3.14, 3.16a, b, 3.20, 3.21, 3.22a(a, b), 3.24, 3.27, 3.28, 3.30, 3.31, 3.37, 3.38
- **Chapter 4:** 4.1, 4.3b, 4.4, 4.5, 4.8, 4.9, 4.10b, 4.11, 4.13, 4.14, 4.19, 4.20, 4.21, 4.22, 4.25, 4.26, 4.30, 4.34, 4.36
- **Chapter 5:** 5.1, 5.2, 5.3, 5.4, 5.6, 5.7, 5.10, 5.13, 5.14, 5.19, 5.20, 5.21, 5.22, 5.28, 5.29, 5.33, 5.34, 5.36a, b(iii)

Notes: the p / q operators may be used where needed; in the O&W textbook, answers to the first 20 problems of each chapter are given at the end of the book.

## MATLAB projects (Buck–Daniel–Singer)

Source: Buck–Daniel–Singer, *Signals and Systems using MATLAB*, Prentice Hall, 2nd Ed., 2002.

| Pages | Problems |
|---|---|
| 8–10 | 1.3 Basic (a), (b), (c) |
| 20–22 | 2.1 Tutorial (a), (b), (c), (d) |
| 22–23 | 2.2 Tutorial (a), (b), (c), (d) |
| 36 | 2.7 Basic (a) |
| 51–52 | 3.2 Tutorial (a), (b), (c) |
| 69–70 | 3.13 Basic (a), (b), (c) |
| 74–75 | 4.2 Basic (a), (b), (c) |

- **MatPro-1:** Problems 1.3, 2.1, 2.2, 2.7 — due 17.11.2006 in Fall 2006 (the Friday of the 8th week in later semesters)
- **MatPro-2:** Problems 3.2, 3.13, 4.2 — due 22.12.2006 in Fall 2006 (the Friday of the 13th week in later semesters)

The same list was also used in 2008 for Assoc. Prof. Dr. İsmail Avcıbaş's EEM 301-02 section (under the title "EEM301-01-MATLAB-PROJECTS").
