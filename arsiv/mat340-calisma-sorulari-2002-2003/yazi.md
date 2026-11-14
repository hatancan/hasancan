---
baslik: MAT340 Olasılık: Çalışma Soruları (2003) ve Ara Sınav Soruları (21 Kasım 2002), Çözümlü Notlarla
ozet: Başkent Üniversitesi olasılık dersi çalışma soruları (10 soru: ağaç diyagramı, sayma, Bayes, bağımsızlık, röle sistemleri) ve 21.11.2002 ara sınavı (röle zinciri, hipergeometrik dağılım); bazı soruların hesaplanmış çözümleriyle.
---

Başkent Üniversitesi'nde Öğr. Gör. Pelin Toktaş'ın olasılık derslerine ait iki belge: **"Çalışma Soruları 1"** (5 Mart 2003, Bilgisayar Mühendisliği, 2002-2003 bahar, MAT 250 Olasılık ve İstatistik) ve **MAT 240 Olasılık Ara Sınavı** (21 Kasım 2002, Elektrik-Elektronik Mühendisliği, 2002-2003 güz). Belgelerde çözüm yoktur; aşağıda soruların yanına doğrulanmış kısa sonuçlar eklenmiştir. Orijinal PDF'ler yazının sonunda ZIP olarak indirilebilir. (Klasörde ayrıca taranmış başka çalışma soruları/cevapları vardı; bunlar bu yazıya alınmadı.)

## Çalışma Soruları 1 (5 Mart 2003)

1. Bir kez zar atılıyor. Sonuç çift ise bir kez daha para atılıyor; tek ise para iki kez atılıyor. Ağaç diyagramından örnek uzayın tüm elemanlarını listeleyiniz.
2. Üç bileşenli sistemde 1 numaralı bileşen ile paralel bağlı 2-3 alt sistemi seri bağlıdır (sistemin çalışması için 1 ile 2-3 alt sisteminin işler olması gerekir). (a) A: tam olarak iki bileşen çalışıyor; (b) B: en az iki bileşen çalışıyor; (c) sistemin çalışması olayı: hangi sonuçlar bu olaylarda yer alır? (ç: çalışan, a: arızalı)
3. 0, 1, 2, 3, 4, 5, 6 rakamlarından (a) kaç tane üç basamaklı sayı yazılabilir? (b) Her rakam bir kez kullanılırsa kaç tane üç basamaklı sayı? (c) …kaç tane çift sayı? (d) …kaç tane tek sayı? (e) …orta hanesinde tek rakam bulunan kaç tane çift sayı?
4. Ampul fabrikasında 60 W'lık 1000 ampulden 100'ü, 100 W'lık 2000 ampulden 150'si kusurlu. Rasgele seçilen kusurlu bir ampulün 60 W'lık olma olasılığı? *(Bayes: (100/3000)/((100+150)/3000) = 100/250 = 0,4.)*
5. a noktasından b noktasına sinyal, R1, R2, R3 röleleriyle iletiliyor (R2 ve R3 paralel kolda, R1 seride varsayılırsa): R1'in bozulma olasılığı 0,005, R2 ve R3'ün 0,001'dir; röleler bağımsızdır. Sinyalin b'ye ulaşamama olasılığı nedir?
6. (a) Hilesiz bir para 10 kez atılırsa ilk beş atışın aynı yüz olma olasılığı? (b) Hilesiz iki zarın toplamı 10'dan büyük olduğuna göre toplamın 12 olma olasılığı? *(1/3)* (c) 4 evli çiftten 3 kişilik komisyon: (i) kaç farklı komisyon? *(C(8,3) = 56)* (ii) 2 kadın 1 erkek içerenler? *(C(4,2)·4 = 24)* (iii) hiçbir iki üyesi evli olmayanlar? *(C(4,3)·2³ = 32)*
7. İçinde 1, 2, 3, 4 numaralı 4 top bulunan bir kutudan iki top çekiliyor. A: ilk topun numarası 1; B: ikinci topun numarası 1. (a) İadesiz çekimde A ve B bağımsız mıdır? *(Hayır: P(A)P(B) = 1/16, P(A∩B) = 0.)* (b) İadeli çekimde? *(Evet: 1/4 · 1/4 = 1/16.)*
8. Urn 1'de 2 beyaz ve 1 siyah, urn 2'de 1 beyaz ve 5 siyah top var. Urn 1'den rasgele bir top çekilip urn 2'ye atılıyor; sonra urn 2'den bir top çekiliyor ve beyaz çıkıyor. Aktarılan topun beyaz olma olasılığı? *(Bayes: (2/3 · 2/7)/(2/3 · 2/7 + 1/3 · 1/7) = (4/21)/(5/21) = 4/5.)*
9. Bir oyuncak firmasında önceki oyuncakların %40'ı başarılı olmuştur; başarılı oyuncakların %80'i, başarısızların %30'u pazar araştırmasında olumlu rapor almıştır. (a) Olumlu rapor alan yeni oyuncağın başarılı olma olasılığı? *(0,32/(0,32+0,18) = 0,64)* (b) Olumlu rapor verildiğine göre başarısız olma olasılığı? *(0,36)*
10. Asansörde 3 kişi var ve 3 kat seçeneği var; her kişi bağımsız ve eşit olasılıkla bir kata iniyor. Her katta tam 1 kişinin inme olasılığı? *(3!/3³ = 2/9)*

## MAT 240 Olasılık Ara Sınavı – 21 Kasım 2002

**Soru 1 (23 puan).** Verici ikili kodla mesaj gönderiyor; veri alıcıya ulaşmadan 3 röleden geçiyor, her rölede 0,20 olasılıkla hata yapılıyor (röleler bağımsız). (a) (5 puan) Vericiden "1" gönderilirse üç röleden de "1" çıkma olasılığı? (b) (8 puan) Alıcıdan da "1" alınma olasılığı (ağaç diyagramıyla)? (c) (10 puan) Gönderilen verilerin %70'i "1" ise, alıcı "1" aldığında vericiden "1" gönderilmiş olma olasılığı?

*Çözüm: (a) 0,8³ = 0,512; (b) çift sayıda hata: 0,512 + 3·0,2²·0,8 = 0,608; (c) Bayes: 0,7·0,608/(0,7·0,608 + 0,3·0,392) ≈ 0,7835.*

**Soru 2 (17 puan; bu soruda sonuçlar hesaplanmadan bırakılabilir).** Üretim hattında 20 işçi gündüz, 15 işçi gece, 10 işçi geceyarısından sabaha kadar çalışıyor. Kalite kontrol bölümü, seçilen işçiyi tekrar seçmeden 6 işçiyi anket için seçiyor. (a) (4 puan) 6 işçi hepsi gündüz vardiyasından olmak üzere kaç farklı şekilde seçilebilir? (b) (6 puan) 6 işçinin de aynı vardiyadan olma olasılığı? (c) (7 puan) Seçilen 6 işçinin en az iki farklı vardiyadan olma olasılığı?

*Çözüm: (a) C(20,6) = 38.760; (b) [C(20,6) + C(15,6) + C(10,6)]/C(45,6) = (38.760 + 5.005 + 210)/8.145.060 ≈ 0,0054; (c) 1 − 0,0054 ≈ 0,9946.*

**Soru 3 (23 puan).** Bir kutuda 10 top var: 8'inin üzerinde 2 $, 2'sinin üzerinde 5 $ yazıyor. Kutudan iadesiz 3 top çekiliyor; X, çekilen 3 top içinde 5 $ yazanların sayısı. (a) (8 puan) X'in olasılık kütle fonksiyonu? (b) (8 puan) Birikimli dağılım fonksiyonu? (c) (7 puan) Varyansı ve standart sapması?

*Çözüm: X hipergeometriktir: P(X = 0) = 7/15, P(X = 1) = 7/15, P(X = 2) = 1/15. F(x): 0 (x < 0), 7/15 (0 ≤ x < 1), 14/15 (1 ≤ x < 2), 1 (x ≥ 2). E(X) = 0,6; Var(X) = 3 · 0,2 · 0,8 · 7/9 = 28/75 ≈ 0,373; σ ≈ 0,611.*

*Not: 5. çalışma sorusundaki şekil metne dökülemediğinden röle bağlantısı (R1 seri, R2 ve R3 paralel) varsayımla yazıldı; kesin sonuç için orijinal PDF'e bakılmalıdır. 6(c)(iii) sonucu 4 çiftten farklı çiftlerden 3 kişi seçilip her biri için 2 cinsiyet seçeneği (C(4,3)·2³ = 32) olarak hesaplanmıştır.*
