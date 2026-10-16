---
baslik: EEM211 Sayısal Mantık Tasarımı: "Sayısal Tasarım" Ders Notu Bölüm 6–11 (Birleşik Devreler, Multivibratörler, Flip-Floplar, Sayıcılar, Kaydediciler, DAC/ADC)
ozet: Türkçe "Sayısal Tasarım / Sayısal Elektronik" ders notunun 6–11. bölümleri (2003–2004): toplayıcılar, karşılaştırıcılar, kod çözücüler ve kodlayıcılar; tek kararlı, serbest çalışan ve çift kararlı multivibratörler, 74121/74122 ve 555; mandallar ve flip-floplar; asenkron ve senkron sayıcılar; kaydırmalı kaydediciler, Johnson ve halka sayıcı; işlemsel yükselteç, D/A ve A/D çeviriciler.
---

Bu yazı, EEM211 Sayısal Mantık Tasarımı dersinin klasöründe bulunan, internetten indirilmiş Türkçe bir **"Sayısal Tasarım"** ders notunun **6–11. bölümlerini** tanıtıyor. Bölümler ayrı PDF'ler (sy-06, sys7–sys11) hâlinde, Eylül 2003 ve Mart 2004'te Word'den oluşturulmuş; sayfaların üst bilgisinde "SAYISAL TASARIM – Derin" (6. bölümde "SAYISAL ELEKTRONİK – I") yazıyor. Notun yazarı ve hangi kuruma ait olduğu belgelerde açıkça belirtilmemiş. Her bölümün konuları ve öne çıkan örnekleri aşağıda özetlendi; formüllerin ve devre şemalarının ayrıntıları için altı PDF yazının sonunda ZIP olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Bölüm 6: Birleşik devreler (combinational)

- **Aritmetik üniteler:** yarım toplayıcı, tam toplayıcı, iki ve dört bitlik paralel toplayıcılar.
- **Karşılaştırıcılar (comparators).**
- **Kod çözücüler (decoders):** iki ve üç bitlik kod çözücüler, yetki (enable) girişli kod çözücüler, BCD-onluk kod çözücü (4028) ve BCD-7 parçalı gösterge kod çözücüsü.
- **Bilgi dağıtıcılar (demultiplexer)** ve **kodlayıcılar (encoder):** onluk-BCD kodlayıcı ve onluk-BCD öncelikli kodlayıcı (priority encoder).
- **Eşlik üreteçleri ve denetleyicileri (parity generators/checkers).**

## Bölüm 7: Multivibratörler (osilatörler)

Sayısal devrelerde tetikleme sinyali olarak kullanılan kare ve dikdörtgen sinyalleri üreten devrelere multivibratör (osilatör) denir. Üç grupta incelenir: tek kararlı (monostable), serbest çalışan (astable) ve çift kararlı (bistable) multivibratörler.

- **Tek kararlı (one-shot):** girişe gelen tetiklemeye karşılık tek bir darbe üretir; darbe süresi dışarıdan bağlanan direnç ve kondansatöre bağlıdır, tetikleme sinyalinin süresinden bağımsızdır. Transistörlü devre, yeniden tetiklenmeyen **74121** (tw = 0,7·R_EXT·C_EXT; harici direnç yoksa iç direnç 2 kΩ, tw ≈ 30 ns) ve yeniden tetiklenebilen **74122** (tw = K·R_EXT·C_EXT·(1 + 0,7/R_EXT), K = 0,32) anlatılıyor.
- **Serbest çalışan:** transistörlü devrede periyot T = 0,7·(R1·C1 + R2·C2); Schmitt tetiklemeli kapıyla yapılan osilatörde yüksek ve düşük süreler eşik gerilimlerinden (ör. Vcc = 5 V için VT+ = 2,75 V, VT− = 1,67 V) hesaplanıyor.
- **Çift kararlı** multivibratörler ve **entegre zamanlama devreleri** (555 tipi zamanlayıcı).

**Örnek (74121):** 10 ms'lik çıkış darbesi için R_EXT = 10 kΩ seçilirse C_EXT = tw / (0,7·R_EXT) bulunur.

*Not: Notta bu hesap 14,285 µF olarak verilmiş; doğrusu C_EXT = 10×10⁻³ / (0,7 × 10×10³) ≈ 1,43 µF'tır (paydaki üs 10⁻³ yerine 10³ yazılmış ve sonuç bir basamak kaymış).*

**Örnek (74122):** 10 µs'lik darbe için C_EXT = 200 pF seçilirse R_EXT = tw/(K·C_EXT) − 0,7 = 10×10⁻⁶ / (0,32 × 200×10⁻¹²) − 0,7 ≈ 156,25 kΩ; standart değer olarak 160 kΩ seçiliyor.

## Bölüm 8: Mandallar (latch) ve flip-floplar

Birleşik devrelerin çıkışı yalnızca o anki girişlere bağlıdır; sıralı devreler ise bir birleşik devre ile bilgiyi saklayan bellek elemanlarından oluşur ve çıkışları saklanan bilgiye de bağlıdır. Senkron sıralı devrelerde bellek elemanları ortak bir saat sinyaliyle aynı anda etkilenir, asenkron devrelerde ise girişlerin değişim sırası belirleyicidir. Bölümün konuları:

- R-S mandalı (NOR ve NAND kapılı), D mandalı;
- kontak sıçramasının (bounce) mandallar yardımıyla engellenmesi;
- R-S, D, J-K ve T flip-floplar, tetikleme sinyali (clock pulse) ve kenar tetikleme;
- flip-floplarda asenkron girişler (preset, clear);
- ana-uydu (master-slave) flip-flop;
- flip-flop uyarma (geçiş) tabloları.

## Bölüm 9: Sayıcılar

Giriş darbelerine bağlı olarak belirli bir durum dizisini tekrarlayan devrelere sayıcı denir; zamanlama (frekans bölme vb.) ve denetim (kodlama, bilgi depolama vb.) devrelerinde kullanılır. Sayıcılar tetikleme sinyalinin uygulanmasına göre asenkron ve senkron, sayma yönüne göre yukarı ve aşağı sayıcılar olarak sınıflandırılıyor. Konular: sayıcılarda mod kavramı, asenkron yukarı ve aşağı sayıcılar, asenkron sayıcılarda sıfırlama (istenen modda sayma) ve senkron sayıcılar.

## Bölüm 10: Kaydediciler (registers)

Sayısal bilgileri geçici bir süre saklayan devrelere kaydedici denir. Bölümde kaydediciler bilgi giriş-çıkışına ve kaydırma yönüne göre sınıflandırılıyor:

- sola ve sağa kaydırmalı kaydediciler, dört bitlik sola-sağa kaydırmalı kaydedici;
- seri giriş-seri çıkış (SISO), seri giriş-paralel çıkış (SIPO), paralel giriş-paralel çıkış (PIPO) ve paralel giriş-seri çıkış (PISO) kaydediciler;
- kaydırmalı kaydedici sayıcılar: Johnson sayıcı ve halka (ring) sayıcı.

## Bölüm 11: Sayısal-analog (DAC) ve analog-sayısal (ADC) dönüştürücüler

- Sayısal ve analog sinyaller.
- **İşlemsel yükselteçler:** eviren yükselteç (V_OUT = −V_IN·R_F/R_1), evirmeyen yükselteç (A_V = 1 + R_F/R_1; örnekte kazanç 6 ile 2 V girişten 12 V çıkış) ve toplayıcı yükselteç, sayısal örneklerle.
- **D/A çeviriciler:** ikilik ağırlıklı dirençli D/A çevirici (her giriş bitinin çıkışa katkısının adım adım hesaplanması) ve R-2R merdiven tipi D/A çevirici.
- **A/D çeviriciler:** paralel karşılaştırıcılı (simultane, flash), tek rampalı (tek eğimli) ve çift rampalı (çift eğimli) A/D çeviriciler.
