---
baslik: EEM441 Haberleşme I: AM ve FM Laboratuvar Ön Çalışmaları
ozet: AM, DSB-SC, VCO ve süperheterodin alıcı hazırlıkları; MATLAB ile FM işareti oluşturma örnekleri.
---

EEM441 laboratuvarına ait bu ön çalışmalar, AM ve FM işaretlerini, süperheterodin alıcıyı, VCO türlerini ve MATLAB çizimlerini ele alıyor. 30 Aralık 2010, 22 Kasım 2011 ve 6 Aralık 2011 tarihli çalışmalar ile tarihsiz tamamlayıcı sayfalar bir araya getirildi. Öğrenci bilgileri çıkarılmış PDF kopyaları yazının sonunda indirilebilir.

## AM ve DSB-SC hazırlığı

22 Kasım 2011 tarihli uygulama, deney föyündeki kare dalga mesajı 1 MHz taşıyıcıyla modüle ediyor. İlk bölümde bilgi, taşıyıcı ve taşıyıcılı çift yan bant çıkışı; ikinci bölümde aynı mesajın taşıyıcısı bastırılmış çift yan bant çıkışı çiziliyor.

Tam AM için işaret, s(t) = Ac[1 + ka m(t)] cos(2πfc t) biçimindedir. DSB-SC örneğinde mesaj taşıyıcıyla çarpılır; mesajın işaret değiştirdiği yerde taşıyıcının fazı ters döner.

Modülasyon indisi sayfalarında m = Vm/Vc ve modülasyon yüzdesi 100m olarak tanımlanıyor. Osiloskoptaki zarfın en büyük ve en küçük değerleriyle m = (Vmax − Vmin)/(Vmax + Vmin) bulunuyor. m = 1, yüzde yüz modülasyona; m > 1, zarf algılamada bozulmaya karşılık geliyor. Tek tonlu çift yan bant AM için BW = 2fm.

## Süperheterodin, Costas ve eşzamanlı alıcı

Süperheterodin alıcı, anten ve RF süzgecinden geçen işareti yerel osilatörle karıştırarak sabit ara frekansa taşır. Ara frekansta yükseltme ve süzme, ardından demodülasyon yapılır. Böylece farklı yayınları seçerken aynı ara frekans katı kullanılabilir.

Tamamlayıcı sayfada Costas alıcısı ve eşzamanlı algılayıcı da anılıyor. DSB-SC işareti uygun taşıyıcıyla çarpılıp alçak geçiren süzgeçten geçirilerek mesaj elde edilir. AM için radyo ve çift yönlü telsiz kullanımları veriliyor.

## VCO türleri ve AM–FM karşılaştırması

VCO, kontrol gerilimiyle salınım frekansı değişen osilatördür. Yüksek frekans uygulamasında LC tankına bağlı varikap; düşük frekansta kondansatörün dolma hızını değiştiren akım kaynağı örnekleri bulunuyor. Seri ve paralel Colpitts, Clapp ve Hartley osilatörleri sıralanıyor. Colpitts ve Clapp kapasitif, Hartley endüktif geri beslemeyle açıklanıyor. Küçük frekans ayarı gerektiren durumlarda VCXO anılıyor.

AM'de mesaj taşıyıcı genliğini, FM'de anlık frekansı değiştirir. İdeal FM zarfı sabittir. AM'nin iki yan bandına karşılık tek tonlu FM'de çok sayıda yan bant vardır. FM'de bant genişliği frekans sapmasına ve mesaj bant genişliğine bağlıdır.

## Sayısal integral ile FM

Tarihsiz ön çalışmanın MATLAB kodu şöyledir:

```matlab
Ac = 1;
Am = 5;
fm = 10;
fc = 100;
kf = 100;
t = 0:0.00001:0.2;
m_t = Am*cos(2*pi*fm*t);
integral_m_t = cumtrapz(t,m_t);
s_t = Ac*cos(2*pi*fc*t + kf*integral_m_t);
figure(1); plot(t,m_t); title('Mesaj Sinyali');
figure(2); plot(t,integral_m_t); title('Mesaj Sinyalinin Integrali');
figure(3); plot(t,Ac*cos(2*pi*fc*t)); title('Tasiyici Sinyal');
figure(4); plot(t,s_t); title('Moduleli Sinyal');
```

Çizimler 0–0,2 saniye aralığını kapsar. Mesajın genliği 5, taşıyıcının genliği 1'dir; integral grafiğinin tepe değeri yaklaşık 0,08'dir. 6 Aralık 2011 sürümünde Ac = 10 ve Am = 20 seçilmiştir; aynı `integral_m_t` değişkeni kullanılır, fakat bu değişkeni hesaplayan satır belgede yoktur.

*Not: Belgede kf için Hz yazılsa da faza doğrudan kf∫m(t)dt ekleyen bu kod, kf'yi açısal frekans duyarlılığı olarak kullanır. Hz/birim duyarlılığı amaçlanıyorsa faz teriminde 2π çarpanı gerekir. Kaynak kod değiştirilmeden aktarılmıştır; çalıştırılmamıştır.*

## fmmod örneği

30 Aralık 2010 tarihli çalışmadaki ikinci yaklaşım:

```matlab
Fs = 300;
Fc = 100;
t = [0:Fs]'/Fs;
x = sin(2*pi*300*t);
dev = 50;
y = fmmod(x,Fc,Fs,dev);
figure();
xlabel('fc = 100Hz');
ylabel('fs = 300Hz');
plot(t,y);
```

*Not: Kapakta EEM401 yazıyor; dosya EEM441 arşivinde bulunduğu için burada saklandı. 300 Hz sinüsün yine 300 Hz ile örneklenmesi ideal aritmetikte tüm örnekleri sıfıra getirir; bu kod mesajın doğru örneklenmesine örnek değildir. Kaynaktaki “FM her zaman daha az güç gerektirir”, “AM indisi daima 1'dir” ve AM sıfır geçişlerinin mesaj taşıdığı yönündeki genellemeler de koşulsuz geçerli değildir.*
