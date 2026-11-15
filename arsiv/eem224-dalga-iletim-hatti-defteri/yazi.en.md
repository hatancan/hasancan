---
baslik: EEM224 Electromagnetics I: Wave Propagation and Transmission Line Notebook
ozet: A text transcription of the archived question and solution pages, prepared with personal information removed.
---

This archive record, transcribed to text from photographed pages, contains the question texts along with the legible solution steps. The photographs are kept in a private archive; there is no downloadable file.

A friend's course notes, transcribed from notebook photographs; personal information has been removed. The file names show 1 January 2015. The same pages in the opened notebook folder were not published separately. Because the photo order of the pages differs from the topic order, the topics are grouped together below.

## Wave, Phase Velocity, and Skin Depth
General lossy wave: Ẽ(z)=E₀exp(−αz)exp(−jβz). Propagation constant γ=α+jβ; phase velocity vp=ω/β. The distance over which the amplitude drops to e⁻¹ of its value is δ=1/α; this is called the skin depth. The distinction between a good conductor and a perfect conductor is noted: with finite conductivity, the field penetrates into the material while being attenuated.

Sum of two waves of nearby frequencies:

E=2E₀cos(Δωt−Δβz)cos(ω₀t−β₀z).

The phase velocity of the carrier is ω₀/β₀; the group velocity of the envelope is Δω/Δβ, which in the limit is dω/dβ. In a dispersive medium these two velocities can differ.

## Instantaneous and Average Power
P(t)=E(t)×H(t), in units of W/m². The power flowing out through a closed surface is found by ∮P·dS. In the sinusoidal regime, the average is P=½Re{Ẽ×H̃*}. The notes relate the 1/2 factor to converting the two peak values to their RMS values. Seawater with εr=80, μr=1, σ=4 S/m is given as an example medium; the questions ask for the phase velocity, impedance, phase constant, skin depth, the distance at which the field drops to one tenth, and the power.

## Normal Incidence and Standing Wave
Incident Ẽᵢ=âxEᵢ₀exp(−jβ₁z), reflected Ẽᵣ=âxEᵣ₀exp(jβ₁z), transmitted Ẽₜ=âxEₜ₀exp(−jβ₂z). In the magnetic fields there is a change of direction due to backward propagation. At the boundary, by equating the tangential E and H, Γ=Eᵣ₀/Eᵢ₀=(η₂−η₁)/(η₂+η₁) and τ=1+Γ are obtained.

In a perfect conductor the internal field is zero, Γ=−1 and Eᵣ₀=−Eᵢ₀. The total is Ẽ=−2jâxEᵢ₀sinβz; the electric and magnetic field nodes are shifted by λ/4. The distance between two adjacent minima of the same type is λ/2. With partial reflection, the maximum and minimum amplitudes are 1+|Γ| and 1−|Γ| times the incident amplitude; the standing wave ratio is S=(1+|Γ|)/(1−|Γ|).

*Note: In the notebook, next to a line about converting the −j factor to the time domain, there is a warning "not correct, finding this is homework". That line has not been transcribed as if it were a verified result.*

## Oblique Incidence and Snell's Law
The propagation vector and the electric field are perpendicular to each other; H=(1/η)ân×E. The incident and reflected angles are equal. From phase matching along the boundary, β₁sinθᵢ=β₂sinθₜ. For non-magnetic media, sinθᵢ/sinθₜ=√(ε₂/ε₁). The critical angle is sinθc=√(ε₂/ε₁), applied only for transition from a denser medium to a less dense medium. In parallel polarization, the angle at which the reflection is zero is referred to as the Brewster angle.

## Multiple Boundaries
In the three-layer drawings, the first transmission, the return from the second boundary, and the re-transmission are written out separately. Each contribution is multiplied by the relevant τ and Γ coefficients and the exp(−jβl) phase of the path traveled; the total field is the sum of these contributions. A homework assignment to examine the multiple reflections of two or three boundaries with MATLAB is noted in the notebook.

## Transmission Line Model
The two-conductor line is modeled, for a small segment Δz, with series elements RΔz and LΔz and shunt elements GΔz and CΔz. Voltage and current are the sum of forward and backward waves. For a lossless line, V(z)=V⁺exp(−jβz)+V⁻exp(jβz). At an open end the current is zero and the voltage is maximum; at a short circuit the voltage is zero. The source and load boundary conditions determine these two unknown wave amplitudes.

At the load, ΓL=(ZL−Z₀)/(ZL+Z₀). When ZL=Z₀ there is no reflection. Input impedance of a lossless line:

Zin=Z₀[ZL+jZ₀tan(βl)]/[Z₀+jZLtan(βl)].

## Quarter-Wave Transformer
For l=λ/4, βl=π/2; the input impedance is Zin=Z₀²/ZL. An open end and a short circuit transform into each other at this length. S=1 indicates a matched line, S→∞ indicates total reflection. In the pulse example, the delay of the input and output signals along a 10 km line is plotted; since no specific wave velocity is given, no numerical delay was added.
