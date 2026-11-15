---
baslik: EEM323 Electromagnetics II: Summary of Phasors and Electromagnetic Theory II (Prof. S. Gökhun Tanyer)
ozet: Text content of Prof. Dr. S. Gökhun Tanyer's EEM323 lecture notes on the definition, rationale and conveniences of the phasor representation, and a summary of time-varying fields, including a homework question.
---

The text content of two sets of notes that Prof. Dr. S. Gökhun Tanyer presented in the course **EEM 323 Electromagnetics II** (Fall 2013–2014, November 2013): the phasor representation and a short summary of Electromagnetic Theory II (time-varying fields). The figures and equation images are not reproduced.

## Phasors: definition, rationale and conveniences

**Definition:** The "sine family" consists of all sinusoidal functions with different frequencies and phases.

**Rationale (as presented by the instructor):** If we can write all physical varying signals as a sum of sinusoids, as Fourier showed, and can find a solution for the sine family, then we have found the solution for all other possible functions as well. The signal under study may be a voltage, current, electric field, magnetic field, etc.

The signal has the form A cos(ωt + θ), where ω = 2πf is the frequency in radians, f is the frequency in hertz, and θ is the phase in radians. Using Euler's identities, the signal is rewritten in complex exponential form. Since the factor exp(jωt) is present in all signals, it **can be set aside and left unwritten**; one must only remember that this factor is present in all operations to be carried out (differentiation, addition, subtraction, multiplication, division). The signal is thus written simply in **phasor representation** as A∠θ, and the operations are simplified.

**Operations:**

- **Differentiation:** Differentiating the phasor only means introducing the factor jω ("how easy, isn't it?").
- **Multiplication and division:** The phasor is written in terms of its magnitude and phase. The magnitude of the product of two phasors is the product of the magnitudes, and its phase is the sum of the phases (for division, the magnitudes are divided and the phases are subtracted).
- **Addition and subtraction:** The slides work these out in the real (time-domain) representation and in the phasor domain side by side (with equation images).

**Homework (the instructor's question):** Let two signals be given in phasor representation (of the form A∠θ).

1. Compute the sum of the phasors both in the real representation domain (without suppressing the exp(jωt) factor) and in the phasor representation domain.
2. Compute the difference of the phasors in both domains.
3. Review the "Phasors" article on Wikipedia, watch the video presented there, and explain your results with graphs drawn by hand.

## Summary of Electromagnetic Theory II (Part 1: time-varying fields)

The 19-slide summary covers the following topics in order:

- **Static case:** If the electric and magnetic fields are constant (do not vary with time), they are independent of each other. This independence disappears for time-varying fields. Michael Faraday and **Faraday's law of electromagnetic induction**; transformers.
- **James Clerk Maxwell** (1865, "A Dynamical Theory of the Electromagnetic Field") and **Maxwell's equations**.
- Potential functions, electromagnetic boundary conditions, wave equations and their solutions, source-free wave equations, time-harmonic fields and the use of phasors; scalar potential and vector potential; **Helmholtz equations** (homogeneous vector equations); the electromagnetic spectrum.
- The **Doppler effect**, transverse electromagnetic (TEM) waves, polarization of plane waves (linear, circular, elliptical); plane waves in lossy media, low-loss dielectrics, good conductors.
- **Group velocity**, electromagnetic power flow, the Poynting vector, instantaneous and average power density.
- **Normal incidence** on a conducting plane boundary, standing waves; **oblique incidence** on a conducting boundary (perpendicular and parallel polarization); normal incidence on a dielectric boundary, **reflection and transmission coefficients** and their relationship; standing wave ratio; normal and oblique incidence at multiple dielectric interfaces; **total reflection (critical angle)** and polarizing sunglasses.

## Source note

This post is a summarized and written-up version of **the instructor's own text content** (headings, explanations, questions, homework) from the lecture presentations that Prof. Dr. S. Gökhun Tanyer prepared for the Başkent University EEM 323 Electromagnetics II course (Fall 2013–2014) (OGR-EEM323-DN-1G-Fazorler, 1D-EMT2-Ozet). According to the presentations themselves, the figures, tables and equation images in them were taken from D. K. Cheng's textbooks (*Fundamentals of Engineering Electromagnetics*, *Field and Wave Electromagnetics*); therefore they are **not reproduced here**, and the original presentation file has not been made available for download. For the figures and detailed derivations, Cheng's book should be consulted.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution. It will be removed at the request of the rights holder.*
