---
baslik: EEM214 Elektronik I: BJT ve MOSFET Ders Notları – NPN Çalışması, MOSFET DC Analizi, Küçük Sinyal Modelleri, Akım Aynaları (Keith W. Whites, EE 320, 2009)
ozet: Keith W. Whites'ın EE 320 Electronics I dersinden altı ders notu: BJT yapısı ve NPN'nin fiziksel çalışması, MOSFET sembolleri ve i_D–v_DS bölgeleri, MOSFET DC devre tasarım örnekleri, MOSFET yükselteç ve küçük sinyal π modeli, çözümlü yükselteç örnekleri, ayrık ve tümleşik devrelerde kutuplama ve MOSFET akım aynası.
---

Bu yazı, EEM214 Elektronik I dersinin klasöründe bulunan, **Keith W. Whites**'ın (South Dakota School of Mines and Technology) **EE 320 Electronics I** dersi için 2009 güz döneminde hazırladığı İngilizce ders notlarından transistörlerle ilgili altı tanesini (Lecture 10 ve 26–30) tanıtıyor. Notlar Sedra & Smith'in *Microelectronic Circuits* kitabını izliyor. Aşağıda her dersin ana fikirleri ve çözümlü örneklerin sonuçları Türkçe özetlendi; PDF'ler yazının sonunda ZIP olarak indirilebilir. Aynı yazarın diyot notları için: [Whites EE 320 diyot notları](/arsiv/eem214-whites-ee320-diyot-notlari/).

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Lecture 10: BJT Construction, NPN Physical Operation

Transistör üç uçlu bir elemandır; bir uçtaki akım ya da gerilim, diğer iki uç arasındaki akımı kontrol eder ("elektronik vana"). İki ana aile vardır: BJT ve FET (derste yaklaşık 13 ders BJT, 12 ders FET). BJT, silisyum üzerinde üç katkılı bölgeden (npn ya da pnp) oluşur; arka arkaya iki pn eklemi içerir: **emetör–baz eklemi (EBJ)** ve **kolektör–baz eklemi (CBJ)**. Bu çizim William Shockley'nin ABD patentine (2,569,347) kadar uzanır. Yapı simetrik görünse de değildir (eklem alanları ve katkılar farklıdır), bu yüzden ters aktif mod kolektör ile emetörün yer değiştirmesiyle aynı değildir. Eklemlerin durumuna göre dört mod vardır: kesim, aktif, doyum ve ters aktif. Sayısal devrelerde transistör kesim ile doyum arasında anahtarlanır, doğrusal yükselteçlerde aktif bölgede çalışır. Notun sonunda aktif moddaki npn transistörün fiziksel çalışması anlatılıyor.

## Lecture 26: MOSFET Circuit Symbols, i_D–v_DS Characteristics

Zenginleştirilmiş (enhancement) n kanallı MOSFET sembolünde oklu uç kaynağı ve okun yönü n tipini gösterir; kapıdaki boşluk oksit tabakasını temsil eder. Gövde genellikle kaynağa bağlıdır, bu yüzden daha basit bir sembol yaygındır. Üç çalışma bölgesi:

1. **Kesim:** v_GS < V_t, kanal yok, i_D = 0.
1. **Triyot:** v_GS > V_t ve kanal savak ucunda da sürekli (v_GD > V_t, yani v_DS < v_GS − V_t): i_D = k_n′(W/L)[(v_GS − V_t)v_DS − v_DS²/2]; küçük v_DS'te i_D ≈ k_n′(W/L)(v_GS − V_t)v_DS = v_DS / r_DS, yani gerilimle kontrol edilen bir direnç.
1. **Doyum:** kanal savak ucunda daralmış (v_GD ≤ V_t): i_D = ½k_n′(W/L)(v_GS − V_t)²; eleman ideal bir gerilim kontrollü akım kaynağı gibi davranır.

## Lecture 27: MOSFET Circuits at DC

- **Örnek N27.1:** I_D = 0.4 mA ve V_D = 1 V olacak tasarım (V_t = 2 V, µ_nC_ox = 20 µA/V², W/L = 400/10). V_GD = −1 V < V_t olduğundan doyum varsayılır; (V_GS − 2)² = 1'in uygun kökü **V_GS = 3 V**, V_S = −3 V ve −5 V kaynağa göre R_S = (−3 + 5)/0.4 mA = 5 kΩ.
- **Örnek N27.2:** Kapısı savağına bağlı MOSFET'te V_GD = 0 < V_t, doyum: (V_GS − 2)² = 4 ⇒ **V_GS = 4 V**, V_D = 4 V.
- **Örnek N27.3:** V_D = 0.1 V için tasarım (V_t = 1 V, k_n′W/L = 1 mA/V²); V_GS = 5 V ile kanal savakta kesilmediği için triyot bölgesi; r_DS hesaplanıyor.

## Lecture 28: MOSFET as an Amplifier, Small-Signal Equivalent Circuit Models

"Kavramsal" MOSFET yükseltecinde (V_GS ile kutuplama ve R_D) eleman doyumda kutuplanır ve tüm salınım boyunca v_GD ≤ V_t kalmalıdır. Kapıya v_gs eklenince i_D = ½k_n′(W/L)[(V_GS − V_t) + v_gs]² açılımındaki v_gs² terimi doğrusal olmadığından küçük kalmalıdır: v_gs << 2(V_GS − V_t). Bu koşulda akımın AC bileşeni i_d = g_m·v_gs, **g_m = k_n′(W/L)(V_GS − V_t)** (taşma gerilimi V_OV ile g_m = 2I_D/V_OV) ve kazanç A_v ∝ g_m. Doyumda MOSFET gerilim kontrollü akım kaynağıdır; küçük sinyal π modeli (kapı açık devre, savakta g_m·v_gs akım kaynağı ve ona paralel r_o = V_A/I_D) ve T modeli tanıtılıyor.

## Lecture 29: MOSFET Small-Signal Amplifier Examples

**Örnek N29.1:** Savaktan kapıya 10 MΩ geri beslemeli yükselteç (V_t = 1.5 V, k_n′W/L = 0.25 mA/V², V_A = 50 V, V_DD = 15 V, R_D = 10 kΩ). V_GS = V_DS olduğundan I_D = 1.25×10⁻⁴(15 − 10000·I_D − 1.5)²; iki kökten fiziksel olanı **I_D = 1.06 mA, V_GS = V_DS = 4.4 V**. g_m = 0.25 mA/V² × (4.4 − 1.5) = 0.725 mS; r_o ∥ R_D ∥ R_L ≈ 4521 Ω ile **A_v ≈ −3.28 V/V**; ardından giriş direncinin v_gs = 0 alınmadan, i_i'nin v_i cinsinden bulunarak hesaplanması gösteriliyor.

## Lecture 30: Biasing MOSFET Amplifiers, MOSFET Current Mirrors

Ayrık devrelerde kutuplama BJT'dekine benzer yöntemlerle yapılır; tümleşik devrelerde direnç ve büyük kondansatör pahalı olduğu için DC akım kaynakları kullanılır.

- **Örnek N30.1:** I_D = 1 mA, ±2 V savak salınımı ve 1 MΩ giriş direnci (k_n′W/L = 0.5 mA/V², V_t = 2 V). Kazancı büyütmek için V_D = 0 seçilir; V_GD,min = −2 V < V_t olduğundan salınım boyunca doyum korunur. V_G = 0, V_GS = 4 V, V_S = −4 V ve R_G = 1 MΩ.
- **MOSFET akım aynası:** Kapısı savağına bağlı Q1 doyumda çalışır; I_REF onun V_GS'ini belirler. Aynı V_GS'i paylaşan Q2'nin akımı I_O = I_REF·(W/L)₂/(W/L)₁ olur; tümleşik devrelerde bir "altın akım" bu yolla birçok kata kopyalanır.

## İndirme

ZIP dosyasında altı ders notunun orijinal PDF'leri (320Lecture10 ve 320Lecture26–30) bulunuyor.
