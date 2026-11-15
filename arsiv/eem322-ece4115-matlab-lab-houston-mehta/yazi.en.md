---
baslik: EEM322 Control Systems: MATLAB Control Lab, Parts 1–4 (University of Houston ECE 4115, Nisarg Mehta, 2005)
ozet: University of Houston ECE 4115 Control Systems Lab (Spring 2005) MATLAB presentations: tf, zpk, ss and frd models; impulse, step, lsim, conv, deconv, residue; rlocus, rlocfind, bode, nyquist, margin; DC motor speed control case study (PID, root locus, frequency-domain design).
---

This post brings together four **third-party** presentations saved in the EEM322 Control Systems course folder under the heading "control systems downloaded from various places": the MATLAB lab presentations (Chapters 1–4) of the **University of Houston** **ECE 4115 Control Systems Lab 1** course, **Spring 2005** semester. The presentations were prepared by **Nisarg Mehta** ("Prepared by: Nisarg Mehta"); the files are dated February–April 2005. The note file in the folder gives the source as **http://www.egr.uh.edu/courses/ECE/ECE4115/**. Since the presentations are in English, the content is conveyed in its original language; equations were converted to plain text. The four PowerPoint files and the source note can be downloaded as a ZIP at the end of the post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed at the request of the rights holder.*

In the lab, MATLAB was launched from a network drive: *Start → Run → \\laser\apps*, then MATLAB 7.0.1 in the MatlabR14 folder. Each chapter ended with a homework assignment; the semester ended with a project on model reduction and control system design.

## Chapter 1: System Models

The Control System Toolbox has **4 basic types of LTI models**: Transfer Function (TF), Zero-pole-gain model (ZPK), State-Space models (SS) and Frequency response data model (FRD). The chapter also covers conversion between models and model dynamics.

### Transfer function models

Consider a linear time invariant (LTI) single-input/single-output system:

> y'' + 6y' + 5y = 4u' + 3u

Applying the Laplace transform to both sides with zero initial conditions:

> G(s) = Y(s)/U(s) = (4s + 3)/(s² + 6s + 5)

**tf** – creation of transfer functions. `sys=tf(num,den)` creates a continuous-time transfer function sys with numerator(s) num and denominator(s) den. For SISO models, num and den are row vectors listing the numerator and denominator coefficients in descending powers of s.

**tfdata** – quick access to transfer function data. `[num,den]=tfdata(sys,'v')` returns the numerator and denominator as row vectors (if sys is not a transfer function, it is first converted).

```matlab
>> num = [4 3];
>> den = [1 6 5];
>> sys = tf(num,den)
Transfer function:
    4 s + 3
-------------
s^2 + 6 s + 5
>> [num,den] = tfdata(sys,'v')
num =
     0     4     3
den =
     1     6     5
```

"My first program", Chp1_1.m:

```matlab
%Program to write a Transfer function
%Author: Firstname Lastname
clear all
close all
clc
num = [4 3];
den = [1 6 5];
sys = tf(num,den) %transfer function model
[num1,den1] = tfdata(sys,'v')
```

### Zero-pole-gain models

The same system in zero-pole-gain form: G(s) = (4s + 3)/(s² + 6s + 5) = 4(s + 0.75)/((s + 1)(s + 5)).

**zpk** – `sys=zpk(z,p,k)` creates a continuous-time zero-pole-gain model with zeros z, poles p and gain k (set z=[ ] if there are no zeros). **zpkdata** – `[z,p,k]=zpkdata(sys,'v')` returns the zeros and poles as column vectors and the gain k.

```matlab
%Program to write a Zero-Pole-Gain Model  (Chp1_2.m)
z = -0.75;
p = [-1 -5];
g = 4;
sys1 = zpk(z,p,g)
disp('The zeros, poles and gain corresponding to the system are')
[ze,po,k]=zpkdata(sys1,'v')
```

```
Zero/pole/gain:
 4 (s+0.75)
-----------
(s+1) (s+5)
ze = -0.7500
po = -1
     -5
k  = 4
```

### State-space models

A state-space model for the same system is

> [x1'; x2'] = [0 1; −5 −6]·[x1; x2] + [0; 1]·u,  y = [3 4]·[x1; x2],  x1(0) = x2(0) = 0

```matlab
%Program to write a State-space Model  (Chp1_3.m)
A = [0 1; -5 -6];
B = [0; 1];
C = [3 4];
D = 0;
sys = ss(A,B,C,D)
[A,B,C,D] = ssdata(sys)
```

### Frequency response data models

```matlab
freq = [1000; 2000; 3000];
resp = [1;2;3];
H = frd(resp,freq)
```

### Conversion between models and model dynamics

- `sys_tf = tf(sys)`, `sys_zpk = zpk(sys)`, `sys_ss = ss(sys)` convert an arbitrary LTI model to transfer function, zero-pole-gain and state-space representation respectively.
- **pzmap** – pole-zero map of LTI models; poles are plotted as x's and zeros as o's. `[p,z]=pzmap(sys)` returns them without a plot.
- **pole**, **eig** – compute the poles of LTI models.
- **zero** – transmission zeros; `[z,gain]=zero(sys)` also returns the gain.
- **dcgain** – steady-state (DC or low-frequency, i.e. G(0)) gain.

```matlab
%Program to write a State-space Model and understand model dynamics
num = [4 3];
den = [1 6 5];
sys = tf(num,den)   %sys in transfer function model
sys_ss = ss(sys)    %sys_ss in state space model
pzmap(sys)          %plot pole-zero map
p = pole(sys)       %determine poles
po = eig(sys)       %determine poles
z = zero(sys)       %determine zeros
k = dcgain(sys)     %determine DC gain
```

HW #1: one submission per team (HW1_1.m, HW1_2.m, HW1_3.m).

## Chapter 2: Time Response of Systems

Once a model of a system has been defined, we might be interested in knowing the time response of the system to a certain input. Objectives: impulse response (`impulse`), step response (`step`), general time response (`lsim`), polynomial multiplication (`conv`), polynomial division (`deconv`) and partial fraction expansion (`residue`).

- The **impulse response** of a system is its output when the input is a unit impulse. `impulse(sys)` plots it; `impulse(sys,tfinal)` simulates from t = 0 to tfinal; `impulse(sys,t)` uses a user-supplied time vector; `[y,t]=impulse(sys)` returns the response without plotting (for state-space models `[y,t,x]` also returns the state trajectory).
- The **step response** is the output for a unit step input; `step` has the same calling forms.
- The general response to any input is computed with **lsim**: `lsim(sys,u,t)` plots the response to the input samples u at times t; `lsim(sys,u,t,x0)` specifies the initial state (state-space models only).

**Problem 1:** Given the LTI system G(s) = (3s + 2)/(2s³ + 4s² + 5s + 1), plot (a) the impulse response, (b) the step response, (c) the response to the input u(t) = sin(0.5t), using both `lsim` and `residue`.

```matlab
%Chp2_1.m
A=[3 2];
B=[2 4 5 1];
sys=tf(A,B);
t=0:0.01:10;
%Impulse response
impulse(sys,t);
%Step response
figure
step(sys,t);
%Response to a sinusoidal input
u=sin(0.5*t);
figure
lsim(sys,u,t);
```

### conv, deconv and residue

- `C=conv(A,B)` multiplies two polynomials: (s² + 3s − 1)(2s² − 4s + 3) = 2s⁴ + 2s³ − 11s² + 13s − 3, i.e. `C=conv([1 3 -1],[2 -4 3])` gives `2 2 -11 13 -3`.
- `[Q,R]=deconv(B,A)` divides polynomials so that B = conv(A,Q) + R: (s³ + 6s² + 11s + 6)/(s + 2) → `[Q,R]=deconv([1 6 11 6],[1 2])` gives Q = `1 4 3`, R = `0 0 0 0`.
- `[r,p,k]=residue(B,A)` finds the residues, poles and direct term of the partial fraction expansion of B(s)/A(s). If P(j) = … = P(j+m−1) is a pole of multiplicity m, the expansion includes the terms R(j)/(s − P(j)) + R(j+1)/(s − P(j))² + … + R(j+m−1)/(s − P(j))^m. `[b,a]=residue(r,p,k)` converts back to polynomials.

**Problem 2:** Given G(s) = (3s + 2)/(s³ + 5s² + 8s + 4), find the step response using the residue command. With U(s) = 1/s, Y(s) = G(s)U(s) = (3s + 2)/(s³ + 5s² + 8s + 4) · 1/s and y(t) = L⁻¹{Y(s)}: a partial fraction expansion is performed first, then each fraction is inverted and the individual inverse transforms are added up.

```matlab
%Chp2_2.m
A=[3 2];
B=[1 5 8 4];
Bu=conv(B,[1 0]);
[r,p,k]=residue(A,Bu)
```

```
r = -1.5000   -2.0000    1.0000    0.5000
p = -2.0000   -2.0000   -1.0000         0
k = []
```

Y(s) has four poles, one of them repeated, so

> y(t) = r(1)·e^(p(1)t) + r(2)·t·e^(p(1)t) + r(3)·e^(p(2)t) + r(4)·e^(p(3)t)

*Note: In the slide's expression the indices of the exponential terms are shifted relative to the order of the p vector; the code in Chp2_3.m has the correct form: y(t) = r(1)e^(p(1)t) + r(2)·t·e^(p(2)t) + r(3)e^(p(3)t) + r(4)e^(p(4)t). Numerically, y(t) = 0.5 + e^(−t) − 1.5e^(−2t) − 2t·e^(−2t) (check: y = 0 at t = 0, final value G(0) = 2/4 = 0.5).*

```matlab
%Chp2_3.m
A=[3 2];
B=[1 5 8 4];
sys=tf(A,B);
t=0:0.01:10;
%Step response
[ystep,t]=step(sys,t);
%Step response via the Inverse Laplace Transform
Bu = conv(B,[1,0]);
[r,p] = residue(A,Bu);
ystep_res=r(1)*exp(p(1)*t)+r(2)*t.*exp(p(2)*t)...
    +r(3)*exp(p(3)*t)+r(4)*exp(p(4)*t);
%Figures
subplot(2,1,1),plot(t,ystep_res,'k')
xlabel('t')
ylabel('y')
subplot(2,1,2),plot(t,ystep,'k:')
xlabel('t')
ylabel('y')
```

![Step response computed by inverse Laplace transform (a) and by the step command (b); both settle at 0.5](ch2-sekil.jpg "Step response by inverse Laplace transform (a) and by the step command (b)")

## Chapter 3: Frequency Domain Analysis and Design

Topics: root locus analysis; frequency response plots (Bode, Nyquist); gain margin and phase margin.

### Root locus

The root locus is a plot in the s-plane of all possible locations of the poles of a closed-loop system, as one parameter, usually the gain, is varied from 0 to ∞. By examining that plot the designer can choose values of the controller's parameters and infer the performance of the closed-loop system.

- `rlocus(sys)` computes and plots the root locus of the SISO model for the negative feedback loop as the feedback gain K varies from 0 to Inf; `rlocus(sys,k)` uses user-specified gains; `[r,k]=rlocus(sys)` returns the root locations.
- `[k,poles]=rlocfind(sys)` puts up a crosshair cursor on an existing root locus; the gain at the selected point and all closed-loop poles for that gain are returned. `[k,poles]=rlocfind(sys,p)` computes a gain for each desired root location in p.

**Problem 1:** Plot the root locus of G(s) = K(s + 8)/(s(s + 2)(s² + 8s + 32)).

```matlab
%Chp3_1.m
num=[1 8];
den=conv(conv([1 0],[1 2]),[1 8 32]);
Gsys=tf(num,den)
rlocus(Gsys)
[k,pol]=rlocfind(Gsys)
```

```
Transfer function:
           s + 8
----------------------------
s^4 + 10 s^3 + 48 s^2 + 64 s
Select a point in the graphics window
selected_point =
  -8.2929 - 2.7551i
k =
  775.1330
pol =
   3.2999 + 8.3727i
   3.2999 - 8.3727i
  -8.2999 + 2.7705i
  -8.2999 - 2.7705i
```

![Root locus of K(s+8)/(s(s+2)(s²+8s+32)): two branches cross into the right half plane](ch3-kok-yer.jpg "Root locus plot from Chp3_1.m")

### Bode and Nyquist plots

The MATLAB Control System Toolbox provides functions for the two most common frequency response plots: `bode` and `nyquist`. `logspace(d1,d2,N)` generates N logarithmically equally spaced points between 10^d1 and 10^d2 (e.g. `logspace(-1,2,100)`: 100 points from 0.1 to 100). `bode(sys)`, `bode(sys,{wmin,wmax})`, `bode(sys,w)`; `[mag,phase]=bode(sys,w)` returns magnitudes and phases (degrees) without plotting. `nyquist` has the same calling forms; `[re,im]=nyquist(sys,w)` returns the real and imaginary parts.

**Problem 2:** Given G(s) = 1/(s(s + 1)), draw the Bode diagram for 100 frequencies in the interval [10⁻¹, 10].

```matlab
%Chp3_2.m
A=[1];
B=[1 1 0];
w=logspace(-1,1,100);
sys=tf(A,B);
bode(sys,w);
[mag, phase] = bode(sys,w);
for i=1:length(w)
    magnitude(i)=mag(1,1,i);
    phase_wolag(i)=phase(1,1,i);
end
magdB=20*log10(magnitude);
phase_wlag=-57.3*0.2.*w;
phase_total=phase_wolag+phase_wlag;
figure;
subplot(2,1,1),semilogx(w,magdB)
subplot(2,1,2),semilogx(w,phase_wlag)
```

*Note: The second part of the code adds the phase contribution, −57.3·0.2·ω degrees, of a 0.2 s dead time (e^(−0.2s)) that is not mentioned in the problem. The last line probably intended to plot `phase_total`; as written, `phase_wlag` plots only the phase of the delay.*

### Gain margin and phase margin

For the loop gain transfer function L(s):

- The **gain margin** is the multiplicative amount that the magnitude of L(s) can be increased before the closed-loop system goes unstable.
- The **phase margin** is the amount of additional phase lag that can be associated with L(s) before the closed-loop system goes unstable.

`[Gm,Pm,Wcg,Wcp]=margin(sys)` computes the gain margin Gm, the phase margin Pm (degrees) and the associated crossover frequencies for the SISO open-loop model. Gm is defined as 1/G, where G is the gain at the −180° phase crossing; in dB, Gm_dB = 20·log10(Gm). Gm_dB < 0 means stability is most sensitive to loop gain reduction. With several crossover points, margin returns the smallest margins.

**Problem 3:** Given G(s) = (1280s + 640)/(s⁴ + 24.2s³ + 1604.81s² + 320.24s + 16), draw the Bode and Nyquist plots for 100 frequencies in [10⁻⁴, 10³] and find the gain and phase margins.

```matlab
%Chp3_3.m
A=[1280 640];
B=[1 24.2 1604.81 320.24 16];
w=logspace(-4,3,100);
sys=tf(A,B);
%Bode plot
bode(sys,w)
gtext('(a)')
gtext('(b)')
[Gm,Pm,Wcg,Wcp]=margin(sys)
%Nyquist plot
figure
nyquist(sys,w)
axis([-10 50 -30 30])
```

```
Gm  = 29.8637
Pm  = 72.8960
Wcg = 39.9099
Wcp = 0.9036
```

So the gain margin is about 29.9 (≈ 29.5 dB) at 39.9 rad/s and the phase margin about 72.9° at 0.90 rad/s.

![Bode diagram of Problem 3: magnitude (a) and phase (b) from 10⁻⁴ to 10³ rad/s](ch3-bode.jpg "Bode diagram from Chp3_3.m")

![Nyquist diagram of Problem 3](ch3-nyquist.jpg "Nyquist diagram from Chp3_3.m")

HW3 was due on April 20th, 2005.

## Chapter 4: Case Study – Motor Speed Control

The course summary: introduction to MATLAB; Chapter 1 system models; Chapter 2 time response; Chapter 3 frequency domain analysis and design; and a case study of motor speed control covering modeling, time response, PID controller design, root locus controller design and frequency based controller design. The programs used: Open_loop_response, P_response, PI_response, PID_response, Open_loop_rootlocus, PID_rootlocus, Open_loop_bode, PID_bode.

### Modeling

A DC motor has second order speed dynamics: mechanical properties such as inertia (J) and damping (b), electrical properties such as inductance (L) and resistance (R). The controller's objective is to maintain the speed of rotation of the motor shaft with a particular step response.

![Armature circuit (V, R, L, back EMF e = Kθ̇) and the free body diagram of the rotor (T, J, bθ̇)](ch4-model.jpg "Armature circuit and free body diagram of the rotor")

Parameters:

| Parameter | Value |
| --- | --- |
| Moment of inertia of the rotor (J) | 0.01 kg·m²/s² |
| Damping ratio of the mechanical system (b) | 0.1 Nms |
| Electromotive force constant (K = Ke = Kt) | 0.01 Nm/A |
| Electric resistance (R) | 1 Ω |
| Electric inductance (L) | 0.5 H |
| Input (V) | source voltage |
| Output (θ) | position of shaft |

The rotor and shaft are assumed to be rigid. The motor torque is related to the armature current by T = Kt·i; the back EMF is related to the rotational velocity by e = Ke·θ̇. Based on Newton's law combined with Kirchhoff's law:

> J·θ̈ + b·θ̇ = K·i
> L·(di/dt) + R·i = V − K·θ̇

Using Laplace transforms:

> (Ls + R)·I(s) = V − Ks·Θ(s)
> s(Js + b)·Θ(s) = K·I(s)
> θ̇/V = K / ((Js + b)(Ls + R) + K²)
> θ/V = K / (s((Js + b)(Ls + R) + K²))

*Note: On the slide the first ratio is also written as "θ/V"; K/((Js + b)(Ls + R) + K²) is actually the ratio of speed (θ̇) to voltage, so it has been corrected as above.*

### Open loop response and PID design

When 1 volt is applied to the system, the motor position changes by 70 radians in 2 seconds; the motor doesn't reach a steady state. With a 1 rad/sec step input, the design criteria are: settling time less than 0.04 seconds, overshoot less than 16%, no steady-state error.

PID controller: Kp + Ki/s + Kd·s = (Kd·s² + Kp·s + Ki)/s. Tuning steps on the slide:

1. Proportional controller with gain Kp = 100
1. PID controller with gains Kp = 100, Ki = 1 and Kd = 1
1. Tune the gain Ki = 200
1. Increase Kd to reduce overshoot, Kd = 10

The plots that follow show the step response with a proportional gain Kp = 1.7, PI control with Kp = 1.7, Ki = 20, and PID control (plot title Kp = 17, Ki = 200, Kd = 0.15).

![Step response with PID control: fast rise and small overshoot within 0.1 s](ch4-pid.jpg "Step response with PID controller")

*Note: The gains in the tuning steps (Kp = 100, Ki = 200, Kd = 10) do not match the values in the plot titles (Kp = 1.7 / 17, Ki = 20 / 200, Kd = 0.15); the plots appear to be taken from a different example. The presentation closely resembles the DC motor examples in the University of Michigan's "Control Tutorials for MATLAB".*

### Root locus and frequency design

The remaining slides show the open-loop root locus (P control), finding the gain on the root locus with the same design criteria (settling time < 0.04 s, overshoot < 16%, no steady-state error), the step response with PID and K = 0.13, the original Bode plot and the step response obtained with the frequency design method.

The course ended with a final project, "Model Reduction and Control Systems Design", with the sections Abstract, Introduction, Theoretical Development, Illustrative Examples, Model Reduction, Control System Design, Conclusion and Discussion, References (Homework #3 and the final project were due on April 20th).
