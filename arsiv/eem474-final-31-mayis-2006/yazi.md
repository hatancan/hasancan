---
baslik: EEM474 Güç Elektroniği: 31 Mayıs 2006 final soruları
ozet: 31 Mayıs 2006 EEM474 final sınavının 11 sorusu: serbest dolaşım diyotlu R-L, ON-OFF AC kontrol, buck-boost, 120° eviriciler, DC motor ve step motor.
---

EEM474 Güç Elektroniği dersinin 31 Mayıs 2006 tarihli final sınavının soruları, kâğıdın fotoğraflanmış sayfalarından metne aktarıldı; fotoğraflar yayınlanmadı. Aynı klasördeki bir el yazısı fotoğraf, sınavın 1. ve 5. sorularının çözüm denemesini içeriyor. Sınav kâğıdındaki kişisel bilgiler aktarılmadı.

## Sorular

1. Verilen şekilde R-L yükü için (R, indüktörün iç direncidir) S1 anahtarı t1 süresince kapalı ve t2 süresince açık kalmıştır (Vs,DC kaynağı, D1 diyotu ve yük ile paralel Dm serbest dolaşım diyotu). Bir periyot için: a) Io (yük akımı) ve If (diyot akımı) dalga şekillerini çiziniz ve genel ifadelerini yazınız. b) R = 0 için dalga şekillerini yeniden çiziniz. (10 p)
2. Anahtarlama elemanlarının özelliklerini dikkate alarak tabloda, anahtarlama elemanına uygun özellikleri işaretleyiniz. Elemanlar: GTO, transistör, tristör, IGBT, triyak. Özellikler: tam kontrollü, yarı kontrollü, kontrolsüz, tek yönlü akım, çift yönlü akım geçer, pulse kontrollü, sürekli kontrol sinyali gerekir. (8 p)
3. Verilen ON-OFF metoduyla denetlenen AC gerilim kontrol devresinde (iki antiparalel tristör, yük R) her iki tristör n saykıl süresince iletimde ve m saykıl süresince kesimdedir. Giriş gerilimi vs = Vm sin ωt olduğuna göre a) çıkış geriliminin RMS değerini elde ediniz (verilen bağıntı: 2 sin² ωt = 1 − cos 2ωt). b) Güç katsayısını (PF) n ve m değerlerine göre elde ediniz. (10 p)
4. Verilen devrede (D1–D4 köprüsü, ortasında T1 tristörü, yük R, giriş vs = Vm sin ωt) a) çıkış akımının i1 (tristörün akımı) ve io (R direncinin akımı) dalga şekillerini giriş gerilimi ve tetikleme açısı α'ya bağlı olarak çiziniz. b) İki tristör kullanarak aynı işlevi yerine getirebilen devreyi çiziniz. (10 p)
5. Buck-boost konvertör için kalıcı durumda "periyodik akımdan dolayı indüktör üzerinde oluşan gerilimin ortalama değeri sıfırdır" ilkesine göre Vo/Vin değerini elde ediniz (diğer çözümler kabul edilmeyecektir). (10 p)
6. Verilen üç fazlı DC/AC devresinde bir periyot süresince her anahtar yalnız 120° iletimdedir. Anahtarların iletim (0) anında G1'in iletimi ile başlar ve 60° kayma ile G2, G3, G4, G5, G6 sırasıyla devam eder. Y (yıldız) yükü için Van, Vbn, Vcn değerlerini verilen tabloya (Mode 1–6; her mode 60° iletimi ifade eder) yazınız. (Arka sayfada verilen çizelge kullanılabilir.) (12 p)
7. Verilen tek fazlı tam köprü devresinde (Q1–Q4 IGBT'leri ve D1–D4 diyotları, R-L yük) kare dalga benzeri (quasi-square wave) AC gerilim elde etmek için: a) Denetim devresinden anahtarlara uygulanacak kontrol darbelerini ve yük üzerindeki gerilim ve akım dalga şeklini çiziniz. b) Yük üzerindeki gerilim dalga şekline göre hangi bölümde hangi anahtarların çalıştığını belirtiniz. c) Bu yöntemde çıkış geriliminde hangi ayarlar yapılabilir? (10 p)
8. Şönt bağlı sargılı DC motorda U gerilimi sabit iken yükün azalması ile motorun tepkisinin ne olacağını formülle açıklayınız (Ra, La, E rotoru; Rf, Lf şönt sargıyı (alan sargısını) temsil eder). (10 p)
9. Çözünürlüğü 200 olan bir step motorun rotor hızı 60 r/s (devir/saniye) ile dönmektedir. a) Motorun adımını bulunuz. b) Motorun denetimi için saniyede verilmesi gereken darbe (pulse) sayısını bulunuz. c) Rotorun 23,4°'lik açıyı alabilmesi için gereken darbe sayısını bulunuz. (9 p)
10. Şehir şebekesi ile çalışan saç kurutma makinesini akü ile çalıştırmak için farklı yöntemler öneriniz (UPS ve kesintisiz güç kaynağı ifadeleri geçersizdir). Her öneri için mühendislikçe blok diyagram çizin ve her bloktan beklediklerinizi (kazancını, frekansını, anahtarlama frekansı vb.) değerlerle kabaca maddeler hâlinde belirtiniz. Makinenin özellikleri: 220 V AC (rms), 50 Hz, R = 5 Ω, L = 10 mH ve akü = 12 V DC. (10 p)
11. Step motor ile AC motoru özet olarak karşılaştırınız. (5 p)

## Çözüm denemesi (el yazısı fotoğraf)

**Soru 1.** Fotoğraflanan sayfada R-L yükü ve serbest dolaşım diyotu (Dm) çizilmiş; kaynak gerilimi Vs için 0–t1 aralığında +Vdc, t1–t2 aralığında −Vdc düzeyi, akım için ise t1 anında tepe ve t2 anında ILmin değeri olan, doğrusal artıp azalan üçgen biçimli If ve IL eğrileri gösterilmiştir. R ≠ 0 için bu eğriler üstel (R-L) biçiminde çizilmiştir; çözüm genel ifadeler yazılmadan çizim aşamasında kalmıştır.

**Soru 5.** Çözüm yalnız başlangıç aşamasındadır; kâğıtta "periyodik akımdan dolayı indüktör üzerindeki gerilimin ortalaması sıfırdır" ilkesi yazılmış, devre denklemleri tamamlanmamıştır. Beklenen sonuç: Vo/Vin = −D/(1 − D).

## Hesaplanabilen sonuçlar

- Soru 9: adım açısı 360°/200 = 1,8°; rotor 60 r/s döndüğünden saniyede 60 × 200 = 12 000 darbe gerekir; 23,4° için 23,4/1,8 = 13 darbe verilir.
- Soru 3: n saykıl iletim, m saykıl kesim için Vrms = Vm·√(n/(2(n + m))) = Vs,rms·√(n/(n + m)) ve direnç yükünde PF = √(n/(n + m)) olur.
- Soru 8: şönt motorda U sabitken yük momenti azalınca endüvi akımı Ia = T/(KΦ) azalır; E = U − Ia·Ra arttığından hız ω = E/(KΦ) yükselerek boşta çalışma hızına yaklaşır.

*Not: Sınav kâğıdının fotoğrafında üzerinde başka bir öğrenciye ait yazılı cevap işaretleri bulunduğundan o cevaplar aktarılmamıştır. 120° iletimli üç fazlı eviricide yıldız yük faz gerilimleri her moda göre ±Vs/3 ve ±2Vs/3 düzeylerinde olur; tablo kaynakta çözülmemiştir.*
