---
baslik: EEM401 Sayısal Sinyal İşleme: Sayısal Süzgeçler (Ağ Yapıları, IIR Tasarımı, FIR Tasarımı)
ozet: Selda Güney'in EEM401 Sayısal Süzgeçler I–III sunumları: IIR ve FIR gerçeklemeleri (doğrudan, kanonik, kaskat, paralel, transpoze), Butterworth/Chebyshev/eliptik analog süzgeçler, değişmez dürtü cevabı ve çift doğrusal dönüşüm, pencereleme ve frekans örnekleme.
---

EEM401 Sayısal Sinyal İşleme dersinin (Yrd. Doç. Dr. Selda Güney, 2014–2015 güz) aralık ayındaki üç sunumu: *Sayısal Filtreler I* (gerçekleme), *II* (IIR tasarımı) ve *III* (FIR tasarımı). Orijinal sunumlar yazının sonunda ZIP olarak indirilebilir. Dersin adı slaytlarda "EEM 401 Sayısal Sinyal İşleme"dir.

## I. Sayısal süzgeçlerin gerçeklenmesi

**Avantajlar:** katsayılar değiştirilerek transfer fonksiyonu değiştirilebilir; yüksek güvenirlik ve doğruluk; analog süzgeçlerle gerçeklenemeyecek transfer fonksiyonları gerçeklenebilir. **Dezavantajlar:** maliyet, sürekli enerji kaynağı ihtiyacı.

Tasarıma göre iki tür:

1. **Tekrarlı (özyinelemeli, rekürsif)**: çıkış hem girişin hem çıkışın fonksiyonudur; faz tepkisi doğrusal değildir; kararlı olması için transfer fonksiyonunun kutupları z düzleminde birim daire içinde olmalıdır.
2. **Tekrarsız**: çıkış yalnızca girişe ve girişin önceki değerlerine bağlıdır; doğrusal faz tepkisi vardır, kararlıdır; keskin geçişli transfer fonksiyonu için çok sayıda geciktirme elemanı gerekir.

Doğrusal zamanla değişmeyen (DZD) sistemler **FIR** (sonlu süreli dürtü tepkisi: y[n] = Σ_{k=0}^{M−1} h(k) x(n − k), genelde tekrarsız) ve **IIR** (sonsuz süreli dürtü tepkisi, genelde tekrarlı) olarak ikiye ayrılır.

Gerçekleme yöntemleri: doğrudan, kanonik form, seri (kaskat), paralel, basamak ve kafes gerçekleme.

Sabit katsayılı fark denklemi: y[n] = −Σ_{k=1}^{N} a_k y[n − k] + Σ_{k=0}^{M} b_k x[n − k] ve H(z) = Σ b_k z^(−k) / (1 + Σ a_k z^(−k)). Temel elemanlar: toplayıcı, çarpıcı ve birim geciktirici. Örnek: y[n] = a1·y[n−1] + a2·y[n−2] + b0·x[n].

### IIR sistemler için ağ yapıları

- **Doğrudan biçim I:** H(z) = H2(z)·H1(z); önce v[n] = Σ b_k x[n − k], sonra y[n] = Σ a_k y[n − k] + v[n].
- **Doğrudan biçim II (kanonik):** H1 ve H2'nin sırası değiştirilerek w[n] = Σ a_k w[n − k] + x[n] ve y[n] = Σ b_k w[n − k]; gecikme elemanı sayısı en azdır. Örneğin tek kutuplu sistem için w1[n] = a·w1[n−1] + x[n], y[n] = b0·w1[n] + b1·w1[n−1]. Sinyal akış şemasından dalga değişkenleri (w1[n], w2[n], …) yazılıp z dönüşümüyle birim dürtü tepkisinin elde edilmesi bir örnekle gösterilir.
- **Kaskat biçim:** H(z) birinci/ikinci dereceden bölümlerin çarpımıdır; ikinci dereceden bölümler pratiktir. Örnek:
  H(z) = (1 + 2z⁻¹ + z⁻²) / (1 − 0,75z⁻¹ + 0,125z⁻²) = (1 + z⁻¹)(1 + z⁻¹) / ((1 − 0,5z⁻¹)(1 − 0,25z⁻¹)); doğrudan biçim I ve II ile kaskat gerçeklemesi gösterilir.
- **Paralel biçim:** kısmi kesirlere ayırma. Aynı örnekte H(z) = 8 + 18/(1 − 0,5z⁻¹) − 25/(1 − 0,25z⁻¹) ve ikinci dereceden bölümlerle H(z) = 8 + (−7 + 8z⁻¹)/(1 − 0,75z⁻¹ + 0,125z⁻²).
- **Transpoze biçim:** sinyal akış şemasının tüm dalgalarının yönü değiştirilip giriş ile çıkış yer değiştirirse giriş-çıkış ilişkisi değişmez.

### FIR sistemler için ağ yapıları

Doğrudan biçim I; doğrudan biçim II (I'in transpozesi); kaskat biçim H(z) = Π (b0k + b1k z⁻¹ + b2k z⁻²); doğrusal fazlı FIR sistemler için **kafes biçimi** (h[n] dizisinin simetrik olması gerekir; M çift ve tek durumları ayrı).

## II. IIR süzgeçlerin tasarımı

Amaç, verilen bir frekans yanıtını yaklaşık olarak sağlayan gerçeklenebilir bir G(z) elde etmektir; derste yalnızca genlik yaklaşıklığı ele alınır.

Dört ideal süzgecin dürtü yanıtları nedensel olmadığından ve sonsuz uzunlukta olduğundan gerçeklenemez. Pratikte genlik yanıtı geçirme ve söndürme bandında kabul edilebilir toleranslarla belirtilir; arada **geçiş bandı** vardır. Alçak geçiren süzgeç için: ωp geçirme bandı kenarı, ωs söndürme bandı kenarı, δp geçirme bandındaki en büyük dalgalanma, δs söndürme bandındaki en küçük dalgalanma. Kayıp fonksiyonu A(ω) = −20·log10|G(e^jω)|; αp = −20·log10(1 − δp) ve αs = −20·log10(δs). Hz cinsinden verilen kenar frekanslar örnekleme frekansı F_T ile radyana çevrilir (ω = 2πF/F_T).

En sık kullanılan yöntem: (1) sayısal süzgeç karakteristikleri prototip analog alçak geçiren süzgeç karakteristiklerine dönüştürülür; (2) analog Ha(s) belirlenir; (3) Ha(s) sayısal G(z)'ye dönüştürülür. Nedeni: analog süzgeç tasarımı çok gelişmiştir ve tabloları vardır.

### Analog süzgeç türleri

1. **Butterworth:** |Ha(jΩ)|² = 1 / (1 + (jΩ/jΩc)^(2N)); kutuplar s_k = Ωc·e^(jπ(2k + N + 1)/2N).
2. **Chebyshev:** |Ha(jΩ)|² = 1 / (1 + ε²·V_N²(Ω/Ωc)), V_N(x) = cos(N·cos⁻¹x).
3. **Eliptik.**

### Analog süzgeçten sayısal süzgece dönüşüm

- **Değişmez dürtü cevabı yöntemi:** h[n] = Td·ha(nTd). Ha(s) = Σ A_k/(s − s_k) ise H(z) = Σ Td·A_k / (1 − e^(s_k·Td)·z⁻¹); s düzlemindeki s_k kutupları z düzleminde e^(s_k·Td) kutularına gider. Örnek: 0,89125 ≤ |H(e^jω)| ≤ 1 (0 ≤ ω ≤ 0,2π) ve |H(e^jω)| ≤ 0,17783 (0,3π ≤ ω ≤ π), Td = 1 için Butterworth tasarımında N = 5,8858 ≈ **6** ve Ωc = 0,70474 bulunur; 6. derece Ha(s) = 0,12093 / [(s² + 0,364s + 0,4945)(s² + 0,9945s + 0,4945)(s² + 1,3585s + 0,4945)]; sonuç üç ikinci dereceden bölümden oluşan H(z)'dir.
- **Çift doğrusal dönüşüm (ÇDD):** örtüşme ve kararlılığı etkileyen etmenler nedeniyle daha sık kullanılır: s = (2/T)·(1 − z⁻¹)/(1 + z⁻¹). Sol yarı s düzlemi birim çemberin içine, sağ yarı dışına, jΩ ekseni birim çembere dönüşür; yani kararlı analog fonksiyon kararlı sayısal fonksiyona dönüşür. Frekans ilişkisi Ω = (2/T)·tan(ω/2) doğrusal değildir ve **frekans bükmesi (frequency warping)** yaratır. Tasarım adımları: (1) kenar frekanslara ön bükme uygula (Ωp, Ωs bul); (2) analog süzgeci tasarla; (3) ÇDD ile G(z)'yi elde et. ÇDD yalnız parçalı sabit genlik yanıtlı süzgeçler için kullanılabilir ve analog süzgecin faz yanıtını korumaz. Aynı örnekte ÇDD ile N = 5,305 ≈ 6 ve Ωc = 0,766 bulunup H(z) = 0,0007378(1 + z⁻¹)⁶ / [(1 − 1,2686z⁻¹ + 0,7051z⁻²)(1 − 1,0106z⁻¹ + 0,3583z⁻²)(1 − 0,9044z⁻¹ + 0,2155z⁻²)] elde edilir.
- **Uygunlaştırılmış z dönüşümü** üçüncü yöntem olarak anılır. Sunum, ωp = 0,25π, ωs = 0,55π, αp = 0,5 dB, αs = 15 dB'lik bir alçak geçiren Butterworth tasarımıyla biter.

## III. FIR süzgeçlerin tasarımı

FIR tasarımı, belirtilen genlik yanıtının doğrudan yaklaşıklığına dayanır; genelde doğrusal faz istenir. N. dereceden FIR tasarımı (N + 1) uzunluklu dürtü yanıtı katsayıları {h[n]} ya da frekans yanıtının (N + 1) örneğini bulmaktır. Yöntemler: pencerelenmiş Fourier serisi, frekans örnekleme, bilgisayar tabanlı eniyileme (Parks–McClellan).

- FIR tasarımı ayrık bir işlemdir; analog bölgede eşdeğeri yoktur; tanımlar çoğunlukla zaman bölgesindedir.
- İki avantaj: **kararlılık** ve **doğrusal faz**; aynı özellikli IIR'ye göre katsayı sayısı (derece) çok daha fazladır.
- En basit FIR süzgeç **kayan ortalama (moving average)** süzgecidir: genlik cevabı bakımından oldukça zayıf bir alçak geçirendir ve bant genişliği yalnızca derece ile kontrol edilir.
- Süzgeç denklemi y[n] = Σ_{k=0}^{N−1} b_k x[n − k]; girişe dürtü uygulanırsa katsayılar dürtü cevabının örneklerine eşit olur (b_k = h[k]). Dürtü cevabı simetrik olan nedensel FIR süzgeçler doğrusal fazdadır (çift simetri N = 2n + 2, tek simetri N = 2n + 1).

**Beş aşamalı tasarım:** (1) özellikler belirlenir (geçirme bandı kenarı, söndürme bandı kenarı, kesim frekansı, dalgalanmalar); (2) katsayılar hesaplanır; (3) yapı belirlenir; (4) (isteğe bağlı) benzetim; (5) uygulama.

### Pencereleme yöntemi

h[n] = h_d[n]·w[n]. Önce ideal süzgecin katsayıları h_d[n] = sin(nω_c)/(nπ) hesaplanır (n = 0 için 2f_c); sonuç, h_d'nin frekans bölgesinde pencere yanıtıyla dairesel evrişimidir. Sonra pencere seçilir:

| Pencere | Ana lob genişliği | Yan lob tepesi |
|---|---|---|
| Dikdörtgen | 4π/M | −13 dB |
| Bartlett | 8π/M | −25 dB |
| Hanning | 8π/M | −31 dB |
| Hamming | 8π/M | −41 dB |
| Blackman | 12π/M | −57 dB |

Dikdörtgen pencere en basit olanıdır (w[n] = 1, 0 ≤ n ≤ M), keskin ana lobu fakat geniş yan lobları ve süreksizlik çevresinde büyük salınımı vardır. Hamming, Hanning'den ve Bartlett'ten iyi, Blackman'dan basittir; Blackman'ın yan lobları en iyidir ama denklemi karmaşıktır.

### Frekans örnekleme yöntemi

Frekans cevabı H(e^jω)'nın 0–2π aralığından eşit aralıklı N örnek H_k seçilir ve ters AFD alınır: h[n] = (1/N) Σ_{k=0}^{N−1} H_k·W_N^(−nk), n = 0, 1, …, N − 1. Sunum bu yöntemi örneklerle çözer.
