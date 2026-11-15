---
baslik: EEM438 Data Communications: Wireless Networks and Multimedia Midterm Notes
ozet: Wireless Networks and Multimedia midterm notes. Questions, explanations and documents from the course archive.
---


## Wireless Links, SNR and CDMA

Being wireless is not the same as being mobile. A base station provides access to the infrastructure; in an ad hoc network there is no central base station. Handoff is changing base stations while the connection continues. Attenuation, interference and multipath propagation affect the wireless channel. SNR is the signal-to-noise ratio, and BER is the bit error rate.

In the hidden terminal example, A and C, which cannot hear each other, may collide by transmitting to B at the same time. CDMA separates users with different codes; the receiver correlates with the code.

![Wireless link, SNR and CDMA — handwritten, page 1](belge-295-sayfa-01.jpg "Wireless link, SNR and CDMA — handwritten, page 1")

![Wireless link, SNR and CDMA — handwritten, page 2](belge-295-sayfa-02.jpg "Wireless link, SNR and CDMA — handwritten, page 2")

![Wireless link, SNR and CDMA — handwritten, page 3](belge-295-sayfa-03.jpg "Wireless link, SNR and CDMA — handwritten, page 3")

## 802.11, Scanning and CSMA/CA

A BSS is the service set around an access point; the SSID identifies the network. In passive scanning, beacons are listened for; in active scanning, probes are sent. Association is completed with a request and a response. CSMA/CA transmits after DIFS on an idle channel; on a busy channel it uses random backoff. The ACK arrives after SIFS.

RTS/CTS is meant to reserve the channel and reduce the hidden terminal effect; RTS packets can still collide. The frame is drawn with control, duration, address, sequence control, payload and CRC fields. In power management, the access point buffers data for a sleeping client.

![802.11, scanning and CSMA/CA — handwritten, page 4](belge-295-sayfa-04.jpg "802.11, scanning and CSMA/CA — handwritten, page 4")

![802.11, scanning and CSMA/CA — handwritten, page 5](belge-295-sayfa-05.jpg "802.11, scanning and CSMA/CA — handwritten, page 5")

![802.11, scanning and CSMA/CA — handwritten, page 6](belge-295-sayfa-06.jpg "802.11, scanning and CSMA/CA — handwritten, page 6")

![802.11, scanning and CSMA/CA — handwritten, page 7](belge-295-sayfa-07.jpg "802.11, scanning and CSMA/CA — handwritten, page 7")

![802.11, scanning and CSMA/CA — handwritten, page 8](belge-295-sayfa-08.jpg "802.11, scanning and CSMA/CA — handwritten, page 8")

## Cellular Networks and Mobile IP

2G voice, 2.5G packet data and 3G are compared in the context of carrying voice and data together. The diagrams include BSC, MSC, SGSN and GGSN. The FDMA/TDMA and CDMA methods are noted.

For Mobile IP, the home network, permanent address, care-of address, home agent, foreign agent and correspondent are defined. In indirect routing, data is tunneled through the home agent. In direct routing, the correspondent learns the care-of address. Agent discovery, registration with the home agent, and indirect routing are the three basic components.

![Cellular networks and Mobile IP — handwritten, page 9](belge-295-sayfa-09.jpg "Cellular networks and Mobile IP — handwritten, page 9")

![Cellular networks and Mobile IP — handwritten, page 10](belge-295-sayfa-10.jpg "Cellular networks and Mobile IP — handwritten, page 10")

![Cellular networks and Mobile IP — handwritten, page 11](belge-295-sayfa-11.jpg "Cellular networks and Mobile IP — handwritten, page 11")

![Cellular networks and Mobile IP — handwritten, page 12](belge-295-sayfa-12.jpg "Cellular networks and Mobile IP — handwritten, page 12")

![Cellular networks and Mobile IP — handwritten, page 13](belge-295-sayfa-13.jpg "Cellular networks and Mobile IP — handwritten, page 13")

![Cellular networks and Mobile IP — handwritten, page 14](belge-295-sayfa-14.jpg "Cellular networks and Mobile IP — handwritten, page 14")

![Cellular networks and Mobile IP — handwritten, page 15](belge-295-sayfa-15.jpg "Cellular networks and Mobile IP — handwritten, page 15")

![Cellular networks and Mobile IP — handwritten, page 16](belge-295-sayfa-16.jpg "Cellular networks and Mobile IP — handwritten, page 16")

## Multimedia, Streaming and RTSP

QoS is quality of service. Multimedia is classified as stored streaming, live streaming and interactive real-time communication. Jitter is the variation in packet delays. A receiver buffer and delayed playout smooth out the fluctuation.

The presentation file/metafile carries where the media is located and the player information. UDP leaves the sending rate to the application; TCP can produce a variable arrival rate because of congestion control and retransmission. RTSP is for play, pause and session control; by itself it does not determine which transport protocol the media data will use. In the source, the RTSP control port is given as 554.

![Multimedia, streaming and RTSP — handwritten, page 17](belge-295-sayfa-17.jpg "Multimedia, streaming and RTSP — handwritten, page 17")

![Multimedia, streaming and RTSP — handwritten, page 18](belge-295-sayfa-18.jpg "Multimedia, streaming and RTSP — handwritten, page 18")

![Multimedia, streaming and RTSP — handwritten, page 19](belge-295-sayfa-19.jpg "Multimedia, streaming and RTSP — handwritten, page 19")

![Multimedia, streaming and RTSP — handwritten, page 20](belge-295-sayfa-20.jpg "Multimedia, streaming and RTSP — handwritten, page 20")

![Multimedia, streaming and RTSP — handwritten, page 21](belge-295-sayfa-21.jpg "Multimedia, streaming and RTSP — handwritten, page 21")

![Multimedia, streaming and RTSP — handwritten, page 22](belge-295-sayfa-22.jpg "Multimedia, streaming and RTSP — handwritten, page 22")

![Multimedia, streaming and RTSP — handwritten, page 23](belge-295-sayfa-23.jpg "Multimedia, streaming and RTSP — handwritten, page 23")

![Multimedia, streaming and RTSP — handwritten, page 24](belge-295-sayfa-24.jpg "Multimedia, streaming and RTSP — handwritten, page 24")

## Playout Delay and Loss Recovery

tᵢ is the generation time, rᵢ the reception time, and pᵢ the playout time. The network delay is rᵢ−tᵢ.

- dᵢ = (1−u)dᵢ₋₁ + u(rᵢ−tᵢ)
- vᵢ = (1−u)vᵢ₋₁ + u|rᵢ−tᵢ−dᵢ|
- At the start of a talkspurt, pᵢ = tᵢ + dᵢ + Kvᵢ.

Enlarging the playout buffer reduces the loss of late-arriving packets but delays interaction. In FEC, an extra packet is generated from the XOR of n packets. Piggybacking attaches a lower-quality copy of the previous audio chunk to the next packet. Interleaving spreads small chunks across packets to disperse the effect of loss, but adds delay.

![Playout delay and loss recovery — handwritten, page 25](belge-295-sayfa-25.jpg "Playout delay and loss recovery — handwritten, page 25")

![Playout delay and loss recovery — handwritten, page 26](belge-295-sayfa-26.jpg "Playout delay and loss recovery — handwritten, page 26")

![Playout delay and loss recovery — handwritten, page 27](belge-295-sayfa-27.jpg "Playout delay and loss recovery — handwritten, page 27")

![Playout delay and loss recovery — handwritten, page 28](belge-295-sayfa-28.jpg "Playout delay and loss recovery — handwritten, page 28")

![Playout delay and loss recovery — handwritten, page 29](belge-295-sayfa-29.jpg "Playout delay and loss recovery — handwritten, page 29")

## RTP, RTCP and SIP

RTP carries the media's payload type, sequence number, timestamp and SSRC information; it does not guarantee timely delivery or bandwidth. At 64 kbit/s PCM, 20 ms of audio is 160 bytes. At 8 kHz sampling, the sample interval is 125 µs.

RTCP provides loss, jitter and timing information through receiver and sender reports; it helps synchronize audio and video streams. In the notes, 5% of the session bandwidth is allocated to RTCP, of which 75% goes to receivers and 25% to senders. SIP is a session initiation and management protocol; INVITE, response, ACK, registrar and proxy examples are drawn.

![RTP, RTCP and SIP — handwritten, page 30](belge-295-sayfa-30.jpg "RTP, RTCP and SIP — handwritten, page 30")

![RTP, RTCP and SIP — handwritten, page 31](belge-295-sayfa-31.jpg "RTP, RTCP and SIP — handwritten, page 31")

![RTP, RTCP and SIP — handwritten, page 32](belge-295-sayfa-32.jpg "RTP, RTCP and SIP — handwritten, page 32")

![RTP, RTCP and SIP — handwritten, page 33](belge-295-sayfa-33.jpg "RTP, RTCP and SIP — handwritten, page 33")

![RTP, RTCP and SIP — handwritten, page 34](belge-295-sayfa-34.jpg "RTP, RTCP and SIP — handwritten, page 34")

![RTP, RTCP and SIP — handwritten, page 35](belge-295-sayfa-35.jpg "RTP, RTCP and SIP — handwritten, page 35")

![RTP, RTCP and SIP — handwritten, page 36](belge-295-sayfa-36.jpg "RTP, RTCP and SIP — handwritten, page 36")

![RTP, RTCP and SIP — handwritten, page 37](belge-295-sayfa-37.jpg "RTP, RTCP and SIP — handwritten, page 37")

![RTP, RTCP and SIP — handwritten, page 38](belge-295-sayfa-38.jpg "RTP, RTCP and SIP — handwritten, page 38")

## QoS, Queuing and Resource Reservation

H.323, multiple service classes and packet marking are described. FIFO, priority, round-robin and Weighted Fair Queuing are compared. Traffic policing is explained with average rate, peak rate and burst size. A token bucket allows bursty traffic using accumulated tokens.

In DiffServ, the edge router performs classification and marking, and the core router forwards according to class. PHB behaviors are covered under expedited and assured forwarding. IntServ uses resource reservation and call admission; the R-spec declares the service request and the T-spec the traffic characteristics. RSVP is a signaling protocol; it does not replace the routing algorithm.

![QoS, queuing and resource reservation — handwritten, page 39](belge-295-sayfa-39.jpg "QoS, queuing and resource reservation — handwritten, page 39")

![QoS, queuing and resource reservation — handwritten, page 40](belge-295-sayfa-40.jpg "QoS, queuing and resource reservation — handwritten, page 40")

![QoS, queuing and resource reservation — handwritten, page 41](belge-295-sayfa-41.jpg "QoS, queuing and resource reservation — handwritten, page 41")

![QoS, queuing and resource reservation — handwritten, page 42](belge-295-sayfa-42.jpg "QoS, queuing and resource reservation — handwritten, page 42")

![QoS, queuing and resource reservation — handwritten, page 43](belge-295-sayfa-43.jpg "QoS, queuing and resource reservation — handwritten, page 43")

![QoS, queuing and resource reservation — handwritten, page 44](belge-295-sayfa-44.jpg "QoS, queuing and resource reservation — handwritten, page 44")

![QoS, queuing and resource reservation — handwritten, page 45](belge-295-sayfa-45.jpg "QoS, queuing and resource reservation — handwritten, page 45")

![QoS, queuing and resource reservation — handwritten, page 46](belge-295-sayfa-46.jpg "QoS, queuing and resource reservation — handwritten, page 46")

![QoS, queuing and resource reservation — handwritten, page 47](belge-295-sayfa-47.jpg "QoS, queuing and resource reservation — handwritten, page 47")

![QoS, queuing and resource reservation — handwritten, page 48](belge-295-sayfa-48.jpg "QoS, queuing and resource reservation — handwritten, page 48")
