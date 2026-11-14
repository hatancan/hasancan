---
baslik: EEM335 Bilgisayar Organizasyonu: DRAM Teknolojisi Ödevleri (Yapı, Hata Düzeltme, Tarihçe, DRAM Çeşitleri)
ozet: EEM335 Bilgisayar Organizasyonu dersi için DRAM ödevleri: DRAM hücresi ve satır-sütun organizasyonu, tazeleme (refresh), avantaj ve dezavantajlar, Hamming kodu ile hata düzeltme örneği, DRAM'in tarihi ve FPM, EDO, SDRAM gibi çeşitleri.
---

Başkent Üniversitesi **EEM335 Bilgisayar Organizasyonu** dersinde istenen **DRAM teknolojisi** ödevinin dört öğrenci çalışması (arkadaşların ödevleri; kişisel bilgiler çıkarıldı, kapak sayfaları alınmadı). İki ödev aynı ödev yönergesinin başlıklarını izliyor: **1. DRAM teknolojisi** (a. yapısı ve çalışma prensibi, b. hata oluşumu ve düzeltme, c. avantaj ve dezavantajlar) ve **2. DRAM teknolojisinin tarihi ve güncel durumu** (a. tarihi, b. geçmişten günümüze DRAM çeşitleri). Metin büyük ölçüde internet kaynaklarından derlenmiştir. Orijinal (maskeli) PDF'ler yazının sonunda indirilebilir.

## DRAM nedir, nasıl çalışır?

**Dinamik Rastgele Erişimli Bellek (DRAM)**, bir tümleşik devre içinde her veri bitini ayrı bir **kapasitörde** saklayan rastgele erişimli bellektir ("rastgele erişim": işlemci belleğin herhangi bir noktasına doğrudan erişebilir). Hücre başına tek transistör ve tek kapasitör gerektirdiğinden SRAM'e göre daha küçük alan kaplar ve daha ucuzdur. Kapasitör dolu ise 1, boş ise 0'ı temsil eder. Kapasitörler zamanla yük kaybettiği için veri **tazelenmelidir (refresh)**; bu yenileme yaklaşık 2–4 ms aralıklarla yapılır, güç kesildiğinde veri kaybolur (volatile). Hücreler satır ve sütun kesişimlerinde bir matris (DRAM dizisi) oluşturur; adres, **RAS (row address strobe)** ve **CAS (column address strobe)** sinyalleriyle iki aşamada seçilir. Örnek yonga: 41256 (256K × 1 bit = 256 Kbit); modüller 16 MB (2M×64), 32 MB (4M×64), 64 MB (8M×64) gibi boyutlarda üretilir. Tazeleme okuma/yazma çevrimleriyle ya da özel refresh çevrimiyle yapılır (gizli/transparan refresh, stealing çevrimi).

**SRAM ile karşılaştırma:** DRAM daha yavaş ama daha ucuz ve yoğundur; SRAM daha hızlı, daha fazla güç harcar, daha büyük ve pahalıdır, bu yüzden cache'te kullanılır.

## Hata oluşumu ve Hamming kodu

Ödevlerden birinde DRAM'deki hataları düzeltmek için **Hamming kodu** örneği verilir: veri bitleri uygun konumlara konur, eşlik (parity) bitleri çift eşlik olacak biçimde hesaplanır; örnekte yeni veri sözcüğü (eşlik bitleriyle) 10001100101'dir. Son bit hatalı biçimde 1'den 0'a değişirse (10001100100) eşlik bitleri yeniden ölçülünce hata konumunu gösteren sayı **11** çıkar; 11. bitin değiştirilmesi sözcüğü eski hâline getirir.

## Tarihçe ve çeşitler

DRAM teknolojisinin tarihi; manyetik çekirdek bellekten yarı iletken belleğe geçiş, ilk DRAM yongaları ve bit başına maliyetin hızla düşmesiyle anlatılır. Çeşitler arasında asenkron DRAM türleri (FPM, EDO), **SDRAM** (saatle eşzamanlı), **DDR SDRAM** ve ardıl kuşaklar sayılır. Ayrıntılar ve şekiller ZIP'teki ödevlerdedir.
