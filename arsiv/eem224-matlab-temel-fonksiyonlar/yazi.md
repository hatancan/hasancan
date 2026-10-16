---
baslik: EEM224 Elektromanyetik I: Tanyer: MATLAB temel fonksiyonları ve dalga gösterimi
ozet: MATLAB kaynak kodunun açıklamalı arşiv kaydı; kod ve indirilebilir dosya.
---

S. Gökhan Tanyer’in Başkent Üniversitesi EEM224 dersi için hazırladığı temel06.m dosyası; başlığında temel05SS.m sürümü yazıyor. Vektör oluşturma, sinüs ailesi, eksen ve çizgi ayarları, contour/mesh/surfl, dalga animasyonu ve ödevler içeriyor. Kaynak kod aşağıda, dosya yazının sonunda indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Kaynak kod

```matlab
%%   temel05SS.m
%
%   EEM224 Dersi icin hazırlanmıştır. 
%
%   Temel MATLAB fonksiyonlarının gozden gecirilmesi.
%   Bu dosya, Baskent Univ., Muh. Fak. ogrencileri tarafından ödev ve proje 
%   çalismalarinda kullanılmak uzere hazırlanmıştır. Bu dosyayi ihtiyacınız 
%   dogrultusunda asama asama degistirerek kendi yazilimlarinizi 
%   gelistirebilirsiniz. Basarılar.

%   Dr. S. Gokhun Tanyer
%   14.02.13

%% YAZILIMIN TARİHÇESİ
% Bu kisimda her urettiginiz yazılım surumunun kodunu bir artırarak
% tarihçesini burada kayıt altına alabilirsiniz. Bu sayede, hata
% yaptiginizda eski kayıtlara dönebilir, ayrica eski calismalarinizi gozden
% gecirebilirsiniz.
%       dosya ismi / yıl.ay.gun / calisma durumu / detaylı bilgi.
%       Dosya ismi: Kisa, anlaşılır olmalı. Çift rakamlı surum 
%                   sayisi ile takip edebilir.
%       Tarih: 14 Şubat 2013 için 130204
%       Calisma durumu:   -- henüz üstünde çalışıyorum.
%                         OK  Calisan surumdur.
%                         SS  Calisan ve bir daha dokunmayacağım, koruma
%                             altına almak istedigim Son Sürüm yazılımdır.
%                             Bu durumda temel01SS.m dosyasına da ayrica
%                             saklamanızda fayda var.
%
%
%
%
%temel05SS  130214  OK  Koruma altina alıyorum. 
%temel05            OK  Aksam ders sonrası tamamlandı.
%                   --  Dalga hareketi olacak.
%temel04            OK  Örnek 4: Dalga gösterimi tamam.
%temel03            OK  Örnek 3 tamamlandı. Örnek 4'te dalga hazirlayacagim.
%                   OK  Örnek 3'e geciyorum.
%temel02 130214     --  Örnek 1 ve 2'deki pause etkisizleştirildi. 3'e geçiyorum.
%                   OK  Örnekler 1(A-B), 2(A-G) tamamlandı.
%temel01 130214     --  İlk calisma.
%%  GIRIS - Ekran
%   Bu kisımda kullanacaginiz sekiller, diger yazilimlardan alıntı satırlar,
%   yazılıma giris asamasinda ihtiyac duyacağınız satirlar bulunabilir.

    clear;          %Hafizayı sil.
    figure(1), clf, hold off;
    figure(2), clf, hold off;
    figure(3), clf, hold off;
    figure(4), clf, hold off;      
    %figure(5), clf, hold off;      
    %figure(6), clf, hold off;      
    %figure(7), clf, hold off;      
    %figure(8), clf, hold off;      
    %Not: kullanmadığınız satiri silmek yerine sonra kullanmak üzere " % "
    %işareti ile etkisiz hale getirir, saklayabilirsiniz.
    %Not: Kısım sonlarında iki-üç satir boş bırakmanız görünürlük
    %sağlayacaktır.
    
    
    
%%  GIRIS - Veri hazirlama
%   Ihtiyac duyacaginiz sabit degerler, kullanacağınız matrislerin onceden
%   tanımlanması burada yapılabilir.
%   Not: Kullanacağınız matris boyutu onceden belirli olmasi halinde, 
%   tanımlanması halinde Matlab cok daha hizli calismaktadır. Dongu
%   içerisinde surekli olarak boyutları degisen matris kullanımını 
%   engellemenizde fayda var.



%%   ÖRNEK VERI HAZIRLAMA VE CİZDİRME:
%   Hadi tek boyutlu bir vektor hazırlayalım ve görelim.
    x = [0:1:360];  %Ya da sadece [0:360] kullanbilirsiniz. 1 adim varsayilan değerdir.
                    %eger ";" işaretini kullanmazsanız x degeri ekrana
                    %bastirilacaktır. Gerektiginde veri incelemede
                    %kullanabilirsiniz.

%%   ÖRNEK 1: TEK BOYUTLU VERİLER
%   Hadi basit tek boyutlu bir cizge cizdirelim
    figure(1)   %acik degilse acar. Eger zaten aciksa, ekranin ustune getirir.
    %pause komutu ile burada beklemeye alabilirsiniz. Tıklayınca devam edecektir.
    disp('Örnek 1A - Çizdirilecek');
    pause;       %tam durduruyorum.
    %pause(2);   %ekrana bakabilmek için 2 saniye yeterli olacaktır.
    
    plot(x)     %Bu kadar basit!
    
    y = 2 * x;
    
    figure(1), hold on;
    disp('Örnek 1B - y ilave edilecek');%pause
    pause;          %tam durduruyorum.
    
    plot(y)     %bu da basit degil mi!
    
%%   ÖRNEK 2:
%   x aci olsun. Onu radyana cevirip sinus çizdirelim.
    xrad = pi .* x ./ 180;  %dikkat: vektör çarpımı ".*", vektör bolumu "./"
    z = sin(xrad);

    disp('Örnek 2A - Sinus cizilecek');%pause
    pause;          %tam durduruyorum.
    %pause(2);      %ekrana bakabilmek için 2 saniye yeterli olacaktır. 

    figure(2)
    plot(xrad, z), hold on; %sinüsü ekranda gördünüz. Hadi diğerlerini de çizdirelim.
    
    disp('Örnek 2B - Digerleri cizdirilecek');%pause
    pause;          %tam durduruyorum.
    
    plot(xrad,  cos(xrad), '--')
    plot(xrad, -sin(xrad), '-.')
    plot(xrad, -cos(xrad), ':')
                            %Dikkat: x ekseni radyan degerleri vermektedir.
    %Güzel ve anlaşilir gorunmesi icin soyle de yapabilirdik.
    disp('Örnek 2C - Renkli grafikler cizdirilecek');%pause
    pause;          %tam durduruyorum.
    %pause(2);      %ekrana bakabilmek için 2 saniye yeterli olacaktır. 

    figure(2), hold off, clf;   %Sekli serbest bırakip temizleyelim.

    plot(xrad,  sin(xrad), 'r-',  'LineWidth', 4), hold on;
    plot(xrad,  cos(xrad), 'g--', 'LineWidth', 4)
    plot(xrad, -0.8 .* sin(xrad), 'b-.', 'LineWidth', 4)
    plot(xrad, -cos(xrad), 'm:',  'LineWidth', 4)
 
    %Eksen degerlerine de mudahale etmek mumkun.
    disp('Örnek 2D - Eksen degerleri ayarlanacak');%pause
    pause;          %tam durduruyorum.
    axis([-0.1, 2.1*pi, -1.1, 1.1]);
    
    %Eksen tik degerlerine de mudahale etmek mumkun.
    disp('Örnek 2E - Eksen tik degerleri');%pause
    pause;          %tam durduruyorum.
    %pause(2);      %ekrana bakabilmek için 2 saniye yeterli olacaktır. 
    set(gca, 'xtick',  [0 pi 2*pi]);
    set(gca, 'ytick',  [-1 -0.8 0 0.8 1]);
    
    %Dahası da var.
    disp('Örnek 2F - Grid çizgileri');%pause
    pause;          %tam durduruyorum.
    %pause(2);      %ekrana bakabilmek için 2 saniye yeterli olacaktır. 
    grid on;
    
    %Dahası yine var.
    disp('Örnek 2G - Basliklar');%pause
    pause;          %tam durduruyorum.
    %pause(2);      %ekrana bakabilmek için 2 saniye yeterli olacaktır. 
    title('SİNÜS AİLESİ BİR ARADA');
    xlabel('x (Radyan)');
    ylabel('Olculen Gerilim (Volt)');
    
    disp(' ');
    disp('>>  legend komutunu ogrenin');
    disp('>>  Ayrica fprintf komutunu ogrenin ornek yaratın. ');
    disp(' ');
    %ODEV: legend komutunu ogreniniz.
    %       Aşağıdaki komutu anlayınız.
    %       x = plot(1:10,5*rand(10,1),'marker','square','markersize',12,...
    %           'markeredgecolor','y','markerfacecolor',[.6 0 .6],...
    %           'linestyle','-','color','r','linewidth',2); hold off

    
    
    %% ÖRNEK 3: İKİ BOYUTLU VERİLER
    disp('Örnek 3 - 2B Çizgeler - Baklava - Contour');%pause
    pause;       %tam durduruyorum.
    %pause(2);   %ekrana bakabilmek için 2 saniye yeterli olacaktır.

    clear;
    Rrad    = 1 .* pi .*  [0:360] ./ 180;       %sinüsün fazı
    lenR    = length(Rrad);
    
    x       = ones(lenR,1) * cos(Rrad);  %Dikkat: matris çarpımıdır.
    y       = ones(lenR,1) * sin(Rrad);  %Dikkat: matris çarpımıdır.
    y       = y';
    
    Baklava = zeros (size(x));      %matrisi acalim
    Baklava = sqrt ( x.^2 + y.^2);
    
    %Hadi bakalim, 2B çizgeleri birlikte inceleyelim.
    figure(3), hold off;    %pencereniz yüksekliğin iki katı genişlikte olsun.
    subplot(121), contour(Baklava, 'LineWidth', 3);
    subplot(121), axis('square');
    
    disp('Örnek 3 - 2B Çizgeler - Baklava - 3B gösterim');%pause
    pause;       %tam durduruyorum.
    %pause(2);   %ekrana bakabilmek için 2 saniye yeterli olacaktır.

    subplot(122), mesh(Baklava);
    colormap('copper');
    %subplot(122), axis('square');
    
    %ODEV:  subplot(121) ve 
    %       subplot(122)yerine 
    %       subplot(211) ve 
    %       subplot(212)deneyin bakalım ne oluyor?
    %       Neden subplot(33x)'i denemiyorsunuz. x yerine koyacağınız
    %       rakamlar kaca kadar gidecek? Her sayınin yeri nereye denk
    %       geliyor? İnceleyim bakalım.
    
    %ODEV:  mesh yerine, surf, surfl kullanın, farkini inceleyin.
    
    %Asagidaki komutlari degistirerek farkli cozumleri deneyebilirsiniz.
    disp('Örnek 3 - Baklava cizimi - Farkli renk / bakış açısı tercihi');%pause
    pause;       %tam durduruyorum.
    %pause(2);   %ekrana bakabilmek için 2 saniye yeterli olacaktır.
    
    subplot(122), surfl(Baklava);
    shading('interp'); colormap('winter');
    AZ = 85; EL = 60; view(AZ,EL);
    
        
    
    %% ÖRNEK 4: DALGA GÖSTERİMİ
    disp('Örnek 4 - Dalga gosterimi');%pause
    pause;       %tam durduruyorum.
    %pause(2);   %ekrana bakabilmek için 2 saniye yeterli olacaktır.
        
    clear %hafizayı sil, yeniden başlıyoruz.
        
    t       = 0;                    %anlik fotoğrafi hesapliyoruz.
    f       = 1e9;                  %1 GHz
    c       = 3e8;                  %ışık hızı = 300,000 km
    db      = c /f;                 %dalga boyu = 30 cm.
    
    %100X100lük bir matris oluşturacağız.
    X       = 10 .* [0: 0.3/99 : 0.3];
    Y       = 10 .* [0: 0.3/99 : 0.3];     
    len     = length(X);
    
    %Simdi dongu yapmayi inceleyelim.
    for ix = 1:len
        
        for iy = 1:len
            
            XX  = (X(ix) - 1.5) .* (X(ix) - 1.5);
            YY  = (Y(iy) - 1.5) .* (Y(iy) - 1.5);
            R   (ix,iy)    = 1e-10 + sqrt(XX + YY); %Dikkat: R=0 sorun yaratıyor.
            Att (ix,iy)    = 1 ./ R(ix,iy); %Dalgamizin 1/R ile zayıfladığını kabul 
                                     %edelim. Biliyorum 1/R^2 olmalı ama 1/R
                                     %daha güzel görünüyor.
            faz (ix,iy) = 2 .* pi .* f .* t ...
                        - 2 .* pi ./ db .* R(ix,iy);
        end
    end
        
    Dalga   = sin(faz) .* Att;
    
    figure(4), hold off;    
    surfl(Dalga);
    shading('interp'); colormap('winter');
    AZ = 45;EL = 50; view(AZ,EL);  %Mudahale etmeyebilirsiniz de.
    
       
    
    %% ÖRNEK 5: DALGA HAREKETİNİN GÖSTERİMİ
    disp('Örnek 5 - Dalga hareketinin gosterimi');%pause
    figure(4), hold off;  
    pause;       %tam durduruyorum.
    %pause(2);   %ekrana bakabilmek için 2 saniye yeterli olacaktır.
    
    clear %hafizayı sil, yeniden başlıyoruz.
        
    f       = 1e9;                  %1 GHz
    c       = 3e8;                  %ışık hızı = 300,000 km
    db      = c /f;                 %dalga boyu = 30 cm.
    T       = 1/f;                  %Dalganın periyodu.
    t       = [0 : T/10 : T];       %süre sadece 1 milisaniye
    lenT    = length(t);
    
    
    for it = 1 : lenT
        %100X100lük bir matris oluşturacağız.
        
        X       = 10 .* [0: db/99 : db];
        Y       = 10 .* [0: db/99 : db];     
        len     = length(X);
    
        %Simdi dongu yapmayi inceleyelim.
        for ix = 1:len
        
            for iy = 1:len
            
                XX  = (X(ix) - 1.5) .* (X(ix) - 10*db/2);
                YY  = (Y(iy) - 1.5) .* (Y(iy) - 10*db/2);
                R   (ix,iy)    = 1e-10 + sqrt(XX + YY); %Dikkat: R=0 sorun yaratıyor.
                Att (ix,iy)    = 1 ./ R(ix,iy); %Dalgamizin 1/R ile zayıfladığını kabul 
                                     %edelim. Biliyorum 1/R^2 olmalı ama 1/R
                                     %daha güzel görünüyor.
                faz (ix,iy) = 2 .* pi .* f .* t(it) ...
                            - 2 .* pi ./ db .* R(ix,iy);
            end %iy
        end %ix
        Dalga   = sin(faz) .* Att;
        surfl(Dalga);
        shading('interp'); colormap('copper');
        AZ = 45;EL = 50; view(AZ,EL);  %Mudahale etmeyebilirsiniz de.
        axis([0 100 0 100 -5 5])
        M(it) = getframe;
    end %it
        
    disp('Örnek 5 gosterime hazır! ');
    pause;          %tam durduruyorum.
    %pause(2);   %ekrana bakabilmek için 2 saniye yeterli olacaktır.
    
    movie(M,10,2);
        
    
    %%  ODEV 1: 
    %   A.  İstediğinizde bu yazılımı aynen kullanarak, 
    %           for it = 1 : lenT
    %       için, tel ustunde sinus dalgası yaratınız. 
    %       Dikkat ediniz, grafik tek boyutlu olacak. 
    %
    %   B.  Aynı şekilde gelen dalgayı da gösteriniz.
    %
    %   C.  Her iki dalganın toplamını farklı zamanlarda gösteriniz.
    %
    %   D.  C şıkkındaki sonuçları film halinde gösteriniz.
    %%
    
    
    
    %real(E) ile Guc miktarıni ilerleme yonundeki mesafeye göre çizdiriniz.
    figure(5), hold off
    clear
    
    dum = 0:0.01:20;
    E = sin(dum);
    E2 = E .* E;
    
    plot(dum, E, 'r-',   'LineWidth', 4), hold on;
    plot(dum, E2, 'b--', 'LineWidth', 4)
    title ( 'ALAN GENLIGI VE GUC DEGERI');
    xlabel('Radyan')
    ylabel( 'ALAN (Volt) ,  GUC (Watt)');
    
    
    
    
    

    %% Devami olacak, pek yakında !!
    
    
    
    
%%  SON SON SON SON SON SON SON SON SON SON SON SON SON SON SON SON SON SON
```

*Not: Tarihçe açıklamasındaki 14 Şubat için “130204” yazımı 130214 olmalıdır. f=1 GHz için T=1 ns; “1 milisaniye” yorumu bu değerle uyuşmuyor. 1/R alan genliği ile 1/R² güç yoğunluğu birbirinden ayrılmalıdır; örnek kodun güç grafiği normalize E² gösterimidir.*
