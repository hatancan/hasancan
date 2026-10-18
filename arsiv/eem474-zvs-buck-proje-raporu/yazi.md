---
baslik: EEM474 Güç Elektroniği: ZVS Buck Dönüştürücü Proje Raporu
ozet: Sıfır gerilimde anahtarlamalı buck dönüştürücü, anahtarlama aralıkları ve PSIM dalga şekilleri.
---

31 Mayıs 2013 tarihli bu öğrenci raporu, düşürücü DC/DC dönüştürücüyü ve sıfır gerilimde anahtarlamayı inceliyor. Kişisel bilgileri çıkarılmış kapak ve rapor PDF'leri yazının sonunda indirilebilir.

## Anahtarlamalı DC/DC dönüştürücü

Raporda PWM denetimi, hızlı geçiş cevabı ve ayarlanabilir DC çıkış anlatılıyor. Temel devre elemanları kontrollü güç anahtarı, diyot ve endüktanstır. Sürekli iletim varsayımında endüktans akımı kesilmez; anahtar ve diyodun iletim aralıklarında enerji aktarımı sürer.

## Buck dönüştürücünün iki aralığı

Anahtar iletimdeyken vL = Vs − Vo ve diL/dt = (Vs − Vo)/L. Süre DT olduğundan akım değişimi ΔiL = (Vs − Vo)DT/L.

Anahtar açıkken diyot akımı devralır: vL = −Vo, diL/dt = −Vo/L. Süre (1 − D)T ve ΔiL = −Vo(1 − D)T/L.

Kararlı durumda bir periyottaki toplam akım değişimi sıfırdır. Bu eşitliklerden ideal sürekli iletim için Vo = DVs çıkar.

## ZVS yaklaşımı

Kaynak, anahtara paralel küçük bir kondansatörle kesime geçişte gerilim yükselme hızının sınırlandırılmasını anlatıyor. Anahtarlama enerjisinin kondansatöre aktarılması ve uygun hücrelerde geri kazanılması üzerinde duruyor. Rezonanslı dönüştürücülerde sıfır akım veya sıfır gerilim koşullarının anahtarlama kaybını azaltması vurgulanıyor.

*Not: Raporda ZVS yalnız kesime girme işlemiyle tanımlanmış. Sıfır gerilimde anahtarlama daha genel bir kavramdır; sıfır gerilimde iletime giriş de bu kapsamdadır. Rezonans ve parazitik eleman kayıpları nedeniyle gerçek devrede bütün kayıplar sıfır olmaz.*

## PSIM örneği

PSIM 6.0 içindeki “ZVS Resonant-Switch Converter” örneği kullanılıyor. Raporda üç sonuç grubu var: bobin gerilimi, Q anahtar akımı ve anahtar/kondansatör uç gerilimi. Dalga şekilleri iletim aralığı ile rezonans geçişinin farklı yapısını gösteriyor; kaynak ayrı bir sayısal verim veya kayıp tablosu vermiyor.
