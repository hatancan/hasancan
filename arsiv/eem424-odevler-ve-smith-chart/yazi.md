---
baslik: EEM424 Mikrodalga Kuramı: 2014-2015 Ödevleri (Interferans, Polarizasyon, Mikrodalga Fırın, SAR), Smith Abağı ve Düzlemsel Dalga MATLAB Animasyonu
ozet: Prof. Dr. S. Gökhun Tanyer'in EEM424 Mikrodalga Kuramı ödev föyleri (2014 ve 2015), dersin Smith abağı ve MATLAB ile düzlemsel dalga yayılımı animasyonu kodum.
---

**EEM 424 Mikrodalga Kuramı** dersinde (Prof. Dr. S. Gökhun Tanyer) verilen ödev föyleri, ders için dağıtılan Smith abağı ve ilk ödevlerden biri için yazdığım MATLAB animasyon kodu. Dört PDF ve kod yazının sonunda ZIP olarak indirilebilir.

## Ödev 1 (Şubat 2014)

Teslim: bir hafta içinde verilen ödevler, verildiği haftayı izleyen ilk pazartesi ilk ders girişinde teslim edilir; geç teslimde her gecikilen gün için %20 kayıp (bu ödev için teslim, ekle-sil haftasından sonraki ilk pazartesi, 3 Mart). Tüm cevaplar boş bir kâğıda el yazısıyla ve gerektiğinde şekille hazırlanır; kapak ve plastik poşet kullanılmaz.

1. Rayleigh saçınımı (scattering) nedir?
2. Enterferans (interference) nedir?
3. Polarizasyon (polarization) nedir?
4. İnternet araması: "Frequency Band Allocations" ders notlarını bul; Türkiye'nin tahsislerini bul.
5. İnternet araması: SAR, ISAR, ASAR hakkında belge bul ve ne anladığını açıkla.

## Ödev 01 ve 02 (Şubat 2015, "Microwave Theory and Applications")

**Ödev 01:** (1) Enterferans nedir? (2) Polarizasyon nedir? (internetteki bilgilerden yararlanıp kendi cümlelerinle yaz.) (3) Mikrodalga fırınlar üzerine araştırma: her cihaz için tek satırda marka/model, çalışma frekansı, boyutlar (en/boy/derinlik) ve bilginin kaynağı (internet/mağaza) olan bir tablo. (4) MATLAB yazılımını incele; ne amaçla kullanılabileceğini ve kabiliyetlerini araştır. (5) MATLAB veya benzeri bir yazılımı seçip ödevlerde kullanmak üzere bir sayfalık tanıtım dokümanı hazırla. (6) Sınıfta ilan edildiyse diğer sorular.

**Ödev 02:** (1) Türkiye için frekans bandı tahsisleri. (2) SAR, ISAR, ASAR belgeleri, kullanılan kaynaklar eklenerek. (3) **Az yoğun ortamdan çok yoğun ortama açılı giren düzlemsel dalga:** (A) gelen ve giren (iletilen) dalga açılarını ilişkilendiren eşitliği yaz; (B) şu durumlar için hesapla ve şekil üzerinde göster: (a) yüzeye tam dik giriş, (b) neredeyse dik, (c) yüzeye neredeyse yatay (neredeyse 90°). (4) **Çok yoğun ortamdan az yoğun ortama** açılı giriş için (3)'ü tekrar et. (5) Sınıfta ilan edildiyse diğer sorular.

Kaynak olarak (3) için ilgili bağıntı Snell yasasıdır: n₁·sin θ₁ = n₂·sin θ₂ (EM'de θ_i ve θ_t arasındaki sin θ_t = (n₁/n₂)·sin θ_i ilişkisi); ödev föyünde bağıntı açıkça yazılmamış, ben anımsatıyorum.

## Smith abağı

"The Complete Smith Chart" (Black Magic Design), dersin sayfasında "EEM424 Microwave Theory, Başkent University" başlığıyla dağıtılan boş (kullanılmamış) detaylı abaktır: reaktans ve süseptans bileşenleri, yansıma katsayısı açısı, dalga boyu ölçekleri ve radyal ölçeklenmiş parametreler (SWR, dönüş kaybı, yansıma katsayısı, iletim katsayısı) içerir. Uyumlama ve saplama (stub) ödevlerinde kullanılır.

## MATLAB: düzlemsel dalga yayılımı animasyonu

1 m dalga boylu, +x yönünde yayılan bir düzlemsel dalganın gerçel kısmını zamana göre canlandıran kod (`duzlemsel-dalga-animasyonu.m`, ZIP içinde):

```matlab
[x,y]= meshgrid(5:0.05:15, -5:0.05:5);
l=1;                 % dalga boyu
k=2*pi/l;            % dalga sayısı
f=3e8/l;             % frekans (c/l)
w=2*pi*f;
t=linspace(0,60e-9,200);
z=exp(1i*k*x);
for n=1:length(t)
    surf(x,y,real(z*exp(-1i*w*t(n))));
    view(3)
    zlim([-1.5 1.5])
    xlim([min(min(x)) max(max(x))])
    ylim([min(min(y)) max(max(y))])
    shading interp
    getframe();
end
```

Dalga e^{j(kx − ωt)} biçimindedir; gerçel kısmı kosinüs olarak x yönünde ilerler. Periyot 3,33 ns'dir; 60 ns'lik zaman ekseni 18 periyoda karşılık gelir.

*Bu föyler ve abak dersin öğretim üyesine aittir; hak sahibinin talebi hâlinde kaldırılır.*
