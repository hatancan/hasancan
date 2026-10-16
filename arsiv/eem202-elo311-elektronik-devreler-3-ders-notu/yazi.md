---
baslik: EEM202 Devre Teorisi II: ELO-311 Elektronik Devreler III Ders Notu, Analog Elektronik II (Kaplan, 2010-2011)
ozet: "ELO-311 Elektronik Devreler III" ders notu (2010-2011, sayfa başlıklarında "Analog Elektronik - II, Kaplan"): op-amp tanıtımı ve karakteristikleri, farksal yükselteç, eviren ve evirmeyen yükselteç, fark alıcı, gerilim izleyici, türev ve integral alıcı, karşılaştırıcılar, aktif filtreler, multivibratörler ve gerilim/akım dönüştürücüleri.
---

Bu yazı, ders klasöründe saklanan **"ELO-311 Elektronik Devreler III – Ders Notu – 2010-2011"** başlıklı 72 sayfalık belgeyi tanıtıyor (PDF Ekim 2010). Sayfa başlıklarında **"Analog Elektronik - II"** ve **"Kaplan"** adı geçiyor; belgede kurum adı yok. Not işlemsel yükselteçler (opamp) üzerine; EEM202 laboratuvarındaki aktif süzgeç ve op-amp çalışmaları için ek kaynak olarak klasörde duruyor. Aşağıda bölümler ve ana noktalar özetlendi; orijinal PDF yazının sonunda indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Bölüm 1: İşlemsel yükselteçler

### 1.1 Opamp'ın tanıtılması

Elektronik endüstrisinde üretilen ilk tümdevre bir opamp'tır: 1963'te Fairchild firması tarafından µA702 koduyla üretilmiştir. Opamp'lar geniş frekans sınırlarında sinyal yükseltmek için tasarlanmış, doğrudan eşlemeli ve yüksek kazançlı gerilim yükselteçleridir; proses kontrol, haberleşme, bilgisayar, güç ve işaret kaynakları, ölçü sistemleri gibi pek çok alanda kullanılır. Bölümde opamp sembolü ve terminalleri (eviren "−" ve evirmeyen "+" girişler, besleme bağlantıları), tipik kılıflar, üreticilerin kodlama sistemi, ideal ve pratik opamp özellikleri anlatılıyor.

### 1.2 Farksal (diferansiyel) yükselteç

Opamp'ın giriş katını oluşturan transistörlü farksal yükseltecin yapısı, çalışma karakteristikleri ve fark/ortak işaret kazançları.

### 1.3 Opamp karakteristikleri

Giriş ofset gerilimi ve akımı, giriş polarma akımı, açık çevrim kazancı ve frekans cevabı, değişim hızı (slew rate) ve tam güç bant genişliği, CMRR gibi parametreler. Örnek problemlerden: "Opamp'ın maksimum fark giriş gerilimini bulunuz", "V_oSAT = ±12 V'luk çıkış için tam güçteki bant genişliğini bulunuz".

## Bölüm 2: Temel opamp devreleri

- **2.1 Eviren ve evirmeyen yükselteç:** kapalı çevrim kazancı A_CL, ±12 V'luk simetrik kaynakla beslenen devrelerde çıkış gerilimi ve opamp'tan çekilen akım problemleri.
- **2.2 Temel fark alıcı:** iki girişin farkını yükselten devre; yük akımı I_L problemleri (R1 = R2 = R3 = R_f = 10 kΩ, R_L = 1 kΩ veya 10 kΩ).
- **2.3 Gerilim izleyici.**
- **2.4 Türev ve integral alıcı:** girişine 2 kHz'lik üçgen dalga ve kare dalga uygulanan devrelerde çıkış dalga biçiminin analizi.

## Bölüm 3: Opamp uygulamaları

- **3.1 Gerilim karşılaştırıcıları (komparatör):** girişlerden birine referans, diğerine karşılaştırılacak işaret uygulanır; referansın polaritesine göre pozitif, negatif ve sıfır gerilim seviye dedektörleri ve gürültülü bir girişte dedektör analizi; örnek devrede R1 = 2 kΩ, R2 = 10 kΩ, R_L = 1 kΩ.
- **3.2 Aktif filtreler:** alçak geçiren, yüksek geçiren, bant geçiren ve bant söndüren olmak üzere dört tip aktif filtre; kesim frekansında kazancın 0,707'ye düştüğü bant tanımı.
- **3.3 Multivibratörler:** opamp'la kurulmuş **astable** (kararsız, kare dalga üreteci) ve **monostable** (tek kararlı) multivibratörler; monostable devrenin kararlı hal, geçiş hali ve dönüş konumları ile giriş-çıkış dalga biçimleri.
- **3.4 Gerilim/akım ve akım/gerilim dönüştürücüleri:** endüstride basınç, sıcaklık, debi gibi büyüklükleri ölçen sensörlerin çıkışları standart akım veya gerilim değerlerine dönüştürülür ve bunların birbirine çevrilmesi gerekir; bu işlevler opamp'lı **gerilim/akım** ve **akım/gerilim** dönüştürücüleriyle yapılır.

## İndirilebilir dosya

72 sayfalık orijinal PDF aşağıdan indirilebilir.
