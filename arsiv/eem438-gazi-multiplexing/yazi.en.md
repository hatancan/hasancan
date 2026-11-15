---
baslik: EEM438 Data Communications: Multiplexing: FDM, WDM, TDM and Spread Spectrum (Gazi University, Suat Özdemir)
ozet: Suat Özdemir's Data Communications lecture slides from Gazi University: FDM, WDM, synchronous and statistical TDM, DS services, and spread spectrum (FHSS, DSSS).
---

These are the Chapter 6 (Multiplexing) slides prepared by Suat Özdemir of the Department of Computer Engineering at Gazi University for the course "Veri İletişimi / Data Communications" (slide date 21 March 2011; the footer reads BM 403 Data Communications). They were kept in the EEM438 folder as the course material of a second instructor. The slide text is transcribed below; figures and tables taken from the textbook are not published, and slides without text are marked. The original PDF can be downloaded at the end of the post.

Scope: FDM, WDM, synchronous and statistical TDM, DS services, and spread spectrum (FHSS, DSSS).

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution. It will be removed at the request of the rights holder.*

## Multiplexing

- The goal of multiplexing is efficiency. Multiple channels are combined to form a single channel.
- The goal of spreading is privacy and the prevention of jamming. For this purpose, the bandwidth is increased.
- If the bandwidth of the medium connecting two devices is greater than required, the link can be shared.
- Multiplexing is the general name for the techniques that allow many signals to be transmitted simultaneously over one link.
- A mux (multiplexer) combines many inputs into one source (many-to-one), while a demux (demultiplexer) separates the signals in a single source (one-to-many).
- A link refers to the physical connection; a channel refers to a portion within the link.

## Multiplexing (2)

- There are three basic techniques.
  - Frequency-division multiplexing (FDM)
  - Wave-division multiplexing (WDM)
  - Time-division multiplexing (TDM)

## FDM - Frequency-division multiplexing

- FDM is an analog technique used when the bandwidth of the link is greater than the bandwidth of the signals to be transmitted.
- In FDM, a different carrier signal is modulated by each device.
- FDM is an analog technique that combines analog signals.

## FDM

- Each signal modulates a separate carrier (multiplexer). The combined signal is transmitted over the link.

## FDM (2)

- The demultiplexer separates the signals using a series of filters.

## FDM – Example 1

- Voice channels have a bandwidth of 4 kHz. To combine 3 voice channels, a link with a bandwidth of 12 kHz is needed. A sample configuration might look as follows.

## FDM – Example 2

- Each of 4 channels communicates at 1 Mbps. A configuration for FDM of the 1 MHz channel on a satellite might look as follows.
- Each channel has a bandwidth of 250 kHz, and 16-QAM modulation is used on each channel (4 bits are sent per 1 Hz).

## FDM – Example 3

- Channels with low bandwidth are multiplexed onto channels with higher bandwidth.

## FDM – Example 4

- AMPS (Advanced Mobile Phone System) uses two bands. The 824-849 MHz band is used for sending and the 869-894 MHz band is used for receiving. Each user uses a channel with a bandwidth of 30 kHz in one direction. How many users can communicate simultaneously? Each band is 25 MHz (849-824 and 894-869). 25 MHz / 30 kHz = 833.33. In practice, each band is divided into 832 channels. A total of 42 channels are used for control. 790 channels are allocated to users. Since each user needs two channels (one per direction), 790 users can communicate simultaneously in full duplex.

## FDM – Examples

- AM radio stations are placed into 10 kHz channels by FDM in the 530 kHz-1700 kHz band.
- FM radio stations are placed into 200 kHz channels by FDM in the 88 MHz-108 MHz band.
- TV broadcasts are placed into channels with a bandwidth of 6 MHz.
- First-generation cell phones use FDM. A 30 kHz channel is assigned to each user. The voice signal has a bandwidth of 3 kHz, and since the channel bandwidth in FM is 10 x the modulating signal, the total bandwidth is 30 kHz. Each user is assigned 60 kHz of channels for full-duplex communication.

## WDM – Wavelength division mult.

- WDM is designed to exploit the high bandwidth of fiber optic cable. WDM is a multiplexing technique that combines optical signals.
- WDM is used in SONET (Synchronous Optical Network) networks. Dense WDM (DWDM) combines more channels by multiplexing the channels very close together.

## WDM – Wavelength division mult. (2)

- Today's WDM systems can support 160 different signal components
  - A 10 Gbit/s system over a single fiber can carry 1.6 Tbit/s of data
- For this reason, WDM systems are widely used by telecommunications companies.
- By using WDM and optical amplifiers, telecommunications companies can support multiple technologies (OSI, TCP/IP) together.

## TDM - Time division multiplexing

- TDM shares a link with high bandwidth among multiple connections.
- While FDM shares a portion of the band, TDM shares the entire band according to time.
- There are two types of TDM: synchronous and statistical. In synchronous TDM, a certain time slot is allocated to each input even if there is no data.

## TDM - Synchronous

- In synchronous TDM, the data of each input is divided into units. A unit can be 1 bit, 1 character, or 1 block.
- The time slots of the inputs form a frame. A frame consists of the combination of 1 unit of data from every input.

## TDM - Synchronous (2)

- Example
  - In the figure, one data unit is 1 bit.
  - Input bit duration = 1 / 1 Mbps = 1 μs.
  - Output bit duration = 1 / 4 μs.
  - Output bit rate = 1 / 4 μs = 4 Mbps. (4 x 1 Mbps = 4 Mbps)
  - Frame rate = 1 Mbps (this is the bit rate of 1 input)

## TDM - Synchronous (3)

- TDM is performed with fast switches at both ends. The two switches operate synchronously.
- Interleaving refers to the connection time of the switches at both ends for each input/output at certain intervals.

## TDM - Synchronous (4)

- Example
  - In the figure, 4 channels are multiplexed using TDM. Each channel has a data rate of 100 bytes/s, and each channel is multiplexed 1 byte at a time.
  - Frame size = 4 bytes (32 bits).
  - A frame takes 1 byte from each input per second. Frame rate = 100 frames/s.
  - Frame duration = 1/100 s.
  - Bit rate = frame rate × frame size = 100 frames/s × 32 bits = 3200 bps.

## TDM - Synchronous (5)

- Example
  - A multiplexer combines four 100 kbps channels, taking 2 bits from each channel in each time slot.
  - Since 2 bits are taken from each channel, the link runs at 100 kbps/2 = 50,000 frames/s.
  - Frame duration = 1 / 50,000 = 20 μs.
  - Bit rate = 50,000 * 8 = 400 kbps.
  - Bit duration = 1 / 400 kbps = 2.5 μs.

## TDM - Synchronous (6)

- Time is allocated to each input even if it has no data to send.
- Since empty slots are allocated in frames, efficiency decreases.

## TDM - Synchronous (7)

- Data rate management
  - It may be necessary to combine inputs with different rates.
  - Multilevel multiplexing

## TDM - Synchronous (8)

- Data rate management
  - Multiple slot allocation
- A serial-to-parallel converter is used.
  - Pulse stuffing
- The bit rate is brought up to the desired value with dummy bits.

## TDM - Synchronous (9)

- Frame-level synchronization must be performed between the multiplexer and demultiplexer.
- Synchronization bits (framing bits) are placed at the beginning of each frame.
- Usually 1 bit that alternates between 1 and 0 is placed at the beginning of each frame.

## TDM - Synchronous (10)

- Example
  - Data is generated at 250 characters/s from 4 sources. The interleaved unit is 1 character, and 1 synchronization bit is added per frame.
  - Data rate for each input = 250 * 8 = 2000 bps = 2 kbps.
  - Duration of one character = 1 / 250 = 4 ms.
  - Frame rate = 250 frames/s.
  - Duration of each frame = 1 / 250 = 4 ms.
  - Each frame contains 4*8+1 = 33 bits.
  - Data rate for the link = 250 × 33 = 8250 bps.

## Digital Signal Service

*This slide contains only figures/tables; the visuals are in the original PDF.*


## Digital Signal Service (2)

- A DS-0 service is a single digital channel of 64 kbps.
- DS-1 is a 1.544-Mbps service; 1.544 Mbps is 24 times 64 kbps plus 8 kbps of overhead. It can be used as a single service for 1.544-Mbps transmissions, or it can be used to multiplex 24 DS-0 channels or to carry any other combination desired by the user that can fit within its 1.544-Mbps capacity.
- DS-2 is a 6.312-Mbps service; 6.312 Mbps is 96 times 64 kbps plus 168 kbps of overhead.
- DS-3 is a 44.376-Mbps service; 44.376 Mbps is 672 times 64 kbps plus 1.368 Mbps of overhead.
- DS-4 is a 274.176-Mbps service; 274.176 is 4032 times 64 kbps plus 16.128 Mbps of overhead

## TDM - Statistical

- Synchronous TDM is not efficient because it allocates time to inputs that send no data.
- In statistical TDM, time is allocated to inputs that have data. The number of slots in a frame is less than the number of inputs.
- The multiplexer scans the inputs using a round-robin approach.

## TDM - Statistical (2)

- In synchronous TDM, frames contain only data. In statistical TDM, address information is sent along with the data.
- Addressing is binary, and with n bits N (n = log₂N) outputs can be addressed.
- In statistical TDM, the ratio between address and data is important for communication efficiency.
- Statistical TDM does not need synchronization bits.

## Spread spectrum

- Multiplexing shares a link among multiple sources.
- Spread spectrum shares a link with a wider bandwidth among multiple sources.
- Spread spectrum is used in wireless LANs and wireless WANs.
- If the bandwidth required for each channel is B, spread spectrum expands it to B_ss. (B_ss >> B)
- The spreading process is performed using a spreading code.

## Spread Spectrum

- Spread spectrum techniques use a much larger bandwidth than necessary
  - For a single user this wastes bandwidth, but with multiple users, the users can share the same bandwidth without interference
  - Therefore, with multiple users, spread spectrum is an efficient method in terms of bandwidth

## Spread Spectrum (2)

- Spread spectrum involves spreading the bandwidth required for the data to be transmitted
- For example, CDMA is a multiple access model based on the spread spectrum technique. In CDMA, each user sharing a common channel is given a signal (code) occupying a separate frequency band.
  - Many users can be present on the same band simultaneously
  - The data rate allocated to users can be adjusted according to varying load conditions
- Spreading the data over a wide bandwidth makes jamming and interception more difficult.

## Spread Spectrum (3)

- Narrowband interference example: 6 channels are used with FDM multiplexing.
- Frequency planning is required.
- Channel quality depends on frequency; channel quality is a measure of the interference at that frequency.

## Spread Spectrum (4)

- Because of narrowband interference, the signal quality on channels 3 and 4 is so low that the receiver cannot receive them correctly.
- Solution?

## Spread Spectrum (5)

- Spread the narrowband signal into a broadband signal using a special code
  - Pseudo-noise (PN) sequence, pseudo-noise code
  - A binary sequence that looks random (but can be regenerated by the receiver)
- Spread spectrum increases resistance against narrowband interference

## Spread Spectrum (6)

- All narrowband signals are spread as broadband signals over the same (wide) frequency range.

## Spread Spectrum (7)

- What does the "wasted" spectrum gain us?
  - Resistance to noise
  - Security/encryption
  - Many users can use a wide band with very little interference

## Spread spectrum techniques

- There are two techniques
  - Frequency Hopping Spread Spectrum (FHSS)
  - Direct Sequence Spread Spectrum (DSSS)

## Frequency Hopping Spread Spectrum (FHSS)
- M different carriers are modulated by the inputs.
- In one time interval the source signal modulates one carrier, in the next time interval it modulates another carrier.
- A pseudorandom code generator (pseudorandom noise - PN) generates a k-bit pattern. Each pattern is used for one hop during the time Th (hopping period).

## Frequency Hopping Spread Spectrum (FHSS) (2)
- For M = 8 and k = 3, 8 frequencies from the frequency table are determined by 3 bits.
  - Those who do not know the order of the generated k-bit pattern cannot follow the communication.

## Frequency Hopping Spread Spectrum (FHSS) (3)
- In each cycle, every frequency is hopped to once.

## Frequency Hopping Spread Spectrum (FHSS) (4)
- FDM and FHSS can be used together.

## Direct Sequence Spread Spectrum (DSSS)
- Each data bit is replaced with n bits (chips).
- For wireless LAN, an 11-bit Barker sequence is used.

## Direct Sequence Spread Spectrum (DSSS) (2)
- In the figure, 10110111000 is used as the 11-bit chip sequence.
- The bandwidth of the spread signal is 11 times greater.
- Those who do not know the spreading code cannot understand the communication.
- For binary 1 the code itself is sent, for binary 0 its inverse is sent.
