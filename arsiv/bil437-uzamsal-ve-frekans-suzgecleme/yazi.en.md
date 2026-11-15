---
baslik: BIL437 Computer Vision: Spatial Filtering, Sharpening (Laplacian, Sobel) and Frequency-Domain Filtering
ozet: Week 2 and 3 lectures of the BIL437 Computer Vision course: neighbourhood operations, mean and median filters, the border problem, correlation and convolution, Laplacian and Sobel, the discrete Fourier transform, ideal/Butterworth/Gaussian low-pass and high-pass filters.
---

These are lecture-note summaries of the Lecture 2_1, 2_2 and 3_1 presentations of the BIL437 Computer Vision course (Başkent University, summer 2015). The images in the presentations are taken from Gonzalez & Woods, *Digital Image Processing*; the slides do not name an author, but the author is recorded as **Brian Mac Namee** in the PDF document properties. The original presentations can be downloaded as a ZIP at the end of the post. Previous post: introduction and histogram/point processing.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed at the request of the rights holder.*

## Spatial filtering 1: neighbourhood operations and smoothing

Unlike point operations, **neighbourhood operations** use a rectangular neighbourhood around the centre pixel. Simple examples:

- **Min**: the pixel is set to the smallest value in the neighbourhood,
- **Max**: set to the largest value,
- **Median**: the middle value after the neighbourhood values are sorted (for example, the median of the set [1, 7, 15, 18, 24] is 15). It sometimes gives better results than the mean.

### The filtering operation

A 3×3 filter mask (w) is moved over the image; at each position the products of the mask coefficients and the pixels beneath them are summed, and the result is written to the centre pixel:

g(x, y) = Σ_s Σ_t w(s, t) · f(x + s, y + t)  (s = −a..a, t = −b..b)

**Mean (smoothing) filter**: all coefficients of the 3×3 mask are 1/9; it removes noise and blurs detail. In the example, for the 3×3 neighbourhood with values (104 100 108 / 99 106 98 / 95 90 85), the centre pixel becomes 98.33. On a 500×500 image, as the filter size is increased to 3, 5, 9, 15, 35, detail is gradually lost. In the **weighted mean** filter, pixels closer to the centre are more important: 1/16 × [1 2 1; 2 4 2; 1 2 1].

On noisy images (such as salt-and-pepper noise), the **median filter** often gives better results than the mean filter.

### What happens at the borders?

Pixels at the image border have incomplete neighbourhoods. Solutions: skipping the missing pixels (possible only with some filters), **padding** the image entirely with black or white pixels (**zero padding**), or **copying** the border pixels (**replicate**).

### Correlation and convolution

The operation described so far is **correlation**. In **convolution**, the filter mask is used rotated by 180° (flipped). For symmetric filters, both give the same result.

## Spatial filtering 2: sharpening

Sharpening filters emphasise fine detail and edges and reduce blurring; they are based on taking spatial **derivatives**.

- 1st derivative: ∂f/∂x = f(x + 1) − f(x) (the difference between consecutive values).
- 2nd derivative: ∂²f/∂x² = f(x + 1) + f(x − 1) − 2f(x).

For an example signal (5 5 4 3 2 1 0 0 0 6 0 0 0 0 1 3 1 0 0 0 0 7 7 7 7), the 1st derivative is 0 −1 −1 −1 −1 0 0 6 −6 0 0 0 1 2 −2 −1 0 0 0 7 0 0 0. The 2nd derivative is more useful for image enhancement: it responds more strongly to fine detail and is simpler to implement.

### Laplacian filter

∇²f = [f(x+1, y) + f(x−1, y) + f(x, y+1) + f(x, y−1)] − 4f(x, y)

The corresponding mask is: 0 1 0 / 1 −4 1 / 0 1 0 (it is isotropic). The Laplacian result alone is not an enhanced image; the sharpened image is obtained with g(x, y) = f(x, y) − ∇²f. When the two are combined in a single mask: 0 −1 0 / −1 5 −1 / 0 −1 0. A Laplacian variant that also includes the diagonals is 1 1 1 / 1 −8 1 / 1 1 1; its single-step sharpening counterpart is −1 −1 −1 / −1 9 −1 / −1 −1 −1.

### 1st derivative: gradient and Sobel

The gradient magnitude is approximated as |∇f| ≈ |Gx| + |Gy|. The **Sobel** operators are: for Gy, −1 −2 −1 / 0 0 0 / 1 2 1, and for Gx, −1 0 1 / −2 0 2 / −1 0 1. The image is filtered separately with the two operators and the results are summed. Sobel is mostly used for edge detection (example: making defects visible in a contact lens image).

**Comparison of 1st and 2nd derivatives**: the 1st derivative gives thicker edges and responds more strongly to a grey-level step; the 2nd derivative responds more strongly to fine detail such as thin lines, but produces a double response at step changes.

### Combining methods

Successful enhancement is not achieved with a single operation. In the bone scan example in the presentation, the following are applied in sequence: Laplacian filter → sharpening by subtracting the Laplacian → Sobel filter → smoothing the Sobel result with a 5×5 mean → forming a mask by multiplying the Laplacian-sharpened image by the smoothed Sobel → adding the mask to the sharpened image → finally, a power-law transformation is applied.

## Filtering in the frequency domain

### Fourier and the discrete Fourier transform

Jean Baptiste Joseph Fourier (born 1768, Auxerre) is known for his work *La Théorie Analytique de la Chaleur*. The basic idea: any function that repeats itself periodically can be written as a weighted sum of sines and cosines of different frequencies (a Fourier series).

The **discrete Fourier transform (DFT)** of an M×N image f(x, y):

F(u, v) = Σ_x Σ_y f(x, y) · e^(−j2π(ux/M + vy/N))

and the inverse transform f(x, y) = (1/MN) Σ_u Σ_v F(u, v) · e^(j2π(ux/M + vy/N)). The transform is fully invertible. The image spectrum (frequency components) can be visualised; the example shows an electron microscope image of an integrated circuit and its spectrum.

### Steps of filtering in the frequency domain

1. Compute the DFT F(u, v) of the image.
2. Multiply F(u, v) by the filter function H(u, v): G(u, v) = H(u, v) F(u, v).
3. Take the inverse DFT of the result.

### Smoothing (low-pass) filters

Smoothing is achieved by discarding high frequencies. Let D(u, v) = [(u − M/2)² + (v − N/2)²]^(1/2) be the distance from the centre and D0 the cut-off distance:

- **Ideal low-pass**: H = 1 if D ≤ D0, otherwise 0. In examples with radii D0 = 5, 15, 30, 80, 230, the image becomes very blurred at small radii and ring-shaped oscillations (ringing) appear.
- **Butterworth**: H(u, v) = 1 / (1 + [D(u, v)/D0]^(2n)) (n: order). With a 2nd-order Butterworth, ringing is much reduced.
- **Gaussian**: H(u, v) = e^(−D²(u, v) / 2D0²). There is no ringing. The Gaussian low-pass filter is also used to join broken text characters.

### Sharpening (high-pass) filters

A high-pass filter is the opposite of a low-pass filter: H_hp(u, v) = 1 − H_lp(u, v).

- **Ideal**: 0 if D ≤ D0, 1 if D > D0.
- **Butterworth**: H = 1 / (1 + [D0/D(u, v)]^(2n)).
- **Gaussian**: H = 1 − e^(−D²(u, v) / 2D0²).

Results are compared for D0 = 15, 30, 80; an example of high-frequency emphasis followed by histogram equalisation is also given, and the **Laplacian in the frequency domain** is shown (compared with the 2-D image of the spatial Laplacian mask).

### Fast Fourier transform (FFT) and spatial vs. frequency comparison

The reason Fourier-based methods became widespread is the **FFT** algorithm, which reduces the transform time by a factor of 100–600. Similar tasks can be done in both the spatial and frequency domains: spatial filtering is easier to understand, while filtering in the frequency domain is much faster, especially for large images.
