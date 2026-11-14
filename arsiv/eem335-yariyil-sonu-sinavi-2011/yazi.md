---
baslik: EEM335 Bilgisayar Organizasyonu: Yarıyıl Sonu Sınavı (14 Ocak 2011)
ozet: EEM335 Bilgisayar Organizasyonu 14.01.2011 yarıyıl sonu sınavı soruları: TLB, disk erişim süreleri, 32-bit kayan noktalı sayı, üç durumlu devreler, cache eşleme yöntemleri, sanal adres, DMA sinyalleri ve sayfa tablosu hesabı.
---

Başkent Üniversitesi **EEM335 Bilgisayar Organizasyonu** dersinin **14 Ocak 2011** tarihli yarıyıl sonu sınavı (süre 100 dakika; ders Prof. Dr. Emin Akata'nındır). Sınav kâğıdı tek sayfa; orijinali yazının sonunda indirilebilir. Soruların altındaki *Not* satırlarındaki hesaplar arşive eklenmiştir, kâğıtta çözüm yoktur.

## Soru 1 (30 puan)

Aşağıdakileri yanıtlayınız:

1. TLB (Translation Lookaside Buffer) nedir? Ne işe yarar?
2. Disk kullanımında *seek time*, *rotational delay*, *access time* ve *transfer time* kavramlarını açıklayınız.
3. 32-bit kayan noktalı (floating point) gösterimi `1 01111111 10100010000000000000000` olan sayının ondalık karşılığı nedir? Açıklayarak yanıtlayınız.
4. Üç durumlu (tri-state) devre elemanlarının bus kullanımındaki önemi nedir?
5. DRAM, SRAM, SDRAM ve DDR SDRAM yongalarının temel özellikleri nelerdir?
6. Bir bellek modülünün çıkış sinyalleri arasında kesilme (interrupt) sinyali yer almazken bir I/O modülünün çıkışında yer alır. Nedenini açıklayınız.

*Not: 3. maddede işaret biti 1 (negatif), üs 01111111 = 127 (IEEE 754 kaydırması 127 olduğundan üs = 0), mantis 1,1010001₂ = 1 + 1/2 + 1/8 + 1/128 = 1,6328125 olur; sayı −1,6328125'tir.*

## Soru 2 (7 + 5 + 8 puan)

32-bit adres kullanan, byte seviyesinde adreslenebilen ve cache satır büyüklüğü 128 byte olan bir bellek yapısında:

1. **Doğrudan eşlemeli (direct mapped)** cache'te tag boyu 16 bit olduğuna göre adres kalıbını belirtiniz; adreslenebilir birim sayısını, ana bellekteki blok sayısını ve cache içindeki satır sayısını bulunuz.
2. **Tam ilişkisel (associative)** cache'te adres kalıbını belirtiniz; adreslenebilir birim sayısını, ana bellekteki blok sayısını, cache içindeki satır sayısını ve tag boyunu bulunuz.
3. Cache büyüklüğünü bulunuz ve **2 yollu kümeli ilişkisel (2-way set associative)** cache'te adres kalıbını belirtiniz; adreslenebilir birim sayısını, ana bellekteki blok sayısını, küme içindeki satır sayısını ve cache içindeki küme sayısını bulunuz.

*Not: Satır 128 = 2⁷ byte olduğundan word alanı 7 bittir. (a) 32 − 16 − 7 = 9 bit satır alanı: 512 satır, 2³² adreslenebilir byte, 2²⁵ blok. (b) Tag = 32 − 7 = 25 bit. (c) Cache (a) şıkkındakiyle aynı alınırsa 512 × 128 B = 64 KB'tır; 2 yollu yapıda küme başına 2 satır, 256 küme, kalıp 17 bit tag + 8 bit küme + 7 bit word.*

## Soru 3 (15 puan)

"Logical address", "virtual address" ve "demand paging" kavramlarını açıklayınız.

## Soru 4 (20 puan)

CPU, Disk Denetleyici (Disk Controller), Ana Bellek ve DMA Denetleyici (DMA Controller) içeren bir bağlantı şeması çizerek HRQ, HLDA, DREQ, DACK sinyalleri aracılığıyla DMA işleminin nasıl gerçekleştiğini açıklayınız.

## Soru 5 (4 + 4 + 7 puan)

4 GByte sanal adres alanı olan bir bellek organizasyonunda bu alan toplam 2M adet sayfaya bölünmüştür. Sayfa tablosunun büyüklüğü 8 MByte olarak hesaplanmaktadır.

1. Frame (sayfa) büyüklüğünü bulunuz.
2. Sayfa tablosunda her kaydın ne uzunlukta olacağını bulunuz.
3. 1 sayfa büyüklüğünde kök tablo kullanan 2 seviyeli bir sayfalama düzeni için nasıl bir adres yapısı kurulacağını çizerek açıklayınız.

*Not: Sayfa boyu 4 GB / 2M = 2 KB; kayıt uzunluğu 8 MB / 2M = 4 byte olur. Kök tablo 1 sayfa (2 KB) ise 512 kayıt içerir (9 bit); 21 bitlik sayfa numarasının kalan 12 biti ikinci seviye içindir (4096 kayıtlı, 16 KB = 8 sayfalık ikinci seviye tablolar); sayfa içi ofset 11 bittir (toplam 9 + 12 + 11 = 32 bit).*
