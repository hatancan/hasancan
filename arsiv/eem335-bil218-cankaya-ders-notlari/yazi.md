---
baslik: EEM335 Bilgisayar Organizasyonu: BİL218 Ders Notları, Hafta 1.5–9 (Çankaya Üniversitesi, Doç. Dr. Ersin Elbaşı)
ozet: Çankaya Üniversitesi BİL218 Bilgisayar Organizasyonu ders notları: makine komutu karakteristikleri, komut döngüsü ve kesmeler, bus, hafıza hiyerarşisi ve önbellek, işlemci organizasyonu ve pipeline, RISC/CISC, superscalar, adresleme modları, multicycle; izlence ve Ödev 2.
---

EEM335 klasöründeki "ersin" alt klasöründen: **Çankaya Üniversitesi, BİL 218 Bilgisayar Organizasyonu** dersinin **Doç. Dr. Ersin Elbaşı** tarafından hazırlanan haftalık ders sunumları (Hafta 1.5, 2, 3, 5, 6, 7, 8 ve 9), dersin izlencesi ve "Ödev 2" kâğıdı. Ders kitabı Stallings, *Computer Organization and Architecture: Designing for Performance* (8. baskı, 2010), yardımcı kitap Tanenbaum, *Structured Computer Organization* (5. baskı, 2006). Tüm sunum ve izlence PDF'leri yazının sonunda ZIP olarak indirilebilir. Aynı klasördeki not çizelgesi (öğrenci notları) yayınlanmamıştır.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## İzlence (BİL 218)

Konular: bilgisayar organizasyonu ve mimarisi, bilgisayarın gelişimi, bileşenler, işlemci/veriyolu/kontrol, önbellek, komut kümesi özellikleri, adresleme modları, mikroişlemci organizasyonu (CISC) ve pipeline, pipeline performansı, RISC ve pipeline, komut seviyesinde paralellik, IA-64 mimarisi, kontrol birimi, mikroprogramlanmış kontrol. Değerlendirme: ara sınav %30, katılım %5, ödev %30, final %35.

## Hafta 1.5 – Makine komutu karakteristikleri, operand türleri, assembly

İşlemcinin tüm komutlarına **komut kümesi** denir. Komutun bileşenleri: **opcode** (işlem), kaynak operand(lar), sonuç operand(lar) ve sonraki komut. Operandlar bellekte, CPU yazmacında veya G/Ç aygıtında olabilir. Opcode kısaltmalarına **mnemonic** denir (ADD, SUB, MPY, DIV, LOAD, STOR). Komut türleri: veri işleme (aritmetik/mantık), veri depolama, veri taşıma (G/Ç), kontrol (test ve atlama). Adres sayısı: 3 adresli `OP A,B,C` (A ← B OP C), 2 adresli `OP A,B` (A ← A OP B), 1 adresli `OP A` (AC ← AC OP A), 0 adresli (yığıt).

## Hafta 2 – Bileşenler, komut döngüsü, kesmeler, bus

Donanımsal (hardwired) sistemler esnek değildir; genel amaçlı donanım kontrol sinyallerine göre farklı işler yapar. Mikroişlemci iki adımda çalışır: **fetch** (komutu al) ve **execute** (çalıştır); bu ikiye **komut döngüsü** denir. PC bir sonraki komutun adresini tutar. Kesmeler ve bus tasarım kriterleri de bu haftadadır.

## Hafta 3 – Hafıza ve önbellek

Hafıza karakteristikleri: konum (işlemci, iç, dış), kapasite (word boyu, word sayısı), aktarım birimi (word/blok), **erişim yöntemi** (sıralı – bant; doğrudan – HDD, CD; rastgele – ana bellek; ilişkisel – cache), performans (erişim süresi, çevrim süresi, aktarım hızı), fiziksel tür, uçuculuk ve organizasyon. Ardından hafıza hiyerarşisi ve önbellek tasarım bileşenleri: boyut, eşleme fonksiyonu, yer değiştirme algoritmaları, yazma politikası, satır boyu ve cache sayısı.

## Hafta 5 – İşlemci organizasyonu ve pipeline

İşlemcinin işleri: komut al, yorumla, veri al, işle, veri yaz. **Kullanıcıya görünen yazmaçlar:** genel amaçlı, veri, adres (segment, index, stack pointer) ve koşul kodları (carry, overflow, sign…). **Kontrol ve durum yazmaçları:** PC, IR, MAR, MBR ve program durum sözcüğü (PSW; sign, zero, carry, equal, overflow, kesme izni, supervisor modu). Komut döngüsü fetch, execute ve interrupt aşamalarıdır; ardından komut pipeline'ı işlenir.

## Hafta 6 – RISC

CISC'in gelişim nedenleri (yüksek seviyeli dillerle donanım arasındaki *semantic gap*); programların dinamik analizi: atamalar ağırlıklı çalışır, koşullu atlamalar sık kullanılır, prosedür çağrısı/dönüşü çok zaman harcar; operandların çoğu yerel skalar değişkendir (Pascal ve C'de ortalama %55). **RISC** özellikleri: çok sayıda genel amaçlı yazmaç, yazmaç kullanımını en iyileyen derleyici, az sayıda basit komut, daha iyi pipeline performansı. Bölümde büyük yazmaç dosyası, derleyici tabanlı yazmaç eniyilemesi, RISC pipeline'ı ve RISC–CISC karşılaştırması vardır.

## Hafta 7 – Superscalar

Superscalar mimaride tamsayı ve kayan noktalı aritmetik komutlar ile koşullu atlamalar birbirinden bağımsız ve eşzamanlı çalıştırılır (komut seviyesinde paralellik); RISC'te daha yaygındır. Konular: superscalar ve superpipeline karşılaştırması, paralel çalışmadaki problemler, komut çalıştırma kuralları, **register renaming**, makine paralelliği, **branch prediction**.

## Hafta 8 – Adresleme modları ve komut formatları

Temel adresleme modları: **immediate, direct, indirect, register, register indirect, displacement, stack**. Adresleme tasarımında adres aralığı, esneklik, bellek adresi sayısı ve adres hesaplama karmaşıklığı arasında seçim yapılır. Pentium ve PowerPC adresleme modları ile komut formatları da işlenir.

## Hafta 9 – Multicycle ve kesme

Multicycle çalışmada her komut birden çok adımda tamamlanır; her adım bir saat çevriminde biter, komutlar farklı sayıda çevrim kullanabilir ve bir fonksiyonel birim (tek bellek, tek ALU) komut içinde birden fazla çevrimde paylaşılabilir; veri çevrimler arasında yazmaçlarda taşınır. Ardından kesme oluşturma işlenir.

## Ödev 2 (BİL 218) soruları

1. Bilgisayarların temel fonksiyonu nedir ve bunu nasıl gerçekleştirirler?
2. Kesme nedir, çoklu kesme nedir; bilgisayar fonksiyonunu gerçekleştirirken kesme olursa ne olur? Şekil çizerek açıklayınız.
3. Bus nedir, mimari türleri nelerdir?
4. Bilgisayar hafıza hiyerarşisini çizip avantaj ve dezavantajlarıyla açıklayınız.
5. Erişim metotlarını açıklayınız ve her biri için matematiksel örnek veriniz.
6. Ön bellek nedir, çalışma prensibi nasıldır?
7. Ön bellek eşlemesi (mapping) nedir, çeşitleri nelerdir? Her birini örnekle açıklayınız.

(Soruların ders notlarına ek olarak başka kaynaklarla ayrıntılı açıklanması isteniyor.)
