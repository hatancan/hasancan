---
baslik: EEM322 Denetim Sistemleri: Arduino ile DS18B20 Sıcaklık Okuma Örnekleri (Hacktronics ve Arduino Türkiye)
ozet: 2015 sıcaklık kontrol projesine eşlik eden Arduino örnekleri: çoklu sensör adresleri, DallasTemperature ve doğrudan OneWire okuma.
---

EEM322’nin 2015 bahar dönemi sıcaklık denetimi projesi yanında saklanan üç **Arduino sıcaklık okuma örneği** bu yazıda bir araya getirildi. Çoklu sensör örneği yorumlarında Hacktronics’i; doğrudan OneWire örneği Arduinoturkiye.com’u ve düzenleyen İsmail Buçgün’ü kaynak gösteriyor. Öğrenci adı taşıyan dosya yolları kaldırıldı. Kaynakların arşiv tarihleri Mayıs 2015; kodlar yazının sonunda ZIP olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

Röle denetimini de içeren tamamlanmış öğrenci projesi [Kettle Kontrol yazısında](/arsiv/eem322-kettle-kontrol-projesi/) yer alır. Buradaki dosyalar sıcaklık ölçümünü denemek için kullanılan farklı örneklerdir.

## Üç sensörün adresle okunması

`OneWire` ve `DallasTemperature` kütüphaneleri kullanılır. Veri hattı 3 numaralı pine bağlıdır. Üç aygıt adresi kodda tanımlanır; çözünürlük 10 bit, seri iletişim 9600 baud’dur. İki saniyede bir dönüşüm istenir; her sensörün Celsius ve Fahrenheit değerleri yazdırılır. −127 °C sonucu hata olarak işlenir.

```cpp
// This Arduino sketch reads DS18B20 "1-Wire" digital
// temperature sensors.
// Tutorial:
// http://www.hacktronics.com/Tutorials/arduino-1-wire-tutorial.html

#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into pin 3 on the Arduino
#define ONE_WIRE_BUS 3

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors(&oneWire);

// Assign the addresses of your 1-Wire temp sensors.
// See the tutorial on how to obtain these addresses:
// http://www.hacktronics.com/Tutorials/arduino-1-wire-address-finder.html

DeviceAddress insideThermometer = { 0x28, 0x94, 0xE2, 0xDF, 0x02, 0x00, 0x00, 0xFE };
DeviceAddress outsideThermometer = { 0x28, 0x6B, 0xDF, 0xDF, 0x02, 0x00, 0x00, 0xC0 };
DeviceAddress dogHouseThermometer = { 0x28, 0x59, 0xBE, 0xDF, 0x02, 0x00, 0x00, 0x9F };

void setup(void)
{
  // start serial port
  Serial.begin(9600);
  // Start up the library
  sensors.begin();
  // set the resolution to 10 bit (good enough?)
  sensors.setResolution(insideThermometer, 10);
  sensors.setResolution(outsideThermometer, 10);
  sensors.setResolution(dogHouseThermometer, 10);
}

void printTemperature(DeviceAddress deviceAddress)
{
  float tempC = sensors.getTempC(deviceAddress);
  if (tempC == -127.00) {
    Serial.print("Error getting temperature");
  } else {
    Serial.print("C: ");
    Serial.print(tempC);
    Serial.print(" F: ");
    Serial.print(DallasTemperature::toFahrenheit(tempC));
  }
}

void loop(void)
{ 
  delay(2000);
  Serial.print("Getting temperatures...\n\r");
  sensors.requestTemperatures();
  
  Serial.print("Inside temperature is: ");
  printTemperature(insideThermometer);
  Serial.print("\n\r");
  Serial.print("Outside temperature is: ");
  printTemperature(outsideThermometer);
  Serial.print("\n\r");
  Serial.print("Dog House temperature is: ");
  printTemperature(dogHouseThermometer);
  Serial.print("\n\r\n\r");
}
```

## Bir sensörün indeksle okunması

Bu sürümde veri hattı 2 numaralı pindedir. `requestTemperatures` sonrasında `getTempCByIndex(0)` aynı hatta bulunan ilk aygıtın sıcaklığını verir.

```cpp
#include <OneWire.h>
#include <DallasTemperature.h>
 
// Data wire is plugged into pin 2 on the Arduino
#define ONE_WIRE_BUS 2
 
// Setup a oneWire instance to communicate with any OneWire devices 
// (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);
 
// Pass our oneWire reference to Dallas Temperature.
DallasTemperature sensors(&oneWire);
 
void setup(void)
{
  // start serial port
  Serial.begin(9600);
  Serial.println("Dallas Temperature IC Control Library Demo");

  // Start up the library
  sensors.begin();
}
 
 
void loop(void)
{
  // call sensors.requestTemperatures() to issue a global temperature
  // request to all devices on the bus
  Serial.print(" Requesting temperatures...");
  sensors.requestTemperatures(); // Send the command to get temperatures
  Serial.println("DONE");

  Serial.print("Temperature for Device 1 is: ");
  Serial.print(sensors.getTempCByIndex(0)); // Why "byIndex"? 
    // You can have more than one IC on the same bus. 
    // 0 refers to the first IC on the wire
 
}
```

## OneWire ile scratchpad okunması

Üçüncü örnek, sensör aramasını, CRC kontrolünü, dönüşüm komutunu ve dokuz baytlık scratchpad okumasını doğrudan gerçekleştirir. Tanınan aile kodları 0x10 ve 0x28’dir. Hata yollarında −1000 döndürülür.

```cpp
// Arduinoturkiye.com DS18B20 Dijital Sıcaklık Sensörü Kullanımı
// Tek Sensör Örnek Programı
// Düzenleme: İsmail BUÇGÜN

#include <OneWire.h> // OneWire kütüphanesini ekliyoruz.

// Sıcaklık sensörünü bağladığımız dijital pini 2 olarak belirliyoruz.
int DS18S20_Pin = 2; 

// Sıcaklık Sensörü Giriş-Çıkışı
OneWire ds(DS18S20_Pin);  // 2. Dijital pinde.

void setup(void) {
  Serial.begin(9600); // Seri iletişimi başlatıyoruz.
}

void loop(void) {
  // temperature değişkenini sıcaklık değerini alma fonksiyonuna bağlıyoruz.
  float temperature = getTemp();
  // Sensörden gelen sıcaklık değerini Serial monitörde yazdırıyoruz.
  Serial.print("Sicaklik: ");
  Serial.println(temperature);
  // 1 saniye bekliyoruz. Monitörde saniyede 1 sıcaklık değeri yazmaya devam edecek.
  delay(1000);

}

// Aşağıdaki fonksiyon DS18B20 sıcaklık sensörümüzden gelen verileri
// Celcius cinsinden sıcaklık değerlerine çevirmek için kullanılıyor.
// Herhangi bir değişiklik yapmamız gerekmiyor.

float getTemp(){
  //returns the temperature from one DS18S20 in DEG Celsius

  byte data[12];
  byte addr[8];

  if ( !ds.search(addr)) {
      //no more sensors on chain, reset search
      ds.reset_search();
      return -1000;
  }

  if ( OneWire::crc8( addr, 7) != addr[7]) {
      Serial.println("CRC is not valid!");
      return -1000;
  }

  if ( addr[0] != 0x10 && addr[0] != 0x28) {
      Serial.print("Device is not recognized");
      return -1000;
  }

  ds.reset();
  ds.select(addr);
  ds.write(0x44,1); // start conversion, with parasite power on at the end

  byte present = ds.reset();
  ds.select(addr);    
  ds.write(0xBE); // Read Scratchpad

  for (int i = 0; i < 9; i++) { // we need 9 bytes
    data[i] = ds.read();
  }

  ds.reset_search();

  byte MSB = data[1];
  byte LSB = data[0];

  float tempRead = ((MSB << 8) | LSB); //using two's compliment
  float TemperatureSum = tempRead / 16;

  return TemperatureSum;

}
```

*Not: Son örnekte 0x10 ve 0x28 aileleri kabul edilmesine karşın ham değer her iki durumda da 16’ya bölünüyor. Bu kodda aileye özgü dönüşüm, dönüşümün bitmesini bekleme ve negatif sıcaklığın işaretli ham değer olarak ele alınması ayrıca doğrulanmış değildir. Kaynak kod derlenmeden ve donanımda çalıştırılmadan aktarılmıştır.*
