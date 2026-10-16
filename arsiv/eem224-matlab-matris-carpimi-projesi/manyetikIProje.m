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
