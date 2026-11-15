---
baslik: EEM322 Control Systems: Arduino DS18B20 Temperature Reading Examples (Hacktronics and Arduino Türkiye)
ozet: Arduino examples accompanying the 2015 temperature control project: multiple sensor addresses, DallasTemperature, and direct OneWire reading.
---

The three **Arduino temperature reading examples** kept alongside the EEM322 spring 2015 temperature control project are brought together in this post. In its comments, the multi-sensor example credits Hacktronics; the direct OneWire example credits Arduinoturkiye.com and its editor, İsmail Buçgün. File paths carrying student names have been removed. The archive dates of the sources are May 2015; the code can be downloaded as a ZIP at the end of the post.

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes, with the source credited. It will be removed at the request of the rights holder.*

The completed student project, which also includes relay control, is covered in the [Kettle Control post](/arsiv/eem322-kettle-kontrol-projesi/). The files here are different examples used for trying out temperature measurement.

## Reading Three Sensors by Address

The `OneWire` and `DallasTemperature` libraries are used. The data line is connected to pin 3. Three device addresses are defined in the code; the resolution is 10 bits and the serial communication is 9600 baud. A conversion is requested every two seconds; the Celsius and Fahrenheit values of each sensor are printed. A result of −127 °C is treated as an error.

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

## Reading a Single Sensor by Index

In this version, the data line is on pin 2. After `requestTemperatures`, `getTempCByIndex(0)` returns the temperature of the first device on the same line.

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

## Reading the Scratchpad with OneWire

The third example directly performs the sensor search, the CRC check, the conversion command, and the nine-byte scratchpad read. The recognized family codes are 0x10 and 0x28. In the error paths, −1000 is returned.

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

*Note: In the last example, although both the 0x10 and 0x28 families are accepted, the raw value is divided by 16 in both cases. In this code, the family-specific conversion, waiting for the conversion to finish, and treating a negative temperature as a signed raw value have not been separately verified. The source code was transcribed without being compiled or run on hardware.*
