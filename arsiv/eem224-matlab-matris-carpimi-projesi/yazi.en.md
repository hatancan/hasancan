---
baslik: EEM224 Electromagnetics I: MATLAB Project: Matrix Multiplication Time
ozet: Annotated archive record of MATLAB source code; code and downloadable file.
---

The MATLAB project assignment in the course archive measures elapsed time with tic/toc by repeatedly multiplying identity matrices of different sizes. A copy of the code with the student's name removed can be downloaded below. No verifiable date appears in the document.

## Source code

```matlab
%% Meta Bilgileri %%
%Yazarlar :
% Öğrenci adı çıkarıldı.
%Version : sürüm 1
 
%Not: Grafikleri bilgisayarınızda tam ekran yaparak incelemiz tavsiye
%edilir.
clear all;
clc;
 
%% Parametreler 1%%
deltaN = input ('Adim araligini giriniz:');
MAXN   = input ('Maksimum matris degeriniz giriniz:');
KERE   = input ('Kac carpim yapilacagini giriniz:');

%% Parametreler 2%%
t = zeros(0,MAXN);

%% İşlemleri uygula 2%%
for i = deltaN:deltaN:MAXN
    A = eye(i,i);
    tic;
    for j = 1:KERE
        A = A*A;
    end
    t(i) = toc;
end

%% Grafiği Çiz %%
plot(t)
title('Geçen Zaman - Matris Boyut')
xlabel('Matris Boyut')
ylabel('Gecen Zaman')
```

*Note: t=zeros(0,MAXN) creates an empty array; the array grows in the loop, and skipped indices may appear as zeros in the plot. The deltaN, MAXN and KERE inputs are not validated. The code was not run during archiving; results depend on the hardware and MATLAB version.*
