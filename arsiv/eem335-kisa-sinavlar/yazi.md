---
baslik: EEM335 Bilgisayar Organizasyonu: Kısa Sınavlar ve Yanıtları (2003–2009), Hamming Kod Soruları
ozet: EEM335 Bilgisayar Organizasyonu kısa sınav (quiz) soruları ve yanıtları, 2003-2009: Von Neumann makinesi, cache eşleme (direct, set associative) hesapları, DMA, bellek türleri, bellek haritası, CD land-pit, Hamming kod.
---

Başkent Üniversitesi **EEM335 Bilgisayar Organizasyonu** dersinin 2003–2009 yıllarına ait kısa sınav (quiz) kâğıtları; çoğu yanıt anahtarıyla birlikte, yani sorular çözümlü. Ders Prof. Dr. Emin Akata'nındır. Aynı sınavın birden çok kopyası tek kez alındı; orijinal PDF'ler yazının sonundaki ZIP dosyasındadır. Çizimler (blok şemalar, bellek bağlantı şemaları) metne dökülemediğinden orijinal PDF'e bakılmalıdır.

## Kısa Sınav 1 – 5 Kasım 2003

1. **"Von Neumann Machine" bilgisayar mimarisi kavramı çerçevesinde nasıl bir önem taşır?** ENIAC'ın programı donanım bağlantılarıyla dışarıdan veriliyordu ve programlaması çok zordu. ENIAC projesinde danışman olan Von Neumann ve arkadaşları "IAS Computer" adlı yeni bir yapıda programın da bellekte tutulup oradan işlenmesini öngördüler. Bu **stored program concept** sonraki tüm bilgisayar mimarilerine model oldu.
2. **Bilgisayar evrimi kaç nesilde sınıflandırılır?** Üçüncüsünden sonrasında tanımlar konusunda görüş birliği olmasa da 5 nesil: (1) vakum tüplü, (2) transistörlü, (3) SSI-MSI tümleşik devreli, (4) LSI, (5) VLSI.
3. **Moore yasası neyi öngörür?** Intel'in kurucularından Moore, bir tümleşik devreye konabilecek transistör sayısının her yıl ikiye katlandığını gözlemlemiştir.
4. **Ortalama erişim süresi 2 ms, aktarım hızı 10 Mbit/s olan diskte 2 KByte verinin ortalama okuma/yazma süresi?** T_N = T_A + N/R. N = 2·1024·8 = 16384 bit, R = 10·1.048.576 = 10.485.760 bit/s: T = 2·10⁻³ + 16384/10.485.760 = 0,0035625 s = **3,5625 ms**.

## Kısa Sınav 2 – 24 Aralık 2003

1. **Çok sözcüklü veri aktarımında DMA neden kesilmeli ve programlanmış I/O'dan verimlidir?** Programlanmış I/O'da CPU işlemi tümüyle üstlenir, başka iş yapamaz. Kesilmeli I/O'da CPU bekleme döngüsünden kurtulur ama veri aktarımı yine ona düşer. DMA'da CPU I/O işini DMA modülüne devreder; DMA modülü sistem bus'ını CPU'nun kullanmadığı anlarda ya da *cycle stealing* ile kullanır.
2. **Belleğe haritalanmış I/O ile yalıtılmış (isolated) I/O farkı?** Yalıtılmış I/O'da IOR/IOW sinyalleri ve özel I/O komutları kullanılır; I/O birimleri ile bellek aynı adreslere bağlanabilir. Belleğe haritalanmış I/O'da özel komut yoktur, bellek komutları ve MEMR/MEMW sinyalleri kullanılır; adres alanının bir kısmı I/O'ya ayrılır. Artısı güçlü bellek komutlarının I/O'da da kullanılması, eksisi bellek alanından kayıptır; yalıtılmış I/O'da ise tersidir.
3. **İşletim sistemlerinde kaç tür scheduling yapılır?** Uzun vadeli (işlerin process statüsü alıp kısa vadeli kuyruğa girmesi), orta vadeli (swap-in/swap-out planlaması), kısa vadeli (process'lerin zaman paylaşımıyla verimli işlenmesi veya askıya alınması).
4. **Bir bus cycle 5 ms ise, iki farklı DMA yapısında bir word aktarımı ne kadar sürer?** DMA ile I/O modülleri arasında ayrı bus varsa (a) yalnızca bellek erişimi system bus'ı kullanır: **5 ms**. Aynı bus paylaşılıyorsa (b) bir okuma ve bir yazma için 2 bus cycle: **10 ms**.

## Kısa Sınav 1 – 17 Ekim 2007

1. İlk 4 nesil: **1. nesil** elektronik, vakum tüplü, makine dili, yerleşik programlama; **2. nesil** transistörlü, çekirdek bellekli, yüksek seviyeli diller; **3. nesil** tümleşik devreli, yarı iletken bellekli, çoklu işlem; **4. nesil** VLSI yapılar, mikroişlemciler, ağ yapıları, optik diskler.
2. Von Neumann makinesi programı ve veriyi birlikte bellekte tutar (stored program concept); bellekteki komutlar Aritmetik Mantık Birimi ve Program Kontrol Ünitesi aracılığıyla işlenir, I/O bağlantıları bir kontrol ünitesiyle sağlanır.
3. CPU yazmaçları: **PC** (sonraki komutun adresi), **IR** (işlenen komut), **MAR** (okuma/yazma yapılacak bellek adresi), **MBR** (belleğe yazılacak veya bellekten okunan sözcük), **I/O AR** ve **I/O BR** (MAR/MBR'nin I/O karşılıkları); **Execution Unit** komutun gerektirdiği kontrol sinyallerini üretir. (Puanlar: 32 + 32 + 36, süre 25 dk.)

## Kısa Sınav 2 – 14 Kasım 2007

**Soru 1.** Blok büyüklüğü 8 byte olan, toplam ana belleği 2¹⁶ byte olan yapıda 64 satırlı doğrudan eşlemeli (direct mapped) cache kullanılıyor.

- a) Adres bölümleri: blok 2^w = 8 → w = 3; satır sayısı 2^r = 64 → r = 6; adres 16 bit olduğundan etiket (tag) = 16 − 3 − 6 = **7 bit**.
- b) Ana bellekte `2C96` adresi hangi cache satırına gider? 2C96 = 0010110 **010010** 110; ortadaki 6 bit satır numarasıdır: 010010 = **12H** (18. satır).
- c) `A043` adresindeki byte cache'e gelirken yanında hangi byte'lar taşınır? Blok 8 byte; w = 0 olan ilk adres A040'tır; yani **A040–A047** arasındaki 8 byte.

**Soru 2.** Bellek hiyerarşisi nedir, ne amaçla kullanılır? Erişim hızı arttıkça bit başına maliyet artar; kapasite arttıkça bit başına maliyet azalır ve erişim yavaşlar. Kullanıcı hem büyük kapasite hem düşük maliyet hem de performans ister. Çözüm hiyerarşidir: yukarıdan aşağı inildikçe belleğe daha seyrek erişilir, erişim hızı ve maliyet azalır, kapasite artar.

## Kısa Sınav 1 – 4 Temmuz 2008

Soru 1, 2 (Von Neumann ve nesiller) ve Soru 4 (CPU yazmaçları) 2003 ve 2007 sınavlarındakilerle aynıdır. Soru 3: bir bilgisayarın temel yapısı (CPU, bellek, I/O arayüzü) çizilir; **mikroişlemci**, bir Merkezi İşlem Biriminin (CPU) tek bir tümleşik devrede üretilmiş biçimi olarak tanımlanır.

## Kısa Sınav 2 – 14 Temmuz 2008

64 KByte ana bellek, 2 KByte cache, her blokta 16 word (1 byte = 1 word):

- a) En az **16 bit** adres gerekir (64K = 2¹⁶).
- b) Doğrudan eşleme: cache 2048/16 = **128 satır** → r = 7 bit; blok içi w = 4 bit; tag = 16 − (4 + 7) = **5 bit**. Okumada önce r bitlik satır alanıyla cache satırı seçilir, adresin ilk 5 biti satırın etiketiyle karşılaştırılır; eşitse (hit) son 4 bitle istenen word okunur, değilse blok bellekten cache'e getirilir.
- c) Cache 128 satır, ana bellekte 65536/16 = **4096 blok** vardır. i = j mod m olduğundan Blok-132, 132 mod 128 = **4. cache satırına** gider.
- d) 2 yollu kümeli (2-way set associative): 128/2 = 64 set → 6 bit; word 4 bit; tag = 16 − (6 + 4) = **6 bit** (6 + 6 + 4). Blok-132, 132 mod 64 = **4. sete** gider.

## Kısa Sınav 3 – 30 Temmuz 2008

1. Her yonga 512 × 512 = 256 Kbit sağlar (yongadan 1 bit veri alınır); 8 yonga ile **256 KByte** elde edilir.
2. Bir CD iz kesiminde `001001001010000000010000010000101000001001000` bit örüntüsüne karşılık gelen land-pit değişimi çizilir (CD'de 1 bitleri land-pit geçişine, 0'lar geçişsiz aralığa karşılık gelir; çizim PDF'tedir).
3. **RAM** yaz-oku bellektir (dinamik DRAM ve statik SRAM; DRAM'de yük sızdığından tazeleme gerekir, DRAM daha yavaş ve ucuzdur; cache'te SRAM, ana bellekte DRAM; ikisi de uçucudur). **ROM** üretimde bir kez programlanır, silinmez. **PROM** kullanıcı tarafından özel donanımla bir kez programlanır. **EPROM** morötesi ışıkla silinip yeniden programlanır. **EEPROM** elektriksel sinyalle silinir.
4. DRAM okuma/yazmayı saat eşzamanlaması olmadan yapar, CPU erişim süresini beklemek zorundadır. **SDRAM** (Synchronous DRAM) saatle eşzamanlıdır; işlemin kaç döngü sonra biteceği bellidir, CPU bu sürede başka iş yapabilir.
5. Verilen bellek bağlantı şemasının (3-8 decoder, 2K×8 EPROM, iki adet 1K×4 RAM) haritası: **EPROM: C000–C7FF**, **RAM: E400–E7FF** (adres tabloları PDF'tedir).

## Kısa Sınav 2 – 10 Kasım 2008

Doğrudan eşlemeli cache'te byte adresleme, adres alanları Tag = 8, Line = 13, Word = 1 bit.

- a) Adres 8 + 13 + 1 = 22 bit → ana bellek 2²² = **4 MByte**.
- b) Cache 2¹³ = 8K satır, satır 2 byte → **16 KByte**.
- c) Ana bellekte 4M / 2 = **2M blok**; d) blok büyüklüğü 2¹ = **2 byte**.
- Soru 2: `25DB2D` adresi 22 bit olarak 10 0101 1101 1011 0010 1101 yazılır; Line alanı 0110110010110 = **0D96H**, w = 1: cache'in 0D96H satırının ikinci sözcüğüne yerleşir.
- Soru 3: aynı satıra yerleşebilecek en küçük adres Tag = 0 ile **001B2C**'dir.
- Soru 4: tam ilişkisel (associative) eşlemede adres yapısı Tag = 21 bit, Word = 1 bit olurdu.

## Kısa Sınav 2 – 22 Temmuz 2009

**Soru 1.** 1 byte'lık veri SEC (Single Error Correcting) Hamming koduyla iletiliyor; 211₁₀ hangi bit örüntüsüyle iletilir? 8 bitlik sözcük için 2^k ≥ 8 + k + 1 koşulundan k = 4 kontrol biti gerekir; bunlar 1, 2, 4, 8 numaralı konumlara konur. 211₁₀ = 11010011. Konumlar 12…1: D8 D7 D6 D5 C8 D4 D3 D2 C4 D1 C2 C1. Çift eşlik ile: C1 = D1⊕D2⊕D4⊕D5⊕D7 = 0, C2 = D1⊕D3⊕D4⊕D6⊕D7 = 0, C4 = D2⊕D3⊕D4⊕D8 = 0, C8 = D5⊕D6⊕D7⊕D8 = 1. İletilen örüntü: **110110010100**.

**Soru 2.** 1024 × 1024 × 4 bellek yongalarıyla 8 MByte toplam bellek tasarlayın; MAR ve MBR bağlantılarını gösterin. Yonga 10 bit satır + 10 bit sütun seçer, 4 bit veri verir; bir byte için aynı adresle 2 yonga seçilir → her yonga çifti 1 MByte; 8 MByte için **8 çift** gerekir, çiftleri seçmek için 3 bit: toplam adres 10 + 10 + 3 = **23 bit** (2²³ = 8 MByte). (Çizim PDF'tedir.)

## Hamming kod alıştırmaları

1. Tek bit hata olabilen kanalda Hamming kodlu hexadecimal sayılar iletiliyor; alınan 1000101 sözcüğünden iletilen sayıyı bulun. Konumlar 1–7. 4-5-6-7 konumları kontrolü çift → C1 = 0; 2-3-6-7 konumları tek → C2 = 1; 1-3-5-7 konumları tek → C3 = 1. Hata konumu C1C2C3 = 011 = **3**. Düzeltilmiş sözcük 1010101; mesaj bitleri (3, 5, 6, 7. konumlar) = 1101 = **D**.
2. 6 bitlik veri sözcüğüne kaç denetim biti gerekir? 2^k ≥ m + k + 1 koşulu için 2⁴ = 16 ≥ 6 + 4 + 1 → **4 denetim biti**; 1, 2, 4 ve 8. konumlara yerleşir.
