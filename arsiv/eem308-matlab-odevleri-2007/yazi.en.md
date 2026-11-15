---
baslik: EEM308 Signals and Systems II: EEM302 MATLAB Assignment (2007) and Student Solutions, Pole-Zero Diagrams
ozet: The 2007 MATLAB assignment for EEM302 (today's EEM308) Signals and Systems II: problems from Buck's Computer Explorations book on pole-zero diagrams, the frequency response of a second-order system, the |H(s)| surface, and pole vectors; classmates' .m solutions, with notes.
---

This post brings together the **MATLAB assignment** given by **Asst. Prof. Dr. Mustafa Doğan** in the spring 2007 semester in the **EEM 302 Signals and Systems II** course at Başkent University (the course was later offered under the code EEM 308), along with the MATLAB solutions prepared by classmates for this assignment. The assignment consists of problems selected from the Laplace and z-transform chapters of the book *Computer Explorations in Signals and Systems Using MATLAB* (Buck, Daniel, Singer; 2nd edition). Two short solutions prepared in 2011 under the same assignment system were also added.

The solutions are the work of classmates; names and student numbers in file names and code have been removed, and the files were renamed according to problem number. The assignment distribution list (since it contained student names and numbers) and the photographs of the book pages were not published; the problem assignment is given below anonymously. The cleaned `.m` files can be downloaded as a ZIP at the end of the post.

## Assignment Rules and Problem Distribution

The title of the assignment list: *EEM 302 MATLAB HW — "Computer Explorations in Signals and Systems 2nd ed. – BUCK" — Asst. Prof. Dr. Mustafa Doğan*. The assignments were to be submitted **by 24:00 on Sunday, March 25** to the upload address on the department's web server. The class was divided into eight groups, and each group was given two problems from the book:

| Group | From the Laplace chapter | From the z-transform chapter |
| --- | --- | --- |
| 1 | Page 163 (a) | Page 178 (k) |
| 2 | Page 163 (b) | Page 178 (j) |
| 3 | Page 166 (a) | Page 178 (i) |
| 4 | Page 166 (b) | Page 177 (e) |
| 5 | Page 166 (c) | Page 177 (d) |
| 6 | Page 166 (d) | Page 177 (c) |
| 7 | Page 169 (a) | Page 177 (b) |
| 8 | Page 169 (b) | Page 177 (a) |

Points to note for the assignments:

1. The single file to be submitted must be named in the form `studentNo.m`, as in the example. Everything required in the assignment (all parts) must be inside this m-file, and the file must run.
1. The explanations and answers to the questions will count for much more in the evaluation. The explanations to be evaluated must be printed to the Command Window with `display`, as in the example `display('verbal answers and explanations...');`.
1. Outputs that are not meant to be evaluated must not appear in the Command Window (if `;` is not used, the output appears in the Command Window).

## Page 166 (a) and 178 (i): Pole-Zero Diagrams

**166 (a).** Define the numerator and denominator coefficients of the system function H₁(s) = 4 / (s² + 2s + 17), Re(s) > −1 as the vectors `b1` and `a1`, find the poles with `roots`, and plot them.

**178 (i).** Find and plot the poles and zeros of the system H₃(z) = (0.25 − (√3/2)z⁻¹ + z⁻²) / (1 − (√3/2)z⁻¹ + 0.25z⁻²), |z| > 0.5; explain how the pole and zero locations are related.

There are two solutions for this group. Both follow the same approach; one version of the second also draws the axes, the ROC boundary, and the unit circle, following the logic of the book's `plotpz`:

```matlab
b1=[4];
a1=[1 2 17];
zeros=roots(b1);
poles=roots(a1);

disp('Soru : 166 (a) için');
disp('Kutuplar:');
disp(poles);

figure (1);
plot(real(zeros),imag(zeros),'o');
hold on
plot(real(poles),imag(poles),'x');
grid
title('Soru : 166 (a)');
xlabel('Re');
ylabel('Im');
axis([-5 5 -5 5]);

b=[0.25 -(sqrt(3)/2) 1];
a=[1 -(sqrt(3)/2) 0.25];
zs=roots(b);
ps=roots(a);
disp('Soru : 178 (i) için');
disp('Sıfırlar:'); disp(zs);
disp('Kutuplar:'); disp(ps);
```

Results: in 166 (a) the poles are at **s = −1 ± j4** (there is no finite zero since the numerator is constant). In 178 (i) the poles are at **z = 0.5·e^(±jπ/6)** (= 0.433 ± j0.25) and the zeros at **z = 2·e^(±jπ/6)** (= 1.732 ± j1).

*Note: The solutions only say "2 poles and 2 zeros were found"; the relationship the question actually asks for is this: the zeros are the reflections of the poles with respect to the unit circle (1/p*), and the numerator coefficients are those of the denominator in reverse order. Therefore the system is an all-pass filter, with |H₃(e^jω)| = 1 constant (at z = 1 the numerator and denominator are both 0.384). Also, the `rsmak('circle')` line in the code depends on MATLAB's Spline Toolbox; without this toolbox it gives an error.*

### The |H₁(s)| Surface

Another file prepared for the same problem plots |H₁(s)| as a surface in the s-plane: 32 samples of σ from just to the right of −1 up to 3 (σ = −1 + k/8, k = 1…32), and ω in the range [−10, 10] with a step of 0.5; the grid s = σ + jω is built with `meshgrid`, H₁ = `polyval(b1,s)./polyval(a1,s)` is computed and plotted with `mesh`, and the cross-section of the surface along the jω axis is marked with a blue line (`plot3`). The conclusion in the explanation: the surface grows rapidly as it approaches the poles; how the poles affect the frequency response can be seen in the 3-D plot.

## Page 163 (b): Damping Ratio in a Second-Order System

The problem asks for examining the poles and frequency response for different values of the damping ratio ζ, taking ωₙ = 1 in the second-order system H(s) = ωₙ² / (s² + 2ζωₙs + ωₙ²). Both solutions use the `ord2`, `printsys`, and `freqs` commands to plot |H(jω)| over ω ∈ [−5, 5] for ζ = 0, 1/4, 1, and 2:

```matlab
wn=1
omega=[-5:0.1:5]
damping_ratio=1/4
[num0,den]=ord2(wn,damping_ratio);
num=wn^2*num0
printsys(num,den)
freqs(num,den,omega)
display('0<damping_ratio<1 olduğunda polinomun kutupları kompleks sayı olur dolayısıyla step response ve impulse responsları salınıma sahip olur...');
```

Summary of the explanations in the solutions:

- **ζ = 0:** The poles are on the imaginary axis (s = ±jωₙ).
- **0 < ζ < 1:** The poles are complex conjugates; the step and impulse responses are oscillatory. As ζ decreases, the poles approach the jω axis and |H(jω)| (according to the solutions) peaks at the frequency ω = ωₙ√(1 − ζ²); the system behaves like a non-ideal band-pass filter.
- **ζ = 1:** The poles are on the real axis (double pole); |H(jω)| decreases monotonically as ω increases.
- **ζ > 1:** At low ω values, |H(jω)| becomes more sensitive to changes in ω.
- It is stated that at ω = 0, |H(j0)| = 1 for all four systems, because the function reduces to a constant at this point.

*Note: A few corrections are needed in the solutions. At ζ = 0 the peak does not "fail to form"; on the contrary, |H| goes to infinity at ω = ωₙ = 1 (since the ω grid includes exactly 1, `freqs` produces Inf at this point and it does not appear in the plot). The location of the resonance peak is not ωₙ√(1 − ζ²) but ωₙ√(1 − 2ζ²), and it occurs only for ζ < 1/√2; √(1 − ζ²) is the damped oscillation frequency. The poles are real for ζ ≥ 1 (not only at ζ = 1); for ζ > 1 there are two distinct real poles, one approaching the origin while the other moves away to the left.*

## Page 177: Lengths of the Pole Vectors

The problem asks for computing the lengths and angles of the vectors drawn from 512 points on the unit circle (ω = k·π/256) to the poles of the system H₁(z) = 1 / (1 − 0.9z⁻¹ + 0.81z⁻²), and showing their relationship to the frequency response. The core of the solutions:

```matlab
omega=[0:511]*pi/256;
unitcirc=exp(j*omega);
num=[1 0 0];
den=[1 -0.9 0.81];
ps1=roots(den)
polevectors1=ones(2,1)*unitcirc-ps1*ones(1,512);
polelength1=abs(polevectors1);
poleangle1=atan2(imag(polevectors1),real(polevectors1));
zerovectors1=ones(2,1)*unitcirc;      % two zeros at z = 0
zerolength1=abs(zerovectors1);
plot(omega,polelength1,'r',omega,zerolength1,'g')
```

The poles are at **z = 0.9·e^(±jπ/3)** (= 0.45 ± j0.779); since writing H₁(z) = z²/(z² − 0.9z + 0.81) shows two zeros at z = 0, the length of the zero vectors is 1 at every frequency.

*Note: The concluding sentence in one solution ("|H₁| is minimum where the pole lengths are maximum and minimum, and maximum where they are 1") is wrong. Since the zero lengths are 1, |H₁(e^jω)| = 1 / (|e^jω − p₁|·|e^jω − p₂|): |H₁| is largest around ω ≈ ±π/3, where the pole vectors become shorter, and smallest around ω = π, where they become longer.*

## Page 169 (a) (2011)

A short solution prepared in 2011 from the same problem set defines the causal system as H(s) = 1/(s + 2) with `tf([1],[1 2])`, and for its non-causal counterpart sets up a second transfer function starting from the time-reversed equation (−dy(−t)/dt − 2y(−t) = −x(−t)). The 2011 solution to 177 (b) is identical to the pole vector computation above; according to a note in the file, the detailed explanations and the Laplace question were handwritten and submitted separately.

## Homework: Impulse Response of a Band-Limited 90° Phase Shifter

The same folder also contained a photograph of a classmate's handwritten "Homework" page dated March 27, 2007 (transcribed to text from the photographed page; the photograph is not published). For the system whose frequency response in the band |ω| < ω_c is

H(jω) = e^(jπ/2), 0 < ω < ω_c; H(jω) = e^(−jπ/2), −ω_c < ω < 0

the impulse response is found by the inverse Fourier transform:

h(t) = (1/2π) ∫₀^ω_c e^(jπ/2) e^(jωt) dω + (1/2π) ∫₋ω_c⁰ e^(−jπ/2) e^(jωt) dω
= (1/2πt) (e^(jω_c t) − 1) − (1/2πt) (1 − e^(−jω_c t))
= (cos ω_c t − 1) / (πt)

and using cos ω_c t = 1 − 2 sin²(ω_c t/2), the result is

**h(t) = −2 sin²(ω_c t / 2) / (πt)**

(We checked the result; it is correct.)
