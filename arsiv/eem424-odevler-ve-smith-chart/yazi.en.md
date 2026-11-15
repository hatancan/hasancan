---
baslik: EEM424 Microwave Theory: 2014-2015 Assignments (Interference, Polarization, Microwave Oven, SAR), Smith Chart and Plane Wave MATLAB Animation
ozet: EEM424 Microwave Theory assignment sheets (2014 and 2015) by Prof. Dr. S. Gökhun Tanyer, the course's Smith chart, and my MATLAB code animating plane wave propagation.
---

**EEM 424 Microwave Theory** (Prof. Dr. S. Gökhun Tanyer): the assignment sheets given in the course, the Smith chart distributed for the course, and the MATLAB animation code I wrote for one of the first assignments. The four PDFs and the code can be downloaded as a ZIP at the end of the post.

## Assignment 1 (February 2014)

Submission: assignments given during a week are submitted at the first lecture on the first Monday following the week in which they were given; late submissions lose 20% for each day of delay (for this assignment, the deadline is the first Monday after the add-drop week, March 3). All answers are prepared by hand on blank paper, with figures where necessary; no covers or plastic sleeves are used.

1. What is Rayleigh scattering?
2. What is interference?
3. What is polarization?
4. Internet search: find the lecture notes titled "Frequency Band Allocations"; find Turkey's allocations.
5. Internet search: find documents about SAR, ISAR, and ASAR and explain what you understand from them.

## Assignments 01 and 02 (February 2015, "Microwave Theory and Applications")

**Assignment 01:** (1) What is interference? (2) What is polarization? (Use information from the internet, but write in your own words.) (3) Research on microwave ovens: a table with one row per device giving brand/model, operating frequency, dimensions (width/height/depth), and the source of the information (internet/store). (4) Examine the MATLAB software; research what it can be used for and its capabilities. (5) Choose MATLAB or a similar software and prepare a one-page introduction document for use in the assignments. (6) Other questions, if announced in class.

**Assignment 02:** (1) Frequency band allocations for Turkey. (2) SAR, ISAR, and ASAR documents, with the sources used attached. (3) **A plane wave entering a denser medium from a less dense medium at an angle:** (A) write the equation relating the incident and transmitted (entering) wave angles; (B) calculate and show on a figure for the following cases: (a) entering exactly perpendicular to the surface, (b) nearly perpendicular, (c) nearly parallel to the surface (nearly 90°). (4) Repeat (3) for angled entry **from a denser medium into a less dense medium**. (5) Other questions, if announced in class.

As a reference for (3), the relevant relation is Snell's law: n₁·sin θ₁ = n₂·sin θ₂ (in EM, the relation between θ_i and θ_t is sin θ_t = (n₁/n₂)·sin θ_i); the relation is not written explicitly in the assignment sheet, so I am including it as a reminder.

## Smith chart

"The Complete Smith Chart" (Black Magic Design) is the blank (unused) detailed chart distributed on the course page under the title "EEM424 Microwave Theory, Başkent University". It includes reactance and susceptance components, the reflection coefficient angle, wavelength scales, and radially scaled parameters (SWR, return loss, reflection coefficient, transmission coefficient). It is used in the matching and stub assignments.

## MATLAB: plane wave propagation animation

Code that animates, over time, the real part of a plane wave with a 1 m wavelength propagating in the +x direction (`duzlemsel-dalga-animasyonu.m`, included in the ZIP):

```matlab
[x,y]= meshgrid(5:0.05:15, -5:0.05:5);
l=1;                 % dalga boyu
k=2*pi/l;            % dalga sayısı
f=3e8/l;             % frekans (c/l)
w=2*pi*f;
t=linspace(0,60e-9,200);
z=exp(1i*k*x);
for n=1:length(t)
    surf(x,y,real(z*exp(-1i*w*t(n))));
    view(3)
    zlim([-1.5 1.5])
    xlim([min(min(x)) max(max(x))])
    ylim([min(min(y)) max(max(y))])
    shading interp
    getframe();
end
```

The wave has the form e^{j(kx − ωt)}; its real part travels in the x direction as a cosine. The period is 3.33 ns; the 60 ns time axis corresponds to 18 periods.

*Note: These sheets and the chart belong to the course instructor; they will be removed upon request by the rights holder.*
