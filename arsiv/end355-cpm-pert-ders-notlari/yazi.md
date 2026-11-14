---
baslik: END355 Proje Yönetimi: CPM ve PERT Ağ Modelleri Ders Notları (Kritik Yol, LP ile Hızlandırma, Beta Dağılımı)
ozet: CPM ve PERT proje ağı yöntemleri: ağ diyagramı kuralları, ileri-geri geçişle en erken/en geç zamanlar, kritik yol ve boşluk, LP modeli, süre-maliyet (crashing) analizi, PERT üç zaman tahmini ve proje bitiş olasılığı; çözümlü örneklerle.
---

END355 Proje Yönetimi klasöründeki iki ders notu birleştirildi: 14 sayfalık **"CPM ve PERT – Network Modelleri"** sunumu ve 12 sayfalık **"Proje Yönetimi"** (şebeke diyagramı ve kritik yol yöntemi) sunumu. Notlarda yazar ve kurum adı yok; içerikten inşaat mühendisliği ve yöneylem araştırması derslerine ait oldukları anlaşılıyor. Orijinal PDF'ler yazının sonunda indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir (yazarı ve kurumu belgede belirtilmemiştir); arşiv ve nostalji amacıyla paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## CPM ve PERT nedir?

Proje genelinde yanıt aranan sorular: Proje ne kadar sürecek? Bir aktiviteye ne zaman başlanabilir? Bir aktivitenin gecikmesi tüm projeyi etkiler mi, ne kadar? Projeyi erken bitirmek için hangi aktiviteler hızlandırılmalı?

- **CPM (Critical Path Method, kritik yol yöntemi):** 1950'lerde DuPont de Nemours tarafından geliştirildi; aktivite süreleri deterministiktir, benzer projelerdeki deneyimden bulunur.
- **PERT (Program Evaluation Review Technique):** 1958'de ABD Deniz Kuvvetleri tarafından geliştirildi; aktivite süreleri olasılıklıdır (stokastik).
- İkisi de aktiviteleri ve bağımlılıklarını bir ağ üzerinde gösterir; temel fark PERT'in süre tahminindeki istatistiksel yaklaşımıdır.

## Şebeke (ağ) diyagramı kuralları

Oklar aktiviteleri, düğümler **olayları** (bir veya daha fazla aktivitenin başlaması ya da bitmesi) gösterir.

1. Bir başlangıç ve bir bitiş düğümü bulunur.
2. Her aktivite tek bir okla bir kez gösterilir.
3. İki aktivite aynı başlangıç ve bitiş olayını paylaşamaz; bu durumda süresi sıfır olan **kukla (dummy)** aktivite kullanılır.
4. Öncelik ilişkileri şu sorularla belirlenir: Bu aktivite başlamadan önce hangileri bitmelidir? Bunu hangileri izler? Hangileriyle birlikte yapılabilir?

## CPM terminolojisi

- **Kritik aktivite:** gecikmesi tüm projenin bitişini geciktiren aktivite; **kritik yol:** projedeki en uzun süreli yol, üzerindeki her aktivitenin boşluğu sıfırdır.
- **EB/ES (en erken başlama)**, **ES/EF (en erken bitiş)**, **GB/LS (en geç başlama)**, **GS/LF (en geç bitiş)**.
- **Boşluk (slack, TS):** en geç ile en erken başlama (ya da bitiş) zamanları arasındaki fark; AS = GS − EB − aktivite süresi.
- En erken zamanlar başlangıçtan bitişe (ileri geçiş), en geç zamanlar bitişten başlangıca (geri geçiş) hesaplanır. Bir düğümde birden fazla aktivite bitiyorsa en büyük EF, sonraki aktivitenin en erken başlangıcıdır; geri geçişte düğümden çıkan aktiviteler arasından en küçük LS alınır.

## LP ile CPM

t_i, i. düğümdeki olayın gerçekleşme zamanı olsun. Proje süresini enküçüklemek için:

- Min Z = t_n − t_1
- Kısıtlar: t_j − t_i ≥ T_ij (her (i,j) aktivitesi için), t_i ≥ 0.

## Örnek 1: LP ile CPM (8 aktivite)

| Aktivite | Öncül | Süre (gün) |
|---|---|---|
| A | – | 10 |
| B | – | 12 |
| C | A, B | 15 |
| D | B | 18 |
| E | B | 16 |
| F | C | 11 |
| G | D, E | 10 |
| H | F, G | 8 |

Notlardaki LP çözümünde t₂−t₁ ≥ 12, t₃−t₂ ≥ 0, t₃−t₁ ≥ 10, t₅−t₂ ≥ 16, t₆−t₂ ≥ 18, t₇−t₆ ≥ 10, t₈−t₇ ≥ 8 kısıtlarıyla olay zamanları 12, 30, 40 ve 48 gün bulunur. **Kritik yol B–D–G–H, proje süresi 48 gün**dür (B→C→F→H yolu 46, B→E→G→H yolu 46 gündür).

## Örnek 2: Yeni bir elektronik aletin tasarım ve üretimi

| Kod | Aktivite | Öncül | Süre (gün) |
|---|---|---|---|
| A | Ürün özelliklerinin belirlenmesi | – | 30 |
| B | Bütçe ve fizibilite çalışmaları | A | 8 |
| C | Prototip üretimi | B | 8 |
| D | Hammadde temini ve üretim hazırlıkları | B | 5 |
| E | Son tasarımın hazırlanması | H | 2 |
| F | Üretim | D, E | 25 |
| G | Personel eğitimi | A | 10 |
| H | Personelin prototip hakkındaki önerileri | C, G | 3 |
| I | Satış eğitimi ve kullanım kılavuzu hazırlama | E | 5 |
| J | Pazarlama karmasının belirlenmesi | A | 5 |
| K | Tanıtım kampanyası | I, J | 15 |
| L | Projenin sonlandırılması | F, K | 2 |

*Not: Hesaplandığında kritik yol A–B–C–H–E–F–L olup süre 30 + 8 + 8 + 3 + 2 + 25 + 2 = 78 gündür; A–B–C–H–E–I–K–L yolu 73 gündür.*

## Örnek 3: Park düzenleme projesi (ES/EF, LS/LF tablosu)

Ağaçlık bir sahanın parka dönüştürülmesi: A tesviye hafriyatı (4 gün), B ağaçları kes (A; 4), C ağaçları topla ve değerlendir (B; 5), D yol aç ve stabilize ser (A; 3), E otopark stabilize ser (D; 3), F su ve elektrik tesisatı (D; 4), G bina ve sundurmaları yap (C, E; 5), H çiçeklendirme ve yeşillendirme (C, E; 8), I tesisatı tamamla ve temizle (F, G; 2).

| Aktivite (düğümler) | En erken başlama | En erken bitiş | En geç başlama | En geç bitiş | Boşluk |
|---|---|---|---|---|---|
| 1-2 (A) | 0 | 4 | 0 | 4 | 0 |
| 2-3 (B) | 4 | 8 | 4 | 8 | 0 |
| 2-4 (D) | 4 | 7 | 7 | 10 | 3 |
| 3-5 (C) | 8 | 13 | 8 | 13 | 0 |
| 4-5 (E) | 7 | 10 | 10 | 13 | 3 |
| 4-6 (F) | 7 | 11 | 15 | 19 | 8 |
| 5-6 (G) | 13 | 18 | 14 | 19 | 1 |
| 5-7 (H) | 13 | 21 | 13 | 21 | 0 |
| 6-7 (I) | 18 | 20 | 19 | 21 | 1 |

**Kritik yol: A, B, C, H (1-2-3-5-7); proje süresi 21 gün.**

## Zaman–maliyet analizi (crashing) ve LP ile hızlandırma

Basit CPM'de amaç minimum süreyi bulmaktır; CPM ise ek yatırımla (işçilik, ekipman, malzeme) aktivite sürelerinin belli bir miktar kısaltılabileceğini öngörür. Süre kısaltma ek harcamaya **hızlandırma maliyeti (crash cost)** denir; ek maliyet, toplam sürenin kısalmasıyla elde edilen avantajla karşılanır. Kısaltma maliyeti doğrusal varsayılırsa K_ij, (i,j) aktivitesinin hızlandırma birim maliyeti olmak üzere, projeyi T_max süresinde bitirmenin ek yatırımını enküçükleyen LP:

- Min Z = Σ K_ij · (NT_ij − T_ij)
- Kısıtlar: t_j − t_i ≥ T_ij; CT_ij ≤ T_ij ≤ NT_ij (en kısa ≤ süre ≤ normal süre); t_n − t_1 ≤ T_max; t_i ≥ 0.

D_ij = NT_ij − T_ij (kısaltılan süre) değişkeniyle de yazılabilir. Ek bütçe sınırı NEWB varsa Σ K_ij·D_ij ≤ NEWB; toplam süreye bağlı dolaylı birim maliyet I varsa Min Z = Σ K_ij·D_ij + I·(t_n − t_1); projeyi T_set süresinden erken bitirmenin birim getirisi B ise (ör. yap-işlet-devret projeleri) Min Z = Σ K_ij·D_ij − B·(T_set − t_n).

## PERT

Aktivite deneyimi yoksa süre belirsizliği hesaba katılır: her aktivite için üç süre tahmini yapılır: **iyimser (a)**, **olası (m)** ve **kötümser (b)**. Süreler bağımsız ve Beta dağılımlı varsayılır; beklenen süre t_e = (a + 4m + b)/6, varyans σ² = ((b − a)/6)². Beklenen proje süresi kritik yoldaki beklenen sürelerin toplamı, varyansı kritik yoldaki varyansların toplamıdır; proje bitiş süresi bu ortalama ve varyansla yaklaşık Normal dağılım gösterir.

**Örnek:** E(T) = 29 gün ve σ = √6 gün olan bir projenin (a) beklenen süreden 3 gün önce (26 günde), (b) beklenen süreden en fazla 2 gün geç (31 günde) bitme olasılıkları istenmektedir.

*Not: Standart normal dağılımdan P(T ≤ 26) = Φ(−3/√6) = Φ(−1,22) ≈ 0,11 ve P(T ≤ 31) = Φ(2/√6) = Φ(0,82) ≈ 0,79 bulunur. Notlardaki beta formülü slayt görselinde olduğundan t_e ve σ² ifadeleri standart PERT formülleri olarak yazıldı.*

## Kaynak: şebeke yöntemi özeti (ikinci not)

İkinci sunumda aynı konular şöyle özetleniyor: CPM'de aktivite zamanları deterministik, PERT'te olasılıklıdır. Şebeke diyagramı iki biçimde çizilebilir (aktivite oklarda / aktivite düğümlerde); birinci yöntem (aktivite = ok, olay = düğüm) daha kullanışlıdır. Kritik yol, en erken/geç başlama ve bitiş zamanlarının hesabıyla bulunur; boşluğu sıfır olan aktiviteler kritiktir.
