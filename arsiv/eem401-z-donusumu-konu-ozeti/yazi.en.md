---
baslik: EEM401 Digital Signal Processing: What Did the z-Transform Lectures Cover? (Topic Summary)
ozet: A topic summary of the z-transform lectures (I–III) in EEM401 Digital Signal Processing: the definition and its relation to the DTFT, the region of convergence (ROC), properties, the inverse z-transform, and the system function of constant-coefficient difference equations.
---

In the fall semester of 2014–2015, in the **EEM401 Digital Signal Processing** course I took at Başkent University with Asst. Prof. Dr. Selda Güney, the z-transform was covered in three presentations (z Transform I, II and III). Because these presentations are based on the content and figures of the book *Discrete-Time Signal Processing* by Oppenheim, Schafer and Buck, they are **not published**; below is only a summary of the topics in my own words. For details, please see the book: A. V. Oppenheim, R. W. Schafer, J. R. Buck, *Discrete-Time Signal Processing*, 2nd edition, Prentice Hall. There is no download file.

## 1. Definition and its relation to the DTFT

The z-transform is the discrete-time counterpart of the Laplace transform and a generalization of the Fourier transform. For a sequence x[n], it is the sum X(z) = Σ x[n] z⁻ⁿ. z is a complex variable (z = r·e^{jω}); when r = 1, that is, when z is on the unit circle, the z-transform reduces to the **DTFT** (discrete-time Fourier transform). Not every sequence has a DTFT (for example, aⁿu[n] for |a| > 1); because the z-transform can make the sum converge by multiplying the sequence by r⁻ⁿ, it is useful in these cases as well.

## 2. Region of convergence (ROC)

The set of z values for which the sum converges is called the **region of convergence**. Since each value of r corresponds to a circle in the z-plane, the ROC is a ring or a disk made up of circles centered at the origin. The rules emphasized in the lectures:

- The DTFT exists if and only if the ROC includes the unit circle.
- The ROC cannot contain a pole.
- The ROC of a finite-length sequence is the entire z-plane (except possibly z = 0 and z = ∞).
- The ROC of a right-sided sequence extends outward from the outermost pole, and the ROC of a left-sided sequence extends inward from the innermost pole; the ROC of a two-sided sequence is a ring bounded by poles.
- The same z-transform does not uniquely determine the sequence unless the ROC is given. Example: for an H(z) with given poles, if the system is stable the ROC must include the unit circle, and if it is causal the ROC must be right-sided (both conditions are checked together).

Geometric series examples (such as the right-sided exponential sequence aⁿu[n]) and a table of commonly used transform pairs (sequence–transform–ROC) were also covered.

## 3. Properties

The basic properties of the transform were examined with examples: linearity, time shifting (n₀ an integer; the ROC may change), multiplication by an exponential in the z-plane (the ROC is scaled, and the poles and zeros are scaled; if the multiplier is a complex number of unit magnitude, the plane is rotated), and similar ones.

## 4. Inverse z-transform

The formal inverse transform is based on the Cauchy integral; in most cases, more practical methods are sufficient:

- **Inspection method:** recognition from known pairs.
- **Partial fraction expansion:** X(z) is written as a ratio of polynomials; if M ≥ N, a polynomial term appears, and separate terms arise for first-order poles and for multiple-order poles; each term is inverted by inspection. The coefficients are computed at the pole values; if necessary, the polynomial part is found by long division.
- **Power series expansion:** the z-transform is already a power series; especially for finite-length sequences, the coefficients are directly the sequence values.

## 5. System function and the unilateral z-transform

The third presentation was devoted to deriving the system function H(z) for **constant-coefficient difference equations** and examining it on an example system (with parts a, b, c): H(z) from the difference equation, the pole-zero diagram, stability and causality. In the final section, the **unilateral z-transform** and the time-shifting property were introduced; this is used to solve difference equations with initial conditions.

## Related posts

- My notebook notes: [z-transform, inverse z-transform and decimation-in-time FFT](/arsiv/eem401-z-donusumu-ve-hfd-el-yazisi/)
- Earlier topics in the course: [Discrete-time signals and systems](/arsiv/eem401-ayrik-zamanli-isaretler-ve-sistemler/)
- Next topic: [Digital filters](/arsiv/eem401-sayisal-suzgecler/)
- Exams: [Midterm answer key 2014](/arsiv/eem401-ara-sinav-cevap-anahtari-2014/), [Final exam 2015](/arsiv/eem401-final-sinavi-2015/)

*Note: This post is not a copy of the slides; it is a summary of the topic headings and the flow of the course in my own words.*
