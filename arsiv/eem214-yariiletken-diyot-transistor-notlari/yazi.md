---
baslik: EEM214 Elektronik I: İngilizce Ders Notları, Yarıiletken, pn Eklemi, Diyot Modelleri, MOSFET ve BJT ("Wen", 2006)
ozet: EEM214 Elektronik I klasöründe bulunan, yazar adı yalnız "Wen" olarak kayıtlı İngilizce ders notlarının "Part II – Devices" bölümü: içsel ve katkılı silisyum, pn ekleminin açık devre, ters ve ileri kutuplama ile kırılma bölgesi, diyot modelleri ve uygulamaları, NMOS/PMOS karakteristikleri ve NPN/PNP transistörün çalışma modları, Ebers-Moll modeli.
---

Bu yazı, EEM214 Elektronik I dersinin klasöründe bulunan iki PDF'i tanıtıyor: **Semiconductor and Diode.pdf** (32 sayfa, Lecture 4–5) ve **Transistors.pdf** (34 sayfa, Lecture 6–7). İkisi de LaTeX (Scientific WorkPlace) ile madde madde yazılmış bir ders notu dizisinin **"Part II – Devices: Diode, BJT, MOSFETs"** bölümüne ait (sayfa numaraları 49–114). Yazarı ve kurumu belgede belirtilmemiş; PDF bilgilerinde yazar olarak yalnız "Wen" ve Kasım 2006 tarihi görülüyor. Şekiller Sedra & Smith'in *Microelectronic Circuits* kitabından alınmış. Aşağıda notların içeriği Türkçe özetlendi; PDF'ler yazının sonunda ZIP olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Lecture 4: Semiconductor

- Yarıiletkende iletime katılabilecek yük taşıyıcılarının sayısı iletken ile yalıtkan arasındadır; yarıiletken eleman temelde p tipi ile n tipi silisyumun temas ettiği bir pn eklemidir.
- **İçsel silisyum:** her atom dört değerlik elektronunu komşularıyla kovalent bağlarla paylaşır. Oda sıcaklığında ısıl iyonlaşma eşit sayıda serbest elektron ve delik üretir: n = p = n_i; silisyumda yaklaşık 1.5 × 10¹⁰ taşıyıcı/cm³ (5 × 10²² atom/cm³). n_i² = B·T³·e^(−E_G/kT); silisyum için B = 5.4 × 10³¹, E_G = 1.12 eV, k = 1.38 × 10⁻²³ J/K.
- **Katkılı silisyum:** donör (n tipi) ve akseptör (p tipi) katkılar, çoğunluk ve azınlık taşıyıcı yoğunlukları; sürüklenme ve difüzyon akımları.

## Lecture 5: Diode

- **Fiziksel yapı ve pn eklemi:** açık devrede difüzyon, boşaltılmış bölge ve yerleşik gerilim; ters kutuplamada boşaltılmış bölgenin genişlemesi (W_dep), eklem kapasitesi; kırılma bölgesi (Zener ve çığ); ileri kutuplamada azınlık taşıyıcı enjeksiyonu ve diyot akımı.
- **Karakteristikler:** ileri yön, ters yön ve kırılma bölgesi.
- **Modeller:** büyük sinyal modelleri (ideal diyot, üstel model, parçalı doğrusal model, sabit gerilim düşümü modeli) ve küçük sinyal modeli; her biri için eşdeğer devreler ve diyotlu devre analizi örnekleri.
- **Özel diyotlar:** Zener diyot ve kontrollü doğrultucu (SCR).
- **Uygulamalar:** regülatör, yarım ve tam dalga doğrultucu, tepe doğrultucu, sınırlayıcı, kenetleyici ve diyotlu sayısal mantık.

## Lecture 6: MOS Field-Effect Transistors (MOSFETs)

İki ucunun gerilimiyle üçüncü uçtaki akımı kontrol eden üç uçlu bir eleman; yükselteç ve anahtar tasarımının ve tümleşik devrelerin temel elemanı (uygulamalar: işaret yükseltme, sayısal mantık, bellek). Zenginleştirilmiş NMOS'un yapısı: p tipi alttaş (gövde), yoğun katkılı iki n tipi bölge (kaynak ve savak), ince SiO₂ yalıtkan üzerinde polisilisyum kapı; alttaş ile kaynak/savak arasındaki pn eklemleri ters kutuplu tutulur ve gövde kaynağa bağlanarak eleman üç uçlu kabul edilir. Notta NMOS ve PMOS karakteristikleri, kanal boyu modülasyonu (V_A), iç kapasiteler ve bir özet yer alıyor.

## Lecture 7: Bipolar Junction Transistor (BJT)

NPN ve PNP yapıları; NPN transistörün aktif, ters aktif ve doyum modlarında çalışması (taşıyıcı akışları, baz bölgesindeki azınlık taşıyıcı dağılımı), **Ebers-Moll (EM) modeli**, PNP transistörün aynı modları ve aktif modda i_C, i_B, i_E arasındaki ilişkilerin özeti (i_C = β·i_B, i_E = (β + 1)·i_B, α = β/(β + 1)), doymuş transistörün eşdeğer devresi.

## İndirme

ZIP dosyasında iki PDF'in orijinalleri bulunuyor.
