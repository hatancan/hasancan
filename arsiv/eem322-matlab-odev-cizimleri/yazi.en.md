---
baslik: EEM322 Control Systems: MATLAB Assignments 2005–2013 – Root Locus, Bode and Nyquist Plots, margin and step Commands
ozet: Student work from different years for the EEM322 MATLAB project: Ogata B-6 root locus plots (rlocus), B-8-29 and B-8-30 Bode diagrams, Uraz 6.2(a) and 6.4(a) Nyquist plots, margin output for HW+MATPRO 12, and a help note explaining the use of step, bode, and rlocus.
---

This post brings together the Word documents prepared for the **MATLAB project** of the **EEM322 Control Systems** course at Başkent University. The documents come from different students between 2005 and 2013. Personal information (names, numbers, document author metadata) has been removed: each document was re-converted to PDF from page images, the cover line containing the name and number was covered, and the file names were changed to year and problem number. All of the documents are in the ZIP file at the end of the post.

In the course, each student was given problems from Ogata's *Modern Control Engineering* and Uraz's *Control Systems*. For the MATLAB project, the solution steps of these problems were to be accompanied by MATLAB code and all time response, root locus, Bode, and Nyquist plots (the assignment distribution is in the [syllabus post](/arsiv/eem322-izlence/)). Starting in 2012, the assignment was given over a single parametric system ([HW+MATPRO](/arsiv/eem322-odev-cozumleri-hw-matpro/)).

## MATLAB help note (2004–2005)

The "EEM322 homework help" document that circulated among students summarizes the use of three basic commands. A step function is an input that jumps from zero to a finite value at t = 0; the `step` command plots the unit step response by default.

Example 1, step response of a state-space model:

```matlab
A = [0 1 ; 0 -.05];
B = [0 ; 0.001];
C = [0 1];
D = [ 0];
sys = ss(A,B,C,D);
step(sys); % the time axis is not specified; as in the second example, the time range and
           % resolution can be set by defining a t vector and using the command step(sys,t).
title('Birim Basamak Yaniti');
xlabel(' Time');
ylabel(' y(t) ');
grid on;
```

Example 2, closed-loop transfer function T(s) = (s + 1)/(2s² + s + 3):

```matlab
num=[1 1];
den=[2 1 3];
t=0:0.1:50; % time vector: start 0, step 0.1, end 50
y=tf(num,den);
step(y,t);
title('Birim Basamak Yanıtı');
xlabel(' Time');
ylabel(' y(t) ');
grid on;
```

Short scripts for the Bode plot and the root locus that ask the user for the numerator and denominator:

```matlab
num=input(' Açık Döngü Transfer Fonksiyonun Payını Girin: ');
den=input(' Açık Döngü Transfer Fonksiyonun Paydasını Girin: ');
bode(num, den);
grid on;
```

```matlab
num=input(' Açık Döngü Transfer Fonksiyonun Payını Girin: ');
den=input(' Açık Döngü Transfer Fonksiyonun Paydasını Girin: ');
rlocus(num, den);
```

## Ogata B-6 root locus plots (2005)

In two documents dated May 2005, the root loci for Ogata Chapter 6 problems are computed with `rlocus` and plotted with markers using `plot`. K is swept from 0 to 1000 in steps of 0.2:

```matlab
% Soru 6-8
num=[0 0 1 0.5]
den=[1 1 0 1]
K=[0:0.2:1000]
r=rlocus(num,den,K)
plot(r,'o')
v=[-5 1 -8 8]; axis(v)
grid
title('Root-Locus Plot of problem 6-8')
xlabel('Real Axis')
ylabel('Imag Axis')
```

The same pattern is repeated for B-6-10 with `num=[0 0 0 2 2]`, `den=[1 7 10 0 0]` (that is, 2(s + 1)/[s²(s + 2)(s + 5)], axes [−5 5 −10 10]) and for B-6-12 with `num=[0 0 0 1 1]`, `den=[1 4 11 14 10]` (axes [−5 1 −5 5]). In a separate document for B-6-10, only `rlocus(num,den)` is used.

## 2006: Uraz 5.6(b), 5.6(d) and Ogata B-5 problems

In one student's "EEM322 HW – MATLAB" document, each problem has a root locus, step response, Nyquist, and Bode plot, in that order. Points read from the Bode plots with MATLAB's data cursor:

| Problem | Magnitude point read | Phase point read |
|---|---|---|
| Uraz 5.6(b) | 30.7 dB at 0.491 rad/s | −109° at 0.493 rad/s |
| Uraz 5.6(d) | −28.2 dB at 2.97 rad/s | −148° at 2.96 rad/s |
| Ogata B-5-26 (K = 1) | −27.9 dB at 4.25 rad/s | −36.2° at 4.24 rad/s |
| Ogata B-5-13 | −6.51 dB at 0.56 rad/s | 18.4° at 0.559 rad/s |
| Ogata B-5-27(a) | −4.28 dB at 2.56 rad/s | −180° at 2.56 rad/s |
| Ogata B-5-27(b) | −8.69 dB at 2.55 rad/s | −180° at 2.55 rad/s |

For B-5-13, the unit impulse, unit step, and unit ramp responses are plotted separately. Another document dated 2008 (titled 5.4(d) and 5.6(h)) was not added to the archive because it is a copy of the same plots.

In a second "Matlab Assignment" document from the same year, there are root locus, Nyquist, Bode, and step response plots for Ogata B-8-29 and Uraz 6.4(a). In the Bode plot of B-8-29, −0.0144 dB at 0.645 rad/s (gain crossover) and −179° at 41.5 rad/s (near the phase crossover) were read; for Uraz 6.4(a), 0.0533 dB at 0.866 rad/s and −317° at 0.925 rad/s.

## 2007: Root locus, Bode and Nyquist plots

Root loci for Uraz B.6.2 and B.6.3 (the document has a note: "I did Ogata B.6.2 in place of the problem I could not do"):

```matlab
>> num=[0 1 4];
>> den=[1 2 1];
>> g=tf(num,den)

Transfer function:
    s+4
-------------
s^2 + 2 s + 1

>> rlocus(g)
```

```matlab
>> numm=[0 0 0 0 1];
>> denn=[1 5 9 5 0];
>> f=tf(numm,denn)

Transfer function:
           1
-------------------------
s^4 + 5 s^3 + 9 s^2 + 5 s

>> rlocus(f)
```

In the Bode diagrams of Ogata B-8-29 and B-8-30, MATLAB's stability margin cursors were used:

| Problem | Gain margin | Phase margin | Note |
|---|---|---|---|
| Ogata B-8-29 | 1.26 dB (2 rad/s) | 50.8° (1.48 rad/s), delay margin 0.6 s | Closed loop stable |
| Ogata B-8-30 | – | 84.2° (0.673 rad/s), delay margin 2.18 s | Closed loop stable |

In the Nyquist plot of Uraz 6.2(a), a gain margin of −14 dB (at 0 rad/s) and a phase margin of 22.8° (at 2.1 rad/s, delay margin 0.189 s) were read, and the closed loop was shown to be stable.

## 2008: Bode and Nyquist for three K values

In a two-page document, the Bode and Nyquist plots of the same system are overlaid for K = 0.2, 0.5, and 2. In the Bode plot, the magnitude curves shift upward with K, while the phase curve is a single curve rising from −180° to −90° ("the K values are the same for all phase curves"). In the Nyquist plot, the curves start on the real axis at −0.8, −2, and −8 and proceed to the origin along a semicircle; that is, the zero-frequency gain of the plotted system is −4K.

## 2012–2013: HW+MATPRO 12

The last two documents belong to parameter set 12 of the HW+MATPRO assignment (n = 1, a = 1, b = 3, c = 4, d = 16): G(s) = (s + 1)/[s(s + 3)(s² + 4s + 16)] = (s + 1)/(s⁴ + 7s³ + 28s² + 48s).

```matlab
sys=tf([1,1],[1,7,28,48,0])
rlocusplot(sys)
bode(sys)
stepplot(sys)
figure,nyquist(sys)
[Gm,Pm,Wg,Wp] = margin(sys)
```

```
Gm = 113.5587

Pm = 90.4973

Wg = 4.8041

Wp = 0.0208
```

In the `margin` output, Gm is the absolute value (20 log 113.56 ≈ 41.1 dB), Wg is the phase crossover frequency (where the phase is −180°), and Wp is the gain crossover frequency. The phase crosses −180° at 4.80 rad/s and |G| ≈ 1/113.6 there; since the gain at low frequencies is |G| ≈ 1/(48ω), it drops to 1 at 0.0208 rad/s. The documents include Bode, Nyquist (with dB circles), root locus, and step response plots. Since the step response is plotted for the open-loop G(s) (there is a pole at the origin), it keeps increasing like a ramp.

*Note: The calculation was checked: at ω = 4.804 rad/s the phase of G(jω) is −180° and 1/|G| = 113.57.*
