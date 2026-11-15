---
baslik: BIL437 Computer Vision: MATLAB Introduction Handout, Color Image and FFT-Noise Labs, Programming Assignment 1
ozet: The MATLAB introduction handout, color image processing and frequency-domain filtering/noise lab code, programming assignment with image reduction and logarithmic/power-law transformation, and a plus-sign detection code for the BIL437 Computer Vision course.
---

Practical materials used in the 2015 summer school course **BIL437 Computer Vision** (shared content with "BİL421 Image Processing", according to the title of the lab handouts): a MATLAB introduction handout, two lab handouts, a programming assignment, and a small piece of code I wrote. The original files can be downloaded as a ZIP at the end of the post. The lab handouts and the assignment are the course instructor's material; the author of the MATLAB introduction handout is not stated (it appears to be based on Kermit Sigmon's "MATLAB Primer").

## MATLAB introduction handout (437L1.pdf, 8 pages)

The handout introduces MATLAB under 18 headings:

1. Accessing MATLAB.
2. Entering matrices: `A = [1 2 3; 4 5 6; 7 8 9]`, complex numbers (`1+5i`), `rand(n)`, `magic(n)`; `A(2,3)` is the element in the second row, third column.
3. Matrix and array (element-by-element) operations: `+ - * ^ ' \ /`; with a dot, `.*` and `.^` operate element by element (`[1,2,3,4].^2` → `[1,4,9,16]`). `x = A\b` is the solution of Ax = b.
4. Expressions, variables, saving a session (`who`, `whos`, `clear`, `save`, `load`, `eps`).
5. Functions that generate matrices: `eye, zeros, ones, diag, triu, tril, rand, hilb, magic, toeplitz`.
6. `for`, `while`, `if` and relational/logical operators (`<, >, <=, >=, ==, ~=, &, |, ~`).
7. Scalar functions (`sin, cos, exp, log, abs, round, floor, ceil, rem, sign, sqrt`).
8. Vector functions (`max, min, sort, sum, prod, mean, median, std, any, all`) operate column by column; the largest element of a matrix is `max(max(A))`.
9. Matrix functions (`eig, chol, svd, inv, lu, qr, det, rank, norm, cond, expm` …).
10. Command line editing and recall (arrow keys).
11. Submatrices and colon notation: `1:5`, `0.2:0.2:1.2`, `A(:,3)`, `A(1:4,:)`, `A(:,[2 4]) = …`.
12. M-files and function files; example:

```matlab
function a = randint(m,n,a,b)
%RANDINT Randomly generated integral matrix.
if nargin < 3, a = 0 ; b = 9 ; end
a = floor((b-a+1)*rand(m,n)) + a;
```

13. Text strings, `disp`, `error`, `input`.
16. Output format: `format short`, `format long`, `format rat` …
18. Graphics: `plot`, `plot3`, `mesh`, `surf`; title/axis commands (`title`, `xlabel`, `ylabel`, `axis`), `hold on`, line types, marker types, and color codes (`plot(x,y,'r--')`).

## Lab 1: color image processing (lab_color.pdf)

It consists of six exercises on the `peppers.png` image:

1. **RGB – HSV**: display the H (hue), S (saturation), and V (value/intensity) components using `hsv2rgb`/`rgb2hsv`.
2. **Conversion to gray level**: compare `rgb2gray` with the average `(R+G+B)/3`; the weighted formula is `0.2989*R + 0.5870*G + 0.1140*B`.
3. **RGB – CMY**: `C = 255 − R`, `M = 255 − G`, `Y = 255 − B` (cyan = white − red).
4. **RGB histogram equalization**: each band is equalized separately with `histeq`.
5. **Brightness increase**: 128 is added to each band. The handout includes the warning "Apply to each band (R,G,B) separately!"
6. **RGB filtering**: `imfilter(I,H,'replicate')` with `fspecial('average',7)`, and `medfilt2(…,[7 7])` on each band.

## Lab 2: frequency-domain filtering and noise (lab_fft_noise.pdf)

```matlab
I = imread('eight.tif');
fI = fft2(I);
fS = fftshift(fI);            % shifts the spectrum to the center of the image
H  = fspecial('average',9);
fH = fft2(H, x, y);           % FFT of the filter (zero-padded to the image size)
NI = ifft2(fI .* fH);         % multiplication in the frequency domain = spatial convolution
```

It shows that the same result is obtained with `imfilter(I,H)` (2-D convolution). The second part is noise generation: `imnoise(I,'salt & pepper',0.02)` (density 0.02) and `imnoise(I,'gaussian',0,0.01)` (mean 0, variance 0.01).

## Programming Assignment 1 (due: July 22, 2015, demonstration in the lab)

**Problem 1: image reduction by pixel decimation.** A MATLAB program will be written that shrinks an image by an integer reduction factor X provided by the user; Figure 2.20(a) will be used, and the results will be written to separate files in the original format with `imwrite`.

**Problem 2: enhancement with intensity transformations.** For Figure 3.8(a), (a) s = c·log(1 + r) and (b) s = c·r^γ transformations will be applied. In (a) there is a single parameter c, and in (b) there are c and γ; the aim is to find the best visual enhancement obtainable with each transformation by experimentation, and to explain the reason for the different results between the two (the explanation can be written as a comment in the program).

Notes: only .m source files are submitted; no MATLAB library functions are to be used other than for image reading/writing and input/output; adequate comments and meaningful variable names are expected in the code.

## Plus-sign detection (arti-isareti-bulma.m)

A short piece of code that finds "+"-shaped pixels (the center and its four neighbors equal to 1) in a binary image:

```matlab
function islem1 = islem1(image)
[x,y]=size(image);
image2=zeros(x,y);
for m=1:x-2
    for n=1:y-2
        if image(m+1,n+1)==1 && image(m,n+1)==1 && image(m+1,n)==1 && image(m+1,n+2) && image(m+2,n+1)==1
            image2(m+1,n+1)=1;
        end
    end
end
islem1=image2;
end
```

*Note: The `==1` is missing from the `image(m+1,n+2)` comparison; since the condition is treated as true when the numeric value is nonzero, the result does not change for a binary image.*
