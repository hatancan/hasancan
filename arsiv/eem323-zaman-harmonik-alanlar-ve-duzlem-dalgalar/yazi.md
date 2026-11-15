---
baslik: EEM323 Elektromanyetik II: Zaman-Harmonik Alanlar, Helmholtz Denklemi ve Düzlem Dalga Yayılımı (Prof. S. Gökhun Tanyer)
ozet: Prof. Dr. S. Gökhun Tanyer'in EEM323 dersinde zaman-harmonik alanlar ve Helmholtz dalga denklemi, düzlem dalga yayılımı, faz hızı, eikonal denklemi ve Fermat ilkesi notlarının metin özeti; ödevler dahil.
---

Prof. Dr. S. Gökhun Tanyer'in **EEM 323 Elektromanyetik II** dersinde (2013–2014 güz, Kasım 2013) işlediği üç notun metin içeriği: zaman-harmonik alanlar ve dalga denklemleri, düzlem dalga yayılımının iki bölümü. Şekiller ve çoğu denklem görseli çoğaltılmamıştır.

## 1. Zaman-harmonik alanlar ve dalga denklemleri

Alanın yalnız **tek bir frekans bileşeni** içerdiği varsayılır (diğer frekanslar benzer biçimde incelenir). Alanlar fazör gösterimiyle yazılır: E(x, y, z; t) = Re{E(x, y, z) e^{jωt}}, H için de aynısı; diğer tüm vektör alanlar da vektör fazörlerdir. Hocanın fazörlerle ilgili vurguları:

- Fazörler frekansın değil yalnız konumun fonksiyonudur; yalnızca tek bir f değeri için geçerlidir.
- Ani (anlık) zaman fonksiyonları karmaşık sayı içeremez (elektrik alan V/m cinsinden gerçek bir değer olmalıdır).
- j içeren her elektromanyetik ifade zorunlu olarak fazörler arasındaki bir bağıntıdır.

Fazörler Maxwell denklemlerine konunca zaman türevleri basitçe jω çarpanına dönüşür: ∇ × E = −jωμH ve ∇ × H = jωεE (doğrusal, izotrop ortam). Bu "zincirleme alan üretimi" yalnızca sinüzoidal olduğu için, **enerji kaybı yoksa sonsuza dek sürebilir**; elektromanyetik dalga adı buradan gelir (hocanın kaynağı: kendi çalışması *Müziğin Doğası – Matematiğin Sesi*).

**Kayıpsızlık varsayımı:** genel olarak elektromanyetik dalga yayıldığı malzemede akım üretebilir ve güç harcanabilir; dalga ayrıca yayılırken yayılıp zayıflayabilir. İkisi de genliği azaltır. Malzeme kayıpsız varsayılırsa güç harcanması ihmal edilir.

**Helmholtz dalga denklemi** (kayıpsız, basit, yani doğrusal ve izotrop ortamda): E'nin bukle denklemlerinden ∇ × (∇ × E) = ω²με E bulunur; ∇ × ∇ × E = ∇(∇·E) − ∇²E = −∇²E özdeşliği kullanılarak

> ∇²E + k²E = 0, k = ω√(με) = 2π/λ (rad/m)

elde edilir. n = k/k₀ **kırılma indisi**dir; u = 1/√(με) ortamdaki ışık hızı, boşlukta 1/√(μ₀ε₀) = 300.000 km/s'dir.

**Ödevler (hocanın soruları):**

1. Doğrusal, izotrop ve kaynaksız bölgede manyetik alan şiddeti H için Helmholtz dalga denklemini türetiniz.
2. Hem E hem H dalga denklemi için λ → ∞ limit durumunu inceleyiniz; Maxwell denklemlerini bu limitte çözümleyip Helmholtz denklemini yeniden hesaplayınız ve sonuçları yorumlayınız.

Not ayrıca skaler dalga (Helmholtz) denklemlerine değiniyor ve sonraki düzlem dalga dersine "ön izleme" yapıyor.

## 2. Düzlem dalga yayılımı – 1

**+z yönünde yayılan düzlem dalga.** Kartezyen koordinatlarda skaler Helmholtz denklemi ∂²/∂x² + ∂²/∂y² + ∂²/∂z² + k² = 0 biçimindedir. Alan yalnız x yönünde bileşene sahipse ve ∂/∂x = ∂/∂y = 0 ise denklem d²E_x/dz² + k²E_x = 0'a iner. Çözüm, z yönünde yayılan x-polarizasyonlu düzlem dalgadır: yalnız +z yönünde ilerleyen dalga alınırsa E_x(z, t) = E₀ cos(ωt − kz).

**Keyfi yönde yayılan dalga.** Aynı analiz, birim yön vektörü R = aₓα + a_yβ + a_zγ ile belirlenen keyfi yönde ilerleyen düzlem dalga için de geçerlidir; α, β, γ **yön kosinüsleri**dir ve α² + β² + γ² = 1.

**Düzgün (uniform) faz cepheleri.** Dalga düzgün değilse dalga cephesi düzlemsel olmaz. Dalga cephesi, fazın bir s değerine eşit olduğu yüzeydir (faz = ks, radyan cinsinden; s, λ'nın katlarıysa faz 2π'nin aynı katlarıdır). S(r) fonksiyonu dalga cephesini tanımlar; dışarı yayılan dalga cos(ωt − kS(r)) biçiminde yazılır.

**Faz hızı.** Dalga ilerlerken t, t + Δt olur ve r, r + Δr olur. Dalga üzerinde aynı sabit fazda "dalgayla birlikte yürüyen" bir gözlemci için ωt − kS(r) = ω(t + Δt) − kS(r + Δr) olmalıdır, yani ωΔt = k[S(r + Δr) − S(r)]. Fazdaki fark, S'nin birim yön vektörü boyunca yönlü türevidir: ΔS = ∇S · n̂ Δs. Buradan faz hızı u_p = Δs/Δt = ω/(k|∇S|) bulunur: faz hızı ∇S yönünde en büyüktür. Hocanın notu: fizikte hız vektör, sürat skalerdir; fakat "faz hızı" skaler bir niceliktir.

**Işın yaklaşımı ve eikonal denklemi.** Yerel düzlemsel dalga yapısı Helmholtz denklemine konunca |∇S|, kırılma indisine eşit çıkar; yönü n̂ olduğuna göre

> ∇S(r) = n n̂ (eikonal denklemi)

Bu, eşit faz yüzeylerinin dalga cephelerini oluşturduğunu, dalga cephelerinin yayılma yönüne dik olduğunu ve yaklaşımın büyük dalga sayılarında (küçük dalga boyunda, yani yüksek frekansta) doğru olduğunu söyler. n konuma bağlıysa (dielektrik sabiti ε konumun fonksiyonuysa) ışınlar eğrilir. Yaklaşım en çok lazerler için doğrudur; dalga yayılımının yerel olarak küçük düzlem dalgalar gibi davranması fikri Christiaan Huygens'e dayanır.

**Fermat ilkesi.** Dalganın a ve b noktaları arasındaki yolu alma süresi T = (1/c)∫ n ds ile verilir (c boşlukta ışık hızı, ds ışın boyunca sonsuz küçük yer değiştirme, v = ds/dt ve n = c/v). **Optik yol uzunluğu** ∫ n ds saf geometrik bir niceliktir; yol süresiyle T = (optik yol)/c ilişkilidir. Pierre de Fermat'nın (1601–1665) tarihsel ifadesi eksiktir; tam modern ifade: "ışığın iki sabit nokta arasında izlediği yolun optik uzunluğu bir ekstremumdur; optik uzunluk, fiziksel uzunluğun malzemenin kırılma indisiyle çarpımıdır."

## 3. Düzlem dalga yayılımı – 2

9 slaytlık not, bir **örnek** çözüyor: elektrik alanı x polarizasyonlu ve +z yönünde yayılan bir dalga için vektör dalga denklemi çözülüp sonuçlar yorumlanıyor (çözüm adımları denklem görselleriyle verilmiştir). Sonraki konular: Doppler etkisi ve elektromanyetik dalgaların polarizasyonu.

## Kaynak notu

Bu yazı, Prof. Dr. S. Gökhun Tanyer'in Başkent Üniversitesi EEM 323 Elektromanyetik II dersi (2013–2014 güz) için hazırladığı ders sunumlarındaki **hocanın kendi metin içeriğinin** (başlıklar, anlatım, sorular, ödevler) özetlenip yazıya dökülmüş hâlidir (OGR-EEM323-DN-2D-TimeHarmonicFields, 2E-PlaneWaves-1, 2F-PlaneWaves-2). Sunumlardaki şekiller, tablolar ve denklem görselleri, sunumların kendi ifadesine göre D. K. Cheng'in ders kitaplarından (*Fundamentals of Engineering Electromagnetics*, *Field and Wave Electromagnetics*) alınmıştır; bu yüzden **burada çoğaltılmamıştır** ve orijinal sunum dosyası indirmeye açılmamıştır. Şekil ve ayrıntılı türetmeler için Cheng'in kitabına bakılmalıdır.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*
