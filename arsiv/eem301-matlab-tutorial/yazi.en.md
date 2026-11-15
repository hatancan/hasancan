---
baslik: EEM301 Signals and Systems I: Introduction to MATLAB, Tutorials 1 and 2 (Başkent EEM417 Handout, Adapted from Control Tutorials for MATLAB)
ozet: Two introductory MATLAB handouts from the Başkent University EEE Department: creating vectors and matrices, transpose, matrix multiplication, inv, eig, poly, roots, polyval, conv, deconv; writing m-files with function, plot, colors and markers, hold, subplot, axis, title, xlabel, gtext.
---

This post contains two introductory MATLAB handouts kept in the EEM301 Signals and Systems I folder. The handouts were prepared in 2005 for the Başkent University Department of Electrical and Electronics Engineering course **EEM 417 Control System Design** (**Tutorial_1** and **Tutorial_2 – Introduction to MATLAB**); they were also used in the MATLAB assignments of EEM301. The text is in English. The main headings and sample commands are reproduced below. The original Word files can be downloaded as a ZIP at the end of the post.

The text of the handouts is largely based on the MATLAB basics tutorial of the **Control Tutorials for MATLAB** website of the University of Michigan.

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed upon request of the rights holder.*

## Tutorial 1: Introduction to MATLAB

MATLAB is an interactive program for numerical computation and data visualization; it is used extensively by control engineers for analysis and design. In these courses the **Control System Toolbox** is used in particular: transfer function, zero-pole-gain and state-space models, continuous- and discrete-time systems, time and frequency responses, root loci.

### Getting started

- `intro`: introduction to MATLAB; `helpdesk`: documentation; `demo`: examples
- `help`, `help plot`, `lookfor filter` (keyword search)
- `clc` (clears the command window), `clear` (deletes variables), `close` (closes the figure)
- `more on`: displays output one screen at a time

> When unsure about a command, use help

Typing the name of a variable displays its value; results that are not assigned are stored in the variable `ans`. Multiple commands on one line can be separated by semicolons or commas.

### Number representation

The numbers MATLAB can represent range approximately from 10⁻³⁰⁸ to 10³⁰⁸. All of the following notations denote the same number (there must be no space before the exponent):

```matlab
12345.6789
123456.789e-1
1234.56789E1
12.3456789e3
1234567.89E-2
```

### Arrays: vectors and matrices

```matlab
a = [1 2 3 4 5]      % vector
t = 0:2:20           % time vector from 0 to 20 in steps of 2
b = a + 2            % adds 2 to every element: 3 4 5 6 7
c = a + b            % sum of vectors of the same length
B = [1 2 3 4; 5 6 7 8; 9 10 11 12];   % 3x4 matrix
size(B)              % 3 4
length(a)            % 5
C = B'               % transpose (conjugate transpose for complex; use .' for plain transpose)
D = B * C            % matrix multiplication (order matters)
```

In MATLAB, indexing starts at 1; B(1,1) is the first element of the first row.

Element-by-element operations and matrix functions:

```matlab
E = [1 2;3 4]
F = [2 3;4 5]
G = E .* F     % [2 6; 12 20]
E^3            % [37 54; 81 118]
E.^3           % [1 8; 27 64]
X = inv(E)     % [-2 1; 1.5 -0.5]
eig(E)         % -0.3723, 5.3723
p = poly(E)    % characteristic polynomial: 1 -5 -2
roots(p)       % 5.3723, -0.3723 (same as the eigenvalues)
```

### Polynomials

A polynomial is a vector whose coefficients are written in descending order of degree. For s⁴ + 3s³ − 15s² − 2s + 9, `x = [1 3 -15 -2 9]`; missing terms are filled with zeros, for example `y = [1 0 0 0 1]` for s⁴ + 1.

```matlab
z = polyval([1 0 0 0 1],2)   % value at s = 2: 17
roots([1 3 -15 -2 9])        % -5.5745, 2.5836, -0.7951, 0.7860
x = [1 2];
y = [1 4 8];
z = conv(x,y)                % product: 1 6 16 16
[xx, R] = deconv(z,y)        % division: xx = 1 2, remainder R = 0 0 0 0
```

## Tutorial 2: Functions and plotting

### Functions

MATLAB provides standard functions such as `sin`, `cos`, `log`, `exp`, `sqrt` and the constants `pi`, `i`, `j`; `sin(pi/4)` gives 0.7071. Commands such as `roots`, `plot`, `step` are in fact m-files that have inputs and outputs. You write your own function in a file with the `.m` extension using `function`; the first line has the following form:

```matlab
function [output1,output2] = filename(input1,input2,input3)
```

The following lines starting with `%` form the description displayed by `help filename`. To check the number of inputs, the line `error(nargchk(x,y,nargin));` is recommended. A simple example, `add.m`:

```matlab
function [var3] = add(var1,var2)
%add is a function that adds two numbers
var3 = var1+var2;
```

It is used at the command line as `y = add(3,8)`.

### Plotting

`plot(x,y)` plots the vector x on the horizontal axis and the vector y on the vertical axis; x and y must have the same length. If a single vector is given, its elements are plotted against their indices; for complex numbers, the real part is placed on the horizontal axis and the imaginary part on the vertical axis.

```matlab
t=0:0.25:7;
y = sin(t);
plot(t,y)

x = 0:0.1:100;
y = 3*x;
plot(x,y,'r:')    % red, dotted line
```

The third parameter specifies the color and marker:

| Color | Marker | Line |
|---|---|---|
| y yellow, m magenta, c cyan, r red | . point, o circle, x cross, + plus, * star | - solid |
| g green, b blue, w white, k black | s square, d diamond, v ^ < > triangles | : dotted, -. dash-dot |
| | p pentagram, h hexagram | -- dashed |

Multiple curves on the same axes:

```matlab
x = linspace(0,2*pi,50);
y = sin(x);
z = cos(x);
plot(x,y,'r', x,z,'gx')

% or using hold on / hold off:
plot(x,y,'r')
hold on
plot(x,z,'gx')
hold off
```

### subplot

`subplot(m,n,p)` divides the figure into an m-row by n-column grid and makes the p-th plot active; the ordering is like reading a book, left to right, top to bottom.

```matlab
x = linspace(0,2*pi,50);
y = sin(x);
z = cos(x);
w = tan(x);

subplot(2,2,1)
plot(x,y)
subplot(2,2,2)
plot(x,z)
subplot(2,2,3)
plot(x,w)
```

Every subsequent `plot` command draws over the most recently used subplot; to prevent this, use `clf` or `figure`.

### Axes and text

`axis([xmin, xmax, ymin, ymax])` changes the displayed axis range. For example, since the graph of y = e^(5t) − 1 reaches the order of 8·10¹⁰ over the 0–5 s interval, it is more meaningful to look at the first second:

```matlab
t=0:0.01:5;
y=exp(5*t)-1;
plot(t,y)
axis([0, 1, 0, 50])
title('exponential function')
xlabel('time (sec)')
ylabel('output')
gtext('unnecessary labeling')   % places text where you click with the mouse
```

`text(xcor,ycor,'textstring')` places the text at the given coordinates. Other useful commands: `clf`, `figure`, `close`, `loglog`, `semilogx`, `semilogy`, `grid`.
