---
baslik: STAJ Yaz Stajı: DC/DC konvertörler bitirme tezi (Gazi Üniversitesi Teknik Eğitim Fakültesi, 2000)
ozet: Gazi Üniversitesi Teknik Eğitim Fakültesi'nde 2000 yılında hazırlanmış 77 sayfalık DC/DC konvertörler tezi: akım-gerilim yönüne göre sınıflandırma, düşürücü, yükseltici, düşürücü-yükseltici, CUK ve tam köprü konvertörler, flyback ve forward konvertörler, darbe yolvericili konvertörler.
---

Bu yazı, Gazi Üniversitesi Teknik Eğitim Fakültesi Elektronik-Bilgisayar bölümünün Elektronik programında, Yrd. Doç. Dr. Yılmaz Savaş'ın yönetiminde 2000 yılında hazırlanmış **"DC/DC Konvertörler"** başlıklı 77 sayfalık tezi tanıtır. Tez, staj dosyalarının arasında bulunuyordu ve konvertör devrelerinin kuramını derli toplu verir; TCDD EAM'de incelenen konvertör ve çevirici devreleriyle (bkz. [24 V/12 V konvertör testi](/arsiv/staj-tcdd-eam-24v-konvertor-testi-hemzemin-gecit-sema/)) konu bakımından ilgilidir. Tezin yazarının adı ve numarası, kapak ve jüri sayfası çıkarılarak yayınlanmamıştır; indirilebilir PDF'te bu iki sayfa boş bırakılmıştır. Tam metin, formüller ve şekiller için yazının sonundaki PDF'e bakın.

*Bu içerik üçüncü taraf bir kaynağa aittir (Gazi Üniversitesi Teknik Eğitim Fakültesi, 2000; yönetici Yrd. Doç. Dr. Yılmaz Savaş); arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Özet

Elektrik sistemlerinde bir yüke giden elektriksel gücün kontrol edilmesi gerekir. Güç kontrolünün yollarından biri, bir gerilim seviyesinden başka bir gerilim seviyesine güç dönüştürmektir. Alternatif akımda (AA) bu dönüşüm transformatörlerle verimli biçimde yapılır; ancak transformatörler doğru akım (DC/DC) güç dönüşümü için kullanılamaz. Tezde DC/DC konvertörlerin yük akımı ve gerilimine göre incelenmesi amaçlanmıştır; incelemenin büyük bölümü, anahtarlama modunda çalışan ve gerçekleştirdikleri işleme göre beş gruba ayrılan konvertör çeşitlerine ayrılmıştır.

Gücün DC/DC dönüşümünün verimli yapılabilmesi için anahtar mod konvertörlerine ihtiyaç vardır. Güç konvertörleri reaktif elemanlardan ve anahtarlardan oluşur; çalışma ilkesi, devrede kullanılan anahtarların iletim ve kesim sürelerinin ayarlanmasına dayanır. Yükü besleyen gerilimin frekansı büyük değerlerdeyse, yüke pratik olarak kesintisiz DC güç aktarımı mümkün olur. Bu tür konvertörlerin tatmin edici işletimi, reaktif elemanların uygun konfigürasyonuna ve uygun anahtarlama yöntemlerine bağlıdır.

*(Tezde İngilizce özet de bulunmaktadır.)*

## İçindekiler

**Bölüm 1: Giriş**

**Bölüm 2: DC-DC konvertörlerin sınıflandırılması**

1. Akım ve gerilimin akış yönüne göre konvertörler: A, B, C, D ve E sınıfı konvertörler
1. Gerçekleştirdiği işlem açısından konvertörler:
   düşürücü (buck) konvertör (sürekli akım durumu, sürekli ile kesintili iletim arasındaki sınır, kesintili iletim, çıkış gerilimindeki bozulmalar);
   yükseltici (boost) konvertör (sürekli iletim, sürekli/süreksiz iletim sınırı, süreksiz iletim, parazit yapıcı elemanların etkisi, çıkış gerilimi dalgacığı);
   düşürücü-yükseltici (buck-boost) konvertör (aynı alt başlıklar);
   CUK DC-DC konvertör;
   tam köprü (full-bridge) DC-DC konvertör (iki kutuplu ve tek kutuplu gerilim anahtarlamalı PWM)
1. DC-DC konvertörlerin karşılaştırılması

**Bölüm 3: Manyetik kuplajlı kıyıcılar:** flyback konvertör (devre analizi, sürekli akım durumu, kapasitör gerilimindeki dalgacık) ve forward konvertör (devre analizi, sürekli akım durumu, kapasitör gerilimindeki dalgacık)

**Bölüm 4: Darbe yolvericili ve rezonanslı konvertörler:** darbe yolvericili konvertör, üç tristörlü darbe yolvericili konvertör, şarj akımından bağımsız darbe yolvericili konvertör, rezonanslı darbe konvertörü

**Bölüm 5: Sonuç ve değerlendirme**, **Kaynaklar**

## Konvertörlerin karşılaştırılması (Bölüm 2.3)

Tezin karşılaştırma bölümüne göre düşürücü, yükseltici, düşürücü-yükseltici ve CUK konvertörlerin temel yapıları yalnızca **tek yönlü** enerji aktarımına izin verir; çünkü akım ve gerilimi tek yönde aktarabilirler. **Tam köprü** konvertörde V_o ve I_o'nun yönleri birbirinden bağımsız değiştirilebildiği için çok yönlü güç aktarımı mümkündür; eksenleri V_o ve I_o olan düzlemin dört kadranında da çalışabildiğinden DC/AC konvertör olarak da kullanılabilir. İncelenen konvertörlerin çalışmasından şu sonuçlara varılır:

1. Ortalama akım I_o tasarlanan maksimum değerindedir; bobin akımındaki dalgacık ihmal edilebilir (i_L(t) = I_L), bu da sürekli iletim sağlar.
1. Ortalama gerilim V_o tasarlanan maksimum değerindedir; V_o'daki dalgacık ihmal edilirse v_o(t) = V_o olur.
1. Giriş gerilimi V_d değiştiğinde, darbeleme oranı V_o'yu sabit tutacak biçimde kontrol edilmelidir.

Anahtar kullanım faktörleri (P_o/P_T) grafiklerine göre düşürücü ve yükseltici konvertörlerin anahtar kullanımı, giriş ve çıkış gerilimlerinin birbirine yakın olduğu durumlarda iyidir; düşürücü-yükseltici ve CUK konvertörlerde D = 0,5 (V_o = V_d) için anahtar kullanımı 0,25'tir.

## Manyetik kuplajlı kıyıcılar (Bölüm 3)

Temel kıyıcı tipleri elektriksel yalıtımın gerekmediği ve çıkış geriliminin girişten çok farklı olmadığı durumlar için uygundur; bu şartlardan biri veya birkaçı gerekiyorsa manyetik kuplajlı devreler (flyback ve forward) daha iyi seçimdir. Flyback konvertör uzun yıllardır, televizyon ekranları ve diğer katot ışınlı tüp uygulamalarına yüksek gerilim ve düşük güç sağlamak için kullanılmaktadır. Anahtar DT süresince kapalı, (1−D)T süresince açıktır; anahtar kapalıyken birincil akım (V_d/L1) A/s eğimiyle artar, anahtar açılınca depolanan manyetik enerji ikincil sargı ve diyot üzerinden yüke aktarılır. Seçimde çıkış gücü ve giriş gerilimi iki ana etkendir; karmaşık devreler genelde daha yüksek güçler için uygundur.

## Sonuç ve değerlendirme

AC'den DC gerilim elde eden güç çeviricilere **redresör**, DC'den AC elde edenlere **invertör**, DC'den farklı değerde yine DC gerilim elde edenlere **konvertör** denir. Konvertörler sanayide birçok cihazda vazgeçilmezdir; DC sistemlerde güç aktarımı DC/DC konvertörlerle yapılır. Konvertör, sürekli değiştirilebilir sarım oranlı bir AC transformatörün eşdeğer DC devresi gibi düşünülebilir: bir DC kaynağın gerilim değerini artırıp azaltabilir. Konvertörler çıkışa aktarılan güç oranına göre düşürücü, yükseltici, düşürücü-yükseltici, CUK ve tam köprü olarak adlandırılır; çıkışları sabit olabildiği gibi ayarlanabilir de olduğundan uygulamada geniş kullanım alanı bulmuşlardır.

## Kaynaklar (seçme)

- Mohan N., Undeland T. M., Robbins W. P., *Power Electronics: Converters, Applications and Design*, John Wiley & Sons, 1989.
- F. F. Mazda, *Electronics Engineer's Reference Book*, 6. baskı, Butterworths.
