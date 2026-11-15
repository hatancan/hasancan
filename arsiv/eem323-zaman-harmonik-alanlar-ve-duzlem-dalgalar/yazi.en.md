---
baslik: EEM323 Electromagnetics II: Time-Harmonic Fields, the Helmholtz Equation, and Plane Wave Propagation (Prof. S. Gökhun Tanyer)
ozet: A text summary of Prof. Dr. S. Gökhun Tanyer's EEM323 notes on time-harmonic fields and the Helmholtz wave equation, plane wave propagation, phase velocity, the eikonal equation, and Fermat's principle, including homework assignments.
---

This is the text content of three sets of notes that Prof. Dr. S. Gökhun Tanyer covered in the course **EEM 323 Electromagnetics II** (Fall 2013–2014, November 2013): time-harmonic fields and wave equations, and the two parts of plane wave propagation. Figures and most equation images have not been reproduced.

## 1. Time-harmonic fields and wave equations

The field is assumed to contain only **a single frequency component** (other frequencies are treated in a similar way). Fields are written in phasor notation: E(x, y, z; t) = Re{E(x, y, z) e^{jωt}}, and the same for H; all other vector fields are likewise vector phasors. The instructor's emphases on phasors:

- Phasors are functions of position only, not of frequency; they are valid only for a single value of f.
- Instantaneous time functions cannot contain complex numbers (the electric field must be a real value in V/m).
- Any electromagnetic expression containing j is necessarily a relation between phasors.

When phasors are substituted into Maxwell's equations, time derivatives simply become a factor of jω: ∇ × E = −jωμH and ∇ × H = jωεE (linear, isotropic medium). Because this "chain generation of fields" is sinusoidal, it **can continue forever if there is no energy loss**; this is where the name electromagnetic wave comes from (the instructor's source: his own work *The Nature of Music – The Sound of Mathematics*).

**Lossless assumption:** in general, an electromagnetic wave can induce currents in the material it propagates through, and power can be dissipated; the wave can also spread out and weaken as it propagates. Both reduce the amplitude. If the material is assumed lossless, power dissipation is neglected.

**Helmholtz wave equation** (lossless, simple, i.e. linear and isotropic medium): from the curl equations for E, ∇ × (∇ × E) = ω²με E is obtained; using the identity ∇ × ∇ × E = ∇(∇·E) − ∇²E = −∇²E,

> ∇²E + k²E = 0, k = ω√(με) = 2π/λ (rad/m)

is obtained. n = k/k₀ is the **refractive index**; u = 1/√(με) is the speed of light in the medium, and in vacuum 1/√(μ₀ε₀) = 300,000 km/s.

**Homework (the instructor's questions):**

1. Derive the Helmholtz wave equation for the magnetic field intensity H in a linear, isotropic, source-free region.
2. For both the E and H wave equations, examine the limiting case λ → ∞; solve Maxwell's equations in this limit, recompute the Helmholtz equation, and comment on the results.

The notes also touch on scalar wave (Helmholtz) equations and give a "preview" of the next plane wave lecture.

## 2. Plane wave propagation – 1

**Plane wave propagating in the +z direction.** In Cartesian coordinates the scalar Helmholtz equation has the form ∂²/∂x² + ∂²/∂y² + ∂²/∂z² + k² = 0. If the field has a component only in the x direction and ∂/∂x = ∂/∂y = 0, the equation reduces to d²E_x/dz² + k²E_x = 0. The solution is an x-polarized plane wave propagating in the z direction: taking only the wave traveling in the +z direction, E_x(z, t) = E₀ cos(ωt − kz).

**Wave propagating in an arbitrary direction.** The same analysis also holds for a plane wave traveling in an arbitrary direction specified by the unit direction vector R = aₓα + a_yβ + a_zγ; α, β, γ are the **direction cosines**, and α² + β² + γ² = 1.

**Uniform phase fronts.** If the wave is not uniform, the wavefront is not planar. A wavefront is the surface on which the phase equals a value s (phase = ks, in radians; if s is a multiple of λ, the phase is the same multiple of 2π). The function S(r) defines the wavefront; an outward-propagating wave is written as cos(ωt − kS(r)).

**Phase velocity.** As the wave propagates, t becomes t + Δt and r becomes r + Δr. For an observer "moving with the wave" at a constant phase on it, ωt − kS(r) = ω(t + Δt) − kS(r + Δr) must hold, that is, ωΔt = k[S(r + Δr) − S(r)]. The change in phase is the directional derivative of S along the unit direction vector: ΔS = ∇S · n̂ Δs. From this the phase velocity u_p = Δs/Δt = ω/(k|∇S|) is obtained: the phase velocity is greatest in the direction of ∇S. The instructor's note: in physics, velocity is a vector and speed is a scalar; however, "phase velocity" is a scalar quantity.

**Ray approximation and the eikonal equation.** When the local plane wave structure is substituted into the Helmholtz equation, |∇S| turns out to equal the refractive index; since its direction is n̂,

> ∇S(r) = n n̂ (eikonal equation)

This says that surfaces of equal phase form the wavefronts, that wavefronts are perpendicular to the propagation direction, and that the approximation is accurate at large wavenumbers (short wavelengths, i.e. high frequencies). If n depends on position (if the permittivity ε is a function of position), the rays bend. The approximation is most accurate for lasers; the idea that wave propagation behaves locally like small plane waves goes back to Christiaan Huygens.

**Fermat's principle.** The time the wave takes to travel the path between points a and b is given by T = (1/c)∫ n ds (c is the speed of light in vacuum, ds is an infinitesimal displacement along the ray, v = ds/dt, and n = c/v). The **optical path length** ∫ n ds is a purely geometric quantity; it is related to the travel time by T = (optical path)/c. The historical statement by Pierre de Fermat (1601–1665) is incomplete; the full modern statement is: "the optical length of the path light follows between two fixed points is an extremum; the optical length is the physical length multiplied by the refractive index of the material."

## 3. Plane wave propagation – 2

This 9-slide set works through an **example**: for a wave whose electric field is x-polarized and propagating in the +z direction, the vector wave equation is solved and the results are interpreted (the solution steps are given as equation images). The following topics are the Doppler effect and the polarization of electromagnetic waves.

## Source note

This post is a summarized and written-out version of **the instructor's own text content** (headings, explanations, questions, homework) from the lecture presentations that Prof. Dr. S. Gökhun Tanyer prepared for Başkent University's EEM 323 Electromagnetics II course (Fall 2013–2014) (OGR-EEM323-DN-2D-TimeHarmonicFields, 2E-PlaneWaves-1, 2F-PlaneWaves-2). The figures, tables, and equation images in the presentations were, according to the presentations themselves, taken from D. K. Cheng's textbooks (*Fundamentals of Engineering Electromagnetics*, *Field and Wave Electromagnetics*); for that reason they are **not reproduced here**, and the original presentation file is not offered for download. For the figures and detailed derivations, refer to Cheng's books.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution. It will be removed at the request of the rights holder.*
