---
baslik: EEM301 Signals and Systems I: MATLAB Project 1 Solutions and Pole–Frequency Experiments
ozet: Time shifting, conv, and filter exercises from the 2006, 2008, and 2011 assignment versions; the pole and frequency response code in the sinyal.m file.
---

Three MATLAB Project 1 solutions prepared by classmates were compiled, according to the dates on the source documents, from the versions of **15 November 2006, 23 November 2008, and 24 November 2011**. Personal information was removed; the ID field on the cover page was masked. The ZIP contains the three cleaned PDFs and the **sinyal.m** source code from the same archive. The code was reviewed through the text and formulas only, without being run.

## Plotting the signal and time transformations

Starting example:

```matlab
nx=-3:1:7;
x=[0 0 0 2 0 1 -1 3 0 0 0];
stem(nx,x)
```

The nonzero samples are x[0]=2, x[2]=1, x[3]=−1, and x[4]=3. In the 2008 solution, a delay of two samples and an advance of one sample are shown by keeping the sample values and changing the plot axis:

```matlab
ny1=-1:1:9;
y1=[0 0 0 2 0 1 -1 3 0 0 0];
stem(ny1,y1)
ny2=-4:1:6;
y2=[0 0 0 2 0 1 -1 3 0 0 0];
stem(ny2,y2)
ny3=-7:1:3;
y3=[0 0 0 3 -1 1 0 2 0 0 0];
stem(ny3,y3)
```

In time reversal, both the signs of the indices and the order of the values change. The following lines of the source are:

```matlab
ny4=-6:1:4;
y3=[0 0 0 3 -1 1 0 2 0 0 0];
stem(ny4,y4)
```

*Note: In the last section, the assignment is made to y3 while y4 is plotted; in a clean workspace, y4 is undefined. Also, the ny4 axis shifts the reversed signal one sample to the right; this is inconsistent with the heading "Flipped and Advanced by 1". In the 2006 version, for some shifts both the values within the array and the index axis were shifted; the result is that the desired shift is applied twice.*

## Convolution of two rectangular sequences

```matlab
n=0:5;
x=[1 1 1 1 1 1];
y=conv(x,x);
ny=0:10;
stem(ny,y)
```

Output:

```
1  2  3  4  5  6  5  4  3  2  1
```

Two sequences of length 6 give a triangular result of length 11. The first sample receives a single product, and the center receives six product contributions.

## Convolution of a rectangular sequence with a finite ramp

```matlab
n=0:5;
h=n;
x=[1 1 1 1 1 1];
y=conv(x,h);
ny=0:10;
stem(ny,y)
```

The result is [0,1,3,6,10,15,15,14,12,9,5]. If h[n+5] is used, the same values are shown on the axis −5:5.

In the 2011 version, the following axis is written for the shifted plot:

```matlab
n=-5:1:0;
z=length(n);
ny=0:1:((z.*2)-2-5);
```

*Note: With z=6, this ny has six elements; the conv result has eleven elements. The axis of the relevant plot should be −5:5. In the first conv example of the 2006 version as well, the previous x array was used without being redefined; for the triangular result shown, x must consist of six ones.*

## Difference equations with filter

MATLAB's `filter(b,a,x)` call takes the numerator coefficients as b and the denominator coefficients as a. The definitions of the three systems in the 2008 document:

```matlab
a1=[1]; b1=[0.5 1 2];
a2=[1 -0.8]; b2=[2];
a3=[1 -0.8]; b3=[0 2];
x=[1 2 3 4];
y1=filter(b1,a1,x)
y2=filter(b2,a2,x)
y3=filter(b3,a3,x)
```

| System | Difference equation | First four outputs |
|---|---|---|
| 1 | y[n]=0.5x[n]+x[n−1]+2x[n−2] | 0.5; 2; 5.5; 9 |
| 2 | y[n]−0.8y[n−1]=2x[n] | 2; 5.6; 10.48; 16.384 |
| 3 | y[n]−0.8y[n−1]=2x[n−1] | 0; 2; 5.6; 10.48 |

The 2006 document also shows an attempt in which the order of a and b is swapped: the result of `filter(a1,b1,x)` is [2,0,−2,12]. This is not the same filter.

*Note: In the 2006 document, although a2=[1], b2=[0.8 2] is written for the second system, the results of the recursive system above are given. The written coefficients produce [0.8,3.6,6.4,9.2]. In the 2011 document as well, a2=[1], b2=[2,0.8] is written first, and in the later computation a2=[1 −0.8], b2=[2] is used. These inconsistencies are preserved in the downloaded documents.*

## Convolution of two sparse sequences

x[n]=δ[n]+δ[n−2], h[n]=2δ[n+1]−2δ[n−1]. The intermediate terms cancel each other:

y[n]=2δ[n+1]−2δ[n−3].

```matlab
x=[1 0 1];
nx=0:1:2;
h=[2 0 -2];
nh=-1:1:1;
ny=-1:1:3;
y=conv(x,h);
stem(ny,y)
```

The result is [2,0,0,0,−2] at indices −1:3.

*Note: In the 2006 version, the plot axis of the same example was chosen as 1:9; the sequence positions are detached from the physical time indices. The starting index of a convolution is the sum of the starting indices of the two inputs.*

## sinyal.m: poles and frequency response

The following standalone source file plots the poles of four second-order transfer functions; in the last section, it computes a discrete-time frequency response. The name **sinyal.m**, which contains no personal information, was used instead of the equivalent copy named with a student number.

```matlab
b1=[1]

a1=[1 0 1]
H1=tf(b1,a1)
ps1=roots(a1)
plot(real(ps1),imag(ps1),'x')
grid
axis([-3 3 -3 3])

figure;
a2=[1 0.5 1]
H2=tf(b1,a2)
ps2=roots(a2)
plot(real(ps2),imag(ps2),'x')
grid
axis([-3 3 -3 3])

figure;
a3=[1 2 1]
H3=tf(b1,a3)
ps3=roots(a3)
plot(real(ps3),imag(ps3),'x')
grid
axis([-3 3 -3 3])

figure;
a4=[1 4 1]
H4=tf(b1,a4)
ps4=roots(a4)
plot(real(ps4),imag(ps4),'x')
grid
axis([-3 3 -3 3])

figure;
bx=[0.25 -0.87 1]
ax=[1 -0.87 0.25]
HX=tf(bx,ax)
HX=freqz(bx,ax,512,'whole')
plot(HX)
```

| Denominator | Poles |
|---|---|
| s²+1 | ±j |
| s²+0.5s+1 | −1/4 ± j√15/4 |
| s²+2s+1 | −1, double |
| s²+4s+1 | −2±√3 |

*Note: Models created with tf without a sampling time are continuous-time. freqz, on the other hand, interprets the b and a arrays as discrete-time filter coefficients. The last two lines replace the transfer function variable HX with the frequency response vector; plot(HX) plots the real and imaginary components in the complex plane instead of plotting the magnitude against frequency.*
