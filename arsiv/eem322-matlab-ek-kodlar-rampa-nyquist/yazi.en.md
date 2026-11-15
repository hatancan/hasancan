---
baslik: EEM322 Control Systems: Additional MATLAB Work: Ramp, Root Locus, Bode and Nyquist
ozet: Appendices of student MATLAB work: B-5-17, B-5-31, B-8-16, root locus examples and standalone source files.
---

The additional **MATLAB assignment plots and source files** found in the EEM322 course folder were gathered together from the work of different classmates. The creation metadata of the original Word files dates back to 2004, 2007 and 2013; the archive date of the compilation is based on the newest document, dated 17 May 2013. File names bearing student names were changed; Office author information was removed from the PDF copies. The PDFs and MATLAB files are available for download as a ZIP at the end of the post.

## B-5-17: Step response of a third-order system

The model in the document is **T(s) = 10/(s³ + 6s² + 8s + 10)**. In the MATLAB plot, the peak is marked as 1.21, the overshoot as 21.4%, and the peak time as 2.67 s.

```matlab
num=[0 0 0 10];
den=[1 6 8 10];
step(num,den)
grid
```

## B-8-16: Nyquist plot

The model is **G(s) = (s² + 2s + 1)/(s³ + 0.2s² + s + 1)**. The document contains a screenshot of the Nyquist curve with gain/phase margin markings.

```matlab
num=[0 1 2 1];
den=[1 0.2 1 1];
nyquist(num,den)
grid
```

## B-5-31: Varying K in the ramp response

For the system T(s) = K/(s² + s + K), B = 1 is held constant and K = 0.5, 8 and 50 are tried. The same template was run for each value of K:

```matlab
num=[0 0 0.5];
den=[1 1 0.5];
t=0:0.1:10;
r=t;
y=lsim(num,den,r,t);
plot(t,r,'-',t,y,'o')
grid
title('Ramp response for different values of K');
xlabel('t Sec')
ylabel('Output')
text(3.2,6.5,'Unit Ramp Input')
text(6.0,3.1,'Output')
```

`Rl1.m` repeats the same experiment with K = 150. In the plot, the line shows the input ramp and the circles show the system output.

## B-6-5, B-6-9 and B-6-12: Root locus plots

| Problem | Numerator coefficients | Denominator coefficients |
|---|---|---|
| B-6-5 | [0 0 0 0 1] | [1 4 11 14 10] |
| B-6-9 | [0 0 1 9] | [1 4 11 0] |
| B-6-12 | [0 0 0 1 1] | [1 4 11 14 10] |

In the document, the `rlocus(num,den)` call is followed by `axis`, `grid` and title commands. The denominator of B-6-5 and B-6-12 factors as (s² + 2s + 2)(s² + 2s + 5). `Rl2.m` is a separate file that sets the axes to the range −10…10 for B-6-12.

## Standalone MATLAB files

The code below is reproduced with the contents of the sources preserved. The files were not run; note that the polynomial definitions and commands may be used for different purposes in the sources.

### Uraz 5.4(b): polynomial roots and root locus

```matlab
clc;
clear all;

p=[1 5 9 20 2];
roots(p);

num=[1 5 9 20 0];
den=[0 0 0 0 1];
rlocus(num,den);
%axis('square');
grid on;
title('Root Locus');
```

### B-6-11: polynomial roots and root locus

```matlab
clc;
clear all;

p=[1 4 8 2];
roots(p);

num=[0 0 0 1];
den=    [1 4 8 0];
rlocus(num,den);
%axis('square');
grid on;
title('Root Locus');
```

### Ramp response for K = 150

```matlab
num=[0  0 150];
den=[1 1 150];
t=0:0.1:10;
r=t;
y=lsim(num,den,r,t);
plot(t,r,'-',t,y,'o')
grid 
title('Ramp response for different values of K');
xlabel('t Sec')
ylabel('Output')
text(3.2,6.5,'Unit Ramp Input')
text(6.0,3.1,'Output')
```

### Root locus for B-6-12

```matlab
num=[0 0 0 1 1];
den=[1 4 11 14 10];
rlocus(num,den);
v=[-10 10 -10 10];
axis(v);axis('square')
grid;
title('Root-Locus Plot of G(s)=K(s+1)/[(s^2+2s+2)(s^2+2s+5)]')
```

### Uraz 6.1(d): polar plot

```matlab
num=[0 0 1 -5];
den=[1 11 10 0];
Polar(num,den)
grid
title('H(s) nin Polar çizimi')
```

### Uraz 6.1(d): Bode plot

```matlab
num=[0 0 1 -5];
den=[1 11 10 0];
bode(num,den)
grid
title('H(s) nin Bode çizimi')
```

### Uraz 6.2(c): Nyquist plot

```matlab
num=[0 0 10 10];
den=[1 -11 10 0];
nyquist(num,den)
grid
title('H(s) nin Nyquist çizimi')
```

### Additional Bode example

```matlab
num=[0 0 0 (0.25*3.4626)];
den=[0.25 0.25 1 0];
bode(num,den)
grid
title('G(s) nin Bode çizimi','FontWeight','bold')
```

### Additional Nyquist example

```matlab
num=[0 2 1];
den=[1 -1 0];
nyquist(num,den)
grid
title('G(s) nin Nyquist çizimi','FontWeight','bold')
```

### Bode plot of a bandpass system

```matlab
sys=tf([(4*10^8),0],[1,20001,20000])
bode(sys,'m')
```

*Note: The `roots(p)` polynomial in the file `uraz5bs4b.m` has a constant term of 2; the numerator defined separately for `rlocus` has a constant term of 0. In `b6s11.m` as well, the `roots` polynomial and the open-loop denominator differ. These definitions were not merged or corrected. The separate routine required by the `Polar` call is not present in the archive.*

## Additional screenshot

`Bode-Ekran-Ciktisi.pdf` is a magnitude and phase plot under the heading "C-D". The magnitude first rises and flattens, then falls; the phase goes from +90° to −90°. Since the transfer function is not written on this page, no model was assigned from the plot alone.
