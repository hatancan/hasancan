---
baslik: BIL437 Computer Vision: Introduction to Digital Image Processing, Image Fundamentals, Histograms and Point Processing
ozet: The first four lectures of the BIL437 Computer Vision course: what a digital image is, the human visual system, sampling and quantisation, histogram equalisation, logarithmic and power-law (gamma) transformations.
---

This post is a set of course-note summaries of the first four lectures (Lecture 1_1 – 1_4) of **BIL437 Computer Vision**, which I took in the 2015 summer school at Başkent University. Although the folder name is "Computer Security", the lecture slides are titled "Bil-437 Computer Vision" and the lab handouts are titled "Image Processing"; the content is digital image processing. The slides cite Gonzalez & Woods, *Digital Image Processing* (2002), as the source of the images; the slides do not name an author, but the PDF document properties list the author as **Brian Mac Namee**. The originals of the four lectures can be downloaded as a ZIP at the end of this post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution. It will be removed at the request of the rights holder.*

## 1. Introduction: digital images and image processing

The course opens with the saying "a picture is worth ten thousand words".

- A **digital image** is the representation of a two-dimensional image by a finite number of numerical values (pixels). Pixel values can represent things such as gray level, colour, height, or opacity. Digitisation means that the image is an approximation of the real scene.
- Common formats: 1 sample per point (black-and-white or gray), 3 samples (R, G, B), 4 samples (R, G, B and alpha/opacity). The course mostly uses grayscale images.
- The two main tasks of image processing: improving image information for human interpretation; and processing image data for storage, transmission and machine perception.
- Processing levels: **low-level** (input image, output image; noise removal, sharpening), **mid-level** (input image, output features; object segmentation and recognition), **high-level** (input features, output understanding; scene understanding, autonomous navigation).

### A brief history

- 1920s: Bartlane cable picture transmission in the newspaper industry; images are coded and sent over the London–New York submarine cable, and reconstructed at the receiver with a telegraph printer. Later improvements raise the number of tones to 15.
- 1960s: the space race and computers; in 1964, computer enhancement of Ranger 7 images of the Moon.
- 1970s: use in medicine; in 1979, Hounsfield and Cormack share the Nobel Prize in Medicine for the invention of computed tomography (CAT).
- 1980s to today: image enhancement/restoration, artistic effects, medical visualisation, industrial inspection, forensics, human-computer interfaces.

Application examples in the lecture: correcting images from the Hubble telescope's flawed mirror, edge detection in an MRI slice of a dog's heart, satellite images and GIS (a map of night-time lights), printed circuit board (PCB) inspection, licence plate and fingerprint recognition, face and gesture recognition.

### Key stages in digital image processing

Image acquisition, image enhancement, image restoration, morphological processing, segmentation, object recognition, representation and description, image compression and colour image processing; all are organised around a "knowledge base" (the problem domain).

## 2. Digital image fundamentals

### The human visual system

- The lens focuses light onto the retina. The retina contains roughly 6–7 million **cones** (sensitive to colour, concentrated around the fovea) and 75–150 million **rods** (sensitive to low light, more widely distributed).
- Blind spot experiment: draw a dot and a cross 6 inches apart on a sheet of paper; close the right eye and look at the cross with the left eye while slowly moving the paper toward the face, and the dot disappears.
- The eye can perceive roughly 10^10 different light intensities, but the number of levels it can distinguish at the same time is much smaller (brightness adaptation). Perceived intensity also depends on the surrounding regions (Mach bands, optical illusions).

### Light and the electromagnetic spectrum

Light is the narrow part of the electromagnetic spectrum that the eye can perceive. The colour we perceive depends on the nature of the light reflected from an object: when white light falls on a green object, most wavelengths are absorbed and green is reflected.

### Image representation and acquisition

- An image is an array of pixels with M rows and N columns; gray levels are usually in the range 0 (black) – 255 (white), and the image is treated as a matrix f(row, column).
- An image is formed when a scene is illuminated and the energy reflected from objects is absorbed (X-ray, ultrasound and electron microscopy follow the same principle). The incoming energy produces a voltage in the sensor material; sensors are arranged as a single sensor, a strip (line) or an array (matrix).

### Sampling, quantisation and resolution

- **Sampling**: measurement at a finite number of points in space; **quantisation**: rounding continuous amplitude values to a finite number of levels.
- **Spatial resolution**: the smallest discernible detail in an image (pixel size, DPI in printing).
- **Intensity level resolution**: the number of levels is 2^k; 1 bit = 2, 4 bits = 16, 8 bits = 256, 16 bits = 65,536 levels. As the number of levels decreases (256 → 128 → 64 → 32 → 16 → 8 → 4 → 2), false contours appear.
- The answer to "how much resolution is enough?" depends on what one wants to see in the image: an image that is adequate for counting vehicles may not be enough for reading licence plates.

## 3. Image enhancement: histogram processing

Image enhancement means making an image more useful: emphasising detail, removing noise, making it look more pleasing. The techniques fall into two groups:

- **Spatial domain** techniques: operating directly on pixels,
- **Frequency domain** techniques: operating on the Fourier or wavelet transform.

In this course, gray levels are taken in the range [0, 1] for most operations (0 is black, 1 is white).

A **histogram** shows the distribution of gray levels in an image and is especially useful in segmentation. The histogram of a dark image is concentrated on the left, that of a bright image on the right; the histogram of a high-contrast image is the most evenly spread.

**Histogram equalisation** corrects dark or washed-out images by spreading out the frequencies:

- s_k = T(r_k) = Σ (j = 1..k) p_r(r_j) = Σ (j = 1..k) n_j / n
- r_k: input intensity, s_k: processed intensity, n_j: frequency of intensity j, n: total number of pixels.

## 4. Point processing and gray-level transformations

If the value of the output pixel depends only on the input pixel at the same location, it is written as s = T(r).

- **Thresholding**: s = 0.0 if r ≤ threshold; s = 1.0 if r > threshold.
- **Negative/identity** (linear), **logarithmic** and **power-law** (exponential) transformations are the three most common groups.
- **Logarithmic transformation**: s = c · log(1 + r). It expands a narrow range of low gray levels into a wide output range; it is useful for inputs with a very wide range of values (for example, making the Fourier spectrum of an image visible). The inverse log transformation does the opposite. Usually c = 1 is taken.
- **Power law (gamma)**: s = c · r^γ. γ < 1 expands the dark input range (in the example, an MRI image of a fractured spine with γ = 0.6, 0.4, 0.3), while γ > 1 darkens the image (an aerial photograph of a runway with γ = 3.0, 4.0, 5.0). Since monitors respond non-linearly, **gamma correction** is performed with this transformation.
- **Piecewise linear transformations**: contrast stretching with user-defined curves.
- **Gray-level slicing**: a particular gray range is highlighted, while other levels are suppressed or preserved.

The next topics are neighbourhood operations, filtering and convolution; see the second post in the series.
