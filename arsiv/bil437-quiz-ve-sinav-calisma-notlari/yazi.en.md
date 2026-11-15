---
baslik: BIL437 Computer Vision: Quiz 1 (Histogram and Transformation) and Handwritten Exam Study Notes
ozet: A transcription of the BIL437 Computer Vision 2015 summer school quiz (image matrix, histogram plotting, piecewise transformation function) and the handwritten list of question topics noted before the exam.
---

This post is a text transcription, from photographed pages, of a quiz from the **BIL437 Computer Vision** course I took in the 2015 summer school, together with the topic list I noted down to prepare for the exam. The photographs themselves have not been published.

## Quiz 1 (duration 15 minutes)

At the top of the exam paper it reads "BİL-437 Computer Vision – Quiz-1, duration: 15 minutes"; the date printed on the paper is 09.07.2014 (since the photograph is dated 7 July 2015, the year is most likely a typo).

**Question.** The image f(x, y) is given below (6 rows × 5 columns):

| 10 | 12 | 14 | 17 | 17 |
|---|---|---|---|---|
| 12 | 12 | 14 | 18 | 19 |
| 14 | 12 | 24 | 10 | 21 |
| 12 | 12 | 18 | 18 | 18 |
| 14 | 17 | 18 | 18 | 18 |
| 12 | 14 | 17 | 17 | 18 |

Accordingly:

1. Plot the histogram of the image f(x, y).
2. Compute the new pixel values of the image that results when the following transformation function T(x, y) is applied to f(x, y) (round fractional numbers up to the next integer).

The transformation function is given as a graph: the horizontal axis marks the old values (0, 10, 12, 14, 16, 18, 20, 24), and the vertical axis marks the new values (around 8, 11, 12, 13, 14, 16); it is a piecewise linear curve that increases up to 16, then stays constant until 20, drops sharply at 20, and then increases again. Because the graph was an unreadable screenshot in the photograph, the exact values of the curve could not be transcribed.

**Histogram (my calculation).** The counts of the gray levels in the image: 10 → 2 pixels, 12 → 7, 14 → 5, 17 → 5, 18 → 8, 19 → 1, 21 → 1, 24 → 1 (30 pixels in total). The handwritten note on the paper also seems to read "professor, in this question write the frequency of all pixels of f(x,y) for each of the values 10 through 12" (the handwriting is hard to read); that is, the histogram is expected to show the pixel count of each level.

The handwritten answer matrix on the paper (the new image with fractional values rounded up) is a 6×5 table whose first row is 8 9 11 13 13; the rows are: 8 9 11 13 13 / 9 9 11 14 14 / 11 9 18 8 16 / 9 9 14 14 14 / 11 13 14 14 14 / 9 11 13 13 14 (the reading of the handwriting is not entirely certain).

## Pre-exam study note (handwritten)

The list below is a handwritten short note of the question types I thought might appear on the exam (the same note appears in two photographs):

1. **Question 1**
   - a) Apply an RGB → CMY transformation and prepare a poster; compute HSI and I (color image processing).
   - b) Transition from the spatial domain to the frequency domain: the spatial-domain convolution formula for a 2nd-order filter, write out the processing steps.
2. An image and its histogram are given: plot the histogram; inverse brightness, darker/lighter transformations.
3. Intensity slicing (gray): an 8×8 matrix is given (half black, half white, plus a grid drawing); **apply an average filter**.
4. An image with salt-and-pepper noise is given; among six options, find which filter corresponds to which image.
5. (Item number drawn as 6) A graph of a piecewise T(r) function (with breaks around 80 and 100, including a linear portion); write the MATLAB code that performs this transformation.

All of these topics match the subjects covered in the course: color models, histograms and transformations, average/median filters. See the other posts in the series.
