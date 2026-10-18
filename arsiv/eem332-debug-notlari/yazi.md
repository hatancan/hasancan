---
baslik: EEM332 Mikroişlemciler: DEBUG Notları ve Kaynak Derlemesi (Fran Golden ve Ders Arşivi)
ozet: DEBUG ile yazmaç ve bellek inceleme, komutları adım adım izleme ve x86 komut tablosu.
---

Bu yazı, Başkent Üniversitesi **EEM332 Mikroişlemciler** ders arşivindeki ilgili notları ve uygulamaları bir araya getiriyor (2002–2010). DEBUG ile yazmaç ve bellek inceleme, komutları adım adım izleme ve x86 komut tablosu. Kaynak: Ders derlemesi; Introduction to DEBUG belgesinde Fran Golden ve özgün eğitim kaynakları belirtilmiştir. Belgelerin PDF arşiv kopyaları ve varsa kaynak kodları yazının sonunda ZIP olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Debug Komutları

Debug Komutları Assembly komutlarının nasıl çalıştıklarını deneyerek görmek ve yazılan programların amacına uygun çalışıp çalışmadığını anlamak varsa hatalarını düzeltmek için DOS'un DEBUG.COM isimli programı kullanılmaktadır. Her ne kadar daha gelişmiş, kullanıcıya hitap eden debuger'lar olsa da kolay bulunulabilirliği ve basit uygulamalarda sağladığı rahatlık sayesinde tercih nedenidir. DEBUG programını kullanabilmek için komutlarını bilmek gereklidir. Burada DEBUG programının bazı komutlarını basit örnekler yardımıyla açıklamaya çalışacağız.

```
C:\>DEBUG
```

-

Çizgi işareti artık debug programının komut kabul etmeye hazır olduğunu belirtmektedir.

- R (Register) : Bu komut o andaki register değerlerini ve bayrakların durumunu belirlemekte kullanılır.

```
-R
AX=0000 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=2AF2 ES=2AF2 SS=2AF2 CS=2AF2 IP=0100 NV UP EI PL NZ NA PO NC
2AF2:0100 8B24   MOV   SP,[SI]           DS:0000=20CD
```

-

Bu komut yardımı ile register'lara istenilen değerler (hexadecimal olmak şartıyla) verilebilir.

```
-R AX
```

### AX 0000

### 

':' işaretinden sonra AX register'i için istediğimiz değeri yazarak enter tuşuna basacak olursak;

### 12AF

```
-R
AX=12AF BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=2AF2 ES=2AF2 SS=2AF2 CS=2AF2 IP=0100 NV UP EI PL NZ NA PO NC
2AF2:0100 8B24   MOV   SP,[SI]           DS:0000=20CD
```

- AX registerinin değerinin 12AF olmasını sağlarız.

Register’ları takip eden NV UP EI PL NZ NA PO NC değerleri ise bayrakların durumunu belirtmektedir.

```
-R F
```

### NV UP EI PL NZ AC PO CY -

komutu ile sadece bayrakların durumu da görülerek gerekenler değiştirilebilir. Eğer flag değeri değiştirilmeyecek ise ara çubuğuna basarak bir sonraki flag değerine geçilebilir.

Flag İsmi                          Set(1)                      Clear (0) Overflow - OF                  OV (overflow)              NV (not overflow) Direction - DF              DN (decrement - down)         UP (increment - up) Interrupt - IF                   EI (enable)                 DI (disable) Sign - SF                       NG (negative)                  PL (plus) Zero - ZF                         ZR (zero)                  NZ (not zero) Auxilary Carry- AF           AC (auxilary carry)           NA (not auxilary) Parity - PF                   PE (even parity)              PO (odd parity) Carry - CF                     CY (carry yes)               NC (not carry) Tablo 18-1 Debuger’da kullanılan Flag kısaltmaları

- D (Dump / Display): Bu komut ile belleğin istediğimiz segment'inin istediğimiz offset'inden itibaren bilgileri görebiliriz. İstersek görmek istediğimiz alanı sınırlama imkanına da sahibiz.

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

```
-D DS:100,115
2AF2:0100 8B 24 17 5A 18 BA 4A 29-A2 4F F6 C9 07 AE 07 09 .$.Z..J).O......
2AF2:0110 20 8C 07 BA 4F 80                    ...O.
```

-

Görüldüğü gibi eğer D komutunun yanına gösterilmesi istenen aralığın adresi verilecek olursa sadece belirlenen adres aralığındaki değerler ekranda görüntülenecektir.

- A ( Assembly) : Bu komut Debug yardımıyla basit programlar yazmayı sağlar. Debug içinde yazılan programlar COM uzantılı programlarda olduğu gibi 100H offset adresinden başlarlar. Bu neden ile program çalıştırılacağı zaman mutlaka IP register'ının değerinin R komutu ile 100H e getirilmesi gerekmektedir.

```
-A
2AF2:0100 MOV AX,5
2AF2:0103 ADD AX,4
2AF2:0106 SHR AX,1
2AF2:0108 ^C
```

- A komutu verildikten sonra CS'in 100H adresinden itibaren assembly program yazmanıza imkan sağlanmış olur. Burada verilen her türlü sayı mutlaka hexadecimal formda olmalıdır. Komut yazmanız bittiğinde Ctrl-C tuşlarına basarak işlemi sonlandırabilirsiniz.

- T (Trace) : Yazılmış olan assembly komutları teker teker çalıştırılarak işlem sonunda register ve bayrakların aldıkları değerleri ekranda gösterir. T komutu çalışmaya IP nin gösterdiği noktadan itibaren başlar ve her komut işlendikten sonra durur.

```
-R
AX=12AF BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=2AF2 ES=2AF2 SS=2AF2 CS=2AF2 IP=0100 NV UP EI PL NZ NA PO NC
2AF2:0100 B80500  MOV   AX,0005
```

```
-T
```

```
AX=0005 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=2AF2 ES=2AF2 SS=2AF2 CS=2AF2 IP=0103 NV UP EI PL NZ NA PO NC
2AF2:0103 050400  ADD   AX,0004
-T
```

```
AX=0009 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=2AF2 ES=2AF2 SS=2AF2 CS=2AF2 IP=0106 NV UP EI PL NZ NA PE NC
2AF2:0106 D1E8   SHR   AX,1
-T
```

```
AX=0004 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=2AF2 ES=2AF2 SS=2AF2 CS=2AF2 IP=0108 NV UP EI PL NZ AC PO CY
2AF2:0108 A24FF6  MOV   [F64F],AL           DS:F64F=11
```

-

Bu örnekte görüldüğü gibi az evvel yazdığımız assembly kodunu çalıştırmış olduk. Her işlemden sonra register ve bayraklar üzerindeki değişikleri rahat izlememiz için hazırlanmış bir komuttur.

Eğer kullanıcı ister ise T komutunun yanına bir sayı da verebilir. Bu durumda verilen sayı kadar komut satırı arka arkaya çalıştırılır, her seferinde register ve flag değerleri ekrana yazılır. Örnek;

### -T5

Ya da kullanıcı istediği bir offset’ten (adresten ) itibaren kaç komut çalıştıracağını da söyleyebilir. Örnek;

```
-T=200,5
```

Bu komut 200H offset'inden itibaren 5 komut arka arkaya çalıştır demektir.

- U (Unassembly) : CS’de yazılı olan makine kodunu kullanıcının anlayacağı formdaki mnemonic'lere çevirmek için kullanılan bir komuttur. Her çağırılışında 32 byte uzunluğunda makine kodunun mnemonic'lerini kullanıcıya gösterir.

```
-U CS:112
2AF2:0112 07      POP   ES
2AF2:0113 BA4F80    MOV    DX,804F
2AF2:0116 FC      CLD
2AF2:0117 807463BA    XOR   BYTE PTR [SI+63],BA
2AF2:011B C6418208    MOV   BYTE PTR [BX+DI-7E],08
2AF2:011F 83745BBA    XOR   WORD PTR [SI+5B],-46
2AF2:0123 D208     ROR    BYTE PTR [BX+SI],CL
2AF2:0125 847453    TEST DH,[SI+53]
2AF2:0128 BADE04    MOV    DX,04DE
2AF2:012B 0908     OR    [BX+SI],CX
2AF2:012D 85744B    TEST SI,[SI+4B]
2AF2:0130 BAEA08    MOV    DX,08EA
```

-

Bu komut ile CS:112 adresinden itibaren 32 byte makine kodu unassembly edilerek mnemonic karşılıkları gösterilmiştir.

İstenirse başlangıç adresi ve kaç byte unassembly edilmesi gerektiği de parametre olarak verilebilir.

```
-U CS:100L8
```

Bu komut CS:100H adresinden itibaren 8 byte'ı unassembly edecektir.

- E (Edit) : Bellekte herhangi bir yerdeki değerleri değiştirmek amacıyla kullanılan bir komuttur.

-

```
-E DS:10
2AF2:0010 5A.
```

Komut DS:10H adresindeki byte'in değerinin değiştirilmesi için kullanıcının bir hexadecimal değer girmesini bekler. Eğer değer değiştirilmeyecek ise ara çubuğu yardımıyla bir sonraki byte'a geçilerek onun değeri değiştirilebilir. Bu işlemi bitirmek için ENTER tuşuna basılmalıdır.

- F (Fill) : Bellek başlangıç ve bitiş adresleri belirlenen bir alanı belirlenen bir sayı ile doldurmak amacıyla kullanılır.

-

```
-F DS:100,120,AB
```

F komutundan yararlanarak DS'in 100H-120H arasındaki kısım ABH değeri ile doldurulacaktır. Bu işlemden sonra D komutu ile DS:100H adresinden itibaren incelersek işlemin olması gibi yapıldığını kontrol etmiş oluruz.

```
-D DS:100
2AF2:0100 AB AB AB AB AB AB AB AB-AB AB AB AB AB AB AB AB ................
2AF2:0110 AB AB AB AB AB AB AB AB-AB AB AB AB AB AB AB AB ................
2AF2:0120 AB 5B BA D2 08 84 74 53-BA DE 04 09 08 85 74 4B .[....tS......tK
2AF2:0130 BA EA 08 86 74 43 12 28-BA F6 08 87 74 3B BA 02 ....tC.(....t;..
2AF2:0140 50 08 90 20 88 74 33 BA-0E 08 89 74 2B BA 1A 41 P.. .t3....t+..A
2AF2:0150 82 08 8A 74 23 BA 26 08-8B 74 1B BA 32 54 24 08 ...t#.&..t..2T$.
2AF2:0160 8D A2 BA 3E 08 8E 48 00-74 0B BA 86 08 FF 74 03 ...>..H.t.....t.
2AF2:0170 BA 4A 50 E9 1D A0 C0 C9-BA 56 50 E8 17 75 E8 AB .JP......VP..u..
```

-

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
2AF2:0110 AB FF 2AF2:0020
```

Bu komut 100H-110H adresindeki bilgiler ile 10H adresinden başlayan bilgileri karşılaştırır ve farklı olanları listeler.

### -C 100,110,100

-

100H-110H adresindekileri yine 100H adresindekiler ile karşılaştırmaktadır. Herhangi bir farklılık bulunmadığı için ekranda hiçbir bilgi görünmez.

### -C DS:100,110,CS:300

```
2AF2:0100 AB 25 2AF2:0300
2AF2:0101 AB 44 2AF2:0301
2AF2:0102 AB 68 2AF2:0302
2AF2:0103 AB 20 2AF2:0303
2AF2:0104 AB DD 2AF2:0304
2AF2:0105 AB 20 2AF2:0305
2AF2:0106 AB 91 2AF2:0306
2AF2:0107 AB CF 2AF2:0307
2AF2:0108 AB 3A 2AF2:0308
2AF2:0109 AB 1C 2AF2:0309
2AF2:010A AB 04 2AF2:030A
2AF2:010B AB 1C 2AF2:030B
2AF2:010C AB 6B 2AF2:030C
2AF2:010D AB 82 2AF2:030D
2AF2:010E AB 04 2AF2:030E
2AF2:010F AB 1C 2AF2:030F
2AF2:0110 AB 04 2AF2:0310
```

Görüldüğü gibi farklı segment'ler üzerindeki bilgiler de karşılaştırılabilmektedir.

```
-G (Go): Programın verilen bir adrese kadar ya da bitene kadar çalışmasını sağlamak amacıyla kullanılır.
```

```
-G
```

Program terminated normally

Program eğer düzgün çalıştı ise yukarıdaki mesaj ekrana gelecektir. Programın dönüş adreslerinde bir hata varsa ya da programda bir mantık hatası yapılmış ise program hiçbir zaman bitmez. Bu durumda makinenin reset edilmesi gerekecektir.

- H (Hex ): Verilen iki sayının hexadecimal toplamını ve farkını hesaplamak için kullanılır.

### -H2E,3

### 0031 002B

-

İlk gösterilen değer iki hexadecimal sayının toplamı diğeri ise farkıdır.

- L (Load) : Belleğe programı tekrar yüklemek için kullanılır.

- M (Move) : Bir yerdeki bir blok bilgiyi başka bir yere taşımak için kullanılır

### - M DS:100,110,CS:500

Bu komut ile DS:100H ile DS:110H arasında kalan bilgi CS:500H adresinden itibaren yerleştirilecektir.

- P (Proceed) : Bu komut T komutu ile benzer özellikler göstermektedir. Komutları çalıştırdıktan sonra register ve flag değerlerini ekranda gösterir. Ancak T komutundan en büyük farklılığı özellikle LOOP, CALL, INT gibi komutların işlenmesindedir. Bu komutlardan herhangi biri P komutu ile çalıştırılacak olursa o işlemin detaylarına girmeden sonucu üretir. (Eğer bir LOOP ise çevrim sonuçlanana kadar, bir CALL ise işlemler yerine getirilip geri dönülene kadar ya da bir INT ise interrupt handler'in yapması gereken tüm işlemler yapıldıktan sonra register ve Bayrakların durumlarını gösterir).

- Q (Quit): Debuger dan çıkmak için kullanılan bir komuttur.

### -Q

```
C:\>
```

## calisma-685

### 8086 REGISTERLARI ve SEGMENTLERİ

Mikro işlemci, register adı verilen 14 adet özel lokasyon içerir. Herbiri 16 bit genişliğinde olan bu lokasyonları özel bellek birimleri olarak düşünebiliriz. Registerlar, mikro işlemci tarafından özel amaçlar için kullanılır. Ayrıca, çeşitli verilerin geçici süreler için saklanması ve bu veriler üzerinde işlem yapılması için registerlardan yararlanılır. Registerlar CPU chip’inin üzerinde yer aldıklarından, registerla yapılan işlemler, bellek bölgeleri üzerinde yapılan işlemlere nazaran çok daha hızlıdır.

8086/8088 mikro işlemcisinin sahip olduğu registerları aşağıdaki gibi guruplara ayırmamız mümkün;

1.Genel amaçlı Registerlar

a) Data Registerları (4 adet )

b) Pointer ve Index Registerları (4 adet )

2.Instruction Pointer Regiterı(1 adet )

3.Program Status Word Registerı (1 adet )

4.Segment Registerları (4 adet )

Yukarıda gösterilen 14 adet registerın 4 tanesi CODE, DATA, STACK VE EXTRA segmentlerin başlangıç adreslerini saklayan CS,DS,SS ve ES registerlarıdır.Bu dört registera genel olarak segment registerları denilmektedir. Geriye kalanlardan 8 tanesi genel amaçlı register, 1 tanesi instruction pointer (komut göstergeci ) registeri ve sonuncusu da program status word (durum göstergeci) registeri olarak bilinmektedir. Program status word registerına flag registerı adını vereceğiz. Genel amaçlı registerler, kendi aralarında iki guruba ayrılırlar. Her iki gurup, 4 adet registerdan oluşur. Bunlardan ilk dört registera data, diğer 4 adet registera ise pointer ve index registerları adı verilir.

### 1.Genel amaçlı registerlar

### a) Data Registerları 

Daha çok, aritmetiksel işlemler için kullanılan DATA registerleri AX,BX,CX ve DX’dir. Herbir DATA registeri diğer registerlerden farklı olarak, bir bütün halinde veya iki parça halinde kullanılabilmektedir. Bir DATA registerini iki alt alana bölebilir, böylece registeri 16 bitlik birtek register halinde veya 8 bitlik iki ayrı register halinde kullanma imkanına sahip olabiliriz. Bu özellik şekil üzerinde gösterilmiştir. Örneğin AX registerini 16 bitlik işlemler için AX’i oluşturan AH ve AL yi ise 8 bitlik işlemler için ele alırız. 16 bit uzunluğundaki data registerlerinden herhangi birisinin yüksek seviyeli kısmı (high order) register isminin ve ‘High’ kelimesinin ilk harfi ile , alçak seviyeli kısmı (Low order) ise ,yine register isminin ve ‘Low’ kelimesinin ilk harfi ile gösterilir. Böylece AX için AH ve AL, BX için BH ve BL ,CX için CH ve CL, DX için DH ve DL olarak isimlendirilen 8- bitlik registerler elde edilir. Bu 8 bit registerlerden birinin değerinin değiştirilmesi ile, kendisini ihtiva eden 16 bit registerinin değerinin de değişeceği ve bunun tersinin de mümkün olacağı açıktır. Fakat bir 16-bit registerin herhangi bir yarımı üzerinde yapılan işlem diğer yarımı üzerinde değişikliğe yol açmayacaktır. Data registerlerinin dışında kalan registerlerinin dışında kalan registerlerin, bu şekilde alt alanlara bölenemeyeceği şekil üzerinde de gösterilmiştir. Ancak flag registerleri için daha da farklı bir kullanım söz konusudur.

Akümülatör olarak isimlendirilebilen AX registeri ; çarpa, bölme, giriş, çıkış, bazı string operasyonlarında word uzunluklu olarak kullanılır. AL registeri byte uzunluklu olup, bazı operasyonların sayaç registeri olarak veya desimal amaçlı aritmetiksel işlemlerde transfer alanı (alıcı alan registeri ) olorak kullanılır. Ah registeri byte uzunluklu bölme ve çarpmalarda kullanılır. Base registerolarak isimlendirilebilen BX , daha çok bellek içindeki verilerin adreslanmesinde kullanılır. CX sayaç registeridir, LOOP komutlarının veya tekrarlı! ; string operasyonlarının sayaç registeri olarak kullanılır. CL registeri shift ve rotate sayacı olarak kullanılabilir. Data registeri ismi verilen DX , word uzunluklu çarpma ve bölme operasyonlarında kullanılır.

### b) Pointer ve Index Registerları 

Yukardaki şekil üzerinde de gösterildiği gibi; pointer ve indeks registerları SP, BP, SI ve DI ’dir. Ancak, IP ve BX registerlerini de birer pointer ya da indeks registerı olarak kabul etmek mümkündür. Pointer ve indeks registerleri de, data registerleri gibi aritmetiksel işlemler için kullanılabilmektedirler. Fakat bu registerlerin kullanımındaki asıl amaç çeşitli bellek bölgelerindeki verilere ulaşabilmek için adres göstericisi olarak ele alınmalarıdır. Bellek içindeki bir lokasyonun adresini gösterebilmek için, iki ayrı adres değeri kullanılır. İlk değer, işaret edilen lokasyonu içinde barındıran segmentin adresidir . bu noktada segment registerlerinden yararlanılır. Lokasyonun segment içindeki yerini gösteren ikinci adres değeri ise offset adresi olarak bilinir. Offset adreslerinin gösterilmesi için de , pointer ve indeks registerlarından yararlanılır.

Mikroişlemci, code segment içindeki lokasyonlara erişebilmek için CS ve IP registerlarını kullanır.

```asm
Stack segment içinde bulunan bir veriye ulaşmak için SS registerı ile birlikte SP ya da BP
```

registerlarından birini kullanmak gerekir. Data segment içindeki lokasyonlara erişmek için, data segmentin başlangıcı olan DS registerından, lokasyonun offset adresini göstermesi için de BX, SI veya DI registerlarından yararlanılır. Ekstra segment ya da gelişigüzel seçilen bir segment içerisindeki lokasyonlara erişebilmek için CS, DS, SS’ten yararlanabiliriz.

### 2. Instruction Pointer Registerı :

Komut göstergeci olarak isimlendirebileceğimiz IP registeri, 8088’in icra ünitesi tarafundan icra ettirilecek olan bir sonraki komutun offset adresini içerir. Offset adersi IP ile gösterilen bellek bölgesi code segmenti içindedir. Çünkü programları oluşturan komutlar bu segment içinde bulunur. IP registeri özel amaçlı bir register olması nedeniyle, programcı tarafından direkt olarak kullanılamaz. Ancak bu registerin değerini, stack üzerindeki bilgiler ile dolaylı olarak değiştirmek mümkündür.

### 3. Program Status Word Registerı :

Program status word registeri, kısaca PSW şeklinde gösterebiliriz. Bu registere flag registeri adını vereceğiz. Flag registeri diğer registerlerden oldukça farklıdır. Herşeyden önce, ‘PSW’ gösterimi bir operand değil, sadece bu registerden bahsetmek için kullanılan bir kısaltmadır. Flag registerinin bir bütün olarak veya 16 bitlik, 8 bitlik bir sayı olarak değerlendirilmesi söz konusu değildir. Çünkü flag registerinin sayısal değeri değil, kendisini oluşturan bitlerin herbirinin değeri önem taşımaktadır. Ancak, burada da bir kısıtlama olacak ve registeri oluşturan 16 bitten sadece 9 tanesi kullanılacaktır. Bu 9 bitin herbirinin mevcut değeri çeşitli kontrol komutların icra şekline etki etmekte ya da aritmetiksel veya mantıksal işlemlerin sonucu hakkında bilgi vermektedir.

### 4. Segment Registerları :

8088 ve 8086 işlemcisi kullanan bilgisayarlar, programların veya dataların belleğin iki ayrı alanına yerleştirirler. Bu program ve data alanları maximum 64 K büyüklüğnde olup segment olarak isimlendirilir. 8088 işlemcisi aynı anda 4 ayrı segmente sahip olabilir. Bu segmentler CODE, DATA, STACK ve EXTRA segment olarak isimlendirilir. Bu segmentlere ait ilk byte’ın diğer bir deyişle segmentin başlangıç adresinin gösterilmesi için 4 ayrı register kullanılır. Bunlar; sırası ile CS, DS, SS ve ES olup segment registerleri olarak isimlendirilirler. Code segment registeri olan CS icra gören programı içeren segmentin başlangıç adresini gösterir. Diğer bir deyişle, CS ile adreslenen segment içinde makine dili komutları yer almaktadır. Stack segment registeri olan SS, geçerli stack segmentin başlangıç adresini içerir. Stack segmen! t,çeşitli verilerin geçici olarak saklandığı bir bellek bloğudur.

```asm
Data segment registeri olan DS ,geçerli data segmentinin başlangıç adresidir. Bu segment genel olarak
```

program değişkenleri tarafından kullanılır. Diğer bir deyişle, bilgi işlem operasyonlarına tabi tutulan bilgiler, data segment içindeki lokasyonlarda yer alırlar. Ekstra segment registeri olan ES geçerli ekstra segmentin başlangıç adresini içerir. Ekstra segment, genel olarak string operasyonları için kullanılır. Yeterli bellek büyüklüğüne sahip olan sistemlerde bu 4 segment, belleğin farklı parçalarıdır. Geniş belleğe sahip olmayan sistemlerde ise, bu segmentler üstüste gelebilir.

### 8086 SEGMENTLERİ

*Yukarıda registerlardan bahsederken, 8086 segmentlerinin de detaylı olarak bahsi

### geçmişti.Ancak yeniden segmentleri özetleyecek olursak

```asm
Code Segment:
Bu segment çalışan programı içeren segmentin adresini gösterir. Diğer bir deyişle CS ile
adreslenen segment içinde makine dili komutları yer almaktadır. Segmentin ilk baytından itibaren
```

program parçası çalıştırılmaya başlanır.

```asm
Data Segment:
```

Data segmenti register’i olan DS geçerli data segmentinin başlangıç adresini içerir. Bu segment genel olarak program değişkenlerini tarafından kullanılır. Diğer bir deyişle bilgi işlem operasyonlarında tabii tutulan bilgiler Data Segment içindeki lokasyonlara (bölümlerde) yer alır.

```asm
Stack Segment:
Bu segment alt programlara giderken dönüş adreslerini saklamak program bitiminde işletim sistemine
```

dönmek için gerekli bölgelerin saklanmasında kullanılır.

```asm
Extra Segment:
```

Genel olarak string operasyonları için kullanılır.

### DEBUG KOMUTLARI

Assembly komutlarının nasıl çalıştıklarını deneyerek görmek ve yazılan programların amacına uygun çalışıp çalışmadığını anlamak varsa hatalarını düzeltmek için DOS'un DEBUG.COM isimli programı kullanılmaktadır. Her ne kadar daha gelişmiş, kullanıcıya hitap eden debuger'lar olsa da kolay bulunulabilirliği ve basit uygulamalarda sağladığı rahatlık sayesinde tercih nedenidir. DEBUG programını kullanabilmek için komutlarını bilmek gereklidir. Burada DEBUG programının bazı komutlarını basit örnekler yardımıyla açıklamaya çalışacağız.

```
C:\>DEBUG
```

- Çizgi işareti artık debug programının komut kabul etmeye hazır olduğunu belirtmektedir.

- R (Register) : Bu komut o andaki register değerlerini ve bayrakların durumunu belirlemekte kullanılır. Bu komut yardımı ile register'lara istenilen değerler (hexadecimal olmak şartıyla) verilebilir. Register’ları takip eden NV UP EI PL NZ NA PO NC değerleri ise bayrakların durumunu belirtmektedir.

```
-R F
```

### NV UP EI PL NZ AC PO CY -

komutu ile sadece bayrakların durumu da görülerek gerekenler değiştirilebilir. Eğer flag değeri değiştirilmeyecek ise ara çubuğuna basarak bir sonraki flag değerine geçilebilir.

Flag İsmi                        Set(1)                  Clear (0)

Overflow - OF               OV (overflow)          NV (not overflow) Direction - DF             DN (decrement -         UP (increment - up) down) Interrupt - IF               EI (enable)              DI (disable) Sign - SF                   NG (negative)              PL (plus) Zero - ZF                     ZR (zero)               NZ (not zero) Auxilary Carry- AF        AC (auxilary carry)       NA (not auxilary) Parity - PF                PE (even parity)          PO (odd parity) Carry - CF                  CY (carry yes)           NC (not carry) Debuger’da kullanılan Flag kısaltmaları - D (Dump / Display): Bu komut ile belleğin istediğimiz segment'inin istediğimiz offset'inden itibaren bilgileri görebiliriz. İstersek görmek istediğimiz alanı sınırlama imkanına da sahibiz.Eğer D komutunun yanına gösterilmesi istenen aralığın adresi verilecek olursa sadece belirlenen adres aralığındaki değerler ekranda görüntülenecektir.

- A ( Assembly) : Bu komut Debug yardımıyla basit programlar yazmayı sağlar. Debug içinde yazılan programlar COM uzantılı programlarda olduğu gibi 100H offset adresinden başlarlar. Bu neden ile program çalıştırılacağı zaman mutlaka IP register'ının değerinin R komutu ile 100H e getirilmesi gerekmektedir.

```
-A
2AF2:0100 MOV AX,5
2AF2:0103 ADD AX,4
2AF2:0106 SHR AX,1
2AF2:0108 ^C
```

- A komutu verildikten sonra CS'in 100H adresinden itibaren assembly program yazmanıza imkan sağlanmış olur. Burada verilen her türlü sayı mutlaka hexadecimal formda olmalıdır. Komut yazmanız bittiğinde Ctrl-C tuşlarına basarak işlemi sonlandırabilirsiniz.

- T (Trace) : Yazılmış olan assembly komutları teker teker çalıştırılarak işlem sonunda register ve bayrakların aldıkları değerleri ekranda gösterir. T komutu çalışmaya IP nin gösterdiği noktadan itibaren başlar ve her komut işlendikten sonra durur.

Eğer kullanıcı ister ise T komutunun yanına bir sayı da verebilir. Bu durumda verilen sayı kadar komut satırı arka arkaya çalıştırılır, her seferinde register ve flag değerleri ekrana yazılır.

- U (Unassembly) : CS’de yazılı olan makine kodunu kullanıcının anlayacağı formdaki mnemonic'lere çevirmek için kullanılan bir komuttur. Her çağırılışında 32 byte uzunluğunda makine kodunun mnemonic'lerini kullanıcıya gösterir.

- E (Edit) : Bellekte herhangi bir yerdeki değerleri değiştirmek amacıyla kullanılan bir komuttur.

- F (Fill) : Bellek başlangıç ve bitiş adresleri belirlenen bir alanı belirlenen bir sayı ile doldurmak amacıyla kullanılır.

- C (Compare) : Belirlenen aralıktaki bilgileri karşılaştırmak amacıyla kullanılan bir komuttur. Bu komut 100H-110H adresindeki bilgiler ile 10H adresinden başlayan bilgileri karşılaştırır ve farklı olanları listeler.

```
-G (Go): Programın verilen bir adrese kadar ya da bitene kadar çalışmasını sağlamak amacıyla
```

kullanılır.

- H (Hex ): Verilen iki sayının hexadecimal toplamını ve farkını hesaplamak için kullanılır.

- L (Load) : Belleğe programı tekrar yüklemek için kullanılır.

- M (Move) : Bir yerdeki bir blok bilgiyi başka bir yere taşımak için kullanılır

- P (Proceed) : Bu komut T komutu ile benzer özellikler göstermektedir. Komutları çalıştırdıktan sonra register ve flag değerlerini ekranda gösterir. Ancak T komutundan en büyük farklılığı özellikle

```asm
LOOP, CALL, INT gibi komutların işlenmesindedir. Bu komutlardan herhangi biri P komutu ile
```

çalıştırılacak olursa o işlemin detaylarına girmeden sonucu üretir.

- Q (Quit): Debuger dan çıkmak için kullanılan bir komuttur.

### -Q

```
C:\>
```

## ödev

8086 Yazmaçları ve DEBUG Komutları;

8086 YAZMAÇLARI: Merkezi işlem birimi yani cpu bilgisayarın beyni olarak tanımlanabilir. Nasıl insan vücudunda tüm vücut aktivitelerini beyin yönlendiriyorsa bilgisayarda da bu işi cpu yapar.Mikro işlemci milyonlarca transistör ve bunlardan oluşan mantık devrelerinden meydana gelen entegre devre yada çip şeklindedir. Cpu bilgisayarın işlem adımlarının tümünü yönetir. Ana kart üzerindeki tüm bileşenlerle bağlantısı vardır. İşlemci görevlerini yerine getirebilmesi için adres,bellek ve kontrol yolları ile donatılmıştır. Bilgisayarın genel performansı kullanılan işlemci ile doğru orantılı olarak değişir. Intel, 16 bitlik 8086 işlemcisini 1978 yılında piyasaya sürdü. Yüksek seviyeli programlama dillerine ve daha etkin işletim sistemlerine sahip ilk islemci olan 8086, IBM uyumlu sistemlerin temelini oluşturdu. Arkasından çıkan 8088 işlemci ile IBM ilk kişisel bilgisayarı (PC) piyasaya sürdü. Bu ilk PC’nin 16K hafızası, grafik özelliği olmayan ekranı ve bir teyp bandı sürücüsü vardı. Bu ilk işlemci diş veri yolu olarak 8 biti destekliyordu ve 4.77 MHz saat hızında çalışmaktaydı.

Pin Bağlantıları AD15-AD7 (8086) Adres/Data Bus Bu hatlar 8086 üzerindeki adres/data bus hattının multiplex edilmiş upperını (yüksek değerlikli 8-biti) içerir. Bu hatlar ALE ucu lojik 1 iken A15-A8 adres bitleri ve lojik 0 iken D15-D8 data bus bitleri ni içerir. Bu pinler mikroişlemci hold durumunda iken yüksek empedans gösterir.8086/8088 mikroişlemcileri için mimimum mod işlemcileri için MN/MX direkt +5V'a bağlanarak yapılır. Pin +5V'a bir pullup direnciyle bağlanamaz.

### 1. IO/M(8088), M/IO(8086) Bellek Giriş/Çıkış; Hem bellek hem de I/O adreslerinin

bulunduğu Mikroişlemci adres bus hattındaki bellek yada I/O'yu gösteren bir pindir. Mikroişlemci hold durumunda iken yüksek empedans gösterir.

### 2. WR-Write ;8086/8088 'nın bellek yada I/O birimleri için data çıkışını gösteren bir

strobdur. Bu pin Mikroişlemci hold durumunda iken yüksek empedans durumuna geçer.

### 3. INTA-Interrupt kabul edildi ;INTR giriş pininden sorumludur. INTA pini genelde

data üzerindeki interrupt isteklerinden sorumlu olan inrerrupt vektöre bir kapı olarak kullanılır.

### 4. ALE-Adres Latch Enable ;8086/8088 adres data bus hattının adres bilgileri

içerdiğini gösterir. Bu adres bellek yada I/O port numarası olabilir. Mikroişlemci hold durumunda iken bu pinin sinyal vermediğine dikkat edilmelidir.

### 5. DT/R Data Transmit(gönderme)/Receive(alma) ;Mikroişlemcinin veriyi aldığını

veya verdiğini gösterir. Bu sinyal harici data bus bufferlarını etkin hale getirmek için kullanılır.

### 6. DEN-Data Bus Enable ;Harici data bus bufferlarını etkin hale getirmek için

kullanılır.

### 7. HOLD-Hold ;Direkt belleğe erişme isteğidir. HOLD lojik 1 ise mikroişlemci yazılım

yürütme işlemini durdurur ve adres, data ve kontrol bus hatları yüksek empedans durumuna geçerler. Eğer HOLD lojik 0 seviyesinde ise mikroişlemci yazılımını normal olarak yürütür.

### 8. HLDA-Hold Acknowledge(Hold isteği kabul edildi) ;8086/8088'in HOLD

durumuna geçtiğini gösterir.

### 9. SS0 (8088) ; Mikroişlemci max modda çalışırken kullanılan S0'a eşdeğerdir. Bu sinyal

IO/M ve DT/R ile birleştirilerek o andaki bus çevriminin yaptığı işlevi decode etmek için kullanılır.

### DEBUG KOMUTLARI

Assembly komutlarının nasıl çalıştıklarını deneyerek görmek ve yazılan programların amacına uygun çalışıp çalışmadığını anlamak varsa hatalarını düzeltmek için DOS'un DEBUG.COM isimli programı kullanılmaktadır. Her ne kadar daha gelişmiş, kullanıcıya hitap eden debuger'lar olsa da kolay bulunulabilirliği ve basit uygulamalarda sağladığı rahatlık sayesinde tercih nedenidir. DEBUG programını kullanabilmek için komutlarını bilmek gereklidir.

```
C:\>DEBUG;
```

- Çizgi işareti artık debug programının komut kabul etmeye hazır olduğunu belirtmektedir. - R (Register) : Bu komut o andaki register değerlerini ve bayrakların durumunu belirlemekte kullanılır. Bu komut yardımı ile register'lara istenilen değerler (hexadecimal olmak şartıyla) verilebilir. Flag İsmi                    Set(1)                Clear (0) Overflow - OF           OV (overflow)         NV (not overflow) Direction - DF         DN (decrement -        UP (increment - up) down) Interrupt - IF            EI (enable)            DI (disable) Sign - SF               NG (negative)              PL (plus) Zero - ZF                  ZR (zero)             NZ (not zero) Auxilary Carry- AF AC (auxilary carry)         NA (not auxilary) Parity - PF            PE (even parity)         PO (odd parity) Carry - CF              CY (carry yes)          NC (not carry) Tablo 18-1 Debuger’da kullanılan Flag kısaltmaları - D (Dump / Display): Bu komut ile belleğin istediğimiz segment'inin istediğimiz offset'inden itibaren bilgileri görebiliriz. İstersek görmek istediğimiz alanı sınırlama imkanına da sahibiz. D komutunun yanına gösterilmesi istenen aralığın adresi verilecek olursa sadece belirlenen adres aralığındaki değerler ekranda görüntülenecektir. A ( Assembly) : Bu komut Debug yardımıyla basit programlar yazmayı sağlar. Debug içinde yazılan programlar COM uzantılı programlarda olduğu gibi 100H offset adresinden başlarlar. Bu neden ile program çalıştırılacağı zaman mutlaka IP register'ının değerinin R komutu ile 100H e getirilmesi gerekmektedir. - T (Trace) : Yazılmış olan assembly komutları teker teker çalıştırılarak işlem sonunda register ve bayrakların aldıkları değerleri ekranda gösterir. T komutu çalışmaya IP nin gösterdiği noktadan itibaren başlar ve her komut işlendikten sonra durur. Eğer kullanıcı ister ise T komutunun yanına bir sayı da verebilir. Bu durumda verilen sayı kadar komut satırı arka arkaya çalıştırılır, her seferinde register ve flag değerleri ekrana yazılır. - U (Unassembly) : CS’de yazılı olan makine kodunu kullanıcının anlayacağı formdaki mnemonic'lere çevirmek için kullanılan bir komuttur. Her çağırılışında 32 byte uzunluğunda makine kodunun mnemonic'lerini kullanıcıya gösterir.

- E (Edit) : Bellekte herhangi bir yerdeki değerleri değiştirmek amacıyla kullanılan bir komuttur. - F (Fill) : Bellek başlangıç ve bitiş adresleri belirlenen bir alanı belirlenen bir sayı ile doldurmak amacıyla kullanılır. C (Compare) : Belirlenen aralıktaki bilgileri karşılaştırmak amacıyla kullanılan bir komuttur.

```asm
farklı segment'ler üzerindeki bilgiler de karşılaştırılabilmektedir.
```

```
-G (Go): Programın verilen bir adrese kadar ya da bitene kadar çalışmasını sağlamak
```

amacıyla kullanılır.

```
-G
```

Program terminated normally

Program eğer düzgün çalıştı ise yukarıdaki mesaj ekrana gelecektir. Programın dönüş adreslerinde bir hata varsa ya da programda bir mantık hatası yapılmış ise program hiçbir zaman bitmez. Bu durumda makinenin reset edilmesi gerekecektir. - H (Hex ): Verilen iki sayının hexadecimal toplamını ve farkını hesaplamak için kullanılır. - L (Load) : Belleğe programı tekrar yüklemek için kullanılır. - M (Move) : Bir yerdeki bir blok bilgiyi başka bir yere taşımak için kullanılır

### - M DS:100,110,CS:500

Bu komut ile DS:100H ile DS:110H arasında kalan bilgi CS:500H adresinden itibaren yerleştirilecektir. - P (Proceed) : Bu komut T komutu ile benzer özellikler göstermektedir. Komutları çalıştırdıktan sonra register ve flag değerlerini ekranda gösterir. Ancak T komutundan en büyük farklılığı özellikle LOOP, CALL, INT gibi komutların işlenmesindedir. Bu komutlardan herhangi biri P komutu ile çalıştırılacak olursa o işlemin detaylarına girmeden sonucu üretir. (Eğer bir LOOP ise çevrim sonuçlanana kadar, bir CALL ise işlemler yerine getirilip geri dönülene kadar ya da bir INT ise interrupt handler'in yapması gereken tüm işlemler yapıldıktan sonra register ve Bayrakların durumlarını gösterir). - Q (Quit): Debuger dan çıkmak için kullanılan bir komuttur.

### -Q

```
C:\>
```

### KAYNAKLAR

- Assembly kodları ,Mühendislik Mimarlık Fakültesi Bilgisayar Mühendisliği Bölümü

- Mikroişlemciler ,yıldız üniversitesi yayınları

- www.gencbilim.com

## ek-2

### DEBUG KOMUTLARI (EK 2)

Komut                     A Anlamı                    Assembly Kullanım formatı          A [Adres] Yaptığı iş                Assembly dilinde program yazımına giriş. Örnek                     A100 (0100 offset adresinden itibaren program yazımı için) Açıklama                  Assembly dilinde program yazımından çıkış için ENTER’ a basılır. Komut                     C Anlamı                    Compare (karşılaştır) 1- C [1.adres başlangıçı] [1.adres bitimi] [ikinci adres başlangıcı] Kullanım formatı 2- C [1.adresLsayı] [ikinci adres] Hafızanın iki farklı bölgesini karşılaştırır, şayet bu bölgeler aynıysa hiçbir mesaj Yaptığı iş                görünmez, karşılaştırılan bölgeler içinde farklı baytlar varsa bu bölgeler ekranda görülür. C 0010 0015 0020 (0010-0015 ile 0020-0025 adres konumları karşılaştırılır) Örnek                     C 0010L5 0020 (0010 adresinden itibaren 5 konum 0020 adresinden itibaren 5 konumla karşılaştırılır) Açıklama                  Büyük adres sınırları verilirse istenilen bölgelerin hepsi ekranda görülmeyebilir. Komut                     D Anlamı                    Dump (ekrana hafıza dökümü al) Kullanım formatı          D [bellek alanı] Yaptığı iş                Hafızanın istenilen bir bölümünü ekranda gösterir. D200 (0200 offset adresinden itibaren 128 adet bir baytlık hafıza bölgesini ekranda gösterir) Örnek                     D 0010,0050 (0010 ile 0050 offset adresleri arasındaki hafıza bölgesini ekranda gösterir) D100L20 (0100 den itibaren ilk 20h bayt gösterilir) Sadece D yazılıp ENTER’ a basılırsa offset 0100 dan itibaren ekranda döküm Açıklama gösterir. Komutun D cs:0250 gibi bir formatta’da kullanımı mümkündür. Komut                     E Anlamı                    Enter (hafızaya bilgi girişi) Kullanım formatı          E [ADRES] liste Yaptığı iş                Hafızaya istediğimiz bilgi veya bilgileri hızlıca girmek için kullanılır. 1- E 0230 ‘abcdef12345’ (0230 adresinden itibaren abcdef12345 bilgilerini girer, her karakter 1 baytlık yer kaplar) Örnek 2- E 0230 şeklinde kullanılırsa 0230 un içeriğini gösterir, bu bölge istenirse değiştirilebilir veya ENTER’a basılarak değişiklik yapılmadan geçilebilir. Açıklama                  Girilen karakterleri görmek için “D” komutu kullanılabilir. Komut                     F Anlamı                    Fill (doldur)

www.mikroislemciler.com Öğr.Gör. Eren ERENER

Kullanım formatı          F [başlangıç adresi] [bitiş adresi] doldurulacak karakter İstenilen hafıza bölgesini herhangi bir hexadecimal değer ile doldurmak için Yaptığı iş kullanılır. 1- F 0100 0120 AA (0100 adresinden 0120 adresine kadar olan bölgeyi AAh değeri ile doldurur) 2- F 100L100 22 (0100 adresinden itibaren 100h adet konumu 22h bilgisiyle Örnek doldurur) 3- F 100L34 12 AB F1 C4 (0100 adresinden itibaren 34 adet konumu 12 AB F1 C4 bilgi dizisiyle doldurur) Açıklama                  Doldurulan bölgeleri D komutu ile görebilirsiniz. Komut                     G Anlamı                    GO (git, çalıştır) Kullanım formatı          G [ADRES] Yazılan Assembly programını çalıştırmak (mikroişlemciye icra ettirmek) için Yaptığı iş kullanılır. 1- G (CS:IP ‘den itibaren programı çalıştırır, ta ki bir kesintiye uğrayana kadar) Örnek                     G 0200 (mikroişlemci cs:ip ‘den itibaren 0200 offset adresine kadar hafızada yer alan bilgileri icra etmeye (işlemeye) başlar kesintiye uğrayana kadar) Yazılan programın hangi bellek sınırları arasında olduğu programcı tarafından iyi Açıklama                  bilinmeli ve cs:ip program çalıştırılmadan önce kurulmalıdır. Programınız hatalı ise ve Korumalı modda (protected mode) değilseniz sisteminiz kilitlenebilir. Komut                     H Anlamı                    Hexadecimal topla ve çıkar Kullanım formatı          H değer1 değer2 Yaptığı iş                İki hexadecimal (onaltılık) iki sayının toplamını ve farkını ekranda gösterir. Örnek                     H 9 3 (toplam sonucu 000C fark 0006 dır) Açıklama                  Sınır doubleword’ dür. Komut                     I (input) Anlamı                    Porttan değer okuma Kullanım formatı          i port adresi Yaptığı iş                Herhangi bir porttaki 1 baytlık veriyi okur Örnek                     i 2F8 (seri porttan bilgi okur) Açıklama                  Yok Komut                     L Anlamı                    Load (diskten hafızaya yükleme yap) 1- Parametreli kullanım için; L [Yükleme yapılacak ofset adresi] [sürücü no] [başlangıç sektörü] [başlangıç sektöründen itibaren kaç sektör okunacağı] Kullanım formatı          2- Parametresiz kullanım için; - n dosya adı ; önce bu şekilde yüklenecek dosyanın adı yazılır, daha sonra L yazılıp enter’e basılır. Böylece program CS:0100 den itibaren hafızaya yüklenir. Programın uzunluğu BX:CX’e getirilir. Yaptığı iş                Hafızaya program yada sektör(ler) yükleme

### 1) L 0100 0 1 2 (CS:0100 adresine A sürücüsündeki 1. sektör ile 2. sektörü

yükler)

### 2) Debug açıkken;

Örnek                         – n mer.com (mer.com adında bir dosya)

### –L

(mer.com dosyasını CS:0100 den itibaren hafızaya yükler, programın kapladığı alan BX:CX de görülebilir) Parametreli kullanım için sürücü no

### 0 = A, 1 = B, 2 = C, 3 = D ……

Açıklama Windows XP’de parametreli kullanım sınırlıdır. Sadece MS-DOS uyumlu dosyalar için kullanılabilir. Komut                     M (move – taşı) Anlamı                    Hafıza bölgesini taşı. Kullanım formatı          M [başlangıç adresi][bitiş adresi][kopyalanacak bölümün başlangıç adresi] Yaptığı iş                Herhangi bir hafıza bloğunu başka bir yere taşır. Örnek                     M 0100 010F 0200 Açıklama                  Yok

www.mikroislemciler.com Öğr.Gör. Eren ERENER

Komut                     N (name-isim) Anlamı                    Program dosyası için isim seç Kullanım formatı          N dosya ismi İki görevi vardır, birincisi L ve W komutları için isim seçmek, ikincisi debug Yaptığı iş tarafından bellekte icrası test edilen programa dosya parametreleri atamak Örnek                     N dosya1.com Açıklama                  Yok Komut                     O (output) Anlamı                    Port’a değer gönder Kullanım formatı          O port adresi Yaptığı iş                Çıkış portuna bir baytlık bilgi gönderir Örnek                     O 2F8 Açıklama                  Yok Komut                     P (proceed-ilerle) Anlamı                    Bir altyordam veya döngüyü işle Kullanım formatı          P veya P = [ofset adresi] Programda bulunan altyordam, döngü ve interrupt’ları satır-satır işlemek yerine, Yaptığı iş bir defada işler. Örnek                     P (Program hafızaya yüklü iken) Herhangibir programı hafızaya yükledikten sonra, önce T komutu ile sonrada Açıklama aynı programı P komutu ile icra ettirin. Komut                     Q (quit-çık) Anlamı                    Debug’tan çıkarak işletim sistemine dön. Kullanım formatı          Q Yaptığı iş                Komut istemine geri dönüş Örnek                     Q Açıklama                  Debug’tan çıkmak için bu komutu verin Komut                     R (register-kaydedici) Anlamı                    Kaydedicilerin içeriğini görme veya değiştirme Kullanım formatı          R veya R [kaydedici adı] Yaptığı iş                Kaydedicilerin içini görme veya görüp değiştirme rax ; AX kaydedicisinin 16 bitlik değeri akranda görülür ve : olan kısımda imleç yanıp söner, şayet enter’a basılırsa içerik değişmez, içeriği değiştirmek için enter’dan önce bir değer girilmelidir (değer iki bayt’ı aşmamalı). Örnek r ; tek başına kullanıldığında tüm kaydedicilerin 16 bitlik değerlerini gösterir

rf ; bayrak kaydedicilerin içini değiştirmek için kullanılır

### Bayrak kaydedici durumları

Bayrak (flag) Bayrak (flag)                 1’durumu                 0’durumu Overflow                       OV                       NV Direction                      DN                       UP Açıklama                             Interrupt                       EI                      DI Sign                         NG                       PL Zero                         ZR                       NZ Aux. Carry                      AC                       NA Parity                       PE                       PO Carry                        CY                       NC Komut                     S (search-ara) Anlamı                    Hafıza bölgesinde arama yapma Kullanım formatı          S alan liste Yaptığı iş                Belirtilen bayt dizisini hafızada arar, bulduğunda sonuç olarak adres verir. Örnek                     S CS:100 110 65 ; 0100 ile 0110 offsetleri arasında 65 bilgisini arar. Açıklama                  Yok Komut                     T (trace-adım adım izle) Anlamı                    CPU’ya Program komut satırlarını adım-adım icra ettirme Kullanım formatı           T [adres][değer] Yaptığı iş                Programı adım-adım çalıştırır

www.mikroislemciler.com Öğr.Gör. Eren ERENER

T ; tek başına kullanıldığında CS:0100 den itibaren 1 komut satırı işler, Örnek                     T3 ; cs:0100 den itibaren 3 komut satırı işler, T=0101 8 ; CS:0101 adresinden itibaren 8 komut satırı işler. Açıklama                  Yok Komut                     U (Unassemble) Anlamı                    Assembly dilindeki komutların makine kodunda görülmesi Kullanım formatı          U [adres] veya U [adres] L [değer] Yaptığı iş                Assembly kodlarını makine dili formatında ekranda gösterir U100 ; CS:0100 adresinden itibaren 20h baytı gösterir Örnek U100L10; CS:0100 adresinden itibaren 10h baytı gösterir Açıklama                  Değer büyük girilirse istenilen tüm satırlar ekranda bir anda görülemeyebilir. Komut                     W (write-diske yaz) Anlamı                    Hafızadaki programı diske yaz

### 1-W

Kullanım formatı 2-W [adres][sürücü no][sektör][bayt sayısı] Yaptığı iş                Hafızadaki bilgileri disk veya diskete yazar Örnek                     W W komutu tek başına kullanılıyorsa, w komutu yazılmadan önce BX:CX’e Açıklama yazılacak bayt sayısı ve n komutu ile dosya ismi belirlenmelidir.

www.mikroislemciler.com Öğr.Gör. Eren ERENER

## Debug Intro

EEM 332 - Microprocessors Introduction to DEBUG

Notes are taken from; *DEBUG/ASSEMBLY TUTORIAL by Fran Golden http://www.datainstitute.com/debug1.htm **A Guide to DEBUG by Daniel B. Sedory http://www.geocities.com/thestarman3/asm/debug/debug.htm

COM Extensions

### 1. COM programs are very small and compact programs that cannot be larger than 65K bytes

```asm
in size.
```

### 2. The PSP of a COM program is located in the first 100 Hex (256 Dec) locations of the

program.

### 3. The first instruction of the COM program must start at offset 100 in memory.

### 4. DOS creates the PSP for the COM program, which means we don't have to be concerned

with this when we assemble a program.

### 5. All the data, code, and the stack area are in the same segment of memory. (1 segment is

### 65K)

EXE Extensions

### 1. The EXE programs can be any size from (200 bytes-640k bytes)

### 2. The PSP must be setup by the programmer, when the program is assembled.

### 3. The programmer determines where the first instruction is in the program.

### 4. The EXE program uses separate segments for the data, code and stack area in memory.

From the above comparison you can see it is much more difficult to assemble an EXE program than it is a COM program. The debug utility program was designed to work only with a COM program by setting up the PSP area each time we enter debug. Once in debug, we can start assembly of a program at offset 100 and not be concerned with PSP or where the data, code, and stack is located. It is possible to look at an EXE program with debug if we rename the program with a different extension before we load it into memory.

Assembly language ---------------------- Programming in the early days of computing had to be written using the machine code of the microprocessor and as a result required specialized people who had this ability. The use of computers was restricted to the companies and corporations with the finances to support such a specialized operation. It didn't take long for the programmers to write the code to do most of the hard work in binary. One of the most important programs written was the Assembler, which was a conversion type program that allowed the use of English words to represent the instruction set of the CPU, that was compiled into machine code after they were written. One such program is Debug.com that is supplied by the MicroSoft corp. in most versions of DOS.

Debug, which is a small but powerful assembler, converts English sounding words called mnemonics into the machine code. All instructions for the 8088 have a mnemonic word to

```asm
represent them in debug. For example, in the program above, the code can be written in an
```

assembler language that is much easier to write and understand.

The mnemonic form of that program is shown below.

mnemonic form----------machine code

```asm
MOV AX,0005------------B80500
ADD BX,AX---------------01C3
MOV [120],AX------------891E2001
```

Details of Each Command

Assemble: A [address] Creates machine executable code in memory beginning at CS:0100 (or the specified address) from the 8086/8088 (and 8087) Assembly Language instructions which are entered. Although no Macro instructions nor labels are recognized, you can use the pseudo-instructions 'DB' and 'DW' (so you can use the DB opcode to enter ASCII data like this: DB 'This is a string',0D,0A                                                                               ). The 'A' command remembers the last location where any data was assembled, so successive 'A' commands (when no address is specified) will always begin at the next address in the chain of assembled instructions. This aspect of the command is similar to the Dump command which remembers the location of its last dump (if no new address is specified).

The    assembly     process    will   stop    after   you     ENTER      an    empty     line.

### Example (you enter the characters in bold type)

```
-a
```

xxxx:0100 jmp 126 xxxx:0102 db 0d,0a,'This is my first DEBUG program!' xxxx:0123 db 0d,0a,'$' xxxx:0126 xor ax,ax xxxx:0128 mov ah,9 xxxx:012A mov dx,102 xxxx:012D int 21 xxxx:012F mov ax,4c xxxx:0132 int 21 xxxx:0134

```
-g =100
```

This is my first DEBUG program!

Program terminated normally -

NOTE: You can pipe simple 8086/8088 Assembly Language scripts into DEBUG (which can even include a semi-colon ';' followed by comments on any of its lines!).

- DEBUG uses the convention of enclosing operands which refer to Memory locations

```asm
in square brackets '[ ]' (as opposed to an immediate value as an operand).
```

- DEBUG may require you to explicitly tell it whether or not an operand refers to a

word or byte in Memory! In such cases, the data type must be stated using the prefixes 'WORD PTR' or 'BYTE PTR'

- For all 8087 opcodes, the WAIT or FWAIT prefix must be explicitly specified.

Compare: C range address

Compares two blocks of memory. If there are no differences, then DEBUG simply displays

### another prompt (-). Here's an example of what happens when there are differences

-c 140 148 340

```
127D:0143 30 6D       127D:0343
127D:0146 10 63       127D:0346
127D:0148 49 30       127D:0348
```

The bytes at locations 140 through 148 are being compared to those at 340 (through 348, implied); the bytes are displayed side by side for those which are different (with their exact locations on either side of them).

Dump: D [range] D [address] [length] Displays the contents of a block of memory.

### Example

```
-d 100 133
```

xxxx:0100 EB 24 0D 0A 54 68 69 73-20 69 73 20 6D 79 20 66                .$..This is my f xxxx:0110 69 72 73 74 20 44 45 42-55 47 20 70 72 6F 67 72                irst DEBUG progr xxxx:0120 61 6D 21 0D 0A 24 31 C0-B4 09 BA 02 01 CD 21 B8                am!..$1.......!. xxxx:0130 4C 00 CD 21                                                    L..! - This next example uses the option [length]; the 'l24' means a length of 24 hexadecimal

### bytes (that's 36 in decimal)

```
-d 102 l24
```

xxxx:0100       0D 0A 54 68 69 73-20 69 73 20 6D 79 20 66                  ..This is my f xxxx:0110 69 72 73 74 20 44 45 42-55 47 20 70 72 6F 67 72                irst DEBUG progr xxxx:0120 61 6D 21 0D 0A 24                                              am!..$ -

Enter: E address [list] Used to enter data or instructions (as machine code) directly into Memory locations. Example: First we'll change a single byte at location CS:FFCB from whatever it was before to D2

```
-e ffcb d2
```

The next two examples show that either single(') or double(") quote marks are acceptable for entering ASCII data. By allowing both forms, you can include the other type of quote mark

### within your entry string

```
-e 200 'An "ASCII-Z string" is always followed by '
-e 22a "a zero-byte ('00h')." 00
```

Now let's examine a string of 14 hex bytes entered into Memory at location CS:0100 and

### following

```
-e 100 31 C0 B4 09 BA 0E 01 CD 21 B8 4C 00 CD 21
```

This is actually machine code for a program that will display whatever it finds at location CS:010E       until   it   encounters     a    byte      of    24h     (a     '$'    sign).

Here's something a bit more interesting for you to try out: It's essentially the same program, but the data includes all of the bytes from 00h through FFh; except for 24h which was placed at the end of the last line. The DEBUG prompt '-' is purposely left out here so you can copy

```asm
and paste the whole block all at once into DEBUG using a DOS-Window (You'll find Help on
```

### using DOS-Window controls here)

e 100 31 C0 B4 09 BA 0E 01 CD 21 B8 4C 00 CD 21 0D 0A 0D 0A e 112 00 01 02 03 04 05 06 07 08 09 20 0B 0C 20 0E 0F 10 11 e 124 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F 20 21 22 23 e 136 20 25 26 27 28 29 2A 2B 2C 2D 2E 2F 30 31 32 33 34 35 e 148 36 37 38 39 3A 3B 3C 3D 3E 3F 0D 0A 0D 0A 40 41 42 43 e 15a 44 45 46 47 48 49 4A 4B 4C 4D 4E 4F 50 51 52 53 54 55 e 16c 56 57 58 59 5A 5B 5C 5D 5E 5F 60 61 62 63 64 65 66 67 e 17e 68 69 6A 6B 6C 6D 6E 6F 70 71 72 73 74 75 76 77 78 79 e 190 7A 7B 7C 7D 7E 7F 0D 0A 0D 0A 80 81 82 83 84 85 86 87 e 1a2 88 89 8A 8B 8C 8D 8E 8F 90 91 92 93 94 95 96 97 98 99 e 1b4 9A 9B 9C 9D 9E 9F a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 aA aB e 1c6 aC aD aE aF b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 bA bB bC bD e 1d8 bE bF 0D 0A 0D 0A c0 c1 c2 c3 c4 c5 c6 c7 c8 c9 cA cB e 1ea cC cD cE cF d0 d1 d2 d3 d4 d5 d6 d7 d8 d9 dA dB dC dD e 1fc dE dF e0 e1 e2 e3 e4 e5 e6 e7 e8 e9 eA eB eC eD eE eF e 20e f0 f1 f2 f3 f4 f5 f6 f7 f8 f9 fA fB fC fD fE fF 0D 0A e 220 0D 0A 24 The bytes 0Dh and 0Ah produce a Carriage Return and Linefeed on the display, so they were

```asm
replaced by a 20h (a space) in the listing above. The 24h byte was, of course, moved to the
end of the listing and its original location also turned into a space. A blank line was placed at
```

the beginning and after every 64 bytes in the listing using the sequence '0D 0A 0D 0A.' So, we should see four separate lines of 64 characters each (a few of those being blank spaces in the first line of course) when the program is run, right? Start DEBUG in a DOS-Window, copy and paste the lines above into DEBUG at the '-' prompt, then enter the following

### command

g =100 ( 'g' followed by a SPACE, then '=100') This will run* the program in DEBUG... displaying the lines we mentioned and another stating: "Program terminated normally." [ If possible, do NOT close the DOS-Window or exit DEBUG as we'll be making a 'patch' to the code later.] If you were surprised to find more than four spaces on the first line, or that there appear to be some missing characters at the end of that line, then you might want to study about the Control Characters at the beginning of an ASCII chart. You'll also need to learn about Interrupts and what effect different BIOS and DOS Video Functions have on how the ASCII Characters are displayed. ( *Refer to: The 'G' Gocommand.)

OK, I'll save you the time and tell you what happened: First, the Zero byte displays as a blank space here. The 07h byte sounds a BEEP (but does not display anything), 08h performs a BACKSPACE (erasing the 06h byte character) and 09h is a TAB -- which may jump up to eight columns to the right before reaching the next 'Tab Stop.' But since it just happens to begin in column seven, it only moves one column to the right where our program places the blank space we substituted for 0Ah. Lastly, for some reason, when using Function 09 of INT 21 ("Display a string of characters until a '$' sign is encountered"), the ESC character (1Bh; 27 decimal) doesn't display or do anything either. So, upon reaching the end of the first line, it appears      as     if    five      of    the      characters    were      never     displayed.

If you enter the following two lines into DEBUG ( with more blank-space substitutions inserted ) and run the program again, you'll see all of the displayable characters output on the

### first line in their correct positions

e 112 00 01 02 03 04 05 06 20 20 20 20 0B 0C 20 e 120 0E 0F 10 11 12 13 14 15 16 17 18 19 1A 20 All four rows should come out even now, including the last one, because the FFh (255

```asm
decimal) displays as a blank space! You can prove this by inserting another byte such as 2Eh
```

(a period '.') right after the FFh byte. Since DEBUG has no 'Insert' command, here's another

### 'patch' for you which effectively moves the remaining program bytes up one location

e            21e             2e          0d        0a            0d          0a           24

### Here's how the program output should now look when run again

You can save this program to your hard drive, by first giving it a path and filename (such as,

```
C:\TEMP\ASCIIDSP.COM; see 'N' Name command) and writing the bytes (see 'W' Write
```

### command) to a file like this

-n c:\temp\asciidsp.com -rcx

### CX0000

:124       [ Program Length = 223h - 100h + 1 = 124h ] -w

Fill: F range list This command can also be used to clear large areas of Memory as well as filling smaller

### areas with a continuously repeating phrase or single byte. Examples

```
-f 100 12f 'BUFFER'
-d 100 12f
```

xxxx:0100 42 55 46 46 45 52 42 55-46 46 45 52 42 55 46 46 BUFFERBUFFERBUFF xxxx:0110 45 52 42 55 46 46 45 52-42 55 46 46 45 52 42 55 ERBUFFERBUFFERBU xxxx:0120 46 46 45 52 42 55 46 46-45 52 42 55 46 46 45 52 FFERBUFFERBUFFER

```
-f 0 ffff 0
```

This last example fills all of the assigned Segment with bytes of zeros ( which could also be thought of as clearing the whole Segment ). I use this command whenever I want to be sure that the bytes I'm looking at are those I'm concerned about and not just random bits of code lost in memory!

If you want to examine a file from disk in a 'clean' Segment, then you would first have to start DEBUG without the filename on the command line, clear the Segment using -f 0 ffff 0, and then finally load the file with the Name (n) and Load (L) commands.

Go: G [=address] [addresses] Go is used to run a program and set breakpoints in the program's code.

As we saw in an Example for the ENTER command, the '=address' option is used to tell DEBUG a starting location. If you use 'g' all by itself, execution will begin at whatever location is pointed to by the CS:IP registers. Optional breakpoints ( meaning the program will HALT before executing the code at any of these locations) of up to any ten addresses may be      set      by      simply      listing     them      on      the     command       line.

Requirements: Breakpoints can only be set at an address containing the first byte of a valid 8088/8086 Opcode. So don't be surprised if picking some arbitrary address never halts the program; especially if you're trying to DEBUG a program containing opcodes DEBUG can't understand    (that's    anything     'requiring' a   CPU     above     an     8088/8086)!

CAUTION: DEBUG replaces the original instructions of any listed breakpoint addresses with CCh (an INT 3). The instructions at these locations are restored to their originals ONLY if one of the breakpoints is encountered... If DEBUG does not HALT on any breakpoint, then all your breakpoints are still enabled! So, don't ever save the code as is, unless you're sure that DEBUG has hit one of your breakpoints! ( Saving to a backup copy before using breakpoints is often a better way. )

Hex: H value1 value2 A very simple (add and subtract only) hex calculator. Enter two Hex values (only up to four hex digits each), and DEBUG shows first the SUM and then the DIFFERENCE (no carries

### past the fourth digit). Examples

-h 123 100                    -h 100 123                    -h ffff 1

### 0223 0023                     0223 FFDD                     0000 FFFE

-                             -                             - Input: I port

The use of I/O commands while running Windows may be unreliable! This is especially true when trying to directly access hard disks through I/O commands! Long ago (when DOS was the only OS for PCs), there were dozens of BASIC programs that used I/O commands for all sorts of tasks through the parallel and serial ports (e.g., to change fonts on a printer or values in a modem's control registers). They can also be used for direct communications with your          keyboard         or         floppy          drive's         control        chips. Here's an example of how to read the hours and minutes from your computer's "real time

```asm
clock":
```

-o 70 04 <-- Check the hours. -i 71 18 <----- 18 hours (or 6 p.m.)

-o 70 02 <-- Check the minutes. -i 71 52 <----- 52 minutes The first space wasn't necessary under my version of DEBUG; so you might be able to get away with "o70" and "i71" instead. Here's a page of more complex examples dealing with hard drives and the ATA commands for reading info from the disk controllers!

### Load

L [address] [drive] [firstsector] [number] This command will LOAD the selected number of sectors from any disk's Logical Drive under the control of MS-DOS/Windows into Memory. The address is a location in Memory (use only 4 hex digits to keep it within the memory allocated to DEBUG) the data will be copied to, the drive number is mapped as: 0=A:, 1=B:, 2=C:, etc., firstsector counts from ZERO to the largest sector in the disk volume and number specifies in hexadecimal the total number        of     sectors       that     will    be      copied      into     Memory.

The terminology 'Disk Volume' or 'Logical Drive' means that you can not use L[oad] to load or examine the MBR, for example, or any other sectors outside of the Logical Drive Letters           or           Volumes            assigned            by          DOS/Windows. For example, if you enter the command: L 100 2 0 1 in DEBUG, instead of seeing the very first sector on a hard disk (the MBR), you'll see the first sector of the Boot Record for the Logical drive C: of the first hard disk partition that can accessed by a compatible MS-DOS or Windows                                                                                       OS.

Load can be useful in examining a Floppy Disk, but, unfortunately, only if the disk can be read by MS-DOS/Windows. Unlike hard disks, the very first sector on a floppy disk is an OS Boot sector. Here's what you might see from a Logical disk sector and some dumps from a couple                                    floppy                                      disks.

### Examples

-l 100 2 0 1  [ the C: drive. ]

```
-d 100 10f
```

xxxx:0100 EB 58 90 4D 53 57 49 4E-34 2E 31 00 02 08 20 00 .X.MSWIN4.1... .

```
-d 280 2ff
```

xxxx:0280 01 27 0D 0A 49 6E 76 61-6C 69 64 20 73 79 73 74 .'..Invalid syst xxxx:0290 65 6D 20 64 69 73 6B FF-0D 0A 44 69 73 6B 20 49 em disk...Disk I xxxx:02A0 2F 4F 20 65 72 72 6F 72-FF 0D 0A 52 65 70 6C 61 /O error...Repla xxxx:02B0 63 65 20 74 68 65 20 64-69 73 6B 2C 20 61 6E 64 ce the disk, and xxxx:02C0 20 74 68 65 6E 20 70 72-65 73 73 20 61 6E 79 20 then press any xxxx:02D0 6B 65 79 0D 0A 00 00 00-49 4F 20 20 20 20 20 20 key.....IO xxxx:02E0 53 59 53 4D 53 44 4F 53-20 20 20 53 59 53 7E 01 SYSMSDOS    SYS~. xxxx:02F0 00 57 49 4E 42 4F 4F 54-20 53 59 53 00 00 55 AA .WINBOOT SYS..U. - -l 100 0 0 1  [ a floppy in the >A: drive. ]

```
-d 100 13d
```

xxxx:0100 EB 3C 90 29 47 38 71 33-49 48 43 00 02 01 01 00 .<.)G8q3IHC..... xxxx:0110 02 E0 00 40 0B F0 09 00-12 00 02 00 00 00 00 00 ...@............ xxxx:0120 00 00 00 00 00 00 29 40-16 D8 13 4E 4F 20 4E 41 ......)@...NO NA xxxx:0130 4D 45 20 20 20 20 46 41-54 31 32 20 20 20       ME    FAT12 - -l 100 0 0 1  [ a different floppy in the A: drive. ]

```
-d 100 13d
```

xxxx:0100 EB 3C 90 53 59 53 4C 49-4E 55 58 00 02 01 01 00 .<.SYSLINUX..... xxxx:0110 02 E0 00 40 0B F0 09 00-12 00 02 00 00 00 00 00 ...@............ xxxx:0120 00 00 00 00 00 00 29 7E-CF 55 3C 20 20 20 20 20 ......)~.U<

xxxx:0130 20 20 20 20 20 20 46 41-54 31 32 20 20 20             FAT12 -

```
-d 2d0 2ff
```

xxxx:02D0 42 3B 16 1A 7C 72 03 40-31 D2 29 F1 EB A7 42 6F B;..|r.@1.)...Bo xxxx:02E0 6F 74 20 66 61 69 6C 65-64 0D 0A 00 00 00 00 4C ot failed......L xxxx:02F0 44 4C 49 4E 55 58 20 53-59 53 F4 3C 82 3A 55 AA DLINUX SYS.<.:U. Note that the Linux Boot disk above is the kind formatted as an MS-DOS diskette and not as a true Linux floppy. If it had been a floppy formatted for some other OS or with a faulty boot sector, then MS-DEBUG would not be able to read it. Instead you'd see that old "General failure reading drive A / Abort, Retry, Fail?" error message, and then DEBUG's "Disk error reading drive A" message after having cleared the first error message. This makes DEBUG almost worthless as far as trying to fix an error in a floppy disk's boot sector! However, if you keep a binary copy of a good floppy disk Boot Sector somewhere, you could use DEBUG to overwrite whatever's on a faulty floppy disk's first sector (see Write command). But if you really want to see what's in such a Boot sector (that keeps DEBUG from recognizing it as valid), you'll need to use a disk editor that will allow you to do so; such as Symantec's Norton DiskEdit          (ONLY            in         Physical         Disk         Mode        though).

```asm
NOTE: Just because a floppy disk can't be read by DOS or opened in DEBUG does NOT
```

necessarily mean it's defective. It might simply have been formatted with a different OS (such as Linux) and could easily boot-up on its own; a very good reason for labeling your disks! (CAUTION: Never try booting your system with a disk you're not 100% sure of; unless you disconnect all hard disks and don't have any flash BIOS, because it might contain a nasty boot virus!                                                                                            ) [ Many floppy disks have the letters IHC in their OEM ID field. What kind of OEM Name is that? None. Someone at Microsoft decided that this was where they'd place a new pseudo-random type of identification to make sure that any information cached by 'Windows 9x' from one disk wouldn't be mixed up with info from a different one if you swapped disks. The whole string begins with five pseudo-random hex bytes, and always ends with the characters IHC. All floppy diskettes that are not write-protected will have any original OEM ID overwritten. Once Windows has written this string, it will remain the same for any future disk reads or writes. However, performing even a quick format under Windows, will change the               five               hex               bytes              every             time. Some have concluded that the characters 'IHC' are the first three letters of the word "Chicago" in reverse order, since Chicago was the 'code name' for Windows 95™ before it was ever released (it would have appeared as ' OGACIHC' on the hypothetical disk). Although certainly a possibility, I have no proof of that. Due to my interest in some very old Greek Manuscripts, I still can't help seeing the 3 characters 'IHC' as an Iota, Eta and old style Sigma since this combination of letters was often used as an abbreviation for the Greek word IHSUS.         Just     another        one      of       those      coincidences     of       life. REMEMBER: If you really want to preserve all of the contents of an important diskette, you can't even perform a simple Directory read under a Windows OS, UNLESS it is 'write- protected' and you know the drive's write-protect system is functioning correctly! ]

```asm
Move: M range address
```

This command should really be called: COPY (not Move) as it actually copies all the bytes from      within     the       specified    range      to       a       new        address.

### Examples

### 1) -m 7c00 7cff 600

Copies all the bytes between Offset 7C00 and 7CFF (inclusive) to Offset 0600 and following...

### 2) -m 100 2ff 70

This second example shows that it's very easy to overwrite most of the source you're copying from using the Move command. Apparently, DEBUG stores the source bytes elsewhere before writing them; otherwise, this example would cause a problem when it started overwriting what it hadn't copied yet! This copies the 512 bytes between Offsets 100h and 2FFh (inclusive) to Offset 0070 overwriting the first 368 bytes in the process.

Name: N [pathname] [arglist] This command can be used to load files into DEBUG's Memory after you have started the program, but it's main function is to create a new file under control of the Operating System which DEBUG can WRITE data to.

### Normally, when you want to 'debug' a file, you'd start DEBUG with a command like this

```
C:\WINDOWS>debug test.com . But it's also possible to load a file into DEBUG's Memory
```

from within DEBUG itself by using the 'N' command and then the 'L' command (with no

### parameters at all ) like this

-n c:\temp\test.com -l which will load the file test.com into DEBUG's Memory starting at location CS:0100 (you cannot specify any other location). The 'N' command makes it quite easy to save data or an Assembly program you created in DEBUG to a file on your hard drive!

### For example, these commands (in BOLD; with the DEBUG reponses)

-n c:\temp\dosok.com

```
-a 100
```

cs:0100 jmp 12C cs:0102 db "It's OK to run this program under DOS!" cs:0128 db 0d,0a,24 cs:012B nop cs:012C mov dx,102 cs:012F mov ah,9 cs:0131 int 21 cs:0133 mov ax,4c01 cs:0136 int 21 cs:0138 -rcx

### CX 0000

:38 -w Writing 00038 bytes   [ 56 bytes in decimal ] -q will create a 56-byte file called DOSOK.COM in the C:\TEMP folder. Even when running DEBUG in a DOS-window, though, the file names are still limited to DOS's 8 characters plus 3 for the extension! Output: O port byte

See the comments under the Input command.

Proceed: P [=address] [number]

Proceed acts exactly the same as Debug's T (Trace) command for most types of instructions... EXCEPT: Proceed will immediately execute ALL the instructions (rather than stepping through each one) inside any Subroutine CALL, a LOOP, a REPeated string instruction or any software INTerrupts. This means that you do not have to single-step through any of the code contained in a Subroutine or INT call if you use the Proceed (P) command. This means Proceed will be the command you use most often to debug programs, and Trace will only be used to step into a Subroutine or possibly check the logic of the first few iterations of a LOOP or REP instruction.

Quit: Q Immediately quits (exits) the Debug program! No questions ever asked... should be the easiest command to remember.

Register: R [register] Entering ' r ' all by itself will display all of the 8086 register's contents and the next instruction which the IP register points to in both machine code and an unassembled (Assembly Language) form. For example, if you start DEBUG in a Windows 95B DOS-box

### with the command line

>debug c:\windows\command\choice.com

```asm
and then enter an ' r ' at the first DEBUG prompt, DEBUG will display someting similar to
this:
```

```
AX=0000 BX=0000        CX=1437 DX=0000 SP=FFFE            BP=0000 SI=0000 DI=0000
DS=0ED8 ES=0ED8        SS=0ED8 CS=0ED8 IP=0100             NV UP EI PL NZ NA PO NC
0ED8:0100 E90E01             JMP    0211
```

For an explanation of the names of the registers (AX, BX, CX, etc. and the Flag symbols: NV UP EI PL NZ NA PO NC), see the Appendix (The 8086 CPU Registers). The last line shows that the next CPU instruction (actually the first in this case) to be executed, begins at memory location 100 hex (the Offset) in Segment ED8 hex (0ED8:0100) and that the Hex bytes E90E01 represent the actual binary machine code of the CPU instruction (JMP 0211 in Assembly language) that would be executed by DEBUG if you entered a Trace (t) or Proceed (p) command.

If you enter the ' r ' followed by the abbreviation for an 8086 register, such as: ' rcx ', then DEBUG will display only the contents of that register followed by a line with a colon symbol (:) on which you can enter a hex number to change the contents of that register. If you simply

### press the ENTER key, the contents remain the same. For example

-rcx

### CX 0100

:273

means that the Register command was used to change the contents of the CX register from 0100 to 0273. The command ' rcx ' could be used again to verify that the change had indeed taken place. If you type the letter f after an r: ' rf ', this commands DEBUG to display all of the FLAG register bits with a prompt on the same line which allows you to change any or none of the individual flag bits. For example, here's how you would display the flags and

### change just the Zero Flag bit from being cleared (a 0 bit) to being set (a 1 bit)

-rf

NV UP EI PL NZ NA PO NC                    -zr -rf

### NV UP EI PL ZR NA PO NC                    -

- As you can see above the Zero Flag was changed from NZ (cleared) to ZR (set). See the Appendix The FLAGS Register below for an explanation of all the Flag abbreviations.

Search: S range list Searches within a range of addresses for a pattern of one or more byte values given in a list. The list can be comprised of numbers or character strings enclosed by matching single or

### double quote marks. Examples

-s fe00:0 ffff "BIOS"

```
FE00:0021
FE00:006F
```

```
-d fe00:0
FE00:0000 41 77 61 72 64 20 53 6F-66 74 77 61 72 65 49 42                  Award SoftwareIB
FE00:0010 4D 20 43 4F 4D 50 41 54-49 42 4C 45 20 34 38 36                  M COMPATIBLE 486
FE00:0020 20 42 49 4F 53 20 43 4F-50 59 52 49 47 48 54 20                   BIOS COPYRIGHT
FE00:0030 41 77 61 72 64 20 53 6F-66 74 77 61 72 65 20 49                  Award Software I
FE00:0040 6E 63 2E 6F 66 74 77 61-72 65 20 49 6E 63 2E 20                  nc.oftware Inc.
FE00:0050 41 77 03 0C 04 01 01 6F-66 74 77 E9 12 14 20 43                  Aw.....oftw... C
FE00:0060 1B 41 77 61 72 64 20 4D-6F 64 75 6C 61 72 20 42                  .Award Modular B
FE00:0070 49 4F 53 20 76 34 2E 35-31 50 47 00 DB 32 EC 33                  IOS v4.51PG..2.3
```

-s 0:0 dff 'A20'

```
0000:0C42
```

```
-d 0:c40
0000:0C40 0D 0A 41 32 30 20 68 61-72 64 77 61 72 65 20 65                  ..A20 hardware e
0000:0C50 72 72 6F 72 2E 20 20 43-6F 6E 74 61 63 74 20 74                  rror. Contact t
0000:0C60 65 63 68 6E 69 63 61 6C-20 73 75 70 70 6F 72 74                  echnical support
0000:0C70 20 74 6F 20 69 64 65 6E-74 69 66 79 20 74 68 65                   to identify the
0000:0C80 20 70 72 6F 62 6C 65 6D-2E 0D 0A 24 1A 00 BA F6                   problem...$....
```

-0:0 dff 43 4f 4d

```
0000:0774
0000:07C2
0000:07D4
0000:07E6
```

```
-d 0:770
0000:0770 7A 02 A6 02 43 4F 4D 31-20 20 20 20 8E 00 70 00                  z...COM1     ..p.
0000:0780 C0 A0 7A 02 91 02 4C 50-54 31 20 20 20 20 A0 00                  ..z...LPT1     ..
0000:0790 70 00 C0 A0 7A 02 98 02-4C 50 54 32 20 20 20 20                  p...z...LPT2
0000:07A0 2D 01 70 00 C0 A0 7A 02-9F 02 4C 50 54 33 20 20                  -.p...z...LPT3
0000:07B0 20 20 11 EA 27 27 3F FD-CA 00 70 00 00 80 7A 02                    ..''?...p...z.
0000:07C0 AC 02 43 4F 4D 32 20 20-20 20 DC 00 70 00 00 80                  ..COM2     ..p...
0000:07D0 7A 02 B2 02 43 4F 4D 33-20 20 20 20 00 00 6B 03                  z...COM3     ..k.
0000:07E0 00 80 7A 02 B8 02 43 4F-4D 34 20 20 20 20 E8 D2                  ..z...COM4     ..
```

Trace: T [=address] [number] The T command is used to trace (step through) CPU instructions one at a time. If you enter the T command all by itself, it will step through only ONE instruction beginning at the

location specified by your CS:IP registers, halt program execution and then display all the CPU registers plus an unassembled version of the next instruction to be executed; this is the 'default' mode of the TRACE command. Say, however, you wanted DEBUG to trace and

### execute seven instructions beginning at address CS:0205; to do so, you would enter

```
-t =205 7
```

Remember that the value for the number of instructions to execute must be given in hexadecimal just as all other values used in DEUBG. (Since the T command uses the "hardware trace mode" of the CPU, it's possible to step through instructions in a ROM - Read Only Memory - chip.)

Unassemble: U [range] Disassembles machine instructions into 8086 Assembly code. Without the optional [range], it uses Offset 100 as its starting point, disassembles about 32 bytes and then remembers the next byte it should start with if the command is used again. ( The word 'about' was used above, because it may be necessary to finish with an odd-number of bytes greater than 32, depending upon the last type of instruction DEBUG has to disassemble. )

NOTE: The user must decide whether the bytes that DEBUG disassembles are all 8086 instructions, just data or any of the newer x86 instructions (such as those for the 80286, 80386 on up to the lastest CPU from Intel; which are all beyond the ability of DEBUG to understand)!

### Example

```
-u 126 133
```

xxxx:0126 31C0                           XOR          AX,AX xxxx:0128 B409                           MOV          AH,09 xxxx:012A BA0201                         MOV          DX,0102 xxxx:012D CD21                           INT          21 xxxx:012F B84C00                         MOV          AX,004C xxxx:0132 CD21                           INT          21 -

The 8086 CPU REGISTERS

First, a quick review of how Binary and Hexadecimal numbers are related: When the ones and zeros of four Binary bits are grouped together (from 0000 to 1111; often called a nibble), they can be represented by a single Hex digit (from 0 to F); both of which are used to count from 0 to 15 in Decimal. Eight Binary bits (which allow for any Decimal value from 0 to 255) are

```asm
represented by two Hex digits; for example, the Binary number 10101010 is equal to AA in
```

Hexadecimal. Two-digit Hex numbers (or 8-bit Binary numbers) are called bytes. No matter how many digits a number has in Binary or Hexadecimal, you can switch between the two by grouping and converting every four Binary bits to one Hex digit or vice versa. The Hexadecimal equivalent of a 12-bit Binary must have 3 digits (e.g., 101010111100 = ABC hex), and the largest Decimal number that can be represented by sixteen Binary bits (65,535)

is            equivalent               to                FFFF            in           Hex.

The four main (16-bit) registers of an 8086 CPU are called: The Accumulator (AX), Base (BX), Count (CX) and Data (DX) Registers. Each of these registers has a High (H) and Low (L) 8-bit half which can store one Hexadecimal byte (1 byte = 8 binary bits). Each of these

### high and low halves can be accessed separately by program code

AX:                                                 Accumulator BX:                     AH                AL        Base Register CX:                                                 Count Register DX:                     BH                BL        Data Register

### CH                CL

### DH                DL

<-- 8 bits --> <-- 8 bits -->

< 1 byte >        < 1 byte >

### The other 16-bit ( two-byte ) registers of the 8086 CPU are

SP                Stack Pointer

BP                Base Pointer

SI                Source Index

DI                Destination Index

CS                Code Segment

DS                Data Segment

SS                Stack Segment

ES                Extra Segment

IP                Instruction Pointer

The 8086 CPU uses a method I'll call the SEGMENT: OFFSET scheme whenever it needs to access Memory locations or Jump from one 64kb Segment to another. It does this by combining two 16-bit registers together to form a 20-bit Segment:Offset value ( which means it can access over 1MB of Memory this way). For certain types of tasks, the registers are often grouped together in the same way, but the programmer must still make sure that the CPU will

### use them as expected. Here are a couple tasks which are set by the CPU itself

CS             :         IP               Next Instruction SS             :         SP               Stack Pointer

### Two other sets which are often used together in String operations are

DS             :         SI               Source Index ES             :         DI               Destination Index

The "FLAGS" REGISTER

If you really want to use MS-DEBUG (or any other debugger!) to examine the operation of Assembly programs, then I advise you to copy these abbreviations onto notecards and try to understand why certain bits (flags) do/don't change in the register for each instruction in the program you're examining. ( Make sure you study the final table below if you'll be reading textbooks which discuss the newer 16-bit Flags Register. Newer 32-bit debuggers, such as Borland's Turbo Debugger, display the same eight Flags as DEBUG, but use an abbreviation for the Name of the Flag and simply show whether it's a 0 or 1 bit.)

This is an 8-bit register that holds 1-bit of data for each

### of the eight "Flags" which are to be interpreted as follows

Textbook abbrev. for Flag Name =>            of df if sf zf af pf cf If the FLAGS were all SET (1),               -- -- -- -- -- -- -- -- they would look like this...   =>            OV DN EI NG ZR AC PE CY If the FLAGS were all CLEARed (0), they would look like this...   =>            NV UP DI PL NZ NA PO NC

FLAGS                   SET (a 1-bit)   CLEARed (a 0-bit) ---------------                 --------------- ------------------- Overflow        of    =    OV              NV [No Overflow]

Direction      df    =    DN (decrement)      UP (increment)

Interrupt      if    =    EI   (enabled)      DI (disabled)

Sign     sf    =    NG (negative)       PL (positive)

Zero     zf    =    ZR    [zero]        NZ   [ Not zero]

Auxiliary Carry        af    =    AC                  NA   [ No AC ]

Parity     pf   =      PE   (even)         PO   (odd)

Carry     cf   =      CY   [Carry]        NC   [ No Carry]

==============

### The individual abbreviations appear to have these meanings

OV = OVerflow, NV = No oVerflow.    DN = DowN,              UP (up). EI = Enable Interupt, DI = Disable Interupt.

NG = NeGative, PL = PLus; a strange mixing of terms due to the fact that 'Odd Parity' is represented by PO (rather than POsitive), but they still could have used 'MI' for MInus.

ZR = ZeRo, NZ = Not Zero. AC = Auxiliary Carry, NA = Not Auxiliary carry. PE = Parity Even, PO = Parity Odd. CY = CarrY, NC = No Carry.

To help you understand the display in MS-DEBUG compared to any Assembly texts which make references to a 16-bit FLAGS register, here's the layout of the first 12 bits

### (0 - 11) of the newer 16-bit Flags Register

Symbols used by MS-DEBUG ----------------------------------- OV DN EI    NG ZR    AC    PE    CY            ---> When bit = 1 NV UP DI    PL NZ    NA    PO    NC            ---> When bit = 0

### |xx|xx|xx|--|xx|xx| 0|xx| 0|xx| 1|xx| Newer Designations

Bits: 11 10 9 8 7 6 5 4 3 2 1 0 | | | | | | | | | | | '--- CF - Carry Flag | | | | | | | | | | '--- is always a 1 | | | | | | | | | '--- PF - Parity Flag | | | | | | | | '--- is always a 0 | | | | | | | '--- AF - Auxiliary (Carry) Flag | | | | | | '--- is always a 0 | | | | | '--- ZF - Zero Flag | | | | '--- SF - Sign Flag | | | '--- (TF Trap Flag - not shown in MS-DEBUG) | | '--- IF - Interrupt Flag | '--- DF - Direction Flag '--- OF - Overflow flag

## instructions

8086/80186/80286/80386/80486 Instruction Set Instruction                                          Usage         Modifies flags                  Operands

```asm
AAA - Ascii Adjust for Addition                      AAA           AF CF (OF,PF,SF,ZF undefined)   none
AAD - Ascii Adjust for Division                      AAD           SF ZF PF (AF,CF,OF undefined)   none
AAM - Ascii Adjust for Multiplication                AAM           PF SF ZF (AF,CF,OF undefined)   none
```

AAS - Ascii Adjust for Subtraction                   AAS           AF CF (OF,PF,SF,ZF undefined)   none ADC - Add With Carry                                 ADC d,s       AF CF OF SF PF ZF               r,r m,r r,m r,i m,i a,i

```asm
ADD - Arithmetic Addition                            ADD d,s       AF CF OF PF SF ZF               r,r m,r r,m r,i m,i a,i
AND - Logical And                                    AND d,s       CF OF PF SF ZF (AF undefined)   r,r m,r r,m r,i m,i a,i
BSF - Bit Scan Forward                               BSF d,s       ZF                              r,r r,m r32,r32 r32,m32
```

BSR - Bit Scan Reverse                               BSR d,s       ZF                              r,r r,m r32,r32 r32,m32 BSWAP - Byte Swap                                    BSWAP r32     none                            r32 BT - Bit Test                                        BT d,s        CF                              r16,i8 m16,i8 r16,r16 m16,r16 BTC - Bit Test with Compliment                       BTC d,s       CF                              r16,i8 m16,i8 r16,r16 m16,r16 BTR - Bit Test with Reset                            BTR d,s       CF                              r16,i8 m16,i8 r16,r16 m16,r16 BTS - Bit Test and Set                               BTS d,s       CF                              r16,i8 m16,i8 r16,r16 m16,r16

```asm
CALL - Procedure Call                                CALL d        None                            address
```

CBW - Convert Byte to Word                           CBW           None                            none CDQ - Convert Double to Quad                         CDQ           None                            none

```asm
CLC - Clear Carry                                    CLC           CF                              none
CLD - Clear Direction Flag                           CLD           DF                              none
CLI - Clear Interrupt Flag (disable)                 CLI           IF                              none
```

CMC - Complement Carry Flag                          CMC           CF                              none

```asm
CMP - Compare                                        CMP d,s       AF CF OF PF SF ZF               r,r m,r r,m r,i m,i a,i
```

CMPS - Compare String (B, W or Dw)                   CMPS d,s      AF CF OF PF SF ZF               ES:DI,DS:SI CMPXCHG - Compare and Exchange                       CMPXCHG d,s   AF CF OF PF SF ZF               r,r m,r CWD - Convert Word to Doubleword                     CWD           None                            none (AX -> DX:AX) CWDE - Convert Word to Ext.Dword                     CWDE          None                            none (AX->EAX)

```asm
DAA - Decimal Adjust for Addition                    DAA           AF CF PF SF ZF (OF undefined)   none (AL)
DAS - Decimal Adjust for Subtraction                 DAS           AF CF PF SF ZF (OF undefined)   none (AL)
DEC - Decrement                                      DEC d         AF OF PF SF ZF                  r8 m r16/32
DIV - Divide                                         DIV s         AF,CF,OF,PF,SF,ZF undefined     r8 r16 r32 m8 m16 m32
```

(b:AX/src->q=AL,r=AH, w:DX:AX/src->q=AX,r=DX) IDIV - Signed Integer Division                       IDIV s        AF,CF,OF,PF,SF,ZF undefined     r8 r16 r32 m8 m16 m32 IMUL - Signed Multiply                               IMUL s        CF OF (AF,PF,SF,ZF undefined)   r8 r16 r32 m8 m16 m32 (b:AL*src->AX, w:AX*src->DX:AX) IMUL d,s                                      r16,r16 r32,r32 r16,m16 r32,m32 r16,i r32,i IMUL d,s,i8                                   r16,r16,i r32,r32,i r16,m16,i r32,m32,i

```asm
IN - Input Byte or Word From Port                    IN a,port     None                            a,i8 a,DX
INC - Increment                                      INC d         AF OF PF SF ZF                  r8 r16 r32 m
```

INS - Input String from Port                         INS d,port    None                            ES:DI,DX

```asm
INT - Interrupt                                      INT num       TF IF                           i8
```

INTO - Interrupt on Overflow                         INTO          IF TF                           none IRET/IRETD - Interrupt Return                        IRET          AF CF DF IF PF SF TF ZF         none

```asm
JA Jump if Above                                                   CF=0 and ZF=0
JAE Jump if Above or Equal                                         CF=0
JB Jump if Below                                                   CF=1
JBE Jump if Below or Equal                                         CF=1 or ZF=1
JC Jump if Carry                                                   CF=1
JCXZ Jump if                                                       CX Zero CX=0
JE Jump if Equal                                                   ZF=1
JG Jump if Greater (signed)                                        ZF=0 and SF=OF
JGE Jump if Greater or Equal (signed)                              SF=OF
JL Jump if Less (signed)                                           SF != OF
JLE Jump if Less or Equal (signed)                                 ZF=1 or SF != OF
JMP Unconditional Jump                                             unconditional
JNA Jump if Not Above                                              CF=1 or ZF=1
JNAE Jump if Not Above or Equal                                    CF=1
JNB Jump if Not Below                                              CF=0
JNBE Jump if Not Below or Equal                                    CF=0 and ZF=0
JNC Jump if Not Carry                                              CF=0
JNE Jump if Not Equal                                              ZF=0
JNG Jump if Not Greater (signed)                                   ZF=1 or SF != OF
JNGE Jump if Not Greater or Equal (signed)                         SF != OF
JNL Jump if Not Less (signed)                                      SF=OF
JNLE Jump if Not Less or Equal (signed)                            ZF=0 and SF=OF
JNO Jump if Not Overflow (signed)                                  OF=0
JNP Jump if No Parity                                              PF=0
JNS Jump if Not Signed (signed)                                    SF=0
JNZ Jump if Not Zero                                               ZF=0
JO Jump if Overflow (signed)                                       OF=1
JP Jump if Parity                                                  PF=1
JPE Jump if Parity Even                                            PF=1
JPO Jump if Parity Odd                                             PF=0
JS Jump if Signed (signed)                                         SF=1
JZ Jump if Zero                                                    ZF=1
JCXZ/JECXZ - Jump if CX is Zero                      JCXZ label    None                            addr
JMP - Unconditional Jump                             JMP target    None                            addr
```

LAHF - Load Rister AH From Flags                     LAHF          None                            none

1/2

8086/80186/80286/80386/80486 Instruction Set LDS - Load Pointer Using DS                                  LDS d,s            None                            r16,m32 r,m

```asm
LEA - Load Effective Address                                 LEA d,s            None                            r,m
```

LES - Load Pointer Using ES                                  LES d,s            None LFS - Load Pointer Using FS LGS - Load Pointer Using GS

```asm
LODS - Load String (Byte, Word or Double)                    LODS s             None                            DS:SI->accumulator
LOOP - Decrement CX and Loop if CX Not Zero                  LOOP label         None
LOOPE - Loop While Equal                                     LOOPE label        None
LOOPZ - Loop While Zero                                      LOOPZ label        None
LOOPNZ - Loop While Not Zero                                 LOOPNZ label       None
LOOPNE - Loop While Not Equal                                LOOPNE label       None
```

LSS - Load Pointer Using SS

```asm
MOV - Move Byte or Word                                      MOV d,s            None
MOVS - Move String (Byte or Word)                            MOVS d,s           None                            DS:SI->ES:DI
MOVSX - Move with Sign Extend                                MOVSX d,s          None
MOVZX - Move with Zero Extend                                MOVZX d,s
MUL - Unsigned Multiply                                      MUL s              CF OF (AF,PF,SF,ZF undefined)
```

NEG - Two's Complement Negation                              NEG d              AF CF OF PF SF ZF

```asm
NOP - No Operation (90h)                                     NOP                None
NOT - One's Compliment Negation (Logical NOT)                NOT d              None
OR - Inclusive Logical OR                                    OR d,s             CF OF PF SF ZF (AF undefined)
OUT - Output Data to Port                                    OUT port,a         None
```

OUTS - Output String to Port                                 OUTS port,s        None

```asm
POP - Pop Word off Stack                                     POP d              None
```

POPA/POPAD - Pop All Risters onto Stack                      POPA               None POPF/POPFD - Pop Flags off Stack                             POPF POPFD                                                        all flags

```asm
PUSH - Push Word onto Stack                                  PUSH s
```

PUSHA/PUSHAD - Push All Risters onto Stack                   PUSHA PUSHAD                                                       None PUSHF/PUSHFD - Push Flags onto Stack                         PUSHF PUSHFD                                                       None

```asm
RCL - Rotate Through Carry Left                              RCL d,count        CF OF
RCR - Rotate Through Carry Right                             RCR d,count        CF OF
REP - Repeat String Operation                                REP                None
REPE/REPZ - Repeat Equal / Repeat Zero                       REPE               None
REPNE/REPNZ - Repeat Not Equal / Repeat Not Zero             REPNE              None
RET/RETF - Return From Procedure                             RET nBytes
ROL - Rotate Left                                            ROL d,count        CF OF
ROR - Rotate Right                                           ROR d,count        CF OF
```

SAHF - Store AH Rister into FLAGS                            SAHF               AF CF PF SF ZF

```asm
SAL/SHL - Shift Arithmetic Left / Shift Logical Left         SAL d,count        CF OF PF SF ZF (AF undefined)
SHL d,count        CF OF PF SF ZF (AF undefined)
SAR - Shift Arithmetic Right                                 SAR d,count        CF OF PF SF ZF (AF undefined)
```

SBB - Subtract with Borrow/Carry                             SBB d,s            AF CF OF PF SF ZF

```asm
SCAS - Scan String (Byte, Word or Doubleword)                SCAS string        AF CF OF PF SF ZF
```

SETAE/SETNB - Set if Above or Equal / Set if Not Below       SETAE d            none                            r8 m8 SETB/SETNAE - Set if Below / Set if Not Above or Equal SETBE/SETNA - Set if Below or Equal / Set if Not Above SETE/SETZ - Set if Equal / Set if Zero SETNE/SETNZ - Set if Not Equal / Set if Not Zero SETL/SETNGE - Set if Less / Set if Not Greater or Equal SETGE/SETNL - Set if Greater or Equal / Set if Not Less SETLE/SETNG - Set if Less or Equal/Set if Not greater or Equal SETG/SETNLE - Set if Greater / Set if Not Less or Equal SETS - Set if Signed SETNS - Set if Not Signed SETC - Set if Carry SETNC - Set if Not Carry SETO - Set if Overflow SETNO - Set if Not Overflow SETP/SETPE - Set if Parity / Set if Parity Even SETNP/SETPO - Set if No Parity / Set if Parity Odd

```asm
SHL - Shift Logical Left See: SAL
SHR - Shift Logical Right                                      SHR d,count      CF OF PF SF ZF (AF undefined)
```

SHLD/SHRD - Double Precision Shift                             SHLD d,s,count   CF PF SF ZF (OF,AF undefined) SHRD d,s,count   CF PF SF ZF (OF,AF undefined) STC - Set Carry                                                STC              CF                              none STD - Set Direction Flag                                       STD              DF                              none STI - Set Interrupt Flag                                       STI              IF                              none

```asm
STOS - Store String (B,W,Dword)                                STOS d           None                            accumulator->ES:DI
SUB - Subtract                                                 SUB d,s          AF CF OF PF SF ZF               r,r m,r r,i m,i a,i
TEST - Test For Bit Pattern                                    TEST d,s         CF OF PF SF ZF (AF undefined)   r,r r,m m,r r,i m,i a,i
XCHG - Exchange                                                XCHG d,s         None                            r,r m,r r,m a,r r,a
```

XLAT/XLATB - Translate                                         XLAT X-table     None                            [BX+AL]->AL

```asm
XOR - Exclusive OR                                             XOR d,s          CF OF PF SF ZF (AF undefined)   r,r m,r r,m r,i m,i a,i
```

2/2
