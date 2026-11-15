---
baslik: EEM413 Computer Networks: Handwritten Lecture Notes: From the Internet to VLANs
ozet: Handwritten lecture notes: from the Internet to VLANs. Questions, explanations and documents from the course archive.
---


## The Internet, protocols and access networks

Protocols define the format and order of messages, and the actions to be taken when a message is received. RFC documents and the IETF are associated with the development of Internet standards. At the edge of the network are the end systems; at the core are the routers. Client–server and P2P application architectures are compared.

Access examples are dial-up, DSL, cable/HFC, FTTH and wireless access. The DSLAM aggregates DSL lines on the service provider side. In the FTTH diagram, the OLT, optical distribution and ONT appear. PON is passive and AON is active optical distribution. Physical media are listed as twisted pair, coaxial cable, fiber and radio.

![The Internet, protocols and access networks — handwritten, page 2](belge-105-sayfa-02.jpg "The Internet, protocols and access networks — handwritten, page 2")

![The Internet, protocols and access networks — handwritten, page 3](belge-105-sayfa-03.jpg "The Internet, protocols and access networks — handwritten, page 3")

![The Internet, protocols and access networks — handwritten, page 4](belge-105-sayfa-04.jpg "The Internet, protocols and access networks — handwritten, page 4")

![The Internet, protocols and access networks — handwritten, page 5](belge-105-sayfa-05.jpg "The Internet, protocols and access networks — handwritten, page 5")

## Packet switching and circuit switching

In circuit switching, resources are reserved for the duration of the connection; FDM shares frequency and TDM shares time. In packet switching, connection resources are shared among packets.

The example has 640,000 bits, a 1.536 Mbit/s link and 24 time slots. The user rate is 1,536,000/24 = 64,000 bit/s; transmission takes 10 seconds, and with 0.5 seconds of setup the total is 10.5 seconds.

![Packet switching and circuit switching — handwritten, page 6](belge-105-sayfa-06.jpg "Packet switching and circuit switching — handwritten, page 6")

![Packet switching and circuit switching — handwritten, page 7](belge-105-sayfa-07.jpg "Packet switching and circuit switching — handwritten, page 7")

## Application requirements, TCP and UDP

Applications are compared in terms of data loss tolerance, timing, throughput and security requirements. TCP provides reliable transport, flow control and congestion control. UDP sends datagrams without establishing a connection; it gives no guarantee of delivery, ordering or bandwidth.

*Note: TCP also does not provide absolute timing or minimum-rate guarantees. The short statements in the source about error responsibility do not exclude the protocol's error-control and retransmission functions.*

![Application requirements, TCP and UDP — handwritten, page 8](belge-105-sayfa-08.jpg "Application requirements, TCP and UDP — handwritten, page 8")

![Application requirements, TCP and UDP — handwritten, page 9](belge-105-sayfa-09.jpg "Application requirements, TCP and UDP — handwritten, page 9")

## HTTP, cookies, caching and FTP

HTTP is described with the client–server request/response model. Persistent and non-persistent connections, RTT and object transfer time are compared. The request line and the Host, User-Agent, Connection and Accept-Language headers are shown. The GET, POST, HEAD, PUT and DELETE methods are listed.

Status code examples are 200 OK and 301 Moved Permanently. Cookies help maintain state information, and web caching helps reduce delay and access traffic. Conditional GET avoids re-downloading an object if it has not changed. FTP separates the control connection from the data connection; the note gives port 21 for control and port 20 for active-mode data.

![HTTP, cookies, caching and FTP — handwritten, page 10](belge-105-sayfa-10.jpg "HTTP, cookies, caching and FTP — handwritten, page 10")

![HTTP, cookies, caching and FTP — handwritten, page 11](belge-105-sayfa-11.jpg "HTTP, cookies, caching and FTP — handwritten, page 11")

![HTTP, cookies, caching and FTP — handwritten, page 12](belge-105-sayfa-12.jpg "HTTP, cookies, caching and FTP — handwritten, page 12")

![HTTP, cookies, caching and FTP — handwritten, page 13](belge-105-sayfa-13.jpg "HTTP, cookies, caching and FTP — handwritten, page 13")

## E-mail and DNS

E-mail is explained in terms of user agents, mail servers and SMTP. SMTP is used from the sending server to the receiving server. POP3 and IMAP are for mailbox access; web-based access may use HTTP. IMAP manages folders on the server.

DNS performs name–address resolution in a distributed manner. Root, top-level domain and authoritative servers and a recursive query are drawn. The resource record format is given as (name, value, type, TTL).

![E-mail and DNS — handwritten, page 14](belge-105-sayfa-14.jpg "E-mail and DNS — handwritten, page 14")

![E-mail and DNS — handwritten, page 15](belge-105-sayfa-15.jpg "E-mail and DNS — handwritten, page 15")

![E-mail and DNS — handwritten, page 16](belge-105-sayfa-16.jpg "E-mail and DNS — handwritten, page 16")

![E-mail and DNS — handwritten, page 17](belge-105-sayfa-17.jpg "E-mail and DNS — handwritten, page 17")

![E-mail and DNS — handwritten, page 18](belge-105-sayfa-18.jpg "E-mail and DNS — handwritten, page 18")

## P2P distribution and DHT

F is the file size, N the number of peers, uₛ the server's upload rate, dᵢ the peer's download rate and uᵢ the peer's upload rate.

- Client–server lower bound: Dcs ≥ max(NF/uₛ, F/min(dᵢ)).
- P2P lower bound: Dp2p ≥ max(F/uₛ, F/min(dᵢ), NF/(uₛ+Σuᵢ)).

BitTorrent is described through splitting files into chunks, chunk exchange and the tit-for-tat approach. A DHT distributes key–value mappings among peers. In the ring example, key 13 is held by peer 14, and key 15 by peer 1. Shortcut links speed up lookup. Successor information is used to take over for peers that leave.

*Note: Key placement with a hash function in a DHT does not by itself provide encryption or privacy.*

![P2P distribution and DHT — handwritten, page 19](belge-105-sayfa-19.jpg "P2P distribution and DHT — handwritten, page 19")

![P2P distribution and DHT — handwritten, page 20](belge-105-sayfa-20.jpg "P2P distribution and DHT — handwritten, page 20")

![P2P distribution and DHT — handwritten, page 21](belge-105-sayfa-21.jpg "P2P distribution and DHT — handwritten, page 21")

![P2P distribution and DHT — handwritten, page 22](belge-105-sayfa-22.jpg "P2P distribution and DHT — handwritten, page 22")

## Sockets, multiplexing and reliable transfer

A TCP socket is based on a connection, a UDP socket on datagrams. Multiplexing and demultiplexing connect application processes to the transport layer. TCP connections are distinguished by the four-tuple of source IP, source port, destination IP and destination port. On the receiving side, UDP delivers to the application using destination address/port information.

The checksum is computed with one's complement addition. rdt1.0 handles a perfectly reliable channel; rdt2.x handles bit errors, ACK/NAK and sequence numbers; rdt3.0 handles loss and timeout. Duplicate packet and corrupted ACK problems are drawn separately.

![Sockets, multiplexing and reliable transfer — handwritten, page 23](belge-105-sayfa-23.jpg "Sockets, multiplexing and reliable transfer — handwritten, page 23")

![Sockets, multiplexing and reliable transfer — handwritten, page 24](belge-105-sayfa-24.jpg "Sockets, multiplexing and reliable transfer — handwritten, page 24")

![Sockets, multiplexing and reliable transfer — handwritten, page 25](belge-105-sayfa-25.jpg "Sockets, multiplexing and reliable transfer — handwritten, page 25")

![Sockets, multiplexing and reliable transfer — handwritten, page 26](belge-105-sayfa-26.jpg "Sockets, multiplexing and reliable transfer — handwritten, page 26")

![Sockets, multiplexing and reliable transfer — handwritten, page 27](belge-105-sayfa-27.jpg "Sockets, multiplexing and reliable transfer — handwritten, page 27")

![Sockets, multiplexing and reliable transfer — handwritten, page 28](belge-105-sayfa-28.jpg "Sockets, multiplexing and reliable transfer — handwritten, page 28")

![Sockets, multiplexing and reliable transfer — handwritten, page 29](belge-105-sayfa-29.jpg "Sockets, multiplexing and reliable transfer — handwritten, page 29")

![Sockets, multiplexing and reliable transfer — handwritten, page 30](belge-105-sayfa-30.jpg "Sockets, multiplexing and reliable transfer — handwritten, page 30")

## Congestion control

The NI, CI and ER fields are noted for ATM ABR. The TCP sending rate is approximately cwnd/RTT. During slow start, the window roughly doubles every RTT; during congestion avoidance, it increases by about 1 MSS per RTT.

For MSS = 500 bytes and RTT = 200 ms, one MSS/RTT = 2500 bytes/s = 20 kbit/s. After a loss, the threshold is usually set to half of the previous window. The reactions to a timeout and to three duplicate ACKs are compared.

*Note: The Reno explanation in the notes gives the impression that the window does not drop to 1 MSS after a timeout; in classic Reno, a timeout and three duplicate ACKs are different cases, and after a timeout the window returns to its initial value.*

![Congestion control — handwritten, page 32](belge-105-sayfa-32.jpg "Congestion control — handwritten, page 32")

![Congestion control — handwritten, page 33](belge-105-sayfa-33.jpg "Congestion control — handwritten, page 33")

![Congestion control — handwritten, page 34](belge-105-sayfa-34.jpg "Congestion control — handwritten, page 34")

![Congestion control — handwritten, page 35](belge-105-sayfa-35.jpg "Congestion control — handwritten, page 35")

![Congestion control — handwritten, page 36](belge-105-sayfa-36.jpg "Congestion control — handwritten, page 36")

## Routing and autonomous systems

In distance vector routing, good news can propagate quickly and bad news slowly; the count-to-infinity problem is described. Intra-AS and inter-AS routing are distinguished. RIP uses hop count and is limited to 15 hops; OSPF uses link state and the Dijkstra approach.

For BGP, AS-PATH and NEXT-HOP, local preference, path length and hot-potato routing are noted. Broadcast with a spanning tree, and multicast with RPF, DVMRP, IGMP and PIM dense/sparse mode are compared.

![Routing and autonomous systems — handwritten, page 38](belge-105-sayfa-38.jpg "Routing and autonomous systems — handwritten, page 38")

![Routing and autonomous systems — handwritten, page 39](belge-105-sayfa-39.jpg "Routing and autonomous systems — handwritten, page 39")

![Routing and autonomous systems — handwritten, page 40](belge-105-sayfa-40.jpg "Routing and autonomous systems — handwritten, page 40")

![Routing and autonomous systems — handwritten, page 41](belge-105-sayfa-41.jpg "Routing and autonomous systems — handwritten, page 41")

![Routing and autonomous systems — handwritten, page 42](belge-105-sayfa-42.jpg "Routing and autonomous systems — handwritten, page 42")

![Routing and autonomous systems — handwritten, page 43](belge-105-sayfa-43.jpg "Routing and autonomous systems — handwritten, page 43")

## Link layer and error control

The link layer is concerned with framing, medium access, error control and local delivery. An Ethernet MAC address is 48 bits. Examples of parity, two-dimensional parity and CRC are drawn. In CRC, r zeros are appended to the data D; the remainder of the modulo-2 division by the generator G is R. The transmitted D·2ʳ XOR R is divisible by G with no remainder.

The web access example shows configuration with DHCP, finding the local neighbor with ARP, name resolution with DNS and the object request with HTTP together.

![Link layer and error control — handwritten, page 44](belge-105-sayfa-44.jpg "Link layer and error control — handwritten, page 44")

![Link layer and error control — handwritten, page 45](belge-105-sayfa-45.jpg "Link layer and error control — handwritten, page 45")

![Link layer and error control — handwritten, page 46](belge-105-sayfa-46.jpg "Link layer and error control — handwritten, page 46")

![Link layer and error control — handwritten, page 48](belge-105-sayfa-48.jpg "Link layer and error control — handwritten, page 48")

## ATM, MPLS, switches and VLANs

The short list on exam scope includes ARP, error control, protocols and network access. ATM, MPLS and virtual connection concepts are compared. MPLS uses label-based forwarding.

Hubs, bridges and switches are distinguished. A switch learns from the source MAC address which port reaches which device; it floods an unknown destination out of the appropriate ports. A VLAN provides logical network separation on the same physical switching infrastructure.

![ATM, MPLS, switches and VLANs — handwritten, page 49](belge-105-sayfa-49.jpg "ATM, MPLS, switches and VLANs — handwritten, page 49")

![ATM, MPLS, switches and VLANs — handwritten, page 50](belge-105-sayfa-50.jpg "ATM, MPLS, switches and VLANs — handwritten, page 50")

![ATM, MPLS, switches and VLANs — handwritten, page 51](belge-105-sayfa-51.jpg "ATM, MPLS, switches and VLANs — handwritten, page 51")

![ATM, MPLS, switches and VLANs — handwritten, page 52](belge-105-sayfa-52.jpg "ATM, MPLS, switches and VLANs — handwritten, page 52")

![ATM, MPLS, switches and VLANs — handwritten, page 53](belge-105-sayfa-53.jpg "ATM, MPLS, switches and VLANs — handwritten, page 53")

*Note: The cover and blank pages were not included among the text images; their order is preserved within the 53-page PDF. The source has no day information; the date is the file's last-modified record.*
