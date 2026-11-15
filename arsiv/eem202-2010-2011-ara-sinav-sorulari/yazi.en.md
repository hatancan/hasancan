---
baslik: EEM202 Circuit Theory II: 2009-2010 and 2010-2011 Spring Midterm Exam Questions and Study Problems
ozet: Midterm exam questions from the EEM202 Circuit Theory II course dated 17 April 2010 and 15 April 2011 (phasor transform, maximum power transfer, magnetically coupled circuit and ideal transformer, complex power and power factor correction, three-phase circuit) together with three study problems with answers.
---

This post contains handwritten copies of two past midterm exams for the Başkent University Electrical and Electronics Engineering course **EEM 202 Circuit Theory II**, together with a **study problems** page that comes with answers: the **2009-2010 Spring midterm** (17.4.2010, Lecturer Baran Uslu) and the **2010-2011 Spring midterm** (15.4.2011). The sheets were photographed in January 2015; the content was transcribed to text from the photographed pages, and the photographs themselves are not published. The circuit diagrams are described in words. Two pages in the same photo set were copies of the [Quiz 1 solutions](/arsiv/eem202-kisa-sinav-cozumleri/) already in the archive, so they are not repeated. This post has no downloadable file.

## 2010-2011 Spring midterm (15.4.2011)

Duration: 100 minutes. Grading: Question 1: 10, Questions 2–4: 30 points each.

### Question 1

a) With F denoting the phasor transform; F{3 sin(2t + 30°) − 4 cos(2t − 15°)} = ? (in the form a + jb; a = ?, b = ?)

b) F⁻¹{30 − j40} = ?, ω = 100 rad/s

c) What does the figure below illustrate? (In the figure, a resistor R connected to a 100∠0° V (rms) AC source is equated with "≡" to the same resistor R connected to a 100 V DC source; next to it there is a sine wave and lines showing the rms and DC levels.)

*Note (the answers are our own check calculations): a) Since 3 sin(2t + 30°) = 3 cos(2t − 60°), F{…} = 3∠−60° − 4∠−15° ≈ −2.36 − j1.56, i.e. a ≈ −2.36, b ≈ −1.56. b) 30 − j40 = 50∠−53.13° → 50 cos(100t − 53.13°). c) The figure illustrates the definition of the effective (rms) value: an AC voltage of 100 V rms dissipates the same average power in a resistor as a 100 V DC voltage.*

### Question 2

In the given circuit, what must the load impedance Z_L be so that maximum active power is transferred to Z_L?

Circuit: a dependent voltage source of value 4I_x feeds a branch of 8 Ω + j10 Ω through 2 Ω; from this node the current I_x flows through 4 Ω to node a. The load Z_L is between a and b; from node a there is one more branch through 6 Ω and a 10 V source, closing to node b through a −j5 Ω capacitor.

### Question 3

On the primary side there is the source v_g(t), 50 Ω and 5 Ω resistors and a 5 mH inductor; on the secondary side there is a 20 mH inductor, 10 Ω, 150 Ω and a 60 nF capacitor. i₁(t) and i₂(t) are the mesh currents; the two inductors are coupled.

- v_g(t) = 100 cos(50 000t) V
- k (coupling coefficient) = 0.9

Given the above:

- a) Find i₁(t) = ? and i₂(t) = ?
- b) In the same circuit, if the linear transformer is replaced with an ideal transformer with turns ratio a = 2 (dots in the same positions), calculate i₁(t) = ? and i₂(t) = ?

### Question 4

For the circuit alongside (ω = 16 rad/s): a 28∠0° V source, a series 4 Ω, followed by two parallel branches: a −j4 Ω capacitor and j16 Ω + 12 Ω. The current in the inductive branch is given as **I₂ = −j A**.

- a) Calculate the complex powers of all elements,
- b) The power factor (pf) at the source terminals,
- c) What circuit element must be connected in parallel with the source to make the value in b equal to "0.8 lagging current", and calculate it.

*Note: The given I₂ is consistent with the source voltage: node voltage −j(12 + j16) = 16 − j12 V, capacitor current (16 − j12)/(−j4) = 3 + j4 A, source current 3 + j3 A, and source voltage 4(3 + j3) + 16 − j12 = 28 V.*

## 2009-2010 Spring midterm (17.4.2010)

Duration: 110 minutes. Prepared by: Lecturer Baran Uslu ("Good luck…").

**Warnings:**

1. Each student is responsible for their own paper!
1. Use lowercase letters for the time domain and uppercase letters for the phasor domain.
1. Pay attention to units.
1. Redraw the questions!! (The questions carry equal points.)

### Question 1

In the magnetically coupled circuit given below (20∠0° V source, 10 Ω, first coil j5 Ω, second coil j1 Ω, mutual inductance j2 Ω, 2 Ω on the secondary side and terminals c-d):

- a) k (coupling coefficient) = ?
- b) Find the Thevenin equivalent circuit with respect to terminals c-d.

Pencil note on the paper: ωM = 2, ωL₁ = 5, ωL₂ = 1 → k = ωM/√(ωL₁·ωL₂) = **2/√5**.

### Question 2

In the given circuit (an 11 cos(30 000t) mA current source in parallel with three branches: 1 kΩ + 100 mH, 0.01 µF and 1 kΩ):

- a) Obtain the steady-state expression of v(t).
- b) Draw the phasor diagram of the current in each branch and verify KCL.

### Question 3

In the circuit below the load is drawn inside a box (10∠0° V source, series 2 Ω, a dependent current source of V_x/10 A at node V_x, a 2 Ω resistor and a 2 Ω + j3 Ω load inside the box):

- a) Calculate the active, reactive and complex power of the load.
- b) Find the power factor of the load.
- c) Calculate the capacitance that must be connected in parallel with the load to make the value in b equal to 1.

### Question 4

- a) For 3-phase systems, compare the wye and delta connections of the load in terms of line–phase currents and line–phase voltages (magnitude, phase?, make a drawing!).
- b) In the circuit below, I_aA, I_bB and I_cC currents = ? (Sources 100∠0°, 100∠−120° and 100∠120° V rms; delta-connected unbalanced load: Z_AB = j10 Ω, Z_BC = 20 Ω, Z_CA = −j10 Ω.)

## Study problems (with answers)

### 1) Power factor correction

A load connected to a 480∠0° V rms source draws 50 kW at a power factor of 0.82 lagging; f = 60 Hz. Find the capacitor value to be connected in parallel with the load to make the power factor 0.95. Answer on the page: **C = 546.2 µF should be.**

*Note: With these data, Q₁ = 50·tan(arccos 0.82) ≈ 34.90 kVAr, Q₂ = 50·tan(arccos 0.95) ≈ 16.43 kVAr, ΔQ ≈ 18.46 kVAr and C = ΔQ/(ωV²) = 18 460/(377·480²) ≈ **212.6 µF**. The 546.2 µF on the page does not match these data; the original problem data may have been different.*

### 2) Node voltages and Thevenin

The first part consists of a (6 + j13) mA current source, 50 Ω, j25 Ω (current I_o) and a dependent voltage source of value V_o/10; the second part consists of a dependent current source of value 20I_o, 50 Ω and −j25 Ω. V_o = ? Find it using node voltages and the Thevenin method.

Answer: **V_o = −2 + j4 = 4.47∠116.57° V**

### 3) Thevenin method

A 5∠0° V source, 200 Ω (current I_φ), a dependent voltage source of value (1/5)V₂, −j50 Ω, a j40 Ω inductor (V_o), a dependent current source of value 88I_φ and 10 Ω (V₂). Find the voltage V_o using the Thevenin method.

- V_Th = −66 + j88 = 110∠126.87° V, Z_Th = 30 − j40 Ω
- V_o = V_Th·j40/(Z_Th + j40) = (−66 + j88)(j40)/30 = (−3520 − j2640)/30 = −117.33 − j88 V
- **V_o = 146.66∠216.87° V** (= 146.66∠−143.13° V)
