---
baslik: EEM332 Mikroişlemciler: Laboratuvar 1–2: DEBUG ve Segment Yazmaçları
ozet: DEBUG başlangıcı, CS/DS/SS/ES ve IP yazmaçları, bellek adresleri; föyler ve kişisel bilgileri çıkarılmış öğrenci çözümleri.
---

Bu yazı, Başkent Üniversitesi **EEM332 Mikroişlemciler** ders arşivindeki ilgili notları ve uygulamaları bir araya getiriyor (2006–2015). DEBUG başlangıcı, CS/DS/SS/ES ve IP yazmaçları, bellek adresleri; föyler ve kişisel bilgileri çıkarılmış öğrenci çözümleri. Bir arkadaşın hazırladığı çalışmalar ve ders belgeleri birlikte aktarılmış; öğrenci adları, numaraları ve grup bilgileri çıkarılmıştır. Belgelerin PDF arşiv kopyaları ve varsa kaynak kodları yazının sonunda ZIP olarak indirilebilir.

## eem332_lab01

EEM 332 - Mikroişlemciler

Deney Numarası: 1 Deney Adı: Debug’a Giriş, x86 Yazmaçları ve Makina Komutları

Ön Çalışma 8086 yazmaçları ve DEBUG komutları hakkında bir araştırma yapınız ve en çok dört sayfalık bir özet hazırlayınız. Çalışmalarınıza kullandığınız kaynakların adlarını mutlaka ekleyiniz.

Deneysel Çalışma

Aşağıdaki çalışmaları okuyup, verilen komutları uygulayınız.               Verilen soruların yanıtlarını raporunuzda belirtiniz.

### DEBUG programını çalıştırmak için bir DOS penceresi açılır ve aşağıdaki komut girilir

```
C:\> debug <enter>
```

DEBUG tire “-” istemi ile cevap verir. Tire istemi, DEBUG programının verilecek komutları etkileşimli olarak kabul etmeye hazır olduğunu belirtir. En önemli komutlardan birisi, tüm geçerli komutların bir özetini veren “?” komutudur. Tüm geçerli DEBUG komutlarının bir listesi ders kitabının 118. sayfasında verilmiştir.

Şimdi DEBUG’ı çalıştırınız ve bütün komutların listesini görüntüleyiniz;

```
C:\> debug              <enter>
```

-?                      <enter>

Bu komutlar uygulandığında, ekranda geçerli DEBUG komutlarının bir listesini görülür. Tüm komutlar tek bir harften oluşmaktadır. Bazı komutlar için ek bağımsız değişkenlerin kullanımı gerekmektedir.

### DEBUG Üzerinde Aritmetik İşlemler

“h” komutu, DEBUG’da verilen iki bağımsız değişkenin toplamını ve farkını gösterir. DEBUG sadece 16lık (hexadecimal) sayı sisteminde işlem yapar!

### DEBUG istem satırına aşağıdaki komutu giriniz

-h 3 2 <enter>

### Komut işletildikten sonra ekranda aşağıdaki satır gösterilecektir

0005 0001

Burada, sırasıyla toplama ve çıkarma işlemlerinin sonucu gösterilmektedir, 3+2=5 ve 3-2=1.

### Şimdi aşağıdaki komutu deneyiniz

-h 2 3 <enter>

Bu durumda negatif sonuç, 2-3= -1, 2’nin tümleyeni şeklinde verilir. Negatif bir sayının tanımlanması için o sayının en anlamlı bitinin 1 olup olmamasına bakılır. Öte yandan toplama işlemi sonucu

oluşacak pozitif bir sayının da en anlamlı biti 1 olabilir. Sonucu doğru olarak yorumlamak

### PROGRAMCI’ya kalmaktadır. Örnek olarak, aşağıdaki komutları çalıştırınız

-h E1F6 1E09 <enter>

### Toplamanın pozitif sonucu FFFF olarak görülmektedir! Şimdi aşağıdaki komutu çalıştırınız

-h 5C3F0 4BC6 <enter>

Görülen hata mesajı DEBUG’ın WORD bazında çalışmasından kaynaklanmaktadır. x86 mimarisinde word, 16 bit uzunluğundadır.

### Yazmaçlar ve Hafıza

x86 işlemcileri (en azından 8086 versiyonu) 14 temel yazmaç içerir. Yazmaçların içeriklerini görmek

### için aşağıdaki komutu giriniz

```
-r <enter>
```

İkinci satırın sonundaki 2-harfli kısaltmalara dikkat edin. Bu kısaltmalar FLAGS yazmacındaki özel amaçlı bitlerin değerlerini göstermektedir. Bir yazmacın içeriğini incelemek ve değiştirmek için “r” komutu ve değişken olarak o yazmacın adı kullanılabilir. Örnek olarak aşağıdaki komutları giriniz:

```
-r ax <enter>
```

ax    0000 :3A7 <enter>

Şimdi r komutunu kullanarak tüm yazmaçları tekrar inceleyiniz. AX yazmacının artık 03A7 sayısını sakladığını göreceksiniz.

r komutunu kullanarak BX yazmacına 92A değerini yükleyiniz. Daha sonra AX ve BX yazmaçlarının sırasıyla 3A7 ve 92A sayılarını sakladıklarını gözleyiniz.

Şimdi 3A7+92A işlemini DEBUG komutları kullanmak yerine makina komutlarını kullanarak x86 mikroişlemcisinin hafızasında yapılmasını sağlayacağız. Burada DEBUG sadece komutların işlemciye yüklenmesi için bir araç olarak kullanılacaktır. Hafızanın içeriğinin incelenmesi ve değiştirilmesi için

### “e” komutu kullanılır. Aşağıda verilen komutları uygulayınız

```
-e 100                          <enter>
3756:0100       E4.01           <enter>
-e 101                          <enter>
3756:0101       85.D8           <enter>
```

Yukarıdaki komutları girerken büyük bir ihtimalle 3756, E4 ve 85 değerlerinden farklı değerler göreceksiniz. Bu sayılar DEBUG çalıştırılmadan önce hafızanın durumuyla ilgilidir ve bu aşamada bunun bir önemi yoktur. 01 ve D8 değerlerini 0100 ve 0101 numaralı göreli konumlara (offset) girmeniz gerekmektedir. e 100 komutunu girerek, DEBUG’a mevcut kod parçasında (code segment) 0100 numaralı göreli konumdaki bilgi sekizlisini (byte of data) yükleme emrini vermiş oluruz. Yukarıdaki örnekte 3756:0100 adresindeki mevcut sekizli (byte) E4, kullanıcı tarafından girilen 01 sekizlisi ile değiştirilmiştir. Aynı örnekte kod parçası (code segment)’nın adresi 3756’dir. Bu değer kendi bilgisayarlarınızda farklı olabilir, ancak bunun şu an için bir önemi yoktur.

Kod parçasının adresini 16’lık tabanda 10 ile çarpıp, sonuca göreli konum değeri (offset) eklendiğinde fiziksel adres (physical address) elde edilir. X86 sistemleri hafıza adreslerini genellikle parçalı olarak (segmented form) belirtirler.

### x86 Kullanarak Toplama

### Yazmaç içeriklerini inceleyiniz

```
-r <enter>
```

### Ekrandaki görüntü aşağıdakilere benzeyecektir

```
AX=03A7 BX=092A CX=0000 DX=0000 SP=#### BP=#### SI=#### DI=####
DS=#### ES=#### SS=#### CS=#### IP=0100 NV UP DI PL NZ NA PO NC
```

### #### : 0100 01D8 ADD AX, BX

Burada # 16’lık bir basamağı temsil eder. Görüntünün son satırı 01D8 değerinin hafızada saklanmakta olduğunu belirtir. Bu, aslında ADD AX, BX komutunun makina dili karşılığıdır ve bu komutun çalıştırılması ile belirtilen yazmaçların içerikleri toplanarak sonuç AX yazmacına yazılır. x86 yapısı sekizli-adreslenebilir (byte-addressible) bir yapıda olduğu için bilgi aşağıdaki şekilde

### düzenlenir

3756 : 0100             01

### 3756 : 0101             D8

x86’da komut hafızada bulunduğu halde, komutun çalıştırılabilmesi için komutun nerede bulunduğunun belirtilmesi gerekir. x86 sistemlerde kullanılan yöntemde iki özel yazmaç kullanılır. Bunlar CS ve IP’dir. Bu yazmaçlar bir sonra işlenecek komutun parçalı adresini barındırırlar. Böylece işlenecek olan komutun hafızada bulunduğu yer, kod parçası değeri (CS yazmacında tutulur) ve göreli konum değeri (IP yazmacında tutulur) yardımıyla etkili bir şekilde gösterilir. Gereken durumlar da r komutu kullanılarak IP yazmacına doğru göreli konum değeri yüklenir (örnekte

### 0100).

DEBUG’da bir izleme (trace) komutu “t” bulunur ve bu komut sayesinde her defasında bir tane olmak üzere makina dili komutları çalıştırılabilinir. Mevcut hafıza ve yazmaç içerikleriyle DEBUG’a izleme

### komutunu uygulayalım

```
-t <enter>
```

AX yazmacınin içeriği artık 03A7 ve 092A sayılarının toplamı olan 0CD1’dir. AX yazmacının içeriğinin işlem sonucu elde edilen toplam ile değiştiği görülür. Aynı zamanda IP yazmacının içeriği de 0102 olarak değişir. x86 sistemleri IP yazmacının içeriğini, işlenecek bir sonraki komutun adresine göre kendiliğinden değiştirir.

Şimdi sistemlerinizi kullanarak 092A (BX yazmacında) değerini, 0CD1 (AX yazmacında) değerine ekleyiniz (toplayınız). DEBUG’ın r komutunu kullanarak IP yazmacını uygun değere ayarlamayı unutmayın!

Çıkarma işlemini gerçekleştirmek için gerekli makina dili komutunu kod parçasına (code segment) eklemek gerekmektedir. 29D8 olarak makina dilinde kodlanmış komutu, göreli konum değerini 0100 olarak ayarlayıp, e komutunu kullanarak mevcut kod parçasına ekleyiniz. r komutunu

kullarak SUB AX, BX komutunun hafızaya yerleştirildiğini gözlemleyiniz ve daha sonra izleme (trace) komutunu kullanarak bu işlemin gerçekleştirilmesini sağlayınız.

Çevirici Dili Programlarındaki (Assembler Language Programs) DOS İşlevlerinin

### Kullanımı

```asm
INT komutu, x86 sistemlerinin bilgisayarın önyüklemesi (boot) sırasında DOS aracılığıyla sabit
```

diskten hafızaya kopyalanan özel programlara ulaşılmasını sağlar. Şimdilik INT komutu bir “işlev çağrıcı” olarak düşünülebilir.

DEBUG kullanarak 0200 değerini AX yazmacına ve 0041 değerini DX yazmacına yükleyelim. INT 21 komutunun makina dili karşılğı CD21’dır (INT komutu ve yazmaçlara atanan değerlerin detaylarına internet sayfasında verilen bağlantıdan ulaşılabilir). Hafızada, 0102 göreli konum değerini kullanarak mevcut kod parçasına CD ve bir sonraki göreli konum değerinin gösterdiği parçaya 21 değerlerini giriniz. IP yazmacını 0102 olarak ayarlayınız ve hafıza ve yazmaç içeriklerinin doğru

### olduğunu kontrol ediniz. Daha sonra komutu, aşağıdaki işlemi uygulayarak çalıştırınız

```
-g 104 <enter>
```

g komutu DEBUG’ın “go until” komutudur. Bu satırı uygulayarak x86’ya mevcut IP değerinden başlayarak, belirtilen IP değerine kadar olan bütün komutların çalıştırılmasını sağlarız. Burada kod parçasında değişiklik olmaz (CS:IP yapısında sadece IP değişir). Eğer izleme (t) komutunu kullanmış olsaydık, INT 21 işlevinin içinde bulunan bütün komutların işlenebilmesi için her komut için aynı komutu defalarca kullanmamız gerekirdi ve bazı durumlarda bu oldukça uzun kodların satır satır çalıştırılması anlamına gelmektedir. g komutunun kullanılması sayesinde CS:0104 değerine ulaşılana kadar gereken bütün komutların çalıştırılması sağlanır.

Yukarıdaki işlemin sonunda ekranda A karakterinin yazdığını görürüz. Burada kullandığımız INT işlevi, tüm INT işlevleri içinde 21 numaralı olanıdır. Bu işlevin kullanılmasıyla diğer DOS işlevlerine erişim sağlanabilir. AH yazmacındaki 02 (AH, AX’in en anlamlı sekizlisidir) değeri DOS’a ekrana bir karakter yazacağını gösterir. Ekrana basılacak karakteri ise DL (DL, DX’in en az anlamlı sekizlisidir) yazmacına yazdığımız 41 değeri belirtir. 41, A karakterinin ASCII kodundaki karşılığıdır.

### Programların Sonlandırılması

Çevirici veya makina dili programları çalışmalarını bitirdiğinde, x86 sisteminin işletim sistemi tarafından kontrol edilebilir hale gelmesi gerekmektedir. Bunu gerçekleştirmenin bir yolu INT 20 işlevini çağırmaktır. Yüksek seviye programlama dillerinde (C/C++ gibi) yazılan programlarda derleyici kendiliğinden bu satırı eklemektedir. Kullandığımız alt seviye çevirici dilinde (assembler language) ise programın sonuna INT 20 satırını eklemek programcıya ve onun ihtiyaçlarına bağlıdır.

### Şimdi 2-satırlı şu programı yazalım

```asm
INT 20
INT 21
```

### Bunun için aşağıdaki işlemleri gerçekleştirmemiz gerekmektedir

### 1. DEBUG’ın r komutunu kullanarak AX ve DX yazmaçlarına sırasıyla 0200 ve 0043

değerlerini kaydedelim

### 2. aşağıda verilenleri sırasıyla hafızaya yükleyelim

### CD

### CD

### 3. IP ve CS yazmaçlarına INT 21 komutunun yerini gösteren hafıza adreslerini yükleyelim

### 4. geçerli bir bitiş göreli konum değeri belirterek DEBUG’ın g komutunu kullanıp bu

komutları çalıştıralım

Tebrikler! İlk makina dili programınızı yazıp çalıştırdınız.       Programın çalışmasını laboratuvar sorumlusuna gösteriniz.

SORU 1: 2-satırlı programı çalıştırdığınızda ekranda ne gördünüz? Bunun nedenini açıklayınız.

### Çevirme/Geri Çevirme (Assemble/Disassemble)

Pek çok program iki satırdan daha uzundur. Yazdığınız kodların insan tarafından anlaşılabilen hali olan anımsatıcıları (mnemonics) görmek için IP yazmacının değerini 2-satırlı programnınız başlangıç konumunu gösterecek şekilde ayarlayınız ve DEBUG’ın geri çevirme (unassemble) komutunu

### aşağıdaki şekilde giriniz

```
-u <enter>
```

Programınızın anımsatıcılar şeklinde yazıldığını ve her anımsatıcının yanında hafızada saklanan 16’lık (hexadecimal) bir makina kodunun olduğunu göreceksiniz. Şu ana kadar yaptıklarımız makina dili kodlarını içermekteydi. Anımsatıcıları kullanarak bir program yazmak, yazım ve anlama açısından daha kolaydır. Bu nedenle DEBUG bir çevirme (assemble) komutu “a” içerir. Örnek olarak 2-satırlı programı ele alalım. Mevcut kod parçasında 0100 numaralı göreli konum değerinden başlayarak aynı

### programı anımsatıcılar olarak yazalım

```
-a 100          <enter>
```

```asm
int 21          <enter>
int 20          <enter>
```

<enter>

Yukarıdaki komutlar sayesinde, aynı programı 16’lık makina kodları yerine anımsatıcılar (mnemonics) olarak ifade edebilirsiniz.

### DEBUG Senaryoları (Scripts)

Sadece DEBUG kullanarak çevirici dili programları yazılabilir. Bu durumda bir takım kısıtlamalar söz konusudur. DEBUG’daki bu kısıtlamalarla karşılaşılacağı zaman ayrıntılı bilgi verilecektir. DEBUG’da iki farklı şekilde çevirici dili programlaması yapılabilir. İlk yöntemde DEBUG penceresinde yazılacak kod çalıştırılabilir. İkinci yöntemde ise çevirici dili kodlarının bulunduğu bir dosya yaratılarak DEBUG tarafından çalıştırılması sağlanabilir. İkinci yöntemi gösteren aşağıdaki çalışmayı yapınız:

### 1. Bilgisayarınızdaki herhangi bir kelime işlemci programı veya yazım (Ör: Notepad)

programını kullanarak TEMP.DBG adlı bir dosya yaratınız. Bu dosyanın içeriğinin nasıl olması gerektiği aşağıda verilmiştir. İstediğiniz herhangi bir kelime işlemci veya yazım programını kullanabilirsiniz, ancak dosyayı kaydederken mutlaka TEXT veya ASCII dosyası olarak kaydetmeniz gerekmektedir!

a 100

```asm
mov ah, 02
mov dl, 2a
```

```asm
int 21
int 20
```

n temp.com r bx r cx w q

Yukarıdaki komutları yazarken arada bırakılan boş satırı sizin de uygulamanız gerekmektedir. Bu satır DEBUG’a çevirici kodlarının bitip, DEBUG komutlarının kullanılmaya başlandığını belirtir.

### 2. DOS komut istemini çalıştırarak aşağıdaki komutu yazınız:

```
C:\> DEBUG < TEMP.DBG               <enter>
```

Bu işlemden sonra sabit diskinizde TEMP.COM adlı bir çalıştırılabilir dosya oluşturulacaktır.

SORU 2: TEMP.COM adlı dosyayı çalıştırın. Bu dosya ne iş yapıyor?

SORU 3: Bu belgedeki bilgileri ve DEBUG’ın yardım menüsünü (? komutu) kullanarak TEMP.DBG dosyasındaki satırların hangi işlevleri gerçekleştirdiğini yazınız.

SORU 4: Bu deneyden edindiğiniz bilgileri kısaca özetleyiniz.

## eem332_lab02

EEM 332 - Mikroişlemciler Deney Numarası: 2 Deney Adı: Temel Debug ve Çevirici (Assembly) Komutları

Ön Çalışma “Introduction to Debug” belgesini okuyunuz.

### 1.        Parça (segment) yazmaçlarının(CS, SS, DS, ES) ve Komut Göstericisinin

(instruction pointer - IP) nasıl kullanıldığını açıklayınız.

### 2.        Deneysel çalışma kısmında gördüğünüz, BÜYÜK harflerle yazılmış DEBUG

komutlarını açıklayınız.

Deneysel Çalışma Aşağıda verilen işlemleri gerçekleştiriniz.    Gereken komut satırlarını ve gözlemlediğiniz sonuçları raporunuzda belirtin.

### 1. YAZMAÇ (REGISTER) komutunu kullanarak:

a. yazmaçların mevcut içeriklerini görüntüleyiniz, b. IP yazmacının içeriğini 10016 olarak değiştiriniz, c. DS yazmacının içeriğini 150016 olarak değiştiriniz, d. CS yazmacının içeriğini 160016 olarak değiştiriniz, e. taşma bayrağının (overflow flag) durumunu “taşma yok” (no overflow), eşlik bayrağının (parity flag) durumunu “çift eşlik” (even parity) olarak değiştiriniz.

### 2. Yukarıdaki değişikliklere göre oluşan yeni yazmaç durumlarına göre, aşağıda

verilenler için etkin adresi (effective address) hesaplayınız a. DS:BX b. CS:IP c. SS:BP

### 3. DOLDUR (FILL) komutunu kullanarak DS:10 adresinden başlayarak 16 tane

depolama yerinin mevcut değerlerini 2316 değeriyle değiştiriniz.

### 4. Mevcut bilgi parçasının (data segment) ilk 64 sekizlisinin (byte) içeriklerini DÖKÜM

(DUMP) komutuyla gözlemleyiniz.

### 5. DS:15 adresinden başlayarak 20 depolama yerini, CS:100 adresinden başlayan

depolama yerlerine TAŞI (MOVE) komutunu kullanarak kopyalayınız ve değişiklikleri DÖKÜM (DUMP) komutuyla gözlemleyiniz.

### 6. ARAMA (SEARCH) komutunu kullanarak DS:00 ve DS:100 aralığında 8616 ve

FF16 değerlerinin bulunduğu yerleri belirleyiniz.

### 7. KARŞILAŞTIR         (COMPARE)           komutunu    kullanarak   aşağıdaki   işlemleri

### gerçekleştiriniz

a. DS:15 adresinden başlayan 20 yerin içerikleri ile CS:100 adresinden başlayan yerlerin içeriklerini karşılaştırınız,

b. (a) adımını 32 depolama yeri için tekrarlayın.

### 8. ÇEVİR (ASSEMBLE) komutunu kullanarak aşağıda verilen komutları giriniz ve

GERİ ÇEVİR (UNASSEMBLE) komutuyla bunların oluşturduğu makina dili kodlarını teyit ediniz. Her komut kaç sekizli (byte) yer tutmaktadır?

```asm
MOV AX,00
MOV BX,AX
MOV CX,12
MOV DX,0101
OR CX,AX
OR AX,CX
ADD BX,AX
SUB AX,BX
ROL DX,1
ROR DX,1
ROR DX,1
NOT DX
```

### 9. İZLEME (TRACE) komutunu kullanarak yukarıdaki programı adım adım çalıştırınız

ve yazmaçların içeriklerindeki değişimleri gözlemleyiniz.

```asm
NOT: 16’lık tabandaki sayılar “16” altsimgesiyle belirtilmiştir. Bunun dışında verilen
```

sayılar 10’luk tabana göre verildiğinden, bu sayıları 16’lık tabana çevirmeniz gerekebilir.

EEM 332 – Mikroişlemciler Deney 2 Çalışma Formu

### İsim

1       Aşağıdaki anımsatıcı (mnemonic) komutlarını makina dili kodlarına çeviriniz. a) MOV AX,BX                              Cevap___________ b) MOV AX,0AAAAH                          Cevap ___________ c) MOV AX,[BX]                            Cevap ___________ d) MOV AX,[0004]                          Cevap ___________ e) MOV AX,[BX+SI]                         Cevap ___________ f) MOV AX,[SI]+[0004]                     Cevap ___________ g) MOV AX,[BX][SI]+[0004]                 Cevap ___________

2       Yukarıdaki kodların herbirinin kapladığı sekizli (byte) miktarını belirtiniz. a) Cevap ___________ b) Cevap ___________ c) Cevap ___________ d) Cevap ___________ e) Cevap ___________ f) Cevap ___________ g) Cevap ___________

3       Aşağıdaki işlemleri yapınız ve sonuçları gözlemleyiniz. Her işlemi gerçekleştirmek için yazdığınız komutları belirtiniz. Bütün işlemler için adres koşulu: DS=200, CS=100.

a. DS:1234 adresli konuma ED, DS:1235 adresli konuma BE, DS:1236 adresli konuma CD ve DS:1237 adresli komua AB değerlerini yükleyiniz. b. SI yazmacına 1236 değerini yükleyiniz. c. Yazmaçların bu değişiklikler sonucundaki halini görüntüleyiniz.

### d. CS:0000 adresinden başlayarak aşağıdaki komutları çeviriniz (assemble)

```asm
MOV AX, 1234
MOV BX,[1234]
MOV CX,[SI]
```

e. Yazdığınız komutları izleyebilmek (trace) için gereken CS ve IP yazmaç değerlerini ayarlayınız. f. Programı izleyiniz (trace) ve sonuçları gözlemleyiniz.          AX, BX ve CX yazmaçlarında olan değişiklikleri ve nedenlerini açıklayınız.

## calisma-623

1.)

a)

```
AX=0000 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=13FA ES=13FA SS=13FA CS=13FA IP=0100 NV UP EI PL NZ NA PO NC
```

```
13FA:0100 0000      ADD     [BX+SI],AL      DS:0000=CD
```

b)

```
-r ip
```

### IP 0100

### 

c)

```
-r ds
```

### DS 13FA

:1800

d)

```
-r cs
```

### CS 13FA

:2400

e)

```
-r f
```

NV UP EI PL NZ NA PO NC -pl

```
-r f
```

NV UP EI PL NZ NA PO NC -ov

```
-r f
```

### OV UP EI PL NZ NA PO NC -

f)

```
-r
```

```
AX=0000 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0100 OV UP EI PL NZ NA PO NC
```

```
2400:0100 0000        ADD    [BX+SI],AL               DS:0000=00
```

2.)

```
-f 20 3d 42
```

3.)

```
-d 20 3d
```

```
1800:0020 42 42 42 42 42 42 42 42-42 42 42 42 42 42 42 42 BBBBBBBBBBBBBBBB
```

```
1800:0030 42 42 42 42 42 42 42 42-42 42 42 42 42 42         BBBBBBBBBBBBBB
```

4.)

-m ds:20 33 cs:100

```
-d cs:100 133
```

```
2400:0100 42 42 42 42 42 42 42 42-42 42 42 42 42 42 42 42 BBBBBBBBBBBBBBBB
```

```
2400:0110 42 42 42 42 00 00 00 00-00 00 00 00 00 00 00 00 BBBB............
```

```
2400:0120 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
```

```
2400:0130 00 00 00 00                         ....
```

```
-d ds:20 33
```

```
1800:0020 42 42 42 42 42 42 42 42-42 42 42 42 42 42 42 42 BBBBBBBBBBBBBBBB
```

```
1800:0030 42 42 42 42                         BBBB
```

5.)

a)

-c ds:20 33 cs:100

b)

-c ds:20 47 cs:100

```
1800:0034 42 00 2400:0114
```

```
1800:0035 42 00 2400:0115
```

```
1800:0036 42 00 2400:0116
```

```
1800:0037 42 00 2400:0117
```

```
1800:0038 42 00 2400:0118
```

```
1800:0039 42 00 2400:0119
```

```
1800:003A 42 00 2400:011A
```

```
1800:003B 42 00 2400:011B
```

```
1800:003C 42 00 2400:011C
```

```
1800:003D 42 00 2400:011D
```

6.)

-s ds:00 30 42

```
1800:0020
```

```
1800:0021
```

```
1800:0022
```

```
1800:0023
```

```
1800:0024
```

```
1800:0025
```

```
1800:0026
```

```
1800:0027
```

```
1800:0028
```

```
1800:0029
```

```
1800:002A
```

```
1800:002B
```

```
1800:002C
```

```
1800:002D
```

```
1800:002E
```

```
1800:002F
```

```
1800:0030
```

7.)

```
-a 100
```

```
2400:0100 mov ax,55
```

```
2400:0103 mov bx,ax
```

```
2400:0105 mov cx,20
```

```
2400:0108 mov dx,0110
```

```
2400:010B or cx,ax
```

```
2400:010D or ax,cx
```

```
2400:010F add bx,ax
```

```
2400:0111 sub ax,bx
```

```
2400:0113 rol dx,1
```

```
2400:0115 ror dx,1
```

```
2400:0117 ror dx,1
```

```
2400:0119 not dx
```

```
2400:011B
```

```
-u 100
```

```
2400:0100 B85500       MOV     AX,0055
```

```
2400:0103 89C3        MOV     BX,AX
```

```
2400:0105 B92000       MOV     CX,0020
```

```
2400:0108 BA1001       MOV     DX,0110
```

```
2400:010B 09C1        OR    CX,AX
```

```
2400:010D 09C8        OR     AX,CX
```

```
2400:010F 01C3        ADD    BX,AX
```

```
2400:0111 29D8        SUB    AX,BX
```

```
2400:0113 D1C2        ROL    DX,1
```

```
2400:0115 D1CA        ROR    DX,1
```

```
2400:0117 D1CA        ROR    DX,1
```

```
2400:0119 F7D2        NOT    DX
```

```
2400:011B 0000        ADD    [BX+SI],AL
```

```
2400:011D 0000     ADD    [BX+SI],AL
```

```
2400:011F 0000     ADD    [BX+SI],AL
```

8.)

```
-r ip
```

### IP 0100

:100

```
-t 3
```

```
AX=0055 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0103 OV UP EI PL NZ NA PO NC
```

```
2400:0103 89C3     MOV    BX,AX
```

```
AX=0055 BX=0055 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0105 OV UP EI PL NZ NA PO NC
```

```
2400:0105 B92000    MOV     CX,0020
```

```
AX=0055 BX=0055 CX=0020 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0108 OV UP EI PL NZ NA PO NC
```

```
2400:0108 BA1001    MOV     DX,0110
```

```
-t 3
```

```
AX=0055 BX=0055 CX=0020 DX=0110 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=010B OV UP EI PL NZ NA PO NC
```

```
2400:010B 09C1     OR    CX,AX
```

```
AX=0055 BX=0055 CX=0075 DX=0110 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=010D NV UP EI PL NZ NA PO NC
```

```
2400:010D 09C8    OR    AX,CX
```

```
AX=0075 BX=0055 CX=0075 DX=0110 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=010F NV UP EI PL NZ NA PO NC
```

```
2400:010F 01C3    ADD   BX,AX
```

```
-t 3
```

```
AX=0075 BX=00CA CX=0075 DX=0110 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0111 NV UP EI PL NZ NA PE NC
```

```
2400:0111 29D8    SUB   AX,BX
```

```
AX=FFAB BX=00CA CX=0075 DX=0110 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0113 NV UP EI NG NZ AC PO CY
```

```
2400:0113 D1C2    ROL   DX,1
```

```
AX=FFAB BX=00CA CX=0075 DX=0220 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0115 NV UP EI NG NZ AC PO NC
```

```
2400:0115 D1CA    ROR    DX,1
```

```
-t 3
```

```
AX=FFAB BX=00CA CX=0075 DX=0110 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0117 NV UP EI NG NZ AC PO NC
```

```
2400:0117 D1CA    ROR    DX,1
```

```
AX=FFAB BX=00CA CX=0075 DX=0088 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0119 NV UP EI NG NZ AC PO NC
```

```
2400:0119 F7D2    NOT   DX
```

```
AX=FFAB BX=00CA CX=0075 DX=FF77 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=011B NV UP EI NG NZ AC PO NC
```

```
2400:011B 0000    ADD   [BX+SI],AL          DS:00CA=00
```

## D2 önçalışma

### 1)

a)Code Segment

```asm
Code segment registeri olan CS icra gören programı içeren segmentin başlangıç adresini
```

gösterir. Diğer bir deyişle, CS ile adreslenen segment içinde makine dili komutları yer almaktadır. Stack segment registeri olan SS, geçerli stack segmentin başlangıç adresini içerir. Stack segmen! t,çeşitli verilerin geçici olarak saklandığı bir bellek bloğudur.

b) Data Segment

```asm
Data segment registeri olan DS ,geçerli data segmentinin başlangıç adresidir. Bu segment
```

genel olarak program değişkenleri tarafından kullanılır. Diğer bir deyişle, bilgi işlem operasyonlarına tabi tutulan bilgiler, data segment içindeki lokasyonlarda yer alırlar.

c) Extra Segment

```asm
Ekstra segment registeri olan ES geçerli ekstra segmentin başlangıç adresini içerir.
Ekstra segment, genel olarak string operasyonları için kullanılır. Yeterli bellek
```

büyüklüğüne sahip olan sistemlerde bu 4 segment, belleğin farklı parçalarıdır. Geniş belleğe sahip olmayan sistemlerde ise, bu segmentler üstüste gelebilir.

d) Stack Segment

```asm
Stack segment registeri olan SS, geçerli stack segmentin başlangıç adresini içerir. Stack
```

segmen! t,çeşitli verilerin geçici olarak saklandığı bir bellek bloğudur.

e) IP Çeşitli bellek bölgelerindeki verilere ulaşabilmek için adres göstericisi olarak kullanılır. Bellek içindeki bir lokasyonun adresini gösterebilmek için, iki ayrı adres değeri kullanılır. İlk değer, işaret edilen lokasyonu içinde barındıran segmentin adresidir . bu noktada segment registerlerinden yararlanılır. Lokasyonun segment içindeki yerini gösteren ikinci adres değeri ise offset adresi olarak bilinir. Offset adreslerinin gösterilmesi için de, pointer ve indeks registerlerinden yararlanılır.

### 2)

- R (Register) : Bu komut o andaki register değerlerini ve bayrakların durumunu belirlemekte kullanılır.

### Ör

```
-R
AX=0000 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=2AF2 ES=2AF2 SS=2AF2 CS=2AF2 IP=0100 NV UP EI PL NZ NA PO NC
2AF2:0100 8B24   MOV   SP,[SI]           DS:0000=20CD
```

-

Bu komut yardımı ile register'lara istenilen değerler (hexadecimal olmak şartıyla) verilebilir.

### Ör

```
-R AX
```

### AX 0000

- F (Fill) : Bellek başlangıç ve bitiş adresleri belirlenen bir alanı belirlenen bir sayı ile doldurmak amacıyla kullanılır.

### Ör

-

```
-F DS:100,120,AB
```

F komutundan yararlanarak DS'in 100H-120H arasındaki kısım ABH değeri ile doldurulacaktır. Bu işlemden sonra D komutu ile DS:100H adresinden itibaren incelersek işlemin olması gibi yapıldığını kontrol etmiş oluruz.

- D (Dump / Display): Bu komut ile belleğin istediğimiz segment'inin istediğimiz offset'inden itibaren bilgileri görebiliriz. İstersek görmek istediğimiz alanı sınırlama imkanına da sahibiz.

### Ör

```
-D DS:0
2AF2:0000 CD 20 FF 9F 00 9A EE FE-1D F0 4F 03 5A 25 8A 03 . ........O.Z%..
2AF2:0010 5A 25 17 03 5A 25 14 24-01 01 01 00 02 FF FF FF Z%..Z%.$........
2AF2:0020 FF FF FF FF FF FF FF FF-FF FF FF FF 3B 25 4E 01 ............;%N.
2AF2:0030 16 2A 14 00 18 00 F2 2A-FF FF FF FF 00 00 CE 0B .*.....*........
2AF2:0040 06 1E 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
2AF2:0050 CD 21 CB 00 00 00 00 00-00 00 00 00 00 20 20 20 .!...........
2AF2:0060 20 20 20 20 20 20 20 20-00 00 00 00 00 20 20 20             .....
2AF2:0070 20 20 20 20 20 20 20 20-00 00 00 00 00 00 00 00             ........
```

-

Burada Data segment'in 0000H offset'inden itibaren olan kısmı gösterilmiştir. Eğer herhangi bir aralık verilmemiş ise 128 byte gösterir. Hexadecimal olarak belleğin dökümünü verdikten sonra yanında gösterilebilir ASCII karakter karşılıklarına da yer verilir.

### Ör

```
-D DS:100,115
2AF2:0100 8B 24 17 5A 18 BA 4A 29-A2 4F F6 C9 07 AE 07 09 .$.Z..J).O......
2AF2:0110 20 8C 07 BA 4F 80                    ...O.
```

-

- M (Move) : Bir yerdeki bir blok bilgiyi başka bir yere taşımak için kullanılır

### Ör

### - M DS:100,110,CS:500

Bu komut ile DS:100H ile DS:110H arasında kalan bilgi CS:500H adresinden itibaren yerleştirilecektir.

- C (Compare) : Belirlenen aralıktaki bilgileri karşılaştırmak amacıyla kullanılan bir komuttur.

### -C 100,110,10

```
2AF2:0100 AB 5A 2AF2:0010
2AF2:0101 AB 25 2AF2:0011
2AF2:0102 AB 17 2AF2:0012
2AF2:0103 AB 03 2AF2:0013
2AF2:0104 AB 5A 2AF2:0014
2AF2:0105 AB 25 2AF2:0015
2AF2:0106 AB 14 2AF2:0016
2AF2:0107 AB 24 2AF2:0017
2AF2:0108 AB 01 2AF2:0018
2AF2:0109 AB 01 2AF2:0019
2AF2:010A AB 01 2AF2:001A
2AF2:010B AB 00 2AF2:001B
2AF2:010C AB 02 2AF2:001C
2AF2:010D AB FF 2AF2:001D
2AF2:010E AB FF 2AF2:001E
2AF2:010F AB FF 2AF2:001F
```

```
2AF2:0110 AB FF 2AF2:0020
```

Bu komut 100H-110H adresindeki bilgiler ile 10H adresinden başlayan bilgileri karşılaştırır ve farklı olanları listeler.

### -C 100,110,100

-

100H-110H adresindekileri yine 100H adresindekiler ile karşılaştırmaktadır. Herhangi bir farklılık bulunmadığı için ekranda hiçbir bilgi görünmez.

S (Search) : Hafıza bölgesinde istenilen adres aralığında belli bir değeri arar. Eğer Sonuç bulursa adres olarak ekranda gözlenir.

### Ör

### -S CS:100,110,65

0100 ile 0110 offsetleri arasında 65 bilgisin arar.

## calisma-704

### CS:BX 15000

### CS:IP 16000

### SS:BP 15470

```
-r
AX=0000 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0100 OV DN DI NG NZ NA PO CY
1600:0100 0000      ADD [BX+SI],AL                     DS:0000=00
-f DS:10 1f 23
-d DS:10
1500:0010 23 23 23 23 23 23 23 23-23 23 23 23 23 23 23 23 ################
1500:0020 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0030 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0040 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0050 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0060 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0070 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0080 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
```

-m 15 29 cs:100

```
-d cs:100
1600:0100 23 23 23 23 23 23 23 23-23 23 23 00 00 00 00 00 ###########.....
1600:0110 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0120 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0130 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0140 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0150 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0160 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0170 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
```

-1500:0010 23 23 23 23 23 23 23 23-23 23 23 23 23 23 23 23 ################

```
1500:0020 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0030 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0040 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0050 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0060 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0070 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0080 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
```

-m 15 29 cs:100

```
-d cs:100
1600:0100 23 23 23 23 23 23 23 23-23 23 23 00 00 00 00 00 ###########.....
1600:0110 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0120 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0130 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0140 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0150 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0160 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0170 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
```

-s ds:0000 0100 86 -s ds:0000 0100 ff

```
1500:00F9
```

-c ds:15 29 cs:100 -c ds:15 34 cs:0100 -c ds:0015 0034 cs:0100 --a 100

```
1600:0100 MOV AX,00
1600:0103 MOV BX,AX
1600:0105 MOV CX,12
1600:0108 MOV DX,0101
1600:010B OR CX,AX
1600:010D OR AX,CX
1600:010F ADD BX,AX
1600:0111 SUB AX,BX
1600:0113 ROL DX,1
1600:0115 ROR DX,1
1600:0117 ROR DX,1
1600:0119 NOT DX
1600:011B
```

```
-u
1600:0100 B80000    MOV AX,0000
1600:0103 89C3     MOV BX,AX
1600:0105 B91200    MOV CX,0012
1600:0108 BA0101    MOV DX,0101
1600:010B 09C1     OR  CX,AX
1600:010D 09C8     OR  AX,CX
1600:010F 01C3     ADD BX,AX
1600:0111 29D8     SUB AX,BX
1600:0113 D1C2     ROL DX,1
1600:0115 D1CA      ROR DX,1
1600:0117 D1CA      ROR DX,1
1600:0119 F7D2     NOT DX
1600:011B 0000     ADD [BX+SI],AL
1600:011D 0000     ADD [BX+SI],AL
1600:011F 0000     ADD [BX+SI],AL
```

-

```
1600:0117 ROR DX,1
1600:0119 NOT DX
1600:011B
-t
```

```
AX=0000 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0103 OV DN DI NG NZ NA PO CY
1600:0103 89C3   MOV BX,AX
```

-

```
-t
```

```
AX=0000 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0105 OV DN DI NG NZ NA PO CY
1600:0105 B91200  MOV CX,0012
```

```
-t
```

```
AX=0000 BX=0000 CX=0012 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0108 OV DN DI NG NZ NA PO CY
1600:0108 BA0101  MOV DX,0101
-t
```

```
AX=0000 BX=0000 CX=0012 DX=0101 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=010B OV DN DI NG NZ NA PO CY
1600:010B 09C1   OR    CX,AX
-t
```

```
AX=0000 BX=0000 CX=0012 DX=0101 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=010D NV DN DI PL NZ NA PE NC
1600:010D 09C8    OR   AX,CX
```

--t

```
AX=0012 BX=0000 CX=0012 DX=0101 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=010F NV DN DI PL NZ NA PE NC
1600:010F 01C3   ADD BX,AX
-t
```

```
AX=0012 BX=0012 CX=0012 DX=0101 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0111 NV DN DI PL NZ NA PE NC
1600:0111 29D8   SUB AX,BX
-t
```

```
AX=0000 BX=0012 CX=0012 DX=0101 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0113 NV DN DI PL ZR NA PE NC
1600:0113 D1C2    ROL DX,1
-t
```

```
AX=0000 BX=0012 CX=0012 DX=0202 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0115 NV DN DI PL ZR NA PE NC
1600:0115 D1CA    ROR DX,1
```

--t

```
AX=0000 BX=0012 CX=0012 DX=0101 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0117 NV DN DI PL ZR NA PE NC
1600:0117 D1CA    ROR DX,1
-t
```

```
AX=0000 BX=0012 CX=0012 DX=8080 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0119 OV DN DI PL ZR NA PE CY
1600:0119 F7D2   NOT DX
```

## lab1_rapor(1)

### SORU 1 

### - 2 satırlı programı çalıştırdığımız zaman ekranda

```
AX=0200 BX=0000 CX=0000 DX=0043 SP=FFEE BP=0000 SI=0000 DI=0000
DS=152D ES=152D SS=152D CS=152D IP=0100 NV UP EI PL NZ NA PO NC
152D:0100 CD21   INT 21
```

### - g 104 komutunu girdim

### “C:\>

### C

Program normal olarak sonlandırıldı

```
C:\>“
```

Burada, int 21 yazı yazdırma, int 20 ise programı onlandırma komutlarıdır. Int 21 komutu sayesinde, DX registerina yüklediğimiz 43 degerinin C harfinin ascii kodu karsılıgı oldugunu görüyoruz.

### SORU 2 

TEMP.COM dosyasını çalıştırdığım zaman ekranda

```
C:\>temp.com
```

*

```
C:\>
```

Çıkıyor.Buradan da anlaşıldığı üzere bu dosya ekrana * yazdırıyor.

### SORU 3 

a 100

```
152D:0100 mov ah,02      (AX->AH 02)
152D:0102 mov dl,2a      (DX ->DL2a)
152D:0104 int 21
152D:0106 int 20
```

n temp.com (Parametre listesi) r bx         (bx ?)

### BX 0000

:0 r cx              (cx ?)

### CX 0000

:08 w     (write komutu) 00008 bayt yazılıyor q     (programdan çıkış)

### SORU 4 

8086 registerları Debug komutları hakkında bilgi edindik ve Debug programını çalıştırmayı ve üzerinde işlem yapmayı öğrendik. Debug komutlarıyla ekranda yerleri görünen yazmaçların içeriğini değiştirmeyi bunların yardımlarıyla işlem yapmayı öğrendik ve wordpad de yazdığımız bir Debug programının çıktısını dos ortamında nasıl elde edeceğimizi öğrendik.

## lab1_rapor

### SORU 1 

### - 2 satırlı programı çalıştırdığımız zaman ekrandaki çıktılar

```
AX=0200 BX=0000 CX=0000 DX=0043 SP=FFEE BP=0000 SI=0000 DI=0000
DS=0C81 ES=0C81 SS=0C81 CS=0C81 IP=0100 NV UP EI PL NZ NA PO NC
0C81:0100 CD21   INT 21
```

### - g 104 komutu kullandığımız zaman ekranda

### “C

Program normal olarak sonlandırıldı “ Burada, int 21 yazı yazdırma, int 20 ise programı onlandırma komutlarıdır. Int 21 komutu sayesinde, DX registerina yüklediğimiz 43 degerinin C harfinin ascii kodu karsılıgı oldugunu görüyoruz.

### SORU 2 

TEMP.COM dosyası çıktı olarak ekranda * işaretini gösterdi

### SORU 3 

a 100

```asm
mov ah,02    (AX registerinin high kısmına 02 yazdır)
mov dl,2a    (DX registerinin low kısmına 2a yazdır)
int 21
int 20
```

n temp.com (Parametre listesi) r bx         (bx yazmacının içeriğini değiştir) r cx          (cx yazmacının içeriğini değiştir) w     (write komutu) q     (programdan çıkış)

### SORU 4 

8086 registerları hakkında bilgi edindik ve Debug komutlarını öğrendik. Debug üzerinde aritmetik işlemler yapmayı ve yazmaçların işlevlerini görmeyi , değiştirmeyi,üzerinde istedgmz işlemleri gerçekleştirmeyi öğrendik.

## deney2önçalışma

### R Register Komutu

Komut CPU registerlerinin değerlerini görmek yada değiştirmek için kullanılır. R komutunun kullanım biçimi aşağıda verilmiştir. - R Register Adı Komut registerlerin kullanımı ile ilgili olmak üzere 3 ayrı görevi yerine getirir. R : Komut tek başına kullanılırsa CPU registerlerinin o anki tüm değerleri gösterilir. Registerlerin yanısıra komut Flag registerinin değerlerini de temsili olarak gösterecektir. Komutun kullanımı sonunda CS:IP ile işaret edilen komut da ekranda gösterilecektir. R komutunun kullanımı sonunda aşağıdakine benzer bir görüntü alınacaktır.

```
-R
AX=0000 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=2054 ES=2054 SS=2054 CS=2054 IP =0100 NV UP EI PL NZ NA PO NC
2054:0100 IE PUSH DS
```

R komutundan sonra parametre olarak F harfi kullanılırsa program flagların değiştirilmesi için mevcut flagları ekrana getirir ve istediğiniz flagları değiştirmeniz için bekler. Bu durumda istediğiniz herhangi bir flagi set yada reset edebilirsiniz.

### -RF

### NV UP EI PL NZ NA PO NC - ZRUP

- Yukarıdaki örnekte Zero flagı SET, direction flagı RESET edilmektedir. R komutu ile sadece flagların değil tüm registerlerin degerleri değiştirilebilir. Bunun için R komutundan sonra değiştirilmesi istenen registerin isminin yazılması gerekir. Bu işlem gerçekleştiğinde registerin mevcut degeri ekrana yazılır ve ( : ) iş areti konularak registerin yeni degeri sorulur. Bu işaretin yanına deger 4 digit hexadecimal olarak verilmelidir. Eger bir deger verilmeyip enter tuşuna basılırsa registerin içeriği değiştirilmeyecektir.

### T Trace Komutu 

Trace komutu hafızada bulunan bir programın satırlarının tek tek veya belli bir kısmının çalıştırılması için kullanılır. Komutun kullanımı aşağıda verilmiştir. - T=Adres Değer Komutun parametreleri seçimliktir. Ilk parametre Adres parametresidir ki bu parametre kullanılacaksa komuttan sonra = işaretinin kullanımı zorunludur. Adres parametresi icra ettirilecek ilk komutun adresi olarak alınır. Değer parametresi kaç adet komutun peşpeşe icra ettirileceğini gösterir. Eğer kullanılmamış ise bu değer 1 olarak alınır. Eğer herhangi bir parametre kullanılmaz ise komut CS:IP ile adreslenen yerden başlayarak 1 komut icra ettirilir ve komutun icr asından sonra registerlerin değeri ve işlenecek olan komut ekranda görüntülenir.

### U Unassembly Komutu 

U Komutu bellekteki programın makine dili ve assembly karşılıklarını ekranda listelemek için kullanılır. Komutun kullanım şekli aşağıda verilmiştir. - U Adres1 Adres2 Parametre olarak verilen Adres1 listelenmek istenen programın başlangıç adresini gösterir. Bu

```asm
adres segment ve offset olarak verilebilir. Bu adres verilirken herhangi bir komutu
```

bölmemesine özen göstermek gerekir. Aksi halde ekrana getirilecek list e anlamsız bir liste olacaktır.Ikinci verilen parametre listelemenin sonunu belirler. Burada verilecek adres offset niteliğinde olmalıdır. Segment Adres1’de belirtilen segment adresi olarak alınacaktır.

### A Assembly Komutu 

A Komutu assembly program yazmak için kullanılır. Bu komutun kullanılış şekli; -- A [segment:offset] şeklindedir. Komutun parametresi olan adres, yazılacak programın bellegin neresinden itibaren yerleşeceğini gösterir. Parametre seçimliktir. Eğer verilmeyecek olur ise mevcut CS ve IP üzerindeki değerler komutun parametresi olarak varsayılır. Komuttan sonra hiç bir parametre vermeyeceğiniz gibi sadece offset adresi de verebilirsiniz. Eğer komuttan sonra sadece tek bir sayı verilmişse verilen değer offset olarak algılanır ve IP registerine bu deger verilerek programın default segment ve belirlenen offset üzerinde n yazılması sağlanır. Komutun çalıştırılması ile, default veya belirlenen segment ve offset adresi yeni bir satır başına yazılarak bu adresin yanında komut girişi için beklenir. Her komut girilip enter tuşuna basıldığında debug ilk önce girilen komutu yorumlar ve girile n komut doğru ise segment ve offset adresleri yazılan komut uzunluğu kadar artırılarak yeni komut girişi için beklemeye başlar. Eğer girilen komut hatalı ise hata yeri gösterilerek komutun tekrar girilmesi için aynı segmet ve offset adreslerinde beklenir. Eğer herhangi bir satırda komut girilmeyerek enter tuşuna basılırsa debug komut satırına geri döner.

- D (Dump / Display): Bu komut ile belleğin istediğimiz segment'inin istediğimiz offset'inden itibaren bilgileri görebiliriz. İstersek görmek istediğimiz alanı sınırlama imkanına da sahibiz. D komutunun yanına gösterilmesi istenen aralığın adresi verilecek olursa sadece belirlenen adres aralığındaki değerler ekranda görüntülenecektir.

F (Fill) : Bellek başlangıç ve bitiş adresleri belirlenen bir alanı belirlenen bir sayı ile doldurmak amacıyla kullanılır. -

```
-F DS:100,120,AB
```

F komutundan yararlanarak DS'in 100H-120H arasındaki kısım ABH değeri ile doldurulacaktır. Bu işlemden sonra D komutu ile DS:100H adresinden itibaren incelersek işlemin olması gibi yapıldığını kontrol etmiş oluruz.

- C (Compare) : Belirlenen aralıktaki bilgileri karşılaştırmak amacıyla kullanılan bir komuttur.

```asm
Farklı segment'ler üzerindeki bilgiler de karşılaştırılabilmektedir.
```

- M (Move) : Bir yerdeki bir blok bilgiyi başka bir yere taşımak için kullanılır

### - M DS:100,110,CS:500

Bu komut ile DS:100H ile DS:110H arasında kalan bilgi CS:500H adresinden itibaren yerleştirilecektir.

### Debug: s (search)

Bir adres aralığında bir veya daha çok bayt değeri desenini arar.Sözdizimi

s Aralık Listes, Parametreler Aralık Gerekli. Aramak istediğiniz aralığın başlangıç ve bitiş adreslerini belirtir .Liste Gerekli. Arama yapmak istediğiniz bir veya birden çok bayt değerinin desenini veya bir dizeyi belirtir.

```asm
Code segment:
```

Belleğin ,operatörleri (komutları) sakladığı bölümüne kod segment adı verilir ve belleğin bu bölgesinin başlangıç adresi CS yazmacında tutulur.Program komutlarının başlangıcını tanıtır.sonraki byte’ını işletilecek asıl bellek adresi belirtilen paragrafın kod segment yazmacına yerleştirilmesiyle ve bu değerin komut pointerina (Ip) eklenmesiyle bulunur.

```asm
Data segment:
```

Aynı şekilde, operandların saklandığı bölüme ise veri segment adı verilir.Bu bellek bölgesinin başlangıç adresi DS yazmacında tutulur.Programın veri bölümünün başlangıcını tanıtır.Derleyici bir veri bildirimini karşılarken veri segmenti içerisinde o verinin boyutuna bağlı bir alan ayırır.Verinin belirli bir tipi varsa başlangıç değeri belleğe yerleştirilir.Aksi durumda değeri programın başlangıcından önceki içeriğinden oluşur.

### -DS:BX- -DS:SI-

```asm
Extra segment:
```

Değişik amaçlarla kullanılan (örneğin string işlemleri) bellek bölgesine ise extra segment adı verilir ve adresi ES yazmacında tutulur

### -ES:DI-

```asm
Stack segment:
```

Yığıt segmentleri verilen geçici olarak bellekte tutulduğu bölgeyi ifade eder SS yazmacı bu bölgenin başlangıç adresini belirtir

### -SS:SP-

### -SS:BP-

### IP: (İnstruction pointer)

İşletilecek sonraki komutların adresini içerir. Bunun nedenide yazmacın değişmesinin programı olumsuz yönde etkileyecek olmasıdır.Komut işaretleyicisine doğrudan erişilemez yada değiştirilemez.

## calisma-840

Başkent Üniversitesi Elektrik - Elektonik Mühendisliği Bölümü

EEM 332 – Mikroişlemciler Laboratuvarı

Ön Çalışma/ Rapor

Deney No: # 2 Deney Adı: Temel Debug ve Çevirici (Assembly) Komutları Deney Tarihi: 10/03/2006

### 2)

### DS: 15000

### CS: 16100

### SS: 13A50

### 8)

Byte Sayısı

```asm
MOV AX,00       B80000     3
MOV AX,BX       89C3       2
MOV CX,12       B91200     3
MOV DX,0101     BA0101     3
OR CX,AX        09C1       2
OR AX,CX        09C8       2
ADD BX,AX       01C3       2
SUB AX,BX       29D8       2
ROL DX,1         D1C2       2
ROR DX,1         D1CA       2
ROR DX,1         D1CA       2
NOT DX           F7D2      2
```

### 9)

```asm
MOV AX,00:AX=0000 BX=0000 CX=0000 DX=0000
```

```asm
MOV AX,BX: AX=0000 BX=0000 CX=0000 DX=0000
```

```asm
MOV CX ,12: AX=0000 BX=0000 CX=0012 DX=0000
```

```asm
MOV DX,0101: AX=0000 BX=0000 CX=0012 DX=0101
```

```asm
OR CX,AX:AX=0000 BX=0000 CX=0012 DX=0101
```

```asm
OR AX,CX:AX=0012 BX=0000 CX=0012 DX=0101
```

```asm
ADD BX,AX: AX=0012 BX=0012 CX=0012 DX=0101
```

```asm
SUB AX,BX:AX=0000 BX=0012 CX=0012 DX=0101
```

```asm
ROL DX,1: AX=0000 BX=0012 CX=0012 DX=0202
```

```asm
ROR DX,1: AX=0000 BX=0012 CX=0012 DX=0101
```

```asm
ROR DX,1: AX=0000 BX=0012 CX=0012 DX=8080
```

```asm
NOT DX: AX=0000 BX=0012 CX=0012 DX=7F7F
```

## rapor_2

### 2)

### DS:BX 15000

### CS:IP 16100

### SS:BP 15050

### 8)

```asm
MOV AX,00       B80000   3
MOV AX,BX       89C3     2
MOV CX,12       B91200   3
MOV DX,0101     BA0101   3
OR CX,AX        09C1     2
OR AX,CX        09C8     2
ADD BX,AX       01C3     2
SUB AX,BX       29D8     2
ROL DX,1         D1C2     2
ROR DX,1         D1CA     2
ROR DX,1         D1CA     2
NOT DX           F7D2    2
```

### 9)

```asm
MOV AX,00:AX=0000 BX=0000 CX=0000 DX=0000
MOV AX,BX: AX=0000 BX=0000 CX=0000 DX=0000
MOV CX ,12: AX=0000 BX=0000 CX=0012 DX=0000
MOV DX,0101: AX=0000 BX=0000 CX=0012 DX=0101
OR CX,AX:AX=0000 BX=0000 CX=0012 DX=0101
OR AX,CX:AX=0012 BX=0000 CX=0012 DX=0101
ADD BX,AX: AX=0012 BX=0012 CX=0012 DX=0101
SUB AX,BX:AX=0000 BX=0012 CX=0012 DX=0101
ROL DX,1: AX=0000 BX=0012 CX=0012 DX=0202
ROR DX,1: AX=0000 BX=0012 CX=0012 DX=0101
ROR DX,1: AX=0000 BX=0012 CX=0012 DX=8080
NOT DX: AX=0000 BX=0012 CX=0012 DX=7F7F
```

## calisma-1259

### EEM332-MİKROİŞLEMCİLER

Deney Numarası: 2 Deney Adı: Temel DEBUG ve Çevirici(Assembly) Komutları

### ÖNÇALIŞMA

1-) Parça (Segment) yazmaçlarının ve Komut Göstericisinin (IP) nasıl kullanıldığını açıklayınız. 8086 işlemcisinde 20 adres bacağı olmasına rağmen en büyük yazmacı 16 bittir.Bir tek yazmaç üzerindeki değer ile ancak 64 KB’lık bir alanı adresleyebilmektedir.Bu durumda 20 adres bacağı ile adresleyebilmesi mümkün olan 1 MB’lık bellekten yararlanabilmek için parça bellek erişim yapısı ortaya atılmıştır. 8086 ailesi de ana bellek her bir çift adresten başlamak üzere 64 KB’lık alanlara ayrılmıştır.Temel olarak 4 tane kesim çeşidi vardır.Herhangi bir kesime erişmek için ancak o alanın kesim yazmacını kullanmakla mümkündür.Bu temel kesim yazmaçları ise CS,SS,DS ve ES olarak adlandırılır. Kesim içerisindeki verilere ise kesim içi işaretçilerle ulaşılmaktadır.(IP)Kesim içi işaretçiler göreli konum olarak adlandırılan,kesimin başlangıcından olan uzaklığı belirleyen değerdir.

2-)Deneysel çalışma kısmında gördüğünüz,BÜYÜK harflerle yazılmış DEBUG konutlarını açıklayınız.

a-) YAZMAÇ(REGİSTER) Komutu: Bu komut o andaki register değerlerini ve bayrakların durumunu belirlemekte kullanılır. Bu komut yardımı ile register'lara istenilen değerler (hexadecimal olmak şartıyla) verilebilir.

b-) DOLDUR(FILL) Komutu : Bellek başlangıç ve bitiş adresleri belirlenen bir alanı belirlenen bir sayı ile doldurmak amacıyla kullanılır.

c-) DÖKÜM(DUMP) Komutu : Bu komut ile belleğin istediğimiz segment'inin istediğimiz offset'inden itibaren bilgileri görebiliriz. İstersek görmek istediğimiz alanı sınırlama imkanına da sahibiz. D komutunun yanına gösterilmesi istenen aralığın adresi verilecek olursa sadece belirlenen adres aralığındaki değerler ekranda görüntülenecektir.

d-) TAŞI(MOVE) Komutu : Bir yerdeki bir blok bilgiyi başka bir yere taşımak için kullanılır

### e-) ARAMA(SEARCH) Komutu 

f-) KARŞILAŞTIR(COMPARE) Komutu : Belirlenen aralıktaki bilgileri karşılaştırmak amacıyla kullanılan bir komuttur. farklı segment'ler üzerindeki bilgiler de karşılaştırılabilmektedir.

g-) ÇEVİR(ASSEMBLE) Komutu : Bu komut Debug yardımıyla basit programlar yazmayı sağlar. Debug içinde yazılan programlar COM uzantılı programlarda olduğu gibi 100H offset adresinden başlarlar. Bu neden ile program çalıştırılacağı zaman mutlaka IP register'ının değerinin R komutu ile 100H e getirilmesi gerekmektedir.

h-) GERİÇEVİR(UNASSEMBLE) Komutu : CS’de yazılı olan makine kodunu kullanıcının anlayacağı formdaki mnemonic'lere çevirmek için kullanılan bir komuttur. Her çağırılışında 32 byte uzunluğunda makine kodunun mnemonic'lerini kullanıcıya gösterir.

ı-) İZLEME(TRACE) Komutu : Yazılmış olan assembly komutları teker teker çalıştırılarak işlem sonunda register ve bayrakların aldıkları değerleri ekranda gösterir. T komutu çalışmaya IP nin gösterdiği noktadan itibaren başlar ve her komut işlendikten sonra durur. Eğer kullanıcı ister ise T komutunun yanına bir sayı da verebilir. Bu durumda verilen sayı kadar komut satırı arka arkaya çalıştırılır, her seferinde register ve flag değerleri ekrana yazılır.

## ucs-eem332 lab ön çalışma 2

### 1) Segment yazmaçlarının hepsi 16 bittir ve hafızanın segment olarak adlandırılan kısmını

adreslemede kullanılırlar.

```asm
Code Segment Yazmacı (CS) : MS-DOS işletim sisteminde, programları oluşturan kodlar
Code Segment’e yüklenir. Yani komutlar Code Segment yazmaçlarında saklanır. Bu kodlar
```

Instruction Pointer (IP) yardımıyla bulunur. IP işlenecek komutun adres bilgisini saklar. Böylece IP, işlenecek CS’i işaret ettiğinde oradaki komutlar çalıştırılır.

```asm
Stack Segment Yazmacı (SS) : Programlar, Stack Segment (SS) denilen bir hafıza alanını
```

geçici depolama alanı olarak kullanırlar. Örneğin bir dallanma veya interrupt olduğunda, o

```asm
andaki bilgiler SS’e kaydolur. Bu yığıtlar “Last In First Out” tekniğiyle çalışır. Stack
```

Pointer (SP) ise SS’ in adresini tutar. Program gerekli interrupt’ı gerçekleştirdikten sonra, SP yardımıyla SS’deki dosyalar yerinden çıkarılır. Program kaldığı yerden devam eder.

```asm
Data Segment Yazmacı (DS) : .exe türündeki bir programda kullanılacak olan veriler Data
```

Segment’ te tutulur. Programın veri bölümünün başlangıç adresi DS içinde tutulur.

```asm
Extra Segment Yazmacı (ES) : Çeşitli string işlemlerinde kullanılan bellek bölgesine Extra
```

Segment adı verilir. Bu bellek adresi DI ve ES içinde tutulur.

Instruction Pointer (IP) : O anda işletilen komuttan sonraki komutun offset adresini içinde tutar. Her kod işleminden sonra mikroişlemci tarafından 1 arttırılır ve işlem bu şekilde devam eder. Bu register’ın değerini, stack üzerindeki bilgiler ile dolaylı olarak değiştirmek mümkündür.

### 2)

YAZMAÇ (REGISTER) : Bu komut CPU’ nun kullandığı yazmaçların görülmesi ve değiştirilmesi için kullanılmaktadır. Eğer tüm yazmaçlar görüntülenmek istenirse, aşağıdaki gibi bir sonuç elde edilir;

```
-R
```

```
AX=0000 BX=0000 CX=0000 DP=0000 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1787      ES=1787     SS=1787    CS=1787     IP=0100     NV UP EI PL NZ NA PO NC
```

```
1787:01000 0000                      ADD [BX+SI], AL
```

Eğer üzerinde değişme yapılacak bir yazmaç içinse;

```
-R AX
```

### AX 0000

: 0200         şeklinde olur.

DOLDUR (FILL) : Belirlediğimiz bir bellek bölgesini, gireceğimiz bir data ile doldurmak için F komutu kullanılır. Kullanımı şu şekildedir;

```
-F DS:100,110,AB       Bu işlem yapılınca DS’nin 100 – 110 adresi arası AB ile doldurulur.
```

DÖKÜM (DUMP) : Bellek bölgesinin istenilen kısmını göstermek için kullanılır.

```
-D komutu girildiğinde en son görüntülenen bellek bölgesinden sonraki 128 byte görüntülenir.
```

Bu alanı küçültmek için;

```
-D (offset) komutu girilir. Böylece başlangıç adresi offset olarak alınır ve sonraki 128 byte
```

görüntülenir.

```
-D (başlangıç) (bitiş)    komutu girildiğinde ise yalnızca belirlenen yerler arası görüntülenir.
```

TAŞI (MOVE) : Bu komut yardımıyla, belirli bir bölgeyi belleğin başka bir yerine taşıyabiliriz. Bunun komut aşağıdaki gibi kullanılabilir;

- M DS:100,110,CS:500            Bu komut ile DS’nin 100-110 arası bölgesi CS:500 e taşınır.

ARAMA (SEARCH) : Bir bellek bölgesinde istenilen veriyi arar. Bunun için aşağıdaki kod parçası kullanılabilir;

-S (başlangıç) (bitiş) (liste)

KARŞILAŞTIR (COMPARE) : Belirli iki aralık içindeki verileri karşılaştırmak için kullanılır.

-C 100,110,10 kodu girildiğinde 100-110 adresindeki veriler ile 10 adresinden başlayan bilgiler karşılaştırılır ve farklı olanları listelenir. Eğer bu veriler aynıysa ekrana hiçbir şey yazılmaz.

ÇEVİR (ASSEMBLE) : Bu kod yardımıyla Assembly dilinde kod yazılabilir.

- A [segment:offset] şeklinde kodlar Assambly dilinde yazılabilir.

GERİ ÇEVİR (UNASSEMBLE) : Bu kod yardımıyla, Assembly dilinde yazılmış kodlar makine diline çevrilir. Böylece ayrı bir derleyici kullanmadan makine dilinde programlar

### yazılabilir. Kullanım şekli aşağıdaki gibidir

```
-U (başlangıç) (bitiş)
```

Bu başlangıç ve bitiş adresleri segment veya offset olarak verilebilir. Burada dikkat edilmesi gereken nokta, başlangıç ve bitiş noktaları seçilirken bir kod parçasının bölünmeden alınması gerektiğidir.

İZLEME (TRACE) : Bellekte bulunan komutların istediğimiz bir kısmını çalıştırmaya yarar. Bunu tek-tek yapabileceğimiz gibi bir bütün halinde de yapabiliriz. Yani;

```
-T (adım sayısı) kodu girildiğinde girilen adım sayısı kadar komut çalıştırılır.
```

```
-T (başlangıç) (adım sayısı) kodu girildiğinde ise başlangıç adresinden sonraki adım sayısı
```

kadar komut çalıştırılır.

## calisma-834

```asm
		.MODEL SMALL
		.STACK 64
		.DATA
		ORG 0010H			
		SIGN_DATA DB 69,87,96,45,75		;place data definitions here
		;
		.CODE
MAIN		PROC	FAR		;this is the program entry point
		MOV	AX,@DATA	;load the data segment address
		MOV	DS,AX		;assign value to DS
		;
		MOV CX,5;place code here	
		MOV BX,OFFSET SIGN_DATA	
		SUB AL,AL
AGAIN:		CMP AL,[BX]
		JA NEXT 
		MOV AL,[BX]
NEXT:		INC BX
		LOOP AGAIN
		MOV BX,10H
		MOV AH,02H
		MOV DL,[BX]
		INT 21H	
		;		
		MOV	AH,4CH	;set up to
		INT	21H		;return to DOS
MAIN		ENDP			
		END	MAIN		;this is the program exit point
```

## calisma-1231

```
Umut [kişisel bilgi çıkarıldı] Sağdıçoğlu
[kişisel bilgi çıkarıldı]
Deney 2
21.03.2011


Microsoft Windows XP [Sürüm 5.1.2600]
(C) Telif Hakkı 1985-2001 Microsoft Corp.

C:\calisma>debug
-r
AX=0000  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1524  ES=1524  SS=1524  CS=1524  IP=0100   NV UP EI PL NZ NA PO NC
1524:0100 0000          ADD     [BX+SI],AL                         DS:0000=CD
-r ip
IP 0100
:
-r ds
DS 1524
:1500
-r cs
CS 1524
:1600
-r f
NV UP EI PL NZ NA PO NC  -nv pe
-f ds:10,1f,23
-d ds:00,3f
1500:0000  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0010  23 23 23 23 23 23 23 23-23 23 23 23 23 23 23 23   ################
1500:0020  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0030  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
-m ds:15,22,cs:100
-d cs:100
1600:0100  23 23 23 23 23 23 23 23-23 23 23 00 00 00 00 00   ###########.....
1600:0110  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1600:0120  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1600:0130  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1600:0140  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1600:0150  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1600:0160  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1600:0170  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
-s ds:00,100,86
-s ds:00,100,ff
-c ds:15,22,cs:100
-c ds:15,2e,cs:100
-a cs:200
1600:0200 MOV AX,00
1600:0203 MOV BX,AX
1600:0205 MOV CX,12
1600:0208 MOV DX,0101
1600:020B OR CX,AX
1600:020D OR AX,CX
1600:020F ADD BX,AX
1600:0211 SUB AX,BX
1600:0213 ROL DX,1
1600:0215 ROR DX,1
1600:0217 ROR DX,1
1600:0219 NOT DX
1600:021B
-u cs:200
1600:0200 B80000        MOV     AX,0000
1600:0203 89C3          MOV     BX,AX
1600:0205 B91200        MOV     CX,0012
1600:0208 BA0101        MOV     DX,0101
1600:020B 09C1          OR      CX,AX
1600:020D 09C8          OR      AX,CX
1600:020F 01C3          ADD     BX,AX
1600:0211 29D8          SUB     AX,BX
1600:0213 D1C2          ROL     DX,1
1600:0215 D1CA          ROR     DX,1
1600:0217 D1CA          ROR     DX,1
1600:0219 F7D2          NOT     DX
1600:021B 0000          ADD     [BX+SI],AL
1600:021D 0000          ADD     [BX+SI],AL
1600:021F 0000          ADD     [BX+SI],AL
-r
AX=0000  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0100   NV UP EI PL NZ NA PE NC
1600:0100 2323          AND     SP,[BP+DI]                         SS:0000=20CD
-r ip
IP 0100
:200
-t

AX=0000  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0203   NV UP EI PL NZ NA PE NC
1600:0203 89C3          MOV     BX,AX
-t

AX=0000  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0205   NV UP EI PL NZ NA PE NC
1600:0205 B91200        MOV     CX,0012
-t

AX=0000  BX=0000  CX=0012  DX=0000  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0208   NV UP EI PL NZ NA PE NC
1600:0208 BA0101        MOV     DX,0101
-t

AX=0000  BX=0000  CX=0012  DX=0101  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=020B   NV UP EI PL NZ NA PE NC
1600:020B 09C1          OR      CX,AX
-t

AX=0000  BX=0000  CX=0012  DX=0101  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=020D   NV UP EI PL NZ NA PE NC
1600:020D 09C8          OR      AX,CX
-t

AX=0012  BX=0000  CX=0012  DX=0101  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=020F   NV UP EI PL NZ NA PE NC
1600:020F 01C3          ADD     BX,AX
-t

AX=0012  BX=0012  CX=0012  DX=0101  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0211   NV UP EI PL NZ NA PE NC
1600:0211 29D8          SUB     AX,BX
-t

AX=0000  BX=0012  CX=0012  DX=0101  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0213   NV UP EI PL ZR NA PE NC
1600:0213 D1C2          ROL     DX,1
-t

AX=0000  BX=0012  CX=0012  DX=0202  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0215   NV UP EI PL ZR NA PE NC
1600:0215 D1CA          ROR     DX,1
-t

AX=0000  BX=0012  CX=0012  DX=0101  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0217   NV UP EI PL ZR NA PE NC
1600:0217 D1CA          ROR     DX,1
-t

AX=0000  BX=0012  CX=0012  DX=8080  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0219   OV UP EI PL ZR NA PE CY
1600:0219 F7D2          NOT     DX
-t

AX=0000  BX=0012  CX=0012  DX=7F7F  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=021B   OV UP EI PL ZR NA PE CY
1600:021B 0000          ADD     [BX+SI],AL                         DS:0012=23


-u 200
1600:0200 B80000        MOV     AX,0000      3 byte
1600:0203 89C3          MOV     BX,AX	     2 byte	
1600:0205 B91200        MOV     CX,0012	     3 byte
1600:0208 BA0101        MOV     DX,0101	     3 byte
1600:020B 09C1          OR      CX,AX        2 byte
1600:020D 09C8          OR      AX,CX        2 byte
1600:020F 01C3          ADD     BX,AX        2 byte
1600:0211 29D8          SUB     AX,BX        2 byte
1600:0213 D1C2          ROL     DX,1         2 byte
1600:0215 D1CA          ROR     DX,1         2 byte
1600:0217 D1CA          ROR     DX,1         2 byte
1600:0219 F7D2          NOT     DX           2 byte
1600:021B 0000          ADD     [BX+SI],AL   
1600:021D 0000          ADD     [BX+SI],AL
1600:021F 0000          ADD     [BX+SI],AL


///DENEY 2 ÇALIŞMA FORMU\\\

Microsoft Windows XP [Sürüm 5.1.2600]
(C) Telif Hakkı 1985-2001 Microsoft Corp.

C:\calisma>debug
-a
1524:0100 MOV AX,BX
1524:0102 MOV AX,AAAA
1524:0105 MOV AX,[BX]
1524:0107 MOV AX,[0004]
1524:010A MOV AX,[BX+SI]
1524:010C MOV AX,[SI]+[0004]
1524:010F MOV AX,[BX][SI]+[0004]
1524:0112
-u 100
1524:0100 89D8          MOV     AX,BX
1524:0102 B8AAAA        MOV     AX,AAAA
1524:0105 8B07          MOV     AX,[BX]
1524:0107 A10400        MOV     AX,[0004]
1524:010A 8B00          MOV     AX,[BX+SI]
1524:010C 8B4404        MOV     AX,[SI+04]
1524:010F 8B4004        MOV     AX,[BX+SI+04]
1524:0112 0000          ADD     [BX+SI],AL
1524:0114 0000          ADD     [BX+SI],AL
1524:0116 0000          ADD     [BX+SI],AL
1524:0118 0000          ADD     [BX+SI],AL
1524:011A 0000          ADD     [BX+SI],AL
1524:011C 3400          XOR     AL,00
1524:011E 1315          ADC     DX,[DI]

-r ds
DS 1524
:200
-r cs
CS 1524
:100
-f ds:1234,1234,ED
-f ds:1235,1235,BE
-f ds:1236,1236,CD
-f ds:1237,1237,AB
-r SI
SI 0000
:1236
-r
AX=0000  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=1236  DI=0000
DS=0200  ES=1524  SS=1524  CS=0100  IP=0100   NV UP EI PL NZ NA PO NC
0100:0100 0000          ADD     [BX+SI],AL                         DS:1236=CD
-a 00
0100:0000 MOV AX,1234
0100:0003 MOV BX,[1234]
0100:0007 MOV CX,[SI]
0100:0009
-r ip
IP 0100
:0000
-t

AX=1234  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=1236  DI=0000
DS=0200  ES=1524  SS=1524  CS=0100  IP=0003   NV UP EI PL NZ NA PO NC
0100:0003 8B1E3412      MOV     BX,[1234]                          DS:1234=BEED
-t

AX=1234  BX=BEED  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=1236  DI=0000
DS=0200  ES=1524  SS=1524  CS=0100  IP=0007   NV UP EI PL NZ NA PO NC
0100:0007 8B0C          MOV     CX,[SI]                            DS:1236=ABCD
-t

AX=1234  BX=BEED  CX=ABCD  DX=0000  SP=FFEE  BP=0000  SI=1236  DI=0000
DS=0200  ES=1524  SS=1524  CS=0100  IP=0009   NV UP EI PL NZ NA PO NC
0100:0009 0000          ADD     [BX+SI],AL                         DS:D123=85
```

## fig2-2

```asm
;THE FORM OF AN ASSEMBLY LANGUAGE PROGRAM
 USING SIMPLIFIED SEGMENT DEFINITION
		.MODEL SMALL
		.STACK 64
		.DATA
		;
		;place data definitions here
		;
		.CODE
MAIN		PROC	FAR		;this is the program entry point
		MOV	AX,@DATA	;load the data segment address
		MOV	DS,AX		;assign value to DS
		;
		;place code here	
		;	
		MOV	AH,4CH	;set up to
		INT	21H		;return to DOS
MAIN		ENDP			
		END	MAIN		;this is the program exit point
```

## 2010 laboratuvar 2 deneysel çalışma şablonu

Şablondaki DEBUG oturumu; yazmaç ayarı, fiziksel adres, doldurma, taşıma, arama ve karşılaştırma işlemlerini gösterir.

```
A,b,c,d,e şıkkı

-r
AX=0000  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=13B6  ES=13B6  SS=13B6  CS=13B6  IP=0100   NV UP EI PL NZ NA PO NC
13B6:0100 0000          ADD     [BX+SI],AL                         DS:0000=CD

-r ip
IP 0100
:100
-r ds
DS 13B6
:1500
-r cs
CS 13B6
:1600
-r f
NV UP EI PL NZ NA PO NC  -nv pe
-r
AX=0000  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=1600  IP=0100   NV UP EI PL NZ NA PE NC
1600:0100 0000          ADD     [BX+SI],AL                         DS:0000=00


 Effectif adresi yazmak için ilk register i 4 bit sola kaydırırız ve ikinci ile toplarız. Buna göre;

DS:BX = 15000
CS:IP = 16100
SS:BP = 13B60

3)

-f ds:10,1f,23

4)
-d ds:00,3f
1500:0000  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0010  23 23 23 23 23 23 23 23-23 23 23 23 23 23 23 23   ################
1500:0020  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0030  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................

5)
-m ds:15,28,cs:100
-d ds:100
1500:0100  23 23 23 23 23 23 23 23-23 23 23 00 00 00 00 00   ................
1500:0110  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0120  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0130  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0140  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0150  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0160  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
6) 
-s ds:0000 0100 86
-s ds:0000 0100 ff
Yukardaki kodlar ile 00-100 arasındaki adreslerde 86 ve ff i arar.
Sonuç bulamadığı için ekranda herhangi bir açıklama çıkmadı.

7)

A ve b şıkkını aşağıdaki kodları girerek gerçekleştirdim.
-c 15,28,100
-c 15,34,100

Ancak daha önce ds:15 ten başlayan verileri cs:100 ile başlayan depolama yerlerine taşıdığım için ve ilgili depolama bölgelerinin dışındakilerin içi  “00” olduğundan farklı hiçbir değer belirleyemedi ve sonuç göstermedi.

Eğer karşılaştırma fonksiyonunu aşağıdaki gibi kullansaydım sonuç verecekti.

-c 30,36,100
1500:0030  00  23  1500:0100
1500:0031  00  23  1500:0101
1500:0032  00  23  1500:0102
1500:0033  00  23  1500:0103
1500:0034  00  23  1500:0104
1500:0035  00  23  1500:0105
1500:0036  00  23  1500:0106

Burada c:30 ile başlayan adres 00 c:100 ile başlayan adres 23 olduğu için farkı ekranda gösterdi.


8)

-a
13B6:0100 mov ax,00
13B6:0103 mov bx,ax
13B6:0105 mov cx,12
13B6:0108 mov dx,0101
13B6:010B or cx,ax
13B6:010D or ax,cx
13B6:010F add bx,ax
13B6:0111 sub ax,bx
13B6:0113 rol dx,1
13B6:0115 ror dx,1
13B6:0117 ror dx,1
13B6:0119 not dx
13B6:011B

-u 13b6:0100
13B6:0100 B80000        MOV     AX,0000
13B6:0103 89C3          MOV     BX,AX
13B6:0105 B91200        MOV     CX,0012
13B6:0108 BA0101        MOV     DX,0101
13B6:010B 09C1          OR      CX,AX
13B6:010D 09C8          OR      AX,CX
13B6:010F 01C3          ADD     BX,AX
13B6:0111 29D8          SUB     AX,BX
13B6:0113 D1C2          ROL     DX,1
13B6:0115 D1CA          ROR     DX,1
13B6:0117 D1CA          ROR     DX,1
13B6:0119 F7D2          NOT     DX
13B6:011B 0034          ADD     [SI],DH
13B6:011D 00A51300      ADD     [DI+0013],AH


9) Bir üst soruda a kodunu adres vermeden girdiğim için cs:13b6:0100 adresinden itibaren yazmaya başladı. Bu sebeple 1600 de olan cs değerini 

-r cs
CS 1600
:13B6 
Kodu  ile değiştirdim.

AX=0000  BX=0000  CX=0000  DX=0000  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0103   NV UP EI PL ZR NA PE NC
13B6:0103 89C3          MOV     BX,AX
-t

AX=0000  BX=0000  CX=0000  DX=0000  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0105   NV UP EI PL ZR NA PE NC
13B6:0105 B91200        MOV     CX,0012
-t

AX=0000  BX=0000  CX=0012  DX=0000  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0108   NV UP EI PL ZR NA PE NC
13B6:0108 BA0101        MOV     DX,0101
-t

AX=0000  BX=0000  CX=0012  DX=0101  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=010B   NV UP EI PL ZR NA PE NC
13B6:010B 09C1          OR      CX,AX
-t

AX=0000  BX=0000  CX=0012  DX=0101  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=010D   NV UP EI PL NZ NA PE NC
13B6:010D 09C8          OR      AX,CX


AX=0012  BX=0000  CX=0012  DX=0101  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=010F   NV UP EI PL NZ NA PE NC
13B6:010F 01C3          ADD     BX,AX
-t

AX=0012  BX=0012  CX=0012  DX=0101  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0111   NV UP EI PL NZ NA PE NC
13B6:0111 29D8          SUB     AX,BX
-t

AX=0000  BX=0012  CX=0012  DX=0101  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0113   NV UP EI PL ZR NA PE NC
13B6:0113 D1C2          ROL     DX,1
-t

AX=0000  BX=0012  CX=0012  DX=0202  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0115   NV UP EI PL ZR NA PE NC
13B6:0115 D1CA          ROR     DX,1
-t

AX=0000  BX=0012  CX=0012  DX=0101  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0117   NV UP EI PL ZR NA PE NC
13B6:0117 D1CA          ROR     DX,1
-

AX=0000  BX=0012  CX=0012  DX=8080  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0119   OV UP EI PL ZR NA PE CY
13B6:0119 F7D2          NOT     DX
-t

AX=0000  BX=0012  CX=0012  DX=7F7F  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=011B   OV UP EI PL ZR NA PE CY
13B6:011B 0034          ADD     [SI],DH                            DS:0000=00
-t

AX=0000  BX=0012  CX=0012  DX=7F7F  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=011D   NV UP EI PL NZ NA PO NC
13B6:011D 00A51300      ADD     [DI+0013],AH                       DS:0013=23
-t

AX=0000  BX=0012  CX=0012  DX=7F7F  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0121   NV UP EI PL NZ NA PO NC
13B6:0121 0000          ADD     [BX+SI],AL                         DS:0012=23
```

*Not: .dot dosyasının hazırlanmış PDF karşılığı bulunmadığından metni özgün Word dosyasının metin tablosundan çıkarılmıştır. İndirme paketine meta verisiz TXT dökümü eklendi. Kaynaktaki “efektif adres” ifadesi, verilen hesaplarda fiziksel adresi anlatmaktadır.*
