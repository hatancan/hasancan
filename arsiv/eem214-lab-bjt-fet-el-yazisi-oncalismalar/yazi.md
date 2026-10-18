---
baslik: EEM214 Elektronik I: BJT ve FET Laboratuvarı El Yazısı Ön Çalışmaları
ozet: BJT çalışma bölgeleri, kutuplama, emetör izleyici, MOSFET hesapları ve JFET ön çalışma sorularının kişisel bilgiler çıkarılarak metne aktarımı.
---

EEM214 laboratuvarı için farklı öğrencilerin hazırladığı, bir kısmı 2013 tarihli ön çalışmalar fotoğraflanmış ve taranmış sayfalardan metne aktarıldı. Kişisel bilgiler çıkarıldı; fotoğraf ve indirme dosyası paylaşılmıyor. Aynı hesabın farklı kopyaları birlikte ele alındı; kaynakta görülen hatalar ilgili bölümün altında belirtiliyor.

## BJT: baz akımı ve çalışma bölgeleri

İlk ön çalışmada R_B = 100 kΩ, V_BE = 0,6 V ve β = 260 alınır. Kullanılan bağıntılar:

- I_B = (V_BB − V_BE)/R_B.
- I_C = βI_B.
- V_CE = V_CC − I_C R_C.

V_BB = 0,6 V için I_B = 0; 1 V için 4 µA yazılmıştır. Üçüncü durumun başlığında 10 V yazmasına rağmen hesapta 12 V kullanılmış; farklı kopyalarda 114 µA ve 144 µA sonuçları yer almıştır.

*Not: 10 V için sonuç 94 µA, 12 V için 114 µA'dir. 144 µA sonucu verilen sayılarla uyuşmaz. I_C = βI_B bağıntısı ileri aktif bölge içindir.*

R_C = 1 kΩ için kaynakta kullanılan I_B = 0, 20, 40 ve 60 µA değerleri sırasıyla I_C = 0, 5,2, 10,4 ve 15,6 mA verir. İleri aktif bölge bağıntısının doğrudan uygulanmasıyla yazılan tablo:

| V_CC | I_B | I_C | V_CE |
| --- | --- | --- | --- |
| 15 V | 0 | 0 | 15 V |
| 15 V | 20 µA | 5,2 mA | 9,8 V |
| 15 V | 40 µA | 10,4 mA | 4,6 V |
| 15 V | 60 µA | 15,6 mA | −0,6 V |
| 10 V | 0 | 0 | 10 V |
| 10 V | 20 µA | 5,2 mA | 4,8 V |
| 10 V | 40 µA | 10,4 mA | −0,4 V |
| 5 V | 0 | 0 | 5 V |
| 5 V | 20 µA | 5,2 mA | −0,2 V |
| 1 V | 0 | 0 | 1 V |

1 V ve 20 µA satırının gerilim sonucu kaynakta tamamlanmamış. Çizilen yük doğruları V_CE eksenini 1, 5, 10 ve 15 V'ta keser.

*Not: Negatif V_CE sonuçları, devrenin bu akımla ileri aktif bölgede çalışamayacağını gösterir; gerçek çözüm doyum modeliyle yeniden bulunmalıdır. Bir kopyanın ilk satırındaki belirsiz gerilim yazısı diğer kopyadaki 15 V ile karşılaştırılmıştır.*

R_C = 2,2 kΩ ve I_B = 20 µA için bir kopyada 15 V beslemede 2,56 V, 10 V beslemede 1,44 V, 5 V beslemede −6,44 V, 1 V beslemede −10,44 V yazılır. Diğer kopyada ilk sonuç 3,532 V görünmektedir.

*Not: I_C = 5,2 mA kabulüyle ilk iki cebirsel sonuç 3,56 V ve −1,44 V'tur. 3,532 V, akımın daha fazla basamakla hesaplanmasına bağlı olabilir; kaynak bunu açıklamıyor. Negatif sonuçlar yine doyum kontrolü gerektirir.*

V_CE,sat = 0,2 V alınan doyum hesabında:

- V_CC = 15 V, R_C = 1 kΩ: I_C = 14,8 mA. Bir kopyada I_B = 0,56 mA, diğerinde yaklaşık 0,057 mA yazılmıştır.
- V_CC = 10 V, R_C = 2,2 kΩ: diğer kopyada I_C ≈ 4,45 mA, I_B ≈ 0,017 mA bulunur. İlk kopyada başlık 10 V olduğu hâlde denklemde 15 V kullanılmış, 6,72 mA ve 0,025 mA yazılmıştır.

*Not: 14,8 mA/260 ≈ 56,9 µA'dir. 10 V ve 2,2 kΩ için sınır akımı 4,455 mA, β = 260 ile hesaplanan baz akımı 17,13 µA'dir; doyumda zorlanmış β ayrıca değerlendirilir.*

Sayfalarda ileri aktif, kesim ve doyum bölgeleri sıralanır. İleri aktif için I_B > 0 ve V_CE > 0 ifadeleri, doyum için küçük V_CE ve pozitif I_B gösterilmiştir.

*Not: İleri aktif bölgeyi yalnız V_CE > 0 koşulu tanımlamaz; baz-emetör jonksiyonu ileri, baz-kollektör jonksiyonu ters kutuplu olmalıdır.*

## Dört BJT kutuplama devresi

İki sayfalık başka bir çalışmada V_CC = 30 V, β = 100, R_C = 4,7 kΩ, R_B = 470 kΩ, gerektiğinde R_E = 1,2 kΩ kullanılmıştır.

| Devre | Kaynaktaki baz akımı | Kaynaktaki V_CE |
| --- | --- | --- |
| Sabit baz kutuplama | 62,34 µA | 0,7002 V |
| Emetör dirençli kutuplama | 49,56 µA | 0,7068 V |
| Kollektörden baza geri besleme | 31,17 µA | 15,3501 V |
| Gerilim bölücülü kutuplama | −2,735 µA | 31,61689 V |

Kullanılan denklemler:

- Sabit kutuplama: I_B = (V_CC − V_BE)/R_B.
- Emetör dirençli: I_B = (V_CC − V_BE)/[R_B + (β + 1)R_E].
- Geri beslemeli yaklaşım: I_B = (V_CC − V_BE)/(R_B + βR_C).
- Bölücülü: V_Th = V_CC R_B2/(R_B1 + R_B2), R_Th = R_B1 || R_B2; I_B = (V_Th − V_BE)/[R_Th + (β + 1)R_E].

Bölücüde 470 kΩ ve 5,6 kΩ kullanılarak V_Th = 0,3532 V, R_Th = 5,59 kΩ yazılmıştır.

*Not: 470 kΩ || 5,6 kΩ ≈ 5,534 kΩ'dur. V_Th < 0,7 V olduğundan negatif baz akımı ileri aktif modelin geçersizliğini gösterir; basitleştirilmiş modelde transistör kesimdedir. 31,61689 V fiziksel çalışma noktası değildir. Emetör dirençli devrede verilen I_B ile V_CE yaklaşık 0,70 V'tur; küçük farklar yuvarlama kaynaklıdır. Kollektörden beslenen baz akımı da R_C'den geçtiği için tam denklemde β yerine β + 1 bulunur.*

Kararlılık hesabı sayfasında şu sonuçlar yer alır:

- Sabit kutuplama: S(I_CO) = 101 ve S(V_BE) = −101/(470 kΩ).
- Emetör dirençli: S(V_BE) = −100/[470 kΩ + 101 × 1,2 kΩ] ≈ −0,1691 × 10⁻³ A/V; S(I_CO) ≈ 79,86.
- Geri beslemeli: S(V_BE) = −100/[470 kΩ + 101 × 4,7 kΩ]; sonuç −0,1058 yazılmıştır. S(I_CO) ≈ 50,75.
- Bölücülü son satırda direnç yerine 0,180 kullanılmış ve −0,82385 ile 0,011369 sonuçları yazılmıştır.

*Not: Kararlılık katsayısının hangi akıma göre tanımlandığı önemlidir. I_C'nin V_BE'ye türevi için sabit kutuplamada pay −β'dir. Geri beslemeli satırın boyutu yaklaşık −0,1059 mA/V'tur. Son satırdaki 0,180 değeri önceki R_Th hesabıyla uyuşmaz; bu satır doğrulanmış bir tasarım sonucu değildir.*

## Ortak kollektör: emetör izleyici

26 Nisan 2013 tarihli ve başka bir kopyası bulunan çalışmada V_CC = 15 V, R_1 = 47 kΩ, R_2 = 10 kΩ, R_E = 1 kΩ ve β = 100 kullanılır. Kaynaktaki işlem sırası:

1. V_Th = [10/(10 + 47)] × 15 = 2,625 V.
2. R_Th = 10 kΩ || 47 kΩ = 8,25; birim Ω yazılmıştır.
3. I_B = (V_Th − V_BE)/[R_Th + (β + 1)R_E] denkleminde paya 15 − 0,7 konularak 0,131 mA bulunmuştur.
4. I_E = 13,231 mA ve r_e = 25 mV/I_E = 1,89 Ω hesaplanmıştır.
5. R_in,base ≈ β(r_e + R_E); sonuç 101,2 kΩ yazılmıştır. Diğer kopyada toplam R_in ≈ 7,63 kΩ görünür.
6. R_out = r_e || R_E ifadesinin sonucu 0,530 kΩ yazılmıştır.
7. A_V ≈ R_E/(r_e + R_E) = 0,998; gerilimde faz farkı yoktur.
8. A_I ≈ −β(R_1 || R_2)/[(R_1 || R_2) + R_in,base]. Çıkış akımı oku emetör akımına ters seçilmiştir.

*Not: V_Th ≈ 2,632 V ve R_Th ≈ 8,246 kΩ'dur. Doğru V_Th ile I_B ≈ 17,68 µA, I_E ≈ 1,786 mA ve r_e ≈ 14 Ω bulunur. Kaynaktaki 1,89 Ω || 1 kΩ işlemi bile 0,530 kΩ değil yaklaşık 1,886 Ω verir. Gerçek çıkış direnci giriş kaynağının direncine de bağlıdır. Negatif akım kazancı burada seçilen ok yönünden kaynaklanır; emetör izleyicinin gerilim kazancı pozitiftir.*

## MOSFET: ohmik bölge ve doyum

2 Mayıs 2013 tarihli çalışma ile iki taranmış sayfa aynı parametreleri kullanır: μ₀C_ox = 166,67 µA/V², W/L = 3, V_T = 1,45 V; taranmış çözümde V_A = 1/λ = 100 V da verilmiştir.

- Ohmik bölge: I_D = μ₀C_ox(W/L)[(V_GS − V_T)V_DS − V_DS²/2].
- Doyum sınırı: V_DS,sat = V_GS − V_T.
- Doyum, kanal boyu modülasyonu ihmal: I_D = ½μ₀C_ox(W/L)(V_GS − V_T)².
- Ohmik bölgedeki diferansiyel direnç: r = 1/[μ₀C_ox(W/L)(V_GS − V_T − V_DS)].

| V_GS | V_DS | Taranmış çözümde bölge | I_D | Direnç |
| --- | --- | --- | --- | --- |
| 3 V | 0,5 V | Ohmik | 325 µA | 1904,7 Ω |
| 5 V | 0,5 V | Ohmik | 825 µA | 655,7 Ω |
| 2 V | 3 V | Doyum | 75,63 µA | Ohmik bağıntı uygulanmaz |

Diğer kopyada ilk iki direnç 1,9047 × 10⁻³ Ω ve 6,557 × 10⁻⁴ Ω yazılmış; üçüncü duruma da ohmik bağıntı uygulanarak negatif direnç ve −1425,0285 µA bulunmuştur.

*Not: İlk iki dirençte µ katsayısı nedeniyle milyon katlık birim hatası vardır. Üçüncü durum doyumdadır; negatif sonuçlar yanlış bölge denkleminin kullanılmasındandır. V_A = 100 V bilgisi kullanılacaksa doyum akımına 1 + λV_DS çarpanı gelir ve yaklaşık 77,9 µA elde edilir; taranmış çözüm bu etkiyi ihmal etmiştir.*

100 kΩ küçük sinyal direnci için V_DS ≈ 0 alınmış; bir kopyada V_GS = 1,45 V, taranmış çözümde 1,47 V bulunmuştur.

*Not: 100 kΩ koşulu V_GS − V_T ≈ 0,020 V verir; 1,47 V sonucu tutarlıdır.*

Diyot bağlı MOSFET örneğinde V_DD = 5 V, I_D = 100 µA:

V_GS = V_T + √[I_D/(½μ₀C_ox W/L)] ≈ 2,082 V.

R = (5 − 2,082)/(100 µA) ≈ 29,18 kΩ. Kaynakta aynı hesabın yuvarlanmış 29,2 kΩ sonucu da vardır.

## FET ön çalışma: kutuplama ve çıkış direnci

10 Mayıs 2013 tarihli sayfa ile ikinci kopyada kapısı dirençle toprağa bağlı, R_D = 4,7 kΩ, R_S = 1 kΩ ve V_DD = 15 V olan devre çizilir. I_G ≈ 0 yazılır. Çevre denklemi −15 + 4,7k I_D + V_DS + 1k = 0 biçimindedir.

*Not: Son terimde akım eksiktir; doğru boyutlu terim I_D × 1 kΩ olmalıdır.*

Bir sonraki satırda V_DS ≥ V_GS − V_T koşulu ve 3 V ≥ 2 V karşılaştırmasıyla doyum kararı verilir. V_A = 100 V için r_o ≈ V_A/I_D tablosu:

| I_D | r_o |
| --- | --- |
| 1 mA | 100 kΩ |
| 2,5 mA | 40 kΩ |
| 10 mA | 10 kΩ |

Bölücülü FET tasarımında V_DD = 15 V, V_G = 5 V, I_D = 4 mA, V_D = 11 V, I_DSS = 9 mA ve V_P = 3 V yazılmıştır. Bölücü akımı 0,05 mA alınarak R_G1 = (15 − 5)/0,05 mA = 200 kΩ ve R_G2 = 5/0,05 mA = 100 kΩ bulunur.

*Not: V_P işareti kanal tipine bağlıdır; kaynak bu satırda kanal tipini ve işaret kabulünü açıklamıyor.*

## Çözülmemiş Başkent laboratuvar soruları

**Deney 4 ön çalışması:** İlk devre ortak emetörlüdür: üst baz direnci 100 kΩ, alt baz direnci 10 kΩ, giriş kaynak direnci 10 kΩ, kollektör direnci 5 kΩ; emetör topraklıdır. A_I, A_V, Z_o ve Z_i istenir. V_CC sayısal olarak belirtilmemiştir.

İkinci devre ortak bazlıdır. Baz topraklı, kollektör +8 V'a 3,6 kΩ üzerinden, emetör −5 V'a 3,9 kΩ üzerinden bağlıdır. Giriş emetöre, çıkış kollektöre kapasitif kuplajlıdır. β = 75 ve r_o = ∞ için A_V ve A_I istenir. Kaynakta çözüm yoktur.

**Deney 5 ön çalışması:** Ortak kaynaklı, öz kutuplamalı JFET devresinde R_D = 12 kΩ, R_G = 1 MΩ, R_S = 470 Ω, V_DD = 30 V, I_DSS = 3 mA, V_P = −2,4 V ve r_d ≫ R_D verilmiştir. Kaynak direnci kondansatörle AC açısından by-pass edilmiştir. V_GS, I_D, V_DS ve küçük sinyal gerilim kazancı sorulur; çözüm yazılmamıştır.

## 2N5460 P-kanal JFET inceleme notu

İki sayfalık öğrenci raporu G, S ve D uçlarını; N ve P kanal ayrımını ve P-kanal 2N5460 elemanını anlatır. Kapı, kaynak ve savak uçları işlev bakımından BJT'nin baz, emetör ve kollektör uçlarına benzetilir. Transfer karakteristiği sabit V_DS'de I_D'nin V_GS ile değişimidir. V_GS = 0 iken doyum bölgesinde I_D = I_DSS; kapama geriliminde akım yaklaşık sıfırdır.

Raporda aktarılan değerler:

| Parametre | Kaynaktaki değer |
| --- | --- |
| I_DSS | −1 mA ile −5 mA |
| V_GS(off) | 0,75–6,0 V |
| İleri iletim admitansı, y_fs büyüklüğü | 1000–4000 µmho |
| Çıkış admitansı, y_os büyüklüğü | En çok 75 µmho |

g_m kapı gerilimindeki değişime karşı savak akımının değişimini ifade eder. Çıkış admitansı küçük sinyal çıkış direncini bulmakta kullanılır. Rapor, farklı kapama gerilimlerinde akım eğrilerini ve sıcaklıkla değişimi yorumlar; akımın sıcaklık yükselince azaldığını, iletimin akımla artıp eğiminin küçüldüğünü belirtir.

*Not: Bunlar kaynak raporun grafik yorumlarıdır; g_m sabit bir malzeme sayısı değildir ve çalışma noktasına bağlıdır. Çıkış admitansının tersinden direnç elde edilir. Negatif akımlar P-kanal işaret kabulünü yansıtır; mutlak büyüklük aralığı 1–5 mA'dir. Grafiklerin sıcaklık davranışı tüm çalışma noktalarına genellenemez.*

Anahtar örneği +10 V besleme ve 2 kΩ savak direnci kullanır. V_GS < −4 V olduğunda kesim ve V_out = +10 V; V_GS = 0 olduğunda ohmik çalışma ve yaklaşık V_out = 0,3 V yazılmıştır. Yük doğrusu I_D = (10 V − V_DS)/2 kΩ'dur ve eksenleri 5 mA ile 10 V'ta keser.

*Not: Bu son örneğin V_P = −4 V işaretleri N-kanal JFET'e aittir; önceki P-kanal 2N5460 bölümünün doğrudan devamı olarak uygulanmamalıdır. Fotoğraflardaki üretici grafiklerinin ve datasheet'in kendisi paylaşılmadı.*
