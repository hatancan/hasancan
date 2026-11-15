---
baslik: EEM224 Electromagnetics I: Tanyer: Directivity Plot with MATLAB
ozet: Annotated archive entry of a MATLAB source code; code and downloadable file.
---

Dr. S. Gökhan Tanyer's Polar03SS.m example dated 23 February 2013. The source header reads EEM423; it was archived as an addendum in the EEM224 folder. The sinθ and sin²θ surfaces are generated using θ and φ sweeps. The code and downloadable source are below.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed upon the request of the rights holder.*

## Source code

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

*Note: The x2 calculation uses R2, while the y2 and z2 calculations use R1. Therefore, this is not a surface with the same radial function applied to all three axes; the source code has been preserved as is.*
