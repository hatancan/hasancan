---
baslik: EEM211 Sayısal Mantık Tasarımı: Hata Düzeltme Teknikleri – Eşlik, CRC, ARQ ve Hamming Kodu (Trakya Üniversitesi Proje Ödevi, 2009)
ozet: Trakya Üniversitesi BİLM 637 dersi için 2009'da hazırlanmış "Hata Düzeltme Teknikleri" proje ödevi ve sunusu: eşlik denetimi, iki boyutlu eşlik, VRC/LRC, CRC-16, dur-bekle ve kayan pencere protokolleri, ARQ, (11,7) ve (7,4) Hamming kodu, G ve H matrisleriyle hata düzeltme, Reed-Solomon ve Raptor kodları.
---

Bu yazı, EEM211 Sayısal Mantık Tasarımı dersinin klasöründe Hamming kodu konusuna yardımcı kaynak olarak bulunan bir **proje ödevi** ve sunusudur. Ödev, **Trakya Üniversitesi Fen Bilimleri Enstitüsü Bilgisayar Mühendisliği Bölümü**'nde **BİLM 637 Mobil ve Kablosuz Bilişim** dersi (Doç. Dr. Hasan Hüseyin Balık) için bir yüksek lisans öğrencisi tarafından hazırlanmış (Edirne, Aralık 2009). Kapaktaki öğrenci adı ve numarası çıkarıldı. 36 sayfalık rapor iki bölümden oluşuyor: sayısal iletişimin temelleri ve hata sezme/düzeltme teknikleri. Aşağıda raporun özellikle sayısal mantık dersini ilgilendiren kısımları (eşlik, CRC, Hamming kodu) ayrıntılı, diğer kısımları özet olarak aktarıldı. Maskelenmiş raporun PDF'i ve 37 slaytlık sunu yazının sonunda ZIP olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Giriş

Ağda ilerleyen paketler bazı hata risklerine sahiptir; özellikle ağın koşulları iyi değilse paketler kaybolabilir ya da bozulabilir. Ancak bu tip hataların düzeltilmesi mümkündür. Bu çalışmada hata düzeltme teknikleri üzerinde durulmuş, en yaygın kullanılan Hamming kodlama algoritması ve ARQ teknikleri üzerine ağırlık verilmiş, Reed-Solomon ve Raptor göndermede hata düzeltim kodlarına da kısaca değinilmiştir.

## Bölüm I: Sayısal iletişimin temelleri (özet)

Raporun ilk bölümü konunun alt yapısını hatırlatıyor:

- **Sayısal iletişim:** ikili (0/1) kodlanmış verinin sistemler arasında aktarılması. İletim hızı bit/sn ile verilir; örneğin 8 bitlik kodlar kullanan 2400 bit/sn'lik bir hat saniyede 2400 / 8 = 300 karakter taşır.
- **Veri iletimi karakteristikleri:** salınım yapan işaretin genlik, frekans ve fazı değiştirilerek bilgi taşınır; **baud**, hat üzerindeki işaretin değişme hızıdır. Her işaret değişiminde iki bit gönderilirse bit hızı baud'un iki katı olur.
- **Band genişliği ve Shannon kanunu:** bir kanalın taşıyabileceği en yüksek bilgi hızı C = W·log₂(1 + S/N) ile verilir (W band genişliği, S/N işaret-gürültü oranı). Raporda 1000'e 1 S/N oranlı bir ses kanalı için en yüksek sığa 25 900 bit/sn olarak veriliyor.
- **Periyot ve dalga boyu:** T = 1/F; örneğin 2400 Hz'lik bir işaretin periyodu 1/2400 ≈ 0,000416 s. Dalga boyu WL = S / F (S: işaretin yayılma hızı).
- **Kodlama:** n bitle 2ⁿ sembol kodlanabilir; ASCII 7 bitlik (128 karakter), EBCDIC 8 bitlik bir koddur. ASCII'ye hata sezmek için 8. bit (eşlik) eklenebilir.
- **Paralel ve seri iletim:** paralel iletimde her bit ayrı yoldan gider (veri hazır / istek sinyalleriyle); seri iletim asenkron (her karakterde başla ve dur bitleri), senkron (saat veriyle birlikte, blok başında ve sonunda özel kodlar) ve isokron (periyodik, garantili kapasite; ses-görüntü) olarak üçe ayrılır.
- **Hat tipleri:** simpleks (tek yönlü, TV yayını), yarı dupleks (sırayla iki yönlü, telsiz), tam dupleks (aynı anda iki yönlü, telefon).

## Bölüm II: Hata sezme ve düzeltme teknikleri

Veri iletimi sırasında bazı bitlerin bozulması ihtimali az da olsa ihmal edilemez; bir bit bile bozulsa verinin tamamı anlamsız hâle gelebilir. Bozulma olup olmadığını anlamak için **hata sezme**, bozulmuşsa düzeltmek için **hata düzeltme** teknikleri kullanılır; hata giderilemezse veri paketi yeniden gönderilir. Bu işlevler OSI modelinde **veri bağı katmanına** aittir: katman veriyi çerçevelere (frame) böler ve her çerçevenin sonuna bir **çerçeve denetim dizisi (FCS, Frame Check Sequence)** ekler; alıcı aynı hesabı yapıp FCS ile karşılaştırır.

### Protokoller (özet)

- **Dur ve bekle (Idle RQ):** her çerçeveden sonra ACK beklenir. Çerçeve ya da ACK bozulursa zaman aşımıyla yeniden gönderilir; alıcı hatalı çerçeve için NAK gönderirse zaman aşımı beklenmeden tekrar gönderim yapılır.
- **Sürekli tekrar istemi (Continuous RQ):** gönderici ACK beklemeden çerçeveleri art arda yollar, kopyalarını tekrar iletim listesinde tutar.
- **Seçmeli tekrar (selective repeat):** yalnızca hatalı çerçeve yeniden gönderilir.
- **N çerçeve gerile (go-back-N):** sıra dışı bir çerçeve alınınca, son doğrulanan çerçeveden sonraki bütün çerçeveler yeniden istenir.
- **Kayan pencere:** doğrulama beklemeden gönderilebilecek çerçeve sayısı K ile sınırlanır (K = 1 ise dur ve bekle gibi çalışır).

Veri iletiminde iki tip hata görülür: **patlama (burst)** hatasında alıcıya bir süre anlamsız bilgi gelir ve o süredeki bütün bitler bozulabilir; **rastgele (random)** hatada ortamdaki gürültü yüzünden tek tek bitler bozulur. Hatanın iki nedeni vardır: **bit hataları** (elektromanyetik etkiler vb.) ve **paket kayıpları** (ağ tıkanıklığı, aşırı gecikme).

### Hata düzeltme yöntemleri

1. **Sembol yerine koyma:** alıcıda veriyi bir insan değerlendiriyorsa, yanlış alınan karakterin yerine kullanılmayan bir sembol konur; operatör anlayamazsa tekrar iletim istenir.
1. **Tekrar iletme (ARQ, Automatic Repeat Request):** hatalı alınan mesaj otomatik olarak yeniden istenir. En güvenilir ama her zaman en verimli olmayan yöntemdir; istatistiksel olarak ideal mesaj bloğunun 256–512 karakter olduğu belirtiliyor.
1. **İleriye dönük hata düzeltme (FEC):** mesaja iletimden önce fazladan bitler eklenir ve hata, tekrar iletim olmadan alıcıda bulunup düzeltilir. En yaygın örneği R. W. Hamming'in Bell Laboratuvarları'nda geliştirdiği **Hamming kodudur**.

| FEC için kullanılan algoritmalar | ARQ için kullanılan algoritmalar |
|---|---|
| Katlamalı (konvolüsyonel) kodlar | CRC kodları |
| BCH kodları | Seri eşlik |
| Hamming kodları | Blok eşlik |
| Reed-Solomon kodları | Modül toplamı |
| Raptor kodları | |

## Hata bulma teknikleri

Hata bulma teknikleri hangi bitin hatalı olduğunu söylemez, yalnızca hata olduğunu belirler.

- **Artıklık:** her karakter iki kez gönderilir; iki kopya aynı değilse hata vardır.
- **Tam sayım kodlaması:** bütün karakterlerde 1'lerin sayısı aynıdır (ör. her karakterde üç tane 1); 1'ler sayılarak hata bulunur.
- **Yankılama (echoplex):** terminalde yapılan işlem merkeze bildirilir, merkez bunu geri yansıtır; kullanıcı ekranda doğruluğu kontrol eder.

### Eşlik denetimi (parity check)

En sık kullanılan hata sezme yöntemidir. **Çift eşlikte** eşlik biti ile birlikte 1'lerin sayısı çift, **tek eşlikte** tek olur. Çift eşlik biti, veri bitlerinin XOR'lanmasıyla; tek eşlik biti XNOR ile bulunur. Örneğin 0110 verisi için çift eşlik biti 0, tek eşlik biti 1'dir.

| Veri | 1'lerin sayısı | Çift eşlik (even) | Tek eşlik (odd) |
|---|---|---|---|
| 1101 | 3 (tek) | 1 → 11011 | 0 → 11010 |
| 1100 | 2 (çift) | 0 → 11000 | 1 → 11001 |

*Not: Raporda tek eşlik örneğinde 1100 için eklenecek bitin "0" olduğu yazıyor; doğrusu 1'dir (sonuç olarak verilen 11001 doğru).*

### İki boyutlu eşlik, VRC ve LRC

İki boyutlu eşlikte her karakterin kendi eşlik bitinin yanında, bit sıralarına (sütunlara) göre de eşlik bitleri oluşturulur; böylece tek bitlik hatada hatalı bitin yeri de bulunabilir.

- **VRC (düşey artıklık denetimi, karakter eşliği):** her karaktere iletimden önce bir eşlik biti eklenir.
- **LRC (boyuna artıklık denetimi, mesaj eşliği):** her bit konumu için mesajdaki bütün karakterlerin eşliği hesaplanır ve mesajın sonuna son karakter gibi eklenir; LRC'de yalnızca çift eşlik kullanılır.

Örnek: ASCII "THE CAT" mesajı için VRC'de tek eşlik, LRC'de çift eşlik:

| Karakter | T | H | E | boşluk | C | A | T | LRC |
|---|---|---|---|---|---|---|---|---|
| Onaltılı | 54 | 48 | 45 | 20 | 43 | 41 | 54 | 2F |
| b0 (LSB) | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| b1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| b2 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 |
| b3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| b4 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| b5 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| b6 (MSB) | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 |
| b7 (VRC) | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |

LRC bütün iletim hatalarının %95–98'ini bulur; ama aynı bit konumunda çift sayıda karakter bozulursa hatayı göremez. VRC ve LRC birlikte kullanıldığında tek bitlik hatanın yeri bulunabilir. Mesajdaki baytların mod 256 toplamının kullanıldığı **toplama denetimi (checksum)** de bu ailedendir.

### CRC (çevrimli fazlalık sınaması)

CRC, en güvenli ve en yaygın hata bulma tekniğidir; iletim hatalarının yaklaşık %99,95'ini bulur. Veri bitleri bir polinomun katsayıları gibi ele alınır. Veri polinomu P(x), xᵖ ile çarpılır (verinin sağına p tane 0 eklenir) ve p. dereceden **üreteç polinomu G(x)**'e mod 2 (XOR ile) bölünür:

xᵖ·P(x) = Q(x)·G(x) + R(x)

Bölüm atılır, **kalan R(x)** verinin sonuna eklenip gönderilir. Alıcı aldığı diziyi aynı G(x)'e böler; kalan sıfırsa veri hatasız gelmiştir. ABD'de en yaygın kod **CRC-16**'dır; üreteç polinomu:

G(x) = x¹⁶ + x¹² + x⁵ + 1

CRC kodundaki bit sayısı üreteç polinomunun en yüksek kuvvetine eşittir (burada 16).

### ARQ yöntemleri

ARQ'da üç yöntem kullanılır: **olumlu doğrulama** (alıcı hatasız aldığı her çerçeve için onay gönderir), **zaman aşımı sonrasında yeniden gönderim** ve **olumsuz doğrulama ile yeniden gönderim** (alıcı hatalı çerçeve için NAK gönderir). İki tür ARQ vardır: beklemeli tekrar istemi (dur ve bekle) ve sürekli tekrar istemi (N çerçeve gerile, seçmeli tekrar).

## Hamming kodlama sistemi

Hamming kodu, telekomünikasyonda kullanılan doğrusal bir hata kontrol ve düzeltme yöntemidir: **tek bitlik hataları bulup düzeltir**, iki bitlik hataları bulabilir ama düzeltemez. Richard Hamming 1940'larda Bell Laboratuvarları'nda delikli kartlarla çalışan Bell Model V röleli bilgisayarında çalışırken, hafta sonları operatör yokken hatalar yüzünden işlerinin yarıda kalmasından bıkmış, yıllarca süren çalışmalar sonunda 1950'de adını taşıyan yöntemi yayımlamıştır.

Hamming, kodları (n, k) gösterimiyle tanımladı: n toplam bit, k veri biti. Örneğin 7 bitlik ASCII'ye bir eşlik biti eklemek (8,7), üç kez tekrar (3,1) kodudur; **bilgi oranı** k/n'dir (tekrar için 1/3). İki kod sözcüğünü birbirinden ayıran bit sayısına **Hamming uzaklığı** (distance) dendi: eşlik yönteminin uzaklığı 2, (3,1) tekrar kodunun uzaklığı 3'tür. Amaç uzaklığı artırırken bilgi oranını yüksek tutmaktır.

Algoritma:

1. 2'nin kuvveti olan bütün bit konumları (1, 2, 4, 8, 16, …) eşlik bitleri içindir.
1. Diğer konumlar (3, 5, 6, 7, 9, 10, 11, …) veri bitleri içindir.
1. n. konumdaki eşlik biti, n−1 bit atlayıp n bit kontrol eder, n bit atlar, n bit kontrol eder… Yani 1. eşlik biti 1, 3, 5, 7, 9, 11…; 2. eşlik biti 2, 3, 6, 7, 10, 11…; 4. eşlik biti 4–7, 12–15…; 8. eşlik biti 8–15, 24–31… konumlarını denetler.

### (11,7) Hamming kodu örneği

7 bitlik veri "0110001" olsun. Veri bitleri d1…d7, 3, 5, 6, 7, 9, 10, 11. konumlara yerleştirilir ve eşlik bitleri (çift eşlik) hesaplanır:

| Konum | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Bit | p1 | p2 | d1 | p3 | d2 | d3 | d4 | p4 | d5 | d6 | d7 |
| Eşliksiz veri | | | 0 | | 1 | 1 | 0 | | 0 | 0 | 1 |
| Eşlikli veri | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |

Gönderilen kod sözcüğü **00001101001** olur. İletimde baştan 3. bitin bozulduğunu, alıcının **00101101001** aldığını varsayalım. Alıcı her eşlik bitini yeniden denetler; doğruysa 0, yanlışsa 1 yazar:

| Eşlik biti | Denetlediği konumlar | Sonuç | Eşlik kontrol biti |
|---|---|---|---|
| p1 | 1, 3, 5, 7, 9, 11 | Yanlış | 1 |
| p2 | 2, 3, 6, 7, 10, 11 | Yanlış | 1 |
| p3 | 4, 5, 6, 7 | Doğru | 0 |
| p4 | 8, 9, 10, 11 | Doğru | 0 |

Bu bitler p4 p3 p2 p1 sırasıyla yazılınca **0011** = 2 + 1 = **3** elde edilir: hatalı bit 3. konumdadır. 3. bit çevrilerek veri ilk hâli olan 00001101001'e döndürülür.

*Not: Kod sözcüğü ve sendrom kontrol edildi; 0110001 verisinin (11,7) Hamming kodu gerçekten 00001101001'dir.*

### (7,4) Hamming kodu ve Hamming matrisleri

Bugün Hamming kodu denince ilk akla gelen, 1950'de açıklanan **(7,4)** kodudur: her 4 veri bitine 3 kontrol biti eklenir; her tek bitlik hatayı düzeltebilir ya da bütün tek ve iki bitlik hataları bulabilir. Bu kod iki matrisle çalışır: **kod üretici matris G** (7×4) ve **eşlik kontrol matrisi H** (3×7). Bu örnekte veri bitleri ilk 4, eşlik bitleri son 3 konumdadır.

```
G =  1 0 0 0        H =  0 1 1 1 1 0 0
     0 1 0 0             1 0 1 1 0 1 0
     0 0 1 0             1 1 0 1 0 0 1
     0 0 0 1
     0 1 1 1
     1 0 1 1
     1 1 0 1
```

G'nin ilk 4 satırı 4×4 birim matristir (veriyi olduğu gibi aktarır), son 3 satırı eşlik bitlerinin hangi veri bitlerinden hesaplandığını gösterir. H'nin son 3 sütunu 3×3 birim matris, ilk 4 sütunu aynı eşlik ilişkileridir.

**Kanal kodlama:** gönderilecek veri "1001" olsun, p = (1, 0, 0, 1)ᵀ. Kodlanmış veri mod 2 çarpımla x = G·p = (1, 0, 0, 1, 1, 0, 0)ᵀ olur.

**Eşlik kontrolü:** hata yoksa alınan r = x olur ve z = H·r = (0, 0, 0)ᵀ çıkar.

**Hatanın düzeltilmesi:** tek bitlik hata varsa r = x + eᵢ (eᵢ, i. konumu 1 olan sıfır vektörü) ve

H·r = H·(x + eᵢ) = H·x + H·eᵢ = 0 + H·eᵢ = H·eᵢ

olur; yani z, H'nin i. sütununa eşittir ve hatalı bitin yerini gösterir. Örneğin 3. bit bozulursa r = (1, 0, 1, 1, 1, 0, 0)ᵀ ve z = H·r = (1, 1, 0)ᵀ çıkar; bu H'nin 3. sütunudur. 3. bit çevrilince asıl veriye ulaşılır.

## Reed-Solomon ve Raptor kodları (özet)

- **Reed-Solomon** kodları güçlü doğrusal hata düzeltme kodlarıdır; Galois alanları üzerinde çalışır (her sembol 8 bit), R-S(n, k) kodu (n−k)/2 sembol hatasını düzeltebilir. Çözücü karmaşıktır ve paket düzeyindeki kayıplarda bazı kısıtları vardır; gereken işlem gücü blok uzunluğuyla hızla artar.
- **Raptor** kodlarında alıcı k' > k sembol alarak k kaynak sembolünü yeniden oluşturur; alıcı ek yükü R = (k' − k)/k, %1'in altındadır. Veri büyüklüğüne sınır koymaz ve gereken işlem gücü doğrusal artar.

## Sonuç

Farklı hata düzeltme tekniklerini karşılaştırırken paket kayıp oranı, gereken ağ kaynağı (bant genişliği), gönderici ve alıcıdaki işlemci yükü ve algoritmanın karmaşıklığı göz önüne alınmalıdır.

## Sunu

Ödevle birlikte hazırlanan 37 slaytlık sunu aynı konuları özetliyor: sayısal iletişim ve veri iletimi, paralel/asenkron/senkron seri iletim, iletim hattı tipleri, gerçek zamanlı ve gerçek zamanlı olmayan iletişim, veri bağı katmanı ve FCS, dur ve bekle, sürekli tekrar istemi, seçmeli tekrar, çerçeve gerile ve kayan pencere protokolleri, hata türleri, hata bulma teknikleri (artıklık, tam sayım, yankılama, iki boyutlu eşlik, LRC, CRC), üç hata düzeltme yöntemi, FEC ve ARQ algoritmaları, Hamming kodu algoritması, (11,7) örneği, (7,4) kodu ve matrisleri, Reed-Solomon ve Raptor kodları.
