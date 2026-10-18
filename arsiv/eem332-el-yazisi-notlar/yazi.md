---
baslik: EEM332 Mikroişlemciler: 8086 Donanım ve Assembly El Yazısı Notları
ozet: 2011 tarihli ve 2014 arşivli ders sayfalarından adresleme, yığın, bayraklar, döngüler ve bellek bağlantıları.
---

Başkent Üniversitesi EEM332 Mikroişlemciler ders arşivindeki bu içerik, fotoğraflanmış sayfalardan metne aktarıldı. 2011 tarihli ve 2014 arşivli ders sayfalarından adresleme, yığın, bayraklar, döngüler ve bellek bağlantıları. Öğrenci adları ve numaraları çıkarıldı. Fotoğraflar özel arşivde tutulur; bu yazının indirme dosyası yoktur.

## Mikroişlemciye yazılım ve donanım açısından bakış

6 Nisan 2011 tarihli notlar işlemciyi iki yönden ele alır: yazılım tarafında yazmaçlar ve komut kümesi, donanım tarafında bacaklar, veri yolu ve kontrol sinyalleri. 8086 ve 8088 için 40 bacaklı kılıf; sırasıyla 16 ve 8 bit dış veri yolu gösterilmiştir. Minimum mod tek işlemcili bağlantı, maksimum mod daha geniş sistem bağlantıları için anlatılır.

*Not: Kaynaktaki “8086 ile 8088 arasındaki tek fark veri yoludur” ifadesi bir sadeleştirmedir; komut kuyruğu ve bazı bacak işlevleri de farklıdır.*

## Kontrol sinyalleri ve saat

RD ve WR okuma/yazma yönünü, bellek/port seçimi ilgili kontrol sinyalini belirler. ALE, çoklanmış adres/veri hatlarındaki adresin latch üzerinde tutulmasını sağlar; daha sonra aynı uçlardan veri taşınabilir. NMI maskelenemeyen kesme olarak gösterilir; IF ile engellenmez. Reset işlemciyi başlangıç yürütüm durumuna getirir.

Saat darbeleri işlemlerin zamanlamasını belirler. Notlarda bir bellek okuma/yazma çevrimi dört saat darbesiyle gösterilir; tek bir komut birden fazla çevrim gerektirebilir.

*Not: Dört saatlik gösterim bekleme durumları eklenmeyen temel bus çevrimidir. Dinamik RAM için nottaki “reset” sözcüğü yenileme (refresh) işlemini anlatmaktadır. NMI geldiğinde bütün veriler kendiliğinden kaydedilmez; gerekli saklama işlemleri kesme yordamıyla yapılır.*

## Bellek kapasitesi ve adres çözümleme

k adres hattı ve N bit veri genişliği için kapasite 2ᵏ×N bittir. 32 KiB×8 bitlik düzen için 15 adres hattı, 2 KiB bellek için 11 adres hattı gerekir. Üst adres bitleri kod çözücüye, alt bitler belleğin kendi adres girişlerine bağlanır. A19–A14=111100 olan 16 KiB blok F0000H–F3FFFH aralığıdır.

## Segment ve fiziksel adres

Fiziksel adres = segment×10H + ofset. Segment başlangıcı 16 bayt sınırındadır; 16 bit ofset bir segment içinde 64 KiB alanı adresler. CS:IP komut, DS veri, SS:SP yığın için kullanılır. LEA bellekteki veriyi değil etkin adresi yükler.

CS=3489H ve IP=2500H örneğinde nottaki toplama sonucunun son basamakları karışıktır.

*Not: Hesap 34890H+2500H=36D90H olmalıdır. Bu segmentin 0000H–FFFFH ofsetleri 34890H–4488FH aralığına karşılık gelir.*

## MOV ve adresleme örnekleri

```asm
MOV AL,BL
MOV AL,0005H
MOV [1234H],AL
MOV CX,DX
MOV AX,857AH
```

Notlarda doğrudan bellekten belleğe MOV ve farklı genişlikte MOV AL,CX üzeri çizilerek geçersiz gösterilmiştir. Bir yazmaç ara basamak olarak kullanılmalıdır. Temel adresleme biçimleri anlık, yazmaç, doğrudan bellek, yazmaç dolaylı, indisli ve taban+indis+yer değiştirmedir.

MOV AX,[BX+4] örneğinde DS=0100H ve BX=0600H için fiziksel adres 01604H bulunur. Bu adreste B0H, sonraki adreste C0H varsa AX=C0B0H olur. MOV [BP][SI],AH örneğinde varsayılan segment SS’dir; SS=2000H, BP=4000H, SI=0800H için adres 24800H’tir. AH=07H bu adrese yazılır.

## Yazmaçlar ve DEBUG bayrakları

AX/BX/CX/DX, AH/AL gibi yüksek ve düşük baytlarına ayrılabilir. SP yığın işaretçisi, BP taban işaretçisi, SI ve DI indis yazmaçlarıdır. Laboratuvar fotoğrafında DEBUG’un bayrak kısaltmaları gösterilir:

| Bayrak | 1 | 0 |
| --- | --- | --- |
| OF | OV | NV |
| DF | DN | UP |
| IF | EI | DI |
| SF | NG | PL |
| ZF | ZR | NZ |
| AF | AC | NA |
| PF | PE | PO |
| CF | CY | NC |

CF işaretsiz elde/ödünç, OF işaretli taşma, ZF sıfır, SF işaret ve PF düşük baytın çift paritesini ifade eder. BCD işlemlerinde her onluk basamak dört bit ile temsil edilir; aritmetik sonrasında uygun BCD düzeltme komutları gerekir.

## Yığın

8086’da word PUSH, SP’yi 2 azaltır; POP 2 artırır. SS değişmez. SS=0000H, SP=2000H ve AX=1234H için PUSH AX sonrasında SP=1FFEH; [1FFE]=34H, [1FFF]=12H olur.

```asm
PUSH AX
PUSH BX
POP AX
POP BX
```

Bu sıra iki yazmacın içeriğini değiştirir. CALL/RET ile kullanılan alt programlarda gerekli yazmaçlar PUSH/POP ile korunabilir.

## Sıfır bitlerini sayma

NUM=F0E0H için kaynak örnek:

```asm
MOV CX,16
SUB BX,BX
MOV AX,NUM
Back: SHR AX,1
      JC SON
      INC BX
SON: LOOP Back
MOV Count,BX
```

F0E0H içinde yedi adet 1 ve dokuz adet 0 vardır; Count=9 olur. SHR ile çıkan bit CF’ye alınır. JC, 1 biti olduğunda artırmayı atlar.

## Beş baytı toplama

```asm
SUB AL,AL
MOV CX,5
MOV BX,200H
NEXT: ADD AL,[BX]
      INC BX
      LOOP NEXT
```

DS:0200H–0204H baytları AL’de toplanır. Sonuç sekiz bit olduğundan taşma ayrıca izlenmelidir.

## Dizinin her elemanına beş ekleme

DS:1000H–100FH aralığındaki 16 bayt için notta CX=16, DI=1000H başlangıcı; ADD [DI],5, INC DI ve LOOP döngüsü yer alır.

*Not: Kaynakta bellek işleneninin genişliği yazılmamıştır; assembler’ın bunu belirleyebilmesi için ADD BYTE PTR [DI],5 biçimi gerekir. LOOP komutunun CX=0 olması nedeniyle ZF’yi 1 yaptığına dair el yazısı ifade yanlıştır: LOOP bayrakları değiştirmez.*

## İşaretli toplam

DATA1=+80 ve DATA2=+85 için sekiz bit toplam A5H’dir; OF=1, CF=0, SF=1. CBW ile her işlenen ayrı ayrı word’e genişletilip toplandığında sonuç 00A5H, yani +165 olur.

## Karşılaştırma ve koşullu atlama

CMP, çıkarma sonucunu saklamadan bayrakları ayarlar. JE/JZ eşitliği, JNE/JNZ eşit olmamayı, JNC elde olmamasını, JS negatif işareti sınar. JA/JAE işaretsiz büyüklük karşılaştırması içindir. AND AL,04H bit 2’yi maskeleyerek sınama örneğidir.

```asm
MOV CL,03H
SHR AL,CL
JC BIT2_ONE
```

Üç sağa kaydırmadan sonra başlangıçtaki bit 2 CF’de bulunur. Notlardaki başka bir sayaç döngüsü DEC CL ve JNZ kullanır.

## Bayrak aktarımı ve kontrolü

LAHF durum bayraklarının bir bölümünü AH’ye, SAHF AH’den bu bayraklara aktarır. CLC taşıma bayrağını temizler, STC kurar; CLI ve STI maskelenebilir kesmeleri kontrol eder. CLD, DF=0 yaparak dizi işlemlerinin artan adreslere doğru ilerlemesini sağlar.

## Dizi komutları ve iç içe döngüler

MOVSB, DS:SI’den ES:DI’ye bir bayt; MOVSW bir word taşır. LODS kaynak değeri AL/AX’e, STOS AL/AX’i hedefe aktarır. SCAS, AL/AX ile ES:DI’deki değeri karşılaştırır. REP sayacı CX’tir. Notlardaki STOS örneğinde AL=42 değeri ardışık hedef konumlarına yazılır. LODS ve STOS karşılaştırma yapmaz, aritmetik durum bayraklarını değiştirmez.

LOOPE için CX’in sıfır olmaması ve ZF=1, LOOPNE için CX’in sıfır olmaması ve ZF=0 gerekir. İç içe döngülerde dış CX değerinin korunması için yığın kullanılabilir. HLT işlemci yürütümünü uygun kesme veya reset koşuluna kadar durdurur.
