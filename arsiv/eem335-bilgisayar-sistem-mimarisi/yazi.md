---
baslik: EEM335 Bilgisayar Organizasyonu: Bilgisayar Sistem Mimarisi (Doç. Dr. Yalçın Çebi Ders Sunumu)
ozet: Bilgisayar sistem mimarisi ders sunumu: von Neumann mimarisi, 7 katmanlı mimari modeli, veriyolu türleri, transistörün gelişimi, PMOS/NMOS/CMOS, mantık kapıları, tümleşik devreler, işlemci yazmaçları (MDR, MBR, MAR).
---

Bu yazı, EEM335 Bilgisayar Organizasyonu klasöründe bulunan 53 slaytlık **"Bilgisayar Sistem Mimarisi"** sunumunun özetidir. Sunumun her slaytında **Doç. Dr. Yalçın Çebi** adı yazıyor; hazırlanış yılı ve kurum bilgisi belgede yok.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

Sunumun tamamı (slayt PDF'i) yazının sonunda indirilebilir.

## Bilgisayar mimarisi ve von Neumann

Bilgisayar mimarisi, bilgisayar sistemindeki tüm parçaların tasarım ve düzenlenme şeklidir. Neredeyse tüm bilgisayarlarda benzer donanım bileşenleri kullanılır ve modern bilgisayarlar temelde **von Neumann mimarisine** dayanır. John von Neumann bilgisayar organizasyonunu 1950'lerde öngörmüş ve biçimsel hâle getirmiştir. Mimari üç ana bileşen tanımlar:

- **Giriş/çıkış birimleri:** kullanıcının komut girip sonuç görmesini sağlar.
- **Bellek:** işlenecek bilgileri, programları ve deyimleri depolar.
- **İşlemci (Merkezi İşlem Birimi):** verileri önceden programlanmış aşamalarla işler.

Üç birim **veriyolu (bus)** ile bağlıdır, tüm iletişim elektronik sinyallerle olur. Bu mimariyi kullanan bilgisayarlara **depolanmış program bilgisayarları** denir: aynı anda birden fazla program ve veri belleğe yüklenebilir, işlemci bunlar arasında geçiş yapabilir.

## Yedi katmanlı mimari

| Katman | Ad | Grup |
|---|---|---|
| 7 | Uygulama katmanı | Yazılım |
| 6 | Yüksek seviyeli yazılım katmanı | Yazılım |
| 5 | İşletim sistemi katmanı | Yazılım |
| 4 | Makine katmanı | Donanım |
| 3 | Mikroprogram katmanı | Donanım |
| 2 | Sayısal mantık katmanı | Donanım |
| 1 | Fiziksel aygıt katmanı | Donanım |

- **Fiziksel aygıt:** transistör, kapasitör ve dirençler; en karmaşık bilgisayar bile bunların birleşiminden oluşur.
- **Sayısal mantık:** verileri ikili gösterimle depolayıp işleyen **kapılar (gate)**; birçok kapı tek yonga üzerinde birleşerek işlemciyi oluşturur.
- **Mikroprogram:** makine dilindeki deyimleri yorumlar; ROM'daki basit program deyimlerine **mikrokod**, oluşan programa **mikroprogram** denir. Üreticiler aynı makine katmanını farklı yollarla işleyerek farklı hız ve fiyatta işlemciler sunabilir; yazılımlar bilgisayarlar arasında taşınabilir. İlk kuşak ve bazı küçük bilgisayarlarda bu katman yoktur.
- **Makine katmanı:** program yazılabilen en alt katmandır; deyimler donanımca doğrudan işlenir.
- **İşletim sistemi:** donanımın karmaşıklığını yazılımdan gizler, donanımı yazılım hatalarından korur.
- **Yüksek seviyeli yazılım:** makine diline çevrilmesi gereken deyimlerin katmanı.
- **Uygulama:** kullanıcının gördüğü en üst katman.

## Veriyolu ve bilgisayar türleri

Veriyolu, üzerine değişik bileşenler bağlanabilen paralel iletkenlerdir; veri, adres, kontrol sinyallerini ve gücü taşır. **İç veriyolu** işlemcinin içindedir; **dış veriyolu** ayrı donanım elemanlarını bağlar. Mimariye göre üç tür bilgisayar: **tek yongalı** (saat, kamera gibi özel işlerde), **tek kartlı** (kişisel bilgisayarlar ve kontrol sistemleri; PCB üzerinde) ve **çok kartlı, veriyolu tabanlı** (minibilgisayar ve ana bilgisayarlar; her kart ayrı görevde). Çalışırken kart takıp çıkarmaya **sıcak değişim (hot-swap)** denir.

En temel veriyolu mimarisinde tüm bileşenler tek genel amaçlı veriyolundadır (basit ama G/Ç aygıtları işlemci-bellek aktarımını yavaşlatır); **iki veriyollu** mimaride G/Ç ayrı bir veriyolundadır.

## Transistörün gelişimi

- Pascal'ın Pascaline'i (1642) ve Babbage'in Analitik Makinesi (1833) tümüyle mekaniktir; modern bilgisayarlar elektriklidir. Elektrik akımını denetleyen temel aygıt **anahtardır**.
- 1930'larda elektromanyetik aktarıcılar, 1950'lerde vakum tüpleri anahtar görevi yaptı; tüpler çok ısındı ve çabuk bozuldu.
- **1948'de AT&T Bell Laboratuvarları'nda John Bardeen, Walter Brittain ve William Shockley ilk transistörü** üretti (1956 Nobel Fizik Ödülü). 1953'te transistörlü ilk ticari ürün (işitme cihazı), 1954'te ilk transistörlü radyo, bir yıl sonra tümüyle transistörlü ilk bilgisayar geldi.
- İlk transistör altın ve germanyumdan yapıldı; bugün silikon kullanılır. Germanyum ve silikon **yarıiletkendir**.
- **PMOS:** ilk hâlinde iletken, kontrol teline akım uygulanınca yalıtkan olur. **NMOS:** tersi; akım uygulanınca iletken olur. İkisinin birleşimi **CMOS**'tur.
- PMOS ve NMOS ile **DEĞİL (NOT)**, **VE (AND)** (X·Y) ve **VEYA (OR)** (X+Y) kapıları kurulur.

## Tümleşik devreler

Devreleri transistörlerin tek tek bağlanmasıyla üretmek seri üretime uygun değildi. **1958'de Texas Instruments'tan Jack Kilby ile Fairchild Semiconductor'dan Robert Noyce** birbirinden bağımsız olarak tüm transistörleri ve bağlantıları tek silikon tabakada toplama tekniğini geliştirdi (mikroçip, IC). 1959'da patent aldılar, sonra karşılıklı kullanım hakkı değiştirdiler. Noyce daha sonra Intel'i kurdu; Kilby 2000'de Nobel Fizik Ödülü aldı.

## İşlemci ve yazmaçlar

İşlemci **Kontrol Birimi (CU)** ve **Aritmetik Mantık Birimi (ALU)** ile çalışır; bellek denetimi, işlem sıralaması, komut verme ve verilerin girilip işlenip çıkışa aktarılması görevleridir. **Yazmaçlar** işlemci veya diğer bileşenlerin içindeki özel amaçlı geçici bellek yerleridir:

- **Bellek Veri Yazmacı (MDR):** işlemcinin içindedir; işlemciye gelen/giden tüm veri ve deyimler buradan geçer.
- **Bellek Arabellek Yazmacı (MBR):** ana bellek içindedir; belleğe gelen/giden her şey buradan geçer.
- **Bellek Adres Yazmacı (MAR):** verinin ana bellekteki yerini belirten adresi tutar; adres veriyolu üzerinden belleğe gider, okuma/yazma bilgisi kontrol veriyoluyla iletilir.
