---
baslik: EEM224 Elektromanyetik I: Tanyer: MATLAB ile yönlülük çizgesi
ozet: MATLAB kaynak kodunun açıklamalı arşiv kaydı; kod ve indirilebilir dosya.
---

Dr. S. Gökhan Tanyer’in 23 Şubat 2013 tarihli Polar03SS.m örneği. Kaynak başlığında EEM423 yazıyor; EEM224 klasöründeki bir ek olarak arşivlendi. θ ve φ taramalarıyla sinθ ve sin²θ yüzeyleri oluşturuluyor. Kod ve indirilebilir kaynak aşağıda.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Kaynak kod

```matlab
%%   Polarxx.m
%   EEM423 Dersi icin hazırlanmıştır. 
%   Polar (THETA, RHO) komutu kullanilarak yönlülük çizgesi gösterilmiştir.
%   Dr. S. Gokhun Tanyer
%   23.02.13
%% YAZILIMIN TARİHÇESİ
%
%Polar02    130223  SS  Odev olarak verilecek surumdur.
%Polar01    130223  OK  polar plot tamam. 2B henuz yok.
%                   --  İlk calisma.
%%  GIRIS - Ekran
    clear;          %Hafizayı sil.
    figure(1), clf, hold off;
%%  GIRIS - Veri hazirlama
    Theta   = [0 : 0.01 : pi/2];
    Phi     = [0 : 0.01 : 2 * pi];
       
    lenTH   = length(Theta);
    lenPH   = length(Phi); 
        
    Th = zeros (lenTH, lenPH);
    Ph = zeros (lenTH, lenPH);
    R1 = zeros (lenTH, lenPH);
    R2 = zeros (lenTH, lenPH);
    
    for iTh = 1:lenTH
        
        for iPh = 1:lenPH
            
            Th(iTh, iPh)  = Theta (iTh);
            Ph(iTh, iPh)  = Phi (iPh);
            
            R1(iTh, iPh)  = sin (Th(iTh, iPh)) ;
            R2(iTh, iPh)  = sin (Th(iTh, iPh))^2 ;
           
            x2(iTh, iPh)   = R2(iTh, iPh) * sin(Th(iTh, iPh)) * cos(Ph(iTh, iPh));
            y2(iTh, iPh)   = R1(iTh, iPh) * sin(Th(iTh, iPh)) * sin(Ph(iTh, iPh));
            z2(iTh, iPh)   = R1(iTh, iPh) * cos(Th(iTh, iPh)) ;  
        end
    end
    
    surfl (x2, y2,  z2);   hold on; surfl (x2, y2, -z2); 
   
    shading('interp'); colormap('hot'); 
    axis('equal');axis([-1 1 -1 1 -0.6 0.6]);
   

    
    
    
    

    
    
    
%%  SON SON SON SON SON SON SON SON SON SON SON SON SON SON SON SON SON SON
```

*Not: x2 hesabı R2, y2 ve z2 hesapları R1 kullanıyor. Bu nedenle üç eksene aynı radyal fonksiyon uygulanmış bir yüzey değildir; kaynak kod aynen korunmuştur.*
