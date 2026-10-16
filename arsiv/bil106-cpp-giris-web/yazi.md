---
baslik: BIL106 Programlamaya Giriş: Bilgisayarlar ve C++ ile Programlamaya Giriş (Bilgisayar Dersleri sitesi)
ozet: "Bilgisayar Dersleri" (bilgisayardersleri.wordpress.com) sitesinin C++ giriş yazısı: bilgisayarın birimleri, programlama dillerinin kuşakları, C ve C++ tarihçesi, ilk C++ programları, cout/cin, aritmetik, ilişkisel ve eşitlik operatörleri.
---

Bu yazı, BIL106 Programlamaya Giriş dersinin arşiv klasöründe saklanan bir internet sayfası çıktısıdır: **"Bilgisayar Dersleri"** adlı sitenin (**bilgisayardersleri.wordpress.com**) *"C++ İle Programlamaya Giriş"* başlıklı yazısı. Belgede yazar adı geçmiyor; çıktı Ağustos 2016'da alınmış. Metin yer yer *"Şema: s. 15 (Deitel)"* gibi sayfa göndermeleri içeriyor; yani Deitel & Deitel'in *C++ How to Program* kitabının giriş bölümüne dayanan ders notları gibi görünüyor. Sayfanın 15 sayfalık PDF çıktısı yazının sonunda indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Bilgisayarlar ve C++ ile programlamaya giriş

### Bilgisayar nedir?

Bilgisayar, insanın yapabileceğinden milyonlarca hatta milyarlarca kat hızlı hesaplama yapan ve/ya mantıksal kararlar verilebilen bir alettir. Süper bilgisayarlar saniyede yüz milyarlarca toplama yapabilirler ki bu bir insanın basit bir hesap makinesiyle onlarca yılda yapabileceği işlem miktarıdır.

Bilgisayarlar, bilgisayar programı denen komut setlerinin kontrolü altında verileri işlerler. Bilgisayarda çalışan bilgisayar programlarına **yazılım** denir. Bunları geliştiren, yazan kişilere de **bilgisayar programcısı** denir.

Bilgisayar 6 mantıksal bölümden oluşur:

1. Giriş birimi
1. Çıkış birimi
1. Bellek
1. Aritmetik mantık birimi (merkezi işlem birimi)
1. Kontrol birimi (merkezi işlem birimi)
1. İkincil bellek

### İşletim sistemlerinin evrimi

İlk bilgisayarlar bir anda bir iş yapabiliyorlardı. Delikli kartlarla yazılan programlar, kart okuyucudan bilgisayara okutularak sırayla (bir anda bir iş) çalıştırıldı. Bir anda bir işin çalıştığı bu ortamda bilgisayarın tüm kaynakları verimli biçimde kullanılmamış olmaktadır: MİB çalışırken giriş ve çıkış birimleri boş beklemektedir. Daha verimli kaynak kullanımı için giderek **"çoklu programlama"**ya izin veren işletim sistemleri geliştirilmiştir. Bu ortamlarda bir anda birden fazla iş çalışır, ancak hâlâ kullanıcılar programlarını kartlara delerek bilgisayara girmektedir.

1960'larda **"timesharing"** işletim sistemleri geliştirilmiştir. Timesharing bir ortamda kullanıcılar bilgisayara, terminaller (bir ekran ve klavye) aracılığıyla erişirler. Böylelikle onlarca hatta yüzlerce kişi aynı anda tek bir bilgisayara erişebilmekte ve kullanmaktadır.

### Kişisel, dağıtık ve istemci/sunucu işlem

1977'de Apple şirketi kişisel bilgisayarları popülerleştirdi. İlk başta hobisel bir yaklaşım olan kişisel bilgisayar kullanımı, 1981'de IBM'in Personal Computer'ı tanıtmasıyla sadece evlerde değil iş yaşamında da çok yoğun biçimde kullanılmaya başladı.

Fakat bu bilgisayarlar tek başına birimlerdi. Bilgisayardaki veriyi paylaşabilmek için başka bir bilgisayara taşınabilir disklerle taşımak gerekiyordu. Tek başına, bağımsız üniteler hâlinde bulunan bilgisayarların LAN veya büyük ağlar aracılığıyla birbirine bağlanmasıyla **dağıtık işlem** ("distributed processing") başladı. Bugün artık büyük miktarlarda veri, bilgisayar ağlarında yer alan, File Server denen ve ortak kullanılacak program ve verileri saklayan bilgisayarlar aracılığıyla istemci bilgisayarlar tarafından kullanılabilmektedir (**istemci/sunucu ortam**).

C ve C++ günümüzde, bu ortamları (bilgisayar ağları, dağıtık istemci/sunucu ortamlar, bunları destekleyen işletim sistemleri) yazmakta yaygın olarak kullanılan dillerdir.

### Programlama dilleri

Programlamanın evrimi bakımından 4 sınıftan bahsedebiliriz:

1. **Makine dilleri (1. kuşak):** sayılardan oluşan, sadece belirli bir makinenin anlayacağı, hata yapmaya çok açık diller.
1. **Assembly dilleri (2. kuşak):** İngilizce benzeri komutlardan oluşan diller. Assembly dili ile yazılmış bir program, bir çevirici (translator) ile makine diline çevrilerek çalıştırılır. Oldukça anlaşılabilir gözükmesine karşın çok basit bir iş için bile çok sayıda komut yazmak gerekmektedir.
1. **Yüksek seviyeli diller (3. kuşak), "procedural" diller:** "NASIL" yapılacağını ayrıntılı olarak bildirdiğimiz diller. İngilizceye benzer, aritmetik işlemlerde kullandığımız işaretleri kullanır; daha hızlı ve kolay program yazılır. C ve C++ bu gruptadır.
1. **Çok yüksek seviyeli diller (4. kuşak):** "NE" yapılacağını söylediğimiz diller: LISP, SNOBOL, FORTH, SQL…

3. kuşakta çok sayıda dil geliştirilmiştir. Yaygın kabul görenler:

| Dil | Geliştiren | Yıl | Not |
|---|---|---|---|
| Fortran | IBM | 1954 | Mühendislik uygulamalarında hâlâ yaygın olarak kullanılır. |
| Cobol | | 1959 | Günümüz ticari uygulamalarının yarısı Cobol ile yazılmıştır. |
| Pascal | Niklaus Wirth | 1971 | Akademik kullanım için |

### C ve C++'ın tarihçesi

| Dil | Yıl | Geliştiren | Kurum |
|---|---|---|---|
| BCPL | 1967 | Martin Richards | |
| B | 1970 | Ken Thompson | Bell Laboratuvarları |
| C | 1972 | Dennis Ritchie | Bell Laboratuvarları |
| C++ | 1980 | Bjarne Stroustrup | AT&T |

C, UNIX işletim sisteminin yazılmasında kullanıldı; makineden bağımsız bir dildir. 1983–1989 arasında ANSI, C'nin standart tanımını yaptı; standart 1990'da yayımlandı: ANSI/ISO 9899:1990.

C++, C'ye birtakım ek özellikler ile **nesne yönelimli programlama** ("object-oriented programming") yetenekleri getirmiştir. Nesneler tekrar tekrar kullanılabilir yazılım bileşenleridir; yazılım geliştirmede büyük kolaylık (verimlilik) sağlarlar. Diğer nesne yönelimli diller:

- **Smalltalk:** Xerox Palo Alto Araştırma Merkezi
- **Java:** Sun Microsystems, James Gosling, 1995 (1993'te WWW'nin popülerleşmesi)

*Not: Kaynakta "James Goslin 995" yazıyor; doğrusu James Gosling ve 1995 olmalı.*

### C++ standart kitaplık

C++ programları sınıflar ("classes") ve fonksiyonlardan ("functions") oluşur. Bunlar program parçalarıdır. Bunların bir kısmını programcı yazar, bir kısmı da standart kitaplıkta hazır bulunur.

### Yapısal programlama

1960'lara kadar programlama çok karmaşık, zor, maliyetli idi. 1960'larda **yapısal programlama** ortaya çıkmaya başladı. Yapısal programlama; daha açık, net, anlaşılabilir, okuması, izlemesi, sınaması kolay programlar yazmak için bir yaklaşımdır.

Üç temel yapı kullanılır: **sıra**, **tekrar yapısı** ve **karar verme yapısı**. Goto kullanılmaz ya da mümkün olduğunca az kullanılır. Buna uygun ilk dillerden biri (ve en popüleri diyebiliriz) Pascal'dır (Niklaus Wirth, 1971). Akademik ortamlarda yapısal programlamayı öğretmek için geliştirildi ve pek çok okulda yaygın olarak kullanıldı. Ancak ticari uygulamalarda ve her türlü iş ortamına uygun uygulamalarda gereksinilen pek çok olanağı içermemesi, üniversite dışında yaygın kabul görmemesine neden olmuştur.

Ada: 1970'ler – 1980'lerin başı, ABD Savunma Bakanlığı (US Dept. of Defense).

### Anahtar yazılım trendi: nesne teknolojisi

Yazılım teknolojisindeki gelişme ve ilerlemeler; yapısal programlama, yapısal tasarım, yapısal analiz ile başladı. Ancak nesne yönelimli analiz, tasarım ve programlama ile daha çok gelişme elde edildi. Nesne yönelimli yaklaşımla çevremizdeki tüm nesneleri (araba, öğrenci, ders, insan, uçak, sınıf vb.) modelleriz. Modellediğimiz bu yazılım parçalarını tekrar tekrar kullanabildiğimiz gibi, bu tarz yazılan yazılımlar daha iyi organize ve anlaşılır oldukları için bakımları da çok kolay olmakta ve programcıya zaman ve maliyetten büyük tasarruf sağlamaktadır (yazılım maliyetinin %80'i programlamanın başındaki ve yazımındaki emeğe değil, sonradan yapılan sürekli bakıma aittir).

C++, nesne yönelimli bir dil olarak anılmasına karşın **hibrit** bir dildir; yani hem yapısal hem de nesne yönelimli program yazmayı mümkün kılar.

"Classes and Data Abstraction" konusuna kadar C++ ile "procedural" programlama kavramlarını göreceğiz: kontrol yapıları, fonksiyonlar, veri türleri, giriş/çıkış, diziler, pointer ve string'ler. Bu bölümlerde C++'ın C kısmı ve C++'ın C'ye getirdiği "procedural" iyileştirmeler (procedural enhancements to C) kapsanacaktır.

### C++ programı yürütme aşamaları

Unix ortamında bir C++ programının yürütülmesi için 6 aşamadan geçilir:

1. **Edit:** kaynak programın bir editör program ile yazılması. Uzantısı .cpp, .cxx veya .c
1. **Ön işleme ("preprocess"):** derleme öncesi bazı işlemler
1. **Derleme:** derlemenin çıktısı amaç programdır
1. **Link:** programımızda kullanacağımızı belirttiğimiz standart kitaplık veya özel kitaplıklarda bulunan fonksiyonların amaç programla bir araya getirilmesi (link edilmesi)
1. **Yükleme ("load"):** programın ve varsa gerekli bazı modüllerin (paylaşılan kitaplıklardan) diskten alınıp belleğe yüklenmesi
1. **Yürütme**

Şema: s. 15 (Deitel).

### Taşınabilirlik ("portability")

Taşınabilir programlar yazmak mümkünse de değişik sistemler ve değişik derleyiciler arasında birtakım problemler çıkmaktadır. Taşınabilirlikle ilgili konular ANSI standart dokümanında yer almaktadır: www.ansi.org. Doküman adı: *Information Technology – Programming languages – C++*. Doküman numarası: ISO/IEC 14882-1998. Daha eski taslak versiyonu (ücretsiz): www.cygnus.com/misc/wp/

### İyi program yazma tavsiyeleri

- C++ programlarınızı basit ve dolambaçsız ("straightforward") biçimde yazın: KIS ("Keep It Simple").
- Kullandığınız C++ sürümünün kılavuzu elinizin altında olmalı.
- En iyi öğretici bilgisayarınızdır. Kitaplarda veya derslerde işlenen konuları, verilen örnekleri bilgisayarda çalıştırarak, çıkan hata mesajlarını okuyup tekrar deneyerek öğrenebilir ve tecrübe kazanabilirsiniz.

## C++ ile programlamaya giriş

### Basit bir program: bir satır metnin yazdırılması

```cpp
// C++ ile ilk programım
#include <iostream>

int main()
{
    std::cout << "Herkese Merhaba!\n";

    return 0;   // program sonu
}
```

```
Herkese Merhaba!
```

- `//` C++'ta açıklama satırının başına konur. Bu satırlar için derleyici bir iş yapmaz; program dökümünde aynen yer alan, programın okunabilirliği ve anlaşılabilirliği için gerekli açıklama satırlarıdır. İyi bir programcı gerekli yerlere gerekli açıklamaları koyar. C dilinde ise açıklama `/*  */` arasına konur.
- `#` ile başlayan satırlar ön derleyici ("preprocessor") içindir. Örnek programımızda `#` ile başlayan satır, ön derleyiciye giriş/çıkış ile ilgili `iostream` başlık dosyasını ("header file") programa dahil etmesini söyler.
- `int main()` her C++ programında olması gerekir. Her C++ programı bir veya birkaç fonksiyondan oluşur. `()` main'in bir fonksiyon olduğunu, "main" sözcüğü de bunun ana fonksiyon olduğunu belirtir.
- `int` integer (tamsayı) anlamındadır. `int main()`'in anlamı: bu ana fonksiyonun çalıştıktan sonra verdiği değer bir tamsayıdır (`return 0` ile dönen sıfır).
- Bir fonksiyonun gövdesi ("body") sol küme parantezi `{` ile başlar, sağ küme parantezi `}` ile biter.
- `std::cout` ekrana çıkış almak için kullanılır; ileriki bölümlerde daha ayrıntılı göreceğiz. `std::cin` klavyeden girileni okumak içindir.
- `<<` "stream insertion operator" (akışa ekleme operatörü).
- `\n` karakterlerinin çıktıda yer almadığına dikkat edin! `\` "escape" karakteridir; `n` imlecin alt satıra konumlanmasını söyler.

| Kaçış dizisi | Anlamı |
|---|---|
| `\n` | yeni satır |
| `\t` | bir "tab" ileri gitmek |
| `\r` | imleç, yazılan satırın başına konumlanır ("carriage return") |
| `\a` | uyarı sesi |

*Not: Kaynakta süslü parantezler için "köşeli parantez" deniyor; `{ }` küme (süslü) parantezidir. Ayrıca sayfadaki kodlarda tırnaklar kıvrık (“ ”) yazılmış; derlenebilmesi için burada düz tırnak (") kullanıldı.*

"Herkese Merhaba!" cümlesini başka nasıl yazdırabilirdik?

```cpp
std::cout << "Herkese ";
std::cout << "Merhaba!\n";
```

Şöyle yazarsam çıktı nasıl olur?

```cpp
std::cout << "Herkes\ne\nMerhaba!\n";
```

```
Herkes
e
Merhaba!
```

### Başka bir basit program: iki tamsayının toplanması

```cpp
// İKİ TAMSAYIYI TOPLAYAN PROGRAM
#include <iostream>

int main()
{
    int tamsayi1, tamsayi2, toplam;   // tanımlamalar

    std::cout << "Birinci tamsayıyı giriniz\n";
    std::cin >> tamsayi1;   // klavyeden girilen sayıyı oku
    std::cout << "İkinci tamsayıyı giriniz\n";
    std::cin >> tamsayi2;   // klavyeden girilen sayıyı oku
    toplam = tamsayi1 + tamsayi2;
    std::cout << "Toplam = " << toplam << std::endl;

    return 0;   // programın başarıyla bittiğini gösterir
}
```

`std::endl`: endl "end line", yani satır sonu demektir. Yaptığı iş, yeni satırı yazdıktan (ekrana yolladıktan) sonra çıkış buffer'larını temizlemektir. Bilindiği gibi, çıkışa gönderilecek veriler gönderilmeden önce çıkış buffer'larında biriktirilir. Çıkış işleminden sonra buffer'ların boşaltılması/temizlenmesi için endl kullanırız.

**Önemli notlar:**

- C++, büyük ve küçük harfe duyarlı bir dildir.
- Cümleler `;` (noktalı virgül) ile biter.

**İyi program yazma tavsiyeleri:**

1. Bir fonksiyonun gövdesinin içine yazılan satırlar 3 boşluk içeriden yazılır ("indentation").
1. Tanımlamalar ile yürütülebilir cümleler arasında bir satır boşluk bırakınız.
1. Anlamlı değişken isimleri kullanınız.
1. İkili ("binary") operatörlerin sağında ve solunda birer boşluk bırakınız.

### Aritmetik operatörler

| C++ işlemi | Aritmetik operatör | Cebirsel ifade | C++ ifadesi |
|---|---|---|---|
| Toplama | `+` | f + 7 | `f + 7` |
| Çıkarma | `-` | p − c | `p - c` |
| Çarpma | `*` | bm | `b * m` |
| Bölme | `/` | x/y | `x / y` |
| Modulus | `%` | r mod s | `r % s` |

C++'ta aritmetik işlemlerde operatörlerin öncelik sırası kuralları:

1. Parantez içleri en önce hesaplanır.
1. Daha sonra çarpma, bölme, modulus işlemleri yapılır. Bir aritmetik ifadede birden fazla çarpma, bölme, modulus işlemi varsa, bu işlemlerdeki operatörler **soldan sağa** doğru uygulanır. Çarpma, bölme ve mod operatörlerinin önceliği aynıdır.
1. En son toplama ve çıkarma işlemleri yapılır. Bir ifade birden fazla toplama ve çıkarma işlemi içeriyorsa, bunlara ait operatörler **soldan sağa** uygulanır.

Örnekler: ss. 31–33 (Deitel).

**İyi program yazma tavsiyesi:** Cebirde olduğu gibi gereksiz parantezler konmayabilir. Ancak özellikle uzun ifadelerde alt ifadeleri parantez içine alarak anlaşılabilirliği artırmak iyidir.

### İlişkisel operatörler ve eşitlik operatörleri

| Cebirsel operatör | C++ karşılığı | C++ örneği | Anlamı |
|---|---|---|---|
| > | `>` | `x > y` | x, y'den büyüktür |
| < | `<` | `x < y` | x, y'den küçüktür |
| ≥ | `>=` | `x >= y` | x, y'den büyüktür veya y'ye eşittir |
| ≤ | `<=` | `x <= y` | x, y'den küçüktür veya y'ye eşittir |
| = | `==` | `x == y` | x, y'ye eşittir (eşitlik operatörü) |
| ≠ | `!=` | `x != y` | x, y'ye eşit değildir (eşitlik operatörü) |

*Not: Sayfa çıktısında ≥, ≤ ve ≠ simgeleri görünmüyor (boş kalmış); tabloya eklendi.*

**Sık yapılan hatalar:**

- `==`, `>=`, `<=`, `!=` operatörlerini yazarken iki karakter arasında boşluk bırakılmamalı ve iki karakterin yeri değiştirilmemelidir.
- Eşitlik operatörü `==`'yi, atama için kullanılan `=` ile karıştırmayınız.

### Eşitlik ve bağıntı operatörlerini kullanan bir program örneği

```cpp
// if cümlesi ile eşitlik ve ilişki/bağıntı operatörlerini kullanan bir program
#include <iostream>

using std::cout;   // program cout kullanır
using std::cin;    // program cin kullanır
using std::endl;   // program endl kullanır

int main()
{
    int sayi1, sayi2;

    cout << "İki tamsayi giriniz.\n"
         << "Ben aralarındaki ilişkiyi söyleyeceğim: ";
    cin >> sayi1 >> sayi2;

    if (sayi1 == sayi2)
        cout << sayi1 << sayi2 << "'ye eşittir." << endl;
    if (sayi1 != sayi2)
        cout << sayi1 << sayi2 << "'ye eşit değildir." << endl;
    if (sayi1 < sayi2)
        cout << sayi1 << ", " << sayi2 << "'den küçüktür." << endl;
    if (sayi1 > sayi2)
        cout << sayi1 << ", " << sayi2 << "'den büyüktür." << endl;
    if (sayi1 <= sayi2)
        cout << sayi1 << ", " << sayi2 << "'den küçük veya eşittir." << endl;
    if (sayi1 >= sayi2)
        cout << sayi1 << ", " << sayi2 << "'den büyük veya eşittir." << endl;

    return 0;
}
```

Örnek çalışmalar:

```
İki tamsayı giriniz.
Ben size aralarındaki ilişkiyi söyleyeceğim: 3 7
3, 7'ye eşit değildir.
3, 7'den küçüktür.
3, 7'den küçük veya eşittir.
```

```
İki tamsayı giriniz.
Ben size aralarındaki ilişkiyi söyleyeceğim: 22 12
22, 12'ye eşit değildir.
22, 12'den büyüktür.
22, 12'den büyük veya eşittir.
```

```
İki tamsayı giriniz.
Ben size aralarındaki ilişkiyi söyleyeceğim: 7 7
7, 7'ye eşittir.
7, 7'den küçük veya eşittir.
7, 7'den büyük veya eşittir.
```

*Not: Programdaki ilk iki `if` satırında iki sayı arasına `", "` yazdırılmadığı için bu program aslında "37'ye eşit değildir." basar; gösterilen çıktıya ulaşmak için bu satırlar da `cout << sayi1 << ", " << sayi2 << ...` biçiminde olmalıdır. Örnek çıktılardaki "Ben size aralarındaki…" ifadesi de koddaki metinden biraz farklıdır.*

**Using cümleleri:** `cout` ve `cin`'den önce `std::` kullanımını ortadan kaldırır. Hatırlanacağı gibi ilk basit örneğimizde `std::cout` kullanmıştık. Çok sayıda giriş/çıkış yapılacağı zaman her `cout` ve `cin`'den önce `std::` yazmak çok pratik olmayacaktır. Bu nedenle `using` kullanmakta fayda vardır.

**İyi program yazma tavsiyeleri:**

1. Programın okunabilirliğini artırmak için `if` yapısının içinde yer alan cümleleri 3 boşluk içeriden yazınız.
1. Bir satırda birden fazla cümle yer almamalı.
1. Bir cümle bir satıra sığmayıp alt satırdan devam edecekse, cümleyi anlamlı bir yerinden bölmeye özen gösteriniz.

*Sayfanın etiketleri: c++, c++ dersleri, c++ dosyaları, c++ nedir, c++ programlama, c++ tarihi, C++ ile programlamaya giriş, programlama dilleri.*
