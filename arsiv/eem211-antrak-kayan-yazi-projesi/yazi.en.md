---
baslik: EEM211 Digital Logic Design: 24-Column Scrolling Text Project (ANTRAK, Ali Yetiş)
ozet: Creating scrolling text on an LED matrix using a PIC16F84A, a PC/AT keyboard, an EEPROM, and TTL counters.
---

"24-Column Scrolling Text Project" by Ali Yetiş (TA5CCF), published in the ANTRAK newspaper. The text is signed Kadirli, November 2003; the recorded source address is `www.antrak.org.tr/gazete/122003/ali_yetis.htm`. The article's photographs were not published. The HTML text without images can be downloaded at the end of the post; the hardware and software flow are transferred into the text below.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed upon the rights holder's request.*

## Structure of the Application

The circuit operates independently of a computer; the text is entered from a PC/AT keyboard. The PIC16F84A receives the keyboard codes, stores them in the EEPROM, and sends the column data of the characters to the display. The display consists of 24 columns and 7 used rows. The length of text that can be stored is 63 characters, including spaces; EEPROM address H'00' stores the character count.

The source describes the supported character set as uppercase English letters, the digits 0–9, the period, and the space, and says "35 characters".

*Note: The set described amounts to 38 items: 26 letters, 10 digits, and two symbols. The figure of 35 in the text has been retained and this counting discrepancy is noted; it should not be confused with the text length limit of 63.*

## LED Matrix and Driving

The application is designed for 5×7 character display. Seven rows of the 8×8 modules used are utilized. In the common-cathode configuration, the rows are driven with logic 1 and the selected column with logic 0. When switching to a common-anode configuration, the drive levels need to be changed.

The row data determines the image of the character, while the column scan determines to which position this data is applied at that moment. When the columns are enabled in fast sequence, the image appears continuous. The article describes, for the character L, first the row pattern 1111111 and then three times the row pattern 0000001; the column data is shifted at each step.

## TTL Counter and Decoder Chain

The scanning section uses three 74160 BCD counters, three 7442 decimal decoders, and 7402 NOR gates. The selected output of the 7442 is active and goes to logic 0. The columns are selected by operating the counter/decoder stages in sequence.

When a stage reaches its end, its own counting is stopped and clock pulses are passed to the next stage. Since some of the Q0 and Q9 outputs are used for reset and for transitions between stages, not every decimal output is assigned directly to a display column. A specific output in the last stage returns the entire scan to the beginning.

The source also contains a 25-column animation; the author explains that this first belonged to a hand-built display. The actual project has 24 columns.

## Receiving Serial Data from the Keyboard

The PIC's RB7 pin reads the keyboard CLOCK line, and the RA4 pin reads the DATA line. A PORTB change triggers the interrupt. The first falling edge is skipped as the start bit; eight data bits are received between the second and ninth falling edges. The following parity and stop pulses are left out of consideration in this application.

The received bits are made parallel in a register named VERI. The author describes adding an extra read so that the same character is not written twice, since key-press and key-release events produce separate information.

## EEPROM and Display Flow

At startup, the port directions are set; the program waits for the information the keyboard sends at power-up to finish. The character count is read from the EEPROM. The stored key code is converted into character columns using a conversion table; these columns are transferred to PORTB synchronously with the scan.

The program contains the working areas SUTUN1–SUTUN24, EEPROM read/write counters, temporary W/STATUS save areas, and delay counters. The reset vector is at address H'0000', and the interrupt vector is at address H'0004'.

```asm
ORG H'0000'
GOTO MAIN
ORG H'0004'
GOTO KLYOKU
```

## Application Notes from the Source

The author notes that the scan stopping when a key is pressed could damage the LEDs. They also relate their own experience regarding the length and shielding of the programming cable. These are working notes of the 2003 application.

The source page links to downloads such as `matrix_asm.zip`, `matrix_hex.zip`, character codes, and an Eagle library. Since the link targets are not present in this archive folder, they have not been included as if they were. The assembly text appearing within the article is preserved in the HTML copy; it was not run or compiled.
