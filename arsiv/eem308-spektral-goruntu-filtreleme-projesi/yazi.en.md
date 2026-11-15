---
baslik: EEM308 Signals and Systems II: Spectral Image Filtering Project (2016)
ozet: Proposal and report for a digital signal processing project from the signals archive: periodic noise reduction in MATLAB using a two-dimensional FFT, a logarithmic spectrum mask, and the inverse transform.
---

This post presents the 2016 spectral image filtering project proposal and the student report prepared for the **Digital Signal Processing** course at Başkent University, found in the **EEM308 Signals and Systems II archive**. The documents do not state the EEM308 course code; they are presented under the course in whose archive they were found. PDF copies, with the student name, the e-mail address containing the student number, and the photo samples removed, can be downloaded as a ZIP at the end of the post.

## Proposed project

The project calls for adding noise to a grayscale image in the form of a regularly repeating pattern at a particular frequency. From the FFT magnitude display of the image, the user will select a rectangular region with the mouse; the selected noise region will be removed from the spectrum, and the image will be recovered with the inverse FFT.

The goal is to prepare a MATLAB program that performs these operations. The success criterion is stated as removing the selected noise region and clearing the image of noise. The management plan section was left blank.

### Report, presentation, and schedule

- The report will be at least two pages and in a two-column format.
- The presentation will contain 15–20 slides; a total of 20 minutes is allotted, 15 minutes for the talk and 5 minutes for questions and answers.
- All group members will be present in the classroom during the presentation.
- Proposal submission: **November 11, 2016**.
- Report submission: **December 9, 2016**.
- Presentations: during class hours on **December 13–14**.
- Each group may propose one project; if the same topic is proposed more than once, the group that first submits a complete proposal form has priority.

## Method applied in the report

In the report, the image is converted to grayscale, normalized, and resized to **256 × 256**. The centered spectrum is obtained using the two-dimensional FFT and `fftshift`. For display:

fLog = log(1 + abs(f)).

The mask is built with two thresholds:

filter = (fLog > 0.7 max(fLog)) or (fLog < 0.43 max(fLog)).

In this mask the highest and lowest values are kept; spectrum values lying between the two thresholds are set to zero. The source says the aim is to preserve the bright central component and the low magnitudes. In the mask, black regions are zero and white regions are one.

*Note: The proposal asks for a rectangular selection with the mouse, whereas the code in the report uses automatic magnitude thresholds; interactive region selection is not present in this code.*

## MATLAB code

The report's code is presented here with the corrupted Turkish characters in the comments fixed:

```matlab
% Görüntüyü oku
I = imread('clown.jpg');
% Gri tona çevir ve normalize et
I = rgb2gray(I);
I = double(mat2gray(I));
I = imresize(I, [256 256]);
[rows,cols] = size(I);

% Merkezlenmiş Fourier dönüşümü
f = fftshift(fft2(I));
fLog = log(1 + abs(f));

% Genlik aralığına göre maskele
filter = (fLog > .7*max(fLog(:))) | (fLog < .43*max(fLog(:)));
B = abs(ifft2(f.*filter));

% Sonucun Fourier gösterimi
f1 = fftshift(fft2(B));
fLog1 = log(1 + abs(f1));

colormap(gray)
subplot(3,2,1), imagesc(I); title('Orijinal Görüntü')
subplot(3,2,2), imagesc(fLog); title('Fourier Görüntü')
subplot(3,2,3), imagesc(fLog); title('Fourier Görüntü')
subplot(3,2,4), imagesc(filter); title('Çıktı Maskesi')
subplot(3,2,5), imagesc(fLog1); title('Temizlenme Sonrası Fourier Görüntü')
subplot(3,2,6), imagesc(B); title('Temizlenmiş Görüntü')
annotation('textbox', [0 0.9 1 0.1], ...
    'String', 'FFT ile Görüntü Temizleme', ...
    'EdgeColor', 'none', ...
    'HorizontalAlignment', 'center', ...
    'FontSize', 15, ...
    'FontWeight', 'bold')
```

*Note: The source code uses the file name `clown.jpg`, but the example in the report output is an image of a ball. A separate input image file is not included in this source set.*

*Note: The code passes the `fftshift`-ed spectrum directly to `ifft2`. For a correct inverse transform of a centered spectrum, `ifftshift` should be applied first. In this 256 × 256 even-sized array, the sign pattern caused by the shift can be hidden by `abs`; this does not replace a properly performed reconstruction in general. The source line was not changed.*

## Discussion and conclusion

The report states that some noise components were removed, that the chosen mask preserves some DC components, and that the method is not the best filtering method for every image. The conclusion states that the image was cleared of noise; no error metric or numerical quality comparison is given.

*Note: Preserving the DC component is not an error in itself; it is related to the average brightness of the image. The "margin of error" comment in the report is the source's own wording.*

## References in the report

- Charles Van Loan, *Computational Frameworks for the Fast Fourier Transform*, SIAM, 1992.
- Heideman, Johnson, and Burrus, "Gauss and the history of the fast Fourier transform", IEEE ASSP Magazine, 1984; the 1985 article of the same title in Archive for History of Exact Sciences.
- Gilbert Strang, "Wavelets", American Scientist, 1994.
- Dongarra and Sullivan, "Guest Editors Introduction to the top 10 algorithms", Computing in Science & Engineering, 2000.
- Frank Yates, *The Design and Analysis of Factorial Experiments*, 1937.
