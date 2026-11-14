---
baslik: EEM401 Sayısal Sinyal İşleme: Ders Tanıtımı, Ayrık Zamanlı İşaretler ve Sistemlerin Sınıflandırılması
ozet: Yrd. Doç. Dr. Selda Güney'in EEM401 Sayısal Sinyal İşleme dersinin ilk iki sunumu: ders içeriği ve kaynaklar, sinyal türleri (analog, sayısal, periyodik, enerji ve güç), ayrık zamanlı sistemlerin sınıflandırılması (doğrusallık, zamanla değişmezlik, nedensellik, BIBO kararlılığı).
---

2014–2015 güz yarıyılında Başkent Üniversitesi'nde **Yrd. Doç. Dr. Selda Güney**'den aldığım **EEM401 Sayısal Sinyal İşleme** dersinin ilk iki sunumu (Lecture 1 ve Lecture 2) bu yazıda özetleniyor. Ders slaytlarında adı "EEM 401 Sayısal Sinyal İşleme" olarak geçer (PDF özelliklerinde "Sayısal İşaret İşleme"); klasörün adı olan "Elektromanyetik Dalgalar" yanlıştır. Sunumların orijinali yazının sonunda ZIP olarak indirilebilir.

## Ders tanıtımı

**Kaynaklar:**

1. A. V. Oppenheim ve R. W. Schafer, *Discrete-Time Signal Processing*, Prentice Hall, 3. baskı, 2009
2. S. K. Mitra, *Digital Signal Processing: A Computer Based Approach*, McGraw-Hill, 4. baskı, 2011
3. J. G. Proakis ve D. G. Manolakis, *Sayısal Sinyal İşleme: İlkeler, Algoritmalar ve Uygulamalar*, Pearson/Prentice Hall, 4. baskı, 2010

**İçerik:** ayrık zamanlı işaretler ve sistemler (ana diziler, örnekleme, temel işlemler); ayrık zamanlı sistemler ve sınıflandırılması; ayrık zamanlı Fourier dönüşümü; ayrık zamanlı Fourier serisi; frekans bölgesinde örnekleme; hızlı Fourier dönüşümü; frekans bölgesinde sistem transfer fonksiyonu; z dönüşümü ve uygulamaları; sayısal süzgeç tasarım teknikleri; FIR ve IIR süzgeç tasarım yöntemleri.

**Sayısal sinyal işleme**, bir işaretin sayısal bilgisayarlarda ya da özel amaçlı sayısal donanımda bir sayı dizisi olarak gösterilmesine ve bu dizi üzerinde çeşitli işlemler yaparak istenen bilginin dizi içinden çıkarılmasına dayanır. Amaçlar arasında sinyalleri güçlendirmek, filtrelemek, örüntü algılamak, sinyali iletişim kanalına hazırlamak, diğer sinyallerin girişimini engellemek ve algılayıcıların eksikliklerini gidermek sayılır.

- **Avantajlar:** örneklemeden sonra gürültü kontrolü, yüksek doğruluk, karmaşık algoritmalar, esneklik (parametre değişimi), elektromanyetik girişim, çevre koşulları ve yaşlanma gibi etkilere duyarsızlık.
- **Dezavantajlar:** ayrık zaman artifaktları, daha fazla güç gereksinimi, sayısal saat ve anahtarlama girişimi.

Sistemin blok şeması: analog giriş → A/D dönüştürücü → sayısal giriş sinyali → sayısal sinyal işleyici → sayısal çıkış → D/A dönüştürücü → analog çıkış.

## 1. Ayrık zamanlı sinyaller ve sınıflandırılması

### Sinyal türleri ve tanımlar

**Sinyal (işaret)**: bir fiziksel olayda bulunan bağımsız değişkenlerle aralarındaki ilişkinin matematiksel olarak biçimlendirilmiş hâlidir (örneğin bir devre elemanı uçlarındaki gerilimin zamanla değişimi, ses şiddeti, sıcaklık).

Sınıflandırmalar: sürekli (analog) – ayrık; periyodik – periyodik olmayan; enerji – güç; rastlantı – deterministik sinyaller.

- **Analog sinyal**: hem zamana hem genliğe göre süreklidir (EKG, EMG, EEG, radar ve ses işaretleri). **Sayısal sinyal**: ayrık zamanlarda genliği ayrık değerler alabilen sinyaldir.
- **Periyodik işaret**: f(t) = f(t + T). Ayrık periyodik işaret için N pozitif tamsayı olmak üzere f[n] = f[n + N]. EKG ve ses periyodik olmayan işaretlere örnektir.
- **Enerji işareti**: Σ |f[n]|² (ya da ∫ |f(t)|² dt) sonlu ise. **Güç işareti**: P = lim (1/(2M+1)) Σ |f[n]|² sonlu ve sıfırdan büyükse.
- **Rastlantı sinyalleri**: şimdiki ve gelecekteki değerleri geçmişten hesaplanamaz ya da tahmin edilemez. **Deterministik sinyaller**: değerleri geçmiş değerlerden hesaplanabilir, kesin bir matematiksel formülle ifade edilebilir.

İçindekiler listesinde ayrıca ana ayrık sinyaller, sinyaller üzerinde basit matematiksel işlemler ve analogdan sayısala/sayısaldan analoga dönüştürme başlıkları vardır.

## 2. Ayrık zamanlı sistemler ve sınıflandırılması

Ayrık zamanlı sistem, giriş dizisi denen bir diziyi çıkış dizisine çeviren yazılım ya da donanımların karışımıdır. Sınıflandırma:

- **Deterministik ve stokastik** sistemler: giriş ve çıkış deterministikse deterministik, rastlantısalsa stokastik.
- **Durağan (statik/belleksiz) ve dinamik** sistemler: n anındaki çıkış yalnızca aynı andaki girişe bağlıysa sistem belleksizdir. Örnekler: y[n] = a·x[n] ve y[n] = n·x[n] + b·x³[n] statik ve belleksizdir (geçmiş giriş ya da çıkışı saklamak gerekmez). Diğer durumlarda sistem dinamiktir (belleği vardır).
- **Zamanla değişen ve değişmeyen** sistemler: x[n] → y[n] ise x[n − k] girişi y[n − k] çıkışını veriyorsa sistem zamanla değişmezdir. Test iki deneyle yapılır: (1) x[n] → y[n]; (2) x[n − k] → y_k[n]; sonra y_k[n] = y[n − k] mi diye bakılır.
- **Doğrusal ve doğrusal olmayan** sistemler: toplamsallık (T{x1 + x2} = y1 + y2) ve ölçekleme (T{a·x1 + b·x2} = a·y1 + b·y2) ilkelerini sağlayan sistem doğrusaldır. y = x² ve y = cos x doğrusal değildir.
- **Nedensel ve nedensel olmayan** sistemler: n anındaki çıkış yalnızca şimdiki ve geçmiş girişlere (x[n], x[n − 2]) bağlıysa, gelecek girişlere (x[n + 1], x[n + 2]) bağlı değilse nedenseldir. Gerçek zamanlı uygulamalarda sinyalin gerçek değerini bilemeyeceğimiz için nedensel olmayan sistem gerçeklenemez.
- **Kararlı ve kararsız** sistemler: kararlılık pratik uygulamalarda önemli bir özelliktir; kararsız sistemler genellikle sıra dışı uç davranışlar sergiler. Gevşek bir sistem, her sınırlı girişe sınırlı çıkış veriyorsa **BIBO (bounded input – bounded output)** kararlıdır: |x[n]| ≤ Mx < ∞ ise |y[n]| ≤ My < ∞. Sınırlı bir x[n] için y[n] sınırsızsa sistem kararsızdır.
- **Geribeslemeli ve geribeslemesiz** sistemler.

Kararlılık, nedensellik ve doğrusallık sınaması için sınavlardaki uygulamalar ilerleyen yazılarda (kısa sınav 1, ara sınav) yer alıyor.
