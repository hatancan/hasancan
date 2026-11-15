---
baslik: EEM401 Digital Signal Processing: Course Introduction and Classification of Discrete-Time Signals and Systems
ozet: The first two lectures of Asst. Prof. Dr. Selda Güney's EEM401 Digital Signal Processing course: course content and references, signal types (analog, digital, periodic, energy and power), and classification of discrete-time systems (linearity, time invariance, causality, BIBO stability).
---

This post summarizes the first two lectures (Lecture 1 and Lecture 2) of the **EEM401 Digital Signal Processing** course I took from **Asst. Prof. Dr. Selda Güney** at Başkent University in the 2014–2015 fall semester. In the course slides the name appears as "EEM 401 Sayısal Sinyal İşleme" (in the PDF properties it is "Sayısal İşaret İşleme"); the folder name "Elektromanyetik Dalgalar" (Electromagnetic Waves) is incorrect. The original presentations can be downloaded as a ZIP at the end of the post.

## Course introduction

**References:**

1. A. V. Oppenheim and R. W. Schafer, *Discrete-Time Signal Processing*, Prentice Hall, 3rd edition, 2009
2. S. K. Mitra, *Digital Signal Processing: A Computer Based Approach*, McGraw-Hill, 4th edition, 2011
3. J. G. Proakis and D. G. Manolakis, *Digital Signal Processing: Principles, Algorithms and Applications*, Pearson/Prentice Hall, 4th edition, 2010

**Content:** discrete-time signals and systems (basic sequences, sampling, fundamental operations); discrete-time systems and their classification; the discrete-time Fourier transform; the discrete-time Fourier series; sampling in the frequency domain; the fast Fourier transform; the system transfer function in the frequency domain; the z-transform and its applications; digital filter design techniques; FIR and IIR filter design methods.

**Digital signal processing** is based on representing a signal as a sequence of numbers on digital computers or special-purpose digital hardware, and extracting the desired information from that sequence by performing various operations on it. Its goals include amplifying signals, filtering, pattern detection, preparing the signal for the communication channel, preventing interference from other signals, and compensating for sensor deficiencies.

- **Advantages:** noise control after sampling, high accuracy, complex algorithms, flexibility (parameter changes), and insensitivity to effects such as electromagnetic interference, environmental conditions, and aging.
- **Disadvantages:** discrete-time artifacts, higher power requirements, digital clock and switching interference.

Block diagram of the system: analog input → A/D converter → digital input signal → digital signal processor → digital output → D/A converter → analog output.

## 1. Discrete-time signals and their classification

### Signal types and definitions

A **signal** is the mathematically formulated form of the relationship between the independent variables present in a physical phenomenon (for example, the variation over time of the voltage across a circuit element, sound intensity, or temperature).

Classifications: continuous (analog) – discrete; periodic – aperiodic; energy – power; random – deterministic signals.

- **Analog signal**: continuous in both time and amplitude (ECG, EMG, EEG, radar, and speech signals). **Digital signal**: a signal that can take discrete amplitude values at discrete times.
- **Periodic signal**: f(t) = f(t + T). For a discrete periodic signal, f[n] = f[n + N], where N is a positive integer. ECG and speech are examples of aperiodic signals.
- **Energy signal**: if Σ |f[n]|² (or ∫ |f(t)|² dt) is finite. **Power signal**: if P = lim (1/(2M+1)) Σ |f[n]|² is finite and greater than zero.
- **Random signals**: present and future values cannot be calculated or predicted from the past. **Deterministic signals**: values can be calculated from past values and expressed with an exact mathematical formula.

The table of contents also includes the basic discrete signals, simple mathematical operations on signals, and analog-to-digital/digital-to-analog conversion.

## 2. Discrete-time systems and their classification

A discrete-time system is a combination of software or hardware that transforms an input sequence into an output sequence. Classification:

- **Deterministic and stochastic** systems: a system is deterministic if its input and output are deterministic, and stochastic if they are random.
- **Static (memoryless) and dynamic** systems: a system is memoryless if the output at time n depends only on the input at the same instant. Examples: y[n] = a·x[n] and y[n] = n·x[n] + b·x³[n] are static and memoryless (there is no need to store past inputs or outputs). Otherwise the system is dynamic (it has memory).
- **Time-variant and time-invariant** systems: if x[n] → y[n] and the input x[n − k] produces the output y[n − k], the system is time-invariant. The test is carried out with two experiments: (1) x[n] → y[n]; (2) x[n − k] → y_k[n]; then check whether y_k[n] = y[n − k].
- **Linear and nonlinear** systems: a system that satisfies the principles of additivity (T{x1 + x2} = y1 + y2) and scaling (T{a·x1 + b·x2} = a·y1 + b·y2) is linear. y = x² and y = cos x are not linear.
- **Causal and noncausal** systems: a system is causal if the output at time n depends only on present and past inputs (x[n], x[n − 2]) and not on future inputs (x[n + 1], x[n + 2]). In real-time applications, since we cannot know the actual value of the signal in advance, a noncausal system cannot be realized.
- **Stable and unstable** systems: stability is an important property in practical applications; unstable systems usually exhibit erratic, extreme behavior. A relaxed system is **BIBO (bounded input – bounded output)** stable if every bounded input produces a bounded output: if |x[n]| ≤ Mx < ∞, then |y[n]| ≤ My < ∞. If y[n] is unbounded for some bounded x[n], the system is unstable.
- **Feedback and feedforward (non-feedback)** systems.

Applications of testing stability, causality, and linearity from the exams appear in later posts (quiz 1, midterm).
