---
baslik: EEM311 Elektronik II: Stanford EE113 Electronic Circuits Ders Notları (Gregory T. A. Kovacs, 1997)
ozet: Stanford Üniversitesi EE113 Electronic Circuits dersinin Gregory T. A. Kovacs'a ait 268 sayfalık İngilizce ders notları: BJT tekrarı, op-amp devreleri, ortak emetör/baz/kolektör yükselteçleri, frekans cevabı, kaskod ve fark yükselteçleri, akım kaynakları, çok katlı yükselteçler ve geri besleme.
---

Bu yazı, EEM 311 Elektronik II dersinin hoca slaytlarıyla birlikte saklanan, **Stanford Üniversitesi Elektrik Mühendisliği Bölümü**'nün **EE113 Electronic Circuits** dersine ait **ders notlarını** tanıtıyor. Notlar **Prof. Gregory T. A. Kovacs** tarafından hazırlanmış ("© 1997 Gregory T. A. Kovacs, All Rights Reserved", PDF 12 Nisan 1998 tarihli "Rev0" sürümü). 268 sayfalık İngilizce metin, Elektronik II'nin konularının (yükselteç katları, frekans cevabı, fark yükselteçleri, akım kaynakları, geri besleme) hemen hepsini kapsadığı için ders sırasında ek kaynak olarak kullanılmış. Notların tamamı yazının sonunda PDF olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Dersin amacı ve düzeni

Notların ilk bölümü EE113'ün hedeflerini şöyle sıralıyor:

- Temel analog devrelerin tasarımı ve analizi hakkında pratik bilgi edinmek.
- İşlemsel yükselteçleri (op-amp) ve onları kullanan devreleri öğrenmek.
- Bipolar transistörlerin devrelerde gerçekte nasıl çalıştığını görmek.
- Temel yükselteçleri tasarlamayı, analiz etmeyi ve test etmeyi öğrenmek.
- Fark çiftleri, akım kaynakları ve çok katlı yükselteç tasarımını öğrenmek.
- Geri beslemenin yükselteçlere uygulanışını öğrenmek.

Ders kitabı olarak Sedra & Smith'in *Microelectronic Circuits*'i, yardımcı kaynak olarak Horowitz & Hill (*The Art of Electronics*), Gray & Meyer (*Analysis and Design of Analog Integrated Circuits*), Neudeck ve Muller & Kamins gösteriliyor. Notlandırma: haftalık ödevler %10, ara sınav ve kısa sınavlar %35, final %55 (sınavlar açık kitap). Girişte Kovacs'ın esprili "Analog Boot Camp Drill Routine" marşı da var ("One, two, three, four, / Gain and bandwidth, we want more. / Five, six, seven, eight, / We don't want to oscillate.").

## İçindekiler

| Bölüm | Konu | Sayfa |
| --- | --- | --- |
| 1 | Introduction (amaçlar, ders bilgileri, ders planı) | 1 |
| 2 | Basic Concepts: kaynaklar, işaretler, yükselteç modelleri, gürültü, bozulma (distortion), güç kaynakları ve verim, büyük/küçük işaret, transfer fonksiyonları, Bode çizimleri | 5 |
| 3 | BJT Review: DC (büyük işaret) analizi, kutuplama, DC yük doğrusu, küçük işaret davranışı, hibrit-π modeli, baz–emetör arası direnç ölçekleme, AC yük doğrusu | 25 |
| 4 | Operational Amplifiers: gerilim izleyici, eviren, logaritmik, üstel, evirmeyen, toplayıcı, integral alıcı ve türev alıcı devreler; "gerçek" ve ideal op-amp, op-amp frekans cevabı, op-amp yongalarının iç yapısı, geri beslemeye giriş | 38 |
| 5 | Single-Stage BJT Amplifiers ve Common Emitter Amplifier: klasik kutuplama, baz devresi tasarım stratejisi, emetör direnciyle yerel geri besleme | 54 |
| 6 | BJT Frequency Response | 84 |
| 7 | General Amplifier Frequency Response (genel frekans cevabı kestirimi, zaman sabitleri) | 97 |
| 8 | The Common Base Amplifier | 117 |
| 9 | The Common Collector Amplifier | 127 |
| 10 | Cascaded and Cascode Amplifiers | 135 |
| 11 | Differential Amplifiers | 153 |
| 12 | Current Sources | 188 |
| 13 | Multi-Stage Amplifiers (örnek bir yükseltecin analizi) | 197 |
| 14 | Feedback: negatif geri beslemenin özellikleri, bant genişliğine etkisi, karıştırıcı (mixer) ve örnekleyici (sampler) türleri, dört geri besleme topolojisi, gerçekçi devrelerde analiz, kararlılık ve kutup konumları, kompanzasyon, kutup–sıfır "çadır" modeli, doğrusal osilatörler | 203 |

## Geri besleme bölümünden: dört topoloji

Notların en kapsamlı bölümlerinden biri olan geri besleme konusu, yükselteç türünü karıştırma (mixing) ve örnekleme (sampling) biçimine göre dörde ayırıyor:

| Topoloji | Giriş / çıkış | Yükselteç türü |
| --- | --- | --- |
| Series-shunt (seri karıştırma, gerilim örnekleme) | gerilim girer, gerilim çıkar | Gerilim yükselteci |
| Shunt-series (paralel karıştırma, akım örnekleme) | akım girer, akım çıkar | Akım yükselteci |
| Series-series (seri karıştırma, akım örnekleme) | gerilim girer, akım çıkar | Geçiş iletkenliği (transconductance) yükselteci |
| Shunt-shunt (paralel karıştırma, gerilim örnekleme) | akım girer, gerilim çıkar | Geçiş direnci (transresistance) yükselteci |

Gerçek devrelerde geri besleme ağı temel yükselteci yükler; bu yüzden notlar şu adımları öneriyor:

1. Yükselteci, geri besleme ağının yükleme etkisini ve R_S ile R_L'yi de içeren bir "A devresi" olarak yeniden çiz; açık çevrim kazancını bu devreden hesapla (A').
1. Geri besleme oranı β'yı bul.
1. Kapalı çevrim kazancını düzeltilmiş kazançla hesapla: A_f = A' / (1 + A'β).
1. Gerekirse giriş ve çıkış empedanslarını uygun (1 + A'β) ölçeklemesiyle hesapla.
1. Gerekirse R_S ve R_L'nin etkisini matematiksel olarak çıkararak yükseltecin kendi uçlarından görülen empedansları bul.

> "In real situations, the feedback network is generally passive, and loads the basic amplifier in the loop and thus affects A, Ri and Ro... The trick is to lump these 'bad' effects into the previously mentioned 'A' circuits."
