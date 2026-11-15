---
baslik: EEM401 Digital Signal Processing: 2014 Term Project (Gaussian Noise and Three Butterworth Filters) and MATLAB Solution
ozet: The topic of the EEM401 Digital Signal Processing term project of November 2014: adding Gaussian noise to a grayscale image and filtering it in the frequency domain with three Butterworth low-pass filters; a friend's MATLAB solution (personal information removed).
---

The term project topic of the **EEM401 Digital Signal Processing** course (Asst. Prof. Dr. Selda Güney), dated 21 November 2014, and the MATLAB code a friend of mine wrote for it. Name and student number information was removed from the comment lines in the code; the image file name was changed to `girdi.jpg`, and the personal photograph used in the project was not shared. The project topic PDF and the code can be downloaded as a ZIP at the end of the post.

## Project topic

"EEM401-Digital Signal Processing Course Project": The course project will be carried out using MATLAB; ready-made functions from the libraries may be used.

**Objective.** The student's own color image will be loaded into MATLAB and converted to black and white. Gaussian noise with

- a) a mean of 0,
- b) a standard deviation of 0.02·x

will be added to this image, where x is the last digit of the student number of the student carrying out the project.

The noisy image will be filtered with **three different Butterworth filters whose order and cutoff frequency are to be determined by the student**, and the results will be compared. Running the project will produce six output images: 1) the original image, 2) the black-and-white image, 3) the noisy image, 4) the output of the first filter, 5) the second filter, 6) the third filter.

**Submission.** The project will be sent by e-mail, with the .m file attached, no later than the date of the course's final exam (subject line "EEM401-Term Project"; the message should include the student's first name, last name, and number). No additional report will be submitted; if necessary, explanatory comments can be written in the source code.

## MATLAB solution

```matlab
clear all;
% program resmi okuyor
resimorg = imread('girdi.jpg');
% resim siyah-beyaz yapıldı
resimsiyahbeyaz = rgb2gray(resimorg);
resimgaus = imnoise(resimsiyahbeyaz,'gaussian',0,0.029);
% süzgeçler
cf = fftshift(fft2(resimgaus));
% butterworth 1
[x,y] = meshgrid(-128:127,-128:127);
bl1 = 1./(1+((x.^2+y.^2)/15).^5);
cfbl1 = cf.*bl1;
bt1 = ifft2(cfbl1);
bt1 = uint8(abs(bt1));
% butterworth 2
bl2 = 1./(1+((x.^2+y.^2)/15).^2);
bt2 = uint8(abs(ifft2(cf.*bl2)));
% butterworth 3
bl3 = 1./(1+((x.^2+y.^2)/15).^0.25);
bt3 = uint8(abs(ifft2(cf.*bl3)));
% çıktılar
figure;
subplot(2,3,1), imshow(resimorg), title('Orijinal Resim');
subplot(2,3,2), imshow(resimsiyahbeyaz), title('Siyah Beyaz Resim');
subplot(2,3,3), imshow(resimgaus), title('Gürültü Eklenmiş Resim');
subplot(2,3,4), imshow(bt1), title('Birinci Süzgeç Çıkışı Resim');
subplot(2,3,5), imshow(bt2), title('İkinci Süzgeç Çıkışı Resim');
subplot(2,3,6), imshow(bt3), title('Üçüncü Süzgeç Çıkışı Resim');
```

(The code has been reproduced from the original file with the repetitions in the three filter blocks shortened for readability; the file inside the ZIP is in its original form.)

## How does it work?

1. The image is converted to grayscale and zero-mean Gaussian noise is added with `imnoise`. The last parameter of `imnoise` is the *variance*; the project, however, defines the standard deviation as 0.02·x. The value 0.029 was used in the code.
2. The 2-D FFT is taken and the zero frequency is moved to the center with `fftshift`.
3. On a 256×256 grid, where the squared distance from the center is D² = x² + y², a Butterworth low-pass filter H = 1 / (1 + (D²/15)ⁿ) is built for three different values of n (5; 2; 0.25). As the order increases, the cutoff becomes sharper; for a small value such as 0.25, the filter is very gentle and suppresses less noise.
4. Each filter is multiplied element-wise with the shifted spectrum (multiplication in the frequency domain = convolution in the spatial domain), the result is returned to the image domain with the inverse FFT, and displayed with `uint8(abs(·))`.

Note: The meshgrid is fixed at 256×256; if the image has a different size, it must be resized.

For the 2016 version of this project (masking periodic noise in the FFT magnitude spectrum), see "Spectral Image Filtering Design Project".
