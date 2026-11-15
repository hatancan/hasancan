---
baslik: EEM438 Data Communications: Multimedia, RTP and QoS: Second Set of Notes
ozet: Multimedia, RTP and QoS: Second Set of Notes. Questions, explanations and documents from the course archive.
---


## UDP/TCP, RTSP and Internet Telephony

In a UDP stream, the sending rate is determined by the application; TCP provides reliable transport and congestion control. RTSP carries out control operations such as play and pause. In Internet telephony, silence can be suppressed; speech is divided into small audio chunks. The jitter buffer and playout delay compensate for timing variation.

![UDP/TCP, RTSP and Internet telephony — handwritten, page 1](belge-298-sayfa-01.jpg "UDP/TCP, RTSP and Internet telephony — handwritten, page 1")

![UDP/TCP, RTSP and Internet telephony — handwritten, page 2](belge-298-sayfa-02.jpg "UDP/TCP, RTSP and Internet telephony — handwritten, page 2")

![UDP/TCP, RTSP and Internet telephony — handwritten, page 3](belge-298-sayfa-03.jpg "UDP/TCP, RTSP and Internet telephony — handwritten, page 3")

![UDP/TCP, RTSP and Internet telephony — handwritten, page 4](belge-298-sayfa-04.jpg "UDP/TCP, RTSP and Internet telephony — handwritten, page 4")

![UDP/TCP, RTSP and Internet telephony — handwritten, page 5](belge-298-sayfa-05.jpg "UDP/TCP, RTSP and Internet telephony — handwritten, page 5")

## FEC, Interleaving and CDN

FEC compensates for loss by using extra data. The XOR approach can recover a single loss within a group; a low-rate audio copy can be carried in the next packet. Interleaving spreads the same audio chunk across different packets. A CDN replicates content across different servers; the client is redirected to a suitable copy.

![FEC, interleaving and CDN — handwritten, page 6](belge-298-sayfa-06.jpg "FEC, interleaving and CDN — handwritten, page 6")

![FEC, interleaving and CDN — handwritten, page 7](belge-298-sayfa-07.jpg "FEC, interleaving and CDN — handwritten, page 7")

![FEC, interleaving and CDN — handwritten, page 8](belge-298-sayfa-08.jpg "FEC, interleaving and CDN — handwritten, page 8")

## RTP, RTCP and SIP

RTP carries sequence number, payload type and timestamp; it can be carried over UDP and does not provide any QoS guarantee. At 8 kHz sampling, Tₛ = 1/8000 s = 125 µs; 20 ms of audio contains 160 samples. With 8-bit/sample PCM, this is 160 bytes. RTCP carries loss and jitter reports and synchronizes streams. SIP sets up sessions with INVITE and responses; the registrar manages location, and the proxy manages the signaling path.

![RTP, RTCP and SIP — handwritten, page 9](belge-298-sayfa-09.jpg "RTP, RTCP and SIP — handwritten, page 9")

![RTP, RTCP and SIP — handwritten, page 10](belge-298-sayfa-10.jpg "RTP, RTCP and SIP — handwritten, page 10")

![RTP, RTCP and SIP — handwritten, page 11](belge-298-sayfa-11.jpg "RTP, RTCP and SIP — handwritten, page 11")

![RTP, RTCP and SIP — handwritten, page 12](belge-298-sayfa-12.jpg "RTP, RTCP and SIP — handwritten, page 12")

![RTP, RTCP and SIP — handwritten, page 13](belge-298-sayfa-13.jpg "RTP, RTCP and SIP — handwritten, page 13")

![RTP, RTCP and SIP — handwritten, page 14](belge-298-sayfa-14.jpg "RTP, RTCP and SIP — handwritten, page 14")

## DiffServ, IntServ and RSVP

DiffServ marks flows at the edge and applies class-based behavior in the core. A PHB is the service a class receives at a router. IntServ reserves resources for an application's requirements; call admission evaluates the current load and the new request. In the token bucket and WFQ scheme, r is the rate and b is the bucket capacity; the delay bound b/R is shown.

RSVP carries reservation information. Path and reservation messages, multicast support and teardown are described. RSVP does not select the route; it does not replace routing or data transmission.

![DiffServ, IntServ and RSVP — handwritten, page 1](belge-297-sayfa-01.jpg "DiffServ, IntServ and RSVP — handwritten, page 1")

![DiffServ, IntServ and RSVP — handwritten, page 2](belge-297-sayfa-02.jpg "DiffServ, IntServ and RSVP — handwritten, page 2")

![DiffServ, IntServ and RSVP — handwritten, page 3](belge-297-sayfa-03.jpg "DiffServ, IntServ and RSVP — handwritten, page 3")

![DiffServ, IntServ and RSVP — handwritten, page 4](belge-297-sayfa-04.jpg "DiffServ, IntServ and RSVP — handwritten, page 4")

![DiffServ, IntServ and RSVP — handwritten, page 5](belge-297-sayfa-05.jpg "DiffServ, IntServ and RSVP — handwritten, page 5")

![DiffServ, IntServ and RSVP — handwritten, page 6](belge-297-sayfa-06.jpg "DiffServ, IntServ and RSVP — handwritten, page 6")

![DiffServ, IntServ and RSVP — handwritten, page 7](belge-297-sayfa-07.jpg "DiffServ, IntServ and RSVP — handwritten, page 7")

*Note: The notes contain a statement that interleaving reduces delay; reassembling the pieces requires additional waiting. RTP's lack of a QoS guarantee does not mean that the protocol cannot perform error/status reporting.*
