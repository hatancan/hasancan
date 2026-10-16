---
baslik: EEM224 Elektromanyetik I: MATLAB projesi: Matris çarpım süresi
ozet: MATLAB kaynak kodunun açıklamalı arşiv kaydı; kod ve indirilebilir dosya.
---

Ders arşivindeki MATLAB proje çalışması, farklı boyutlardaki birim matrisleri tekrar tekrar çarparak tic/toc ile süre ölçüyor. Öğrenci adı çıkarılmış kod kopyası aşağıda indirilebilir. Belge içinde doğrulanabilir tarih bulunmuyor.

## Kaynak kod

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

*Not: t=zeros(0,MAXN) boş bir dizi oluşturur; döngüde dizi büyür ve atlanan indeksler grafikte sıfır görünebilir. deltaN, MAXN ve KERE girdileri doğrulanmıyor. Kod arşivleme sırasında çalıştırılmadı; sonuçlar donanım ve MATLAB sürümüne bağlıdır.*
