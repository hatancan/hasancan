---
baslik: EEM224 Electromagnetics I: Fall 2004 Midterm Exam and Solutions (Formerly EEM323)
ozet: Text transcript of questions, key solution steps, and results from an old Electromagnetics exam.
---

This post was prepared from the Fall 2004 Electromagnetics exam and solution pages; it was transcribed to text from photographed pages. The source gives the old course code as EEM323; in the archive it is classified under EEM224. Personal information was not transferred. The photographs are kept in a private archive; there is no download file in this post.


## Question 1: Maxwell's Equations and Continuity

Write the four Maxwell equations and the continuity equation in differential form in the time domain; explain their physical meaning in one sentence each. Derive their integral forms and give their counterparts in the phasor domain.

- ∇×E = −∂B/∂t: a time-varying magnetic field produces circulation of the electric field.
- ∇×H = J + ∂D/∂t: conduction and displacement currents produce circulation of the magnetic field.
- ∇·D = ρ: electric charge is the source of electric flux.
- ∇·B = 0: the net magnetic flux through a closed surface is zero.
- ∇·J = −∂ρ/∂t: conservation of charge.

The first two equations are converted to integral form with Stokes' theorem, and the others with the divergence theorem. For phasor fields, assuming e^(jωt) time dependence, ∂/∂t is replaced by jω. In a linear medium, B=μH and D=εE are used.

## Question 2: Rotating Circular Loop

A loop of radius 3 mm rotates with ω₁=4π×10⁶ rad/s. At t=0 it is parallel to the x-y plane. The magnetic field is in the +z direction, B=2 sin(4π×10⁶t) Wb/m². The induced voltage is required, given the terminal polarity shown.

Φ=BS cos(ω₁t)=9π×10⁻⁶ sin(2ω₁t).

−dΦ/dt=−72π² cos(2ω₁t). The source takes the terminal polarity opposite to the integration direction, giving V_ind=72π² cos(2ω₁t) V.

## Question 3: Obliquely Incident Plane Wave

A wave incident from the material on the z<0 side, with ε_r=2, μ_r=1, onto air has the electric field:

E_inc=(2â_x−3â_y−2√3â_z) cos[ωt−15π(√6x+√2z)] V/m.

The angle of incidence, wave constant, angular frequency, wavelength, and the reflected and transmitted fields are required. In the solution:

θ_i=60°, k=30π√2, ω=9π×10⁹ rad/s, λ=√2/30≈0.0471 m.

The field is decomposed into components perpendicular and parallel to the plane of incidence. The phasor reflection coefficients are computed separately; the total field is the vector sum of the components. In the transmitted solution, exponential attenuation appears in the direction normal to the boundary.

*Note: Because some signs in the long handwritten lines of the last two field expressions could not be read with certainty, they were not re-derived and completed as if they were the source solution.*

## Question 4: Transmission Line

For four lossless line sections, the input impedance is found using the given characteristic impedances, loads, and lengths of λ/2 or λ/4. In the solution, a half-wave line repeats the load; a quarter-wave line performs the transformation Z_in=Z₀²/Z_L.

The half-wave transformation of the first branch gives 25 Ω. The quarter-wave transformation of the second branch is 35²/49=25 Ω. Their parallel combination is 12.5 Ω, and the input impedance of the third branch is 15²/12.5=18 Ω. The fourth quarter-wave branch, terminated in a short circuit, appears as an open circuit at the input; the total Z_in=18 Ω. If the termination of the fourth branch is changed to an open circuit, it appears as a short circuit at the input and the total Z_in=0.
