---
baslik: BIL437 Computer Vision: Noise Removal, Color Image Processing, Morphological Processing, and Segmentation
ozet: Week 4 and 5 lectures of BIL437 Computer Vision: noise models and filters (mean, median, order-statistic), band-reject filter, color models (RGB, HSI), erosion, dilation, edge detection, and thresholding.
---

This is a summary of the lecture notes from the BIL437 Computer Vision lectures Lecture 4_1, 4_2, 5_1, 5_2, and 5_3 (dated 2012, distributed at Başkent University in the 2015 summer school). The images in the lectures are taken from Gonzalez & Woods, *Digital Image Processing*; the slides do not name an author, but the PDF document properties list the author as **Brian Mac Namee**. The original lectures can be downloaded as a ZIP at the end of the post.

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed at the request of the rights holder.*

## Image restoration: noise removal (Lecture 4_1)

**Image restoration** tries to correct a degraded image: determining the degradation process and reversing it; it is similar to enhancement but more objective.

Noise arises during image acquisition (sensors being affected by environmental conditions) and transmission. A noisy image is modeled as:

g(x, y) = f(x, y) + η(x, y)

(f: original pixel, η: noise term, g: degraded pixel). Noise models: **Gaussian** (the most common), Rayleigh, Erlang, exponential, uniform, and **impulse (salt-and-pepper)** noise.

### Noise removal with spatial filters

- **Arithmetic mean**: f̂(x, y) = (1/mn) Σ g(s, t); simple smoothing, blurs the image.
- **Geometric mean**: smoothing similar to the arithmetic mean, but loses less detail.
- **Harmonic mean**: f̂ = mn / Σ (1/g(s, t)); works well for salt noise, fails for pepper noise; it also works well for Gaussian noise.
- **Contraharmonic mean**: f̂ = Σ g^(Q+1) / Σ g^Q; Q is the order of the filter. Q > 0 removes pepper noise, Q < 0 removes salt noise (in the example Q = 1.5 and Q = −1.5). If Q is chosen incorrectly, the result can be catastrophic.
- **Order-statistic filters**: based on ordering the pixel values in the neighborhood.
  - **Median**: removes noise very well without a smoothing effect; particularly good for salt-and-pepper noise (improves further with several passes).
  - The **max filter** works well for pepper noise, the **min filter** for salt noise.
  - **Midpoint**: (max + min) / 2; works well for Gaussian and uniform noise.
  - **Alpha-trimmed mean**: the lowest d/2 and highest d/2 intensity levels are discarded and the remaining mn − d pixels are averaged.

A numerical example is also given: in a 7×5 patch, corrupted pixels with values 204 and 0 (salt and pepper) are removed with the filters.

### Periodic noise and band-reject filters

**Periodic noise**, caused by electrical or electromagnetic interference and producing regular patterns in the image, is best removed in the Fourier domain: a specific frequency range is removed with a **band-reject filter**. The ideal band-reject filter is 1 for D(u, v) < D0 − W/2 and D(u, v) > D0 + W/2, and 0 in the ring of width W in between. Butterworth (order 1) and Gaussian versions also exist; an example is shown on an image with sinusoidal noise and its Fourier spectrum.

### Adaptive filters

The behavior of adaptive filters changes according to image characteristics within the filter window. On an image with salt-and-pepper probabilities Pa = Pb = 0.25, a 7×7 median filter is compared with an adaptive median filter.

Summary: Restoration is more objective than enhancement; spatial techniques are more effective for random noise, and frequency-domain techniques for periodic noise.

## Color image processing (Lecture 4_2)

- In 1666, Isaac Newton discovered that sunlight passed through a glass prism splits into a spectrum of colors.
- The color we perceive in an object depends on the nature of the reflected light (a green object reflects the 500–570 nm range and absorbs the rest). Chromatic light covers roughly the 400–700 nm range; 6–7 million cones in the human eye enable color vision.
- Three quantities describe chromatic light: **radiance**: the total energy emitted from the source (watts); **luminance**: the energy perceived by an observer (lumens), where radiance can be high but luminance low; **brightness**: a subjective, unmeasurable notion of intensity.
- **CIE chromaticity diagram**: the x axis shows the proportion of red, the y axis the proportion of green; the proportion of blue is z = 1 − (x + y). Colors on the boundary are fully saturated; the equal-energy point is pure white in the CIE standard. The whole color range cannot be represented by combining three colors; the color gamuts of RGB monitors and high-quality printers appear in the diagram as different triangles/shapes.

### Color models

- **RGB**: the red, green, and blue components are represented as a cube in a Cartesian coordinate system; black is at the origin, white at the corner farthest from the origin, and cyan-magenta-yellow at the other three corners. A color image consists of three component images; the number of bits per pixel is the color depth. A 24-bit image gives 2^24 = 16,777,216 colors (full color).
- **HSI**: hue, saturation, intensity. RGB is suitable for hardware implementation, but humans naturally describe colors by hue, saturation, and brightness: RGB is suited to color generation, HSI to color description.

## Morphological image processing (Lecture 5_1)

After segmentation is complete, morphological operations are used to remove imperfections in the segmentation and to extract information about the shape/structure of the image. The discussion is for bi-level (binary) images in which object pixels are 1 and background pixels are 0.

- The **structuring element** can be of any size and shape (in the lecture, for convenience, rectangular/cross shapes with the origin at the center).
- **Fit**: all "on" pixels in the structuring element fall on on-pixels in the image. **Hit**: any on-pixel in the structuring element coincides with an on-pixel in the image.
- **Erosion**: f ⊖ s; for the structuring element, g(x, y) is "1 if s fits f, 0 otherwise". It separates connected objects and removes protrusions, but shrinks objects. Examples are given with 3×3 and 5×5 square elements and discs (radius 5, 10, 20).
- **Dilation**: f ⊕ s; "1 if s hits f". It repairs gaps and indentations and enlarges objects.
- The lecture then moves on to operations composed of these (opening, closing, etc.) and to morphological algorithms.

## Segmentation 1: discontinuities, points, lines, edges (Lecture 5_2)

**Segmentation** divides the pixels of an image into groups strongly related to objects; it is usually the first step of automated computer vision applications. Three types of gray-level discontinuities are sought: **points, lines, edges**; they are found with masks and correlation.

- **Point detection**: a single mask is applied, and pixels exceeding a threshold in the filtered image are considered points (example on an X-ray of a turbine blade).
- **Line detection**: done with masks that extract lines one pixel thick and in a specific direction (horizontal, vertical, +45°, −45°) (wire-bond example).
- **Edge**: a connected set of pixels lying on the boundary between two regions. The 1st derivative shows the location of the edge, the 2nd derivative the direction of the edge. Derivative-based edge detectors are very sensitive to noise; therefore it is useful to smooth the image before edge detection. Common 3×3 edge detectors (for a 3×3 region): the horizontal and vertical gradient components are combined.
- The **Laplacian** is not used alone because it is very sensitive to noise; the **Laplacian of Gaussian (LoG, "Mexican hat")** removes noise with a Gaussian and detects edges with the Laplacian.

## Segmentation 2: thresholding (Lecture 5_3)

Thresholding is the first step of most segmentation approaches. With a single threshold: g = 1 if f(x, y) > T, otherwise 0. If the threshold is chosen incorrectly (too low or too high), the result is poor. A robot playing poker interpreting the cards is given as an example.

**Basic global thresholding algorithm**:

1. Choose an initial estimate for T (usually the average gray level of the image).
2. Split the image into two groups using T: G1 (gray level > T) and G2 (≤ T).
3. Compute the average gray levels μ1 and μ2 of G1 and G2.
4. New threshold T = (μ1 + μ2) / 2.
5. Repeat steps 2–4 until the change in T is smaller than a predefined limit.

The algorithm works very well if the histogram is suitable (two-peaked, bimodal). Other histograms cannot be segmented with a single threshold; uneven illumination also breaks a single threshold (example of separating the contents of bottles). Remedy: **adaptive thresholding**: the image is divided into subimages and each is thresholded separately; problematic subimages are subdivided further to obtain a successful result.
