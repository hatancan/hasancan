---
baslik: EEM211 Sayısal Mantık Tasarımı: "Sayısal Tasarım" Sunuları Bölüm 1–4 (Metin Artıklar, 2006)
ozet: Yrd. Doç. Dr. Metin Artıklar'ın Sayısal Tasarım ders sunuları: ikili sayı sistemleri, tümleyenler, işaretli sayılar ve kodlar; Boole cebiri, kanonik biçimler ve mantık kapıları; Karnaugh haritası, etkisiz koşullar, NAND/NOR gerçekleştirme; kombinasyonel devreler (toplayıcı, çıkarıcı, BCD toplayıcı, çarpıcı, karşılaştırıcı, kod çözücü, kodlayıcı, seçici).
---

Bu yazı, EEM211 Sayısal Mantık Tasarımı dersinin "ege_notlari" klasöründe bulunan dört PDF sunuyu tanıtıyor: **Yard. Doç. Dr. Metin Artıklar**'ın hazırladığı **"Sayısal Tasarım"** dersinin ilk dört bölümü (Nisan 2006). Sunuların hangi üniversitede verildiği belgelerde yazmıyor; konu sırası ve örnekleri M. Morris Mano'nun *Digital Design* kitabını izliyor. Toplam yaklaşık 280 slayt; her bölümün başlıkları ve kapsamı aşağıda özetlendi. Dört PDF yazının sonunda ZIP olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Bölüm 1: İki tabanlı sistemler

Sayısal sistemler iletişimden sağlığa, iş dünyasından internete hemen her alanda kullanılır; en önemli özellikleri sonlu sayıda veri üzerinde işlem yapmalarıdır (ör. 0–9 rakamlarıyla sıcaklık gösteren termometre). Bölümün konuları:

- ikili tabandaki sayılar, r tabanlı sayılar ve sayılarda taban;
- onluk sayıların r tabanına dönüştürülmesi, kesirli sayıların dönüşümü;
- 2 tabanlı sayıların 8 ve 16 tabanına, 8 ve 16 tabanlı sayıların 2 tabanına dönüşümü;
- sayıların tümleyeni: (r−1)'e ve r'ye tümleyen, tümleyen kullanarak çıkarma;
- işaretli ikili sayılar: işaretli büyüklük, 1'e tümleyen ve 2'ye tümleyen yöntemleri; işaretli sayılarda toplama ve çıkarma;
- ikili kodlar: BCD ve diğer ağırlıklı kodlar, Gray kodu, hata bulma kodları (tek ve çift eşlik biti);
- kaydediciler (bilgi saklama) ve ikili mantığa giriş: VE, VEYA, TÜMLEYEN işlemleri.

## Bölüm 2: Boole cebiri ve mantık kapıları

- Temel tanımlar: ikili operatör, aksiyomlar, cebirsel yapılara örnek.
- Boole cebiri ve iki elemanlı Boole cebiri; kapalılık, değişme, birim eleman, dağılma ve tümleyen özellikleri; sıradan cebirle farkları.
- Eşdeğerlik (dualite) kuralı, temel teoremler, De Morgan kuralı, operatör öncelikleri.
- Boole fonksiyonları, cebirsel sadeleştirme, fonksiyonların tümleyeni (ör. F1 = x'yz' + x'y'z).
- Kanonik ve standart biçimler: mintermler (mintörm) ve makstermler (makstörm), fonksiyonların minterm ve maksterm cinsinden yazılması ve gerçeklenmesi.
- Diğer mantıksal operatörler ve mantık kapıları, ikiden fazla girişli kapılar, pozitif ve negatif mantık.
- Entegre devreler, entegre üretim teknolojileri ve bilgisayar destekli devre tasarımı.

## Bölüm 3: Boole fonksiyonlarının sadeleştirilmesi

- Karnaugh haritası (K-map) yöntemi: 2, 3 ve 4 değişkenli haritalar.
- Asal çarpanlar (asal içerenler).
- Fonksiyonların çarpımların toplamı ve toplamların çarpımı biçiminde sadeleştirilmesi.
- Etkisiz (don't care) koşullar; ör. F(w, x, y, z) = Σ(1, 3, 7, 11, 15) ve etkisiz terimler.
- NAND ve NOR ile gerçekleştirme: AND, OR ve NOT kapılarının NAND ile kurulması, NAND kapısının iki farklı gösterimi, iki ve çok seviyeli NAND devreleri.
- XOR ve XNOR kapıları, XOR'un NAND ile kurulması, XOR ile tek ve çift eşlik üreteci ve denetleyicisi.

## Bölüm 4: Kombinasyonel devreler

- Kombinasyonel ve senkron ardışıl devrelerin farkı; tek ve çok çıkışlı kombinasyonel devreler.
- Kombinasyonel devre analizi (doğruluk tablosu ve çıkış fonksiyonlarının bulunması) ve tasarım adımları; örnek olarak BCD kodundan 3-fazlası koduna çevirici.
- İkili toplayıcılar ve çıkarıcılar: yarım ve tam toplayıcı sentezi, n bitlik toplayıcılar, ileri basamaklardaki eldelerin önceden hesaplanması (carry lookahead; Sᵢ = Cᵢ ⊕ (Aᵢ ⊕ Bᵢ)), ikili çıkarıcılar ve taşma bayrağı.
- BCD toplayıcılar ve elde (C) koşulu, ikili çarpıcılar, genlik karşılaştırıcı.
- Kod çözücüler ve kod çözücüyle fonksiyon gerçekleştirme, kodlayıcılar ve kodlayıcı tasarımı.
- Seçiciler (çoklayıcı, MUX): 2x1 ve 4x1 seçici, dörtlü 2x1 seçici, seçicilerle Boole fonksiyonu gerçekleştirme (ör. F(x, y, z) = Σ(1, 2, 6, 7) ve F(A, B, C, D) = Σ(1, 3, 4, 11, 12, 13, 14, 15)).
- Yüksek empedans (üç durumlu) çıkışlar.
