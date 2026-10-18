---
baslik: EEM438 Veri İletişimi: DHCP, ICMP ve IP Laboratuvar Ders Notları
ozet: DHCP mesajları, ICMP alanları ve IP parçalama üzerine kısa sınıf notları ve kaynak hatalarına açıklamalar.
---

Ders sırasında tutulmuş anonim kısa notlardır. Kaynak dosyanın tarihi 30 Nisan 2015’tir; metnin UTF-8 kopyası yazının sonunda indirilebilir. Eksik sorular ve cevaplar belirtilerek korundu.

## DHCP

1. UDP kullanılır.
2. Portlar 67–68.
3. İlk adımda MAC ile tanımlama: hostun MAC adresi nedir?
4. Discover ve Request mesajlarının tipleri farklıdır.
5. İlk dört mesaj grubunda Transaction ID aynı mı? Başka gruba geçince değişiyor mu? Notta aynı grupta aynı, başka grupta farklı olduğu yazılmıştır.
6. İlk dört mesajda host ve server arasında hangi adres bilgileri kullanılır?
7. Kaynak IP adresi: 10.0.15.1.
8. Bootstrap içindeki “your IP address / client IP address” alanı.
9. Alt ağlar ve relay agent: notta relay bilgisi varsa adresin başka alt ağdan alındığı söylenmiştir.
10. İstemcinin hangi subnet mask’i kullanacağı gösterilir.
11. Option 50: Requested IP Address; “aynıdır”.
12. Option 51: IP Address Lease Time, 10 gün; “neden?” sorusu yanıtsızdır.
13. DHCP sunucusu Release mesajına yanıt vermiyor; notta bu şekilde yazılmıştır.
14. Filtre temizlenerek kalan paketlerin incelenmesi istenir; açıklama tamamlanmamıştır.

*Not: DHCP relay, istemcinin başka bir alt ağdaki DHCP sunucusuna erişmesine aracılık edebilir; istemciye verilen adresin mutlaka başka bir alt ağa ait olduğu anlamına gelmez. “Transaction IP” yazımı Transaction ID olarak aktarıldı.*

## ICMP

Hedef www.ust.hk. Notta 10 istek ve 10 cevap gözlendiği yazılmıştır.

1. Kaynak ve hedef IP adreslerini gösterme.
2. “Port bilgisi 3. katmanda atanıyor” ifadesi yer alır.
3. Type ve code alanları; iki identifier gösterimi üzerine kısa, tamamlanmamış açıklama.
4. Type = 0, code = 0; diğer alanların ve kaç bayt olduklarının incelenmesi.
5. IP adreslerini tekrar gösterme.
6. “Kodun 17 olması gerekiyordu (cevap)” yazılmıştır.
7. Ping request ile echo/ping paketinin aynı olduğunun kontrolü.
8. İki reply mesajını inceleme.
9. Boş bırakılmıştır.
10. Komut penceresindeki süreler karşılaştırılır; bir atlamada sürenin artması için mesafe veya kayıpla ilgili olası açıklamalar not edilmiştir.

*Not: ICMP TCP/UDP portu kullanmaz; tür ve kod alanları vardır. IPv4 Protocol alanında ICMP = 1, UDP = 17’dir. Notlardaki katman/port ifadesi ve 17 değeri bu nedenle hatalı veya bağlamı eksiktir. Identifier alanının iki gösterimi endian gösterimiyle ilişkilidir; bir yazı dilinin yönüyle açıklanmaz.*

## IP ve parçalama

PingPlotter ile gaia.cs.umass.edu hedefinin incelenmesi istenir.

- Soru 3: IP header length 20 bayt, toplam 56 bayt; kalan 36 bayt.
- Soru 4: Parçalama bilgisi için Flags ve More Fragments alanları incelenir. Kaynakta “parçalanmış olsa 1 olurdu” yazılmıştır.
- Paketler source adresine göre sıralanır.

*Not: 56−20=36 bayt yük hesabı doğrudur. More Fragments = 0, paketin hiç parçalanmadığını tek başına kanıtlamaz; son parçada da 0’dır. Fragment Offset ile birlikte değerlendirilmelidir.*
