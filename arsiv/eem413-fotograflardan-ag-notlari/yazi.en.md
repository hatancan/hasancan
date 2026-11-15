---
baslik: EEM413 Computer Networks: Network and Transport Layer Notes from Photographs
ozet: Network and Transport Layer Notes from Photographs. Readable text transcribed from pages in the course archive.
---

Anonymous notes in the course archive were transcribed to text from photographed pages. The photographs are kept in a private archive; there is no download file in this post. Where a document carries no date, the date record of the source file was used.

## Network architecture and protocols

A protocol defines the format and order of messages in a communication, and the actions to be taken when messages are received. End systems are at the edge of the network; routers are in the network core. In the client–server architecture, an always-available server is contacted. In P2P, end nodes can both provide and receive resources; peers may join and leave the connection.

DSL also uses the telephone access line for data; the DSLAM performs aggregation on the service provider side. In cable/HFC access, the medium is shared. In FTTH, the OLT and ONT are the optical endpoints; PON denotes passive and AON denotes active distribution. For local access, Ethernet and Wi-Fi are given as examples, and cellular systems are given as examples of wide-area wireless access.

Physical media are listed as twisted pair, coaxial, fiber, and radio. In the core, circuit switching and packet switching are compared. Circuit switching reserves resources for a connection. FDM divides frequency, and TDM divides time, into slots. In packet switching, resources are shared on demand; queuing and packet loss may occur.

## Delay, traffic intensity, and throughput

- d_nodal = d_proc + d_queue + d_trans + d_prop.
- Transmission delay d_trans = L/R: L is the packet length, R is the link rate.
- Propagation delay d_prop = d/s: d is the distance, s is the propagation speed in the medium.
- Traffic intensity La/R: a is the average number of packets per second.
- The throughput of a path is limited by the bottleneck link; in the simple two-link example, min(Rₛ, R𝚌).

During processing, the header and bit errors are examined. Queuing delay varies with load. If the buffer is full, an incoming packet may be dropped. In store-and-forward, the router does not begin transmitting a packet onto the next link until it has received the entire packet. Transmission delay and propagation delay are not the same thing.

## Layers and security notes

Five layers: application, transport, network, link, and physical. The application message is encapsulated as a segment/datagram at the transport layer, as a datagram/packet at the network layer, and as a frame at the link layer. OSI additionally separates the presentation and session layers.

Under the security heading, viruses, worms, Trojan horses, spyware, botnets, DoS/DDoS, packet sniffing, and address spoofing are listed. These are the threat classes in the historical course notes.

## Application layer, sockets, and transport selection

Processes communicate through the socket interface. The IP address identifies the host, and the port number identifies the application endpoint. The application's tolerance for data loss, timing needs, throughput, and security requirements affect the choice of transport.

TCP provides reliable in-order transfer, flow control, and congestion control; it has connection setup. UDP transfers connectionless datagrams and gives no guarantee of delivery or ordering. If necessary, an application can build its own reliability mechanism on top of UDP. TCP and UDP alone do not provide a fixed delay or minimum bandwidth guarantee.

## HTTP and web caching

HTTP is a request/response model. In a non-persistent connection, a new TCP connection is opened for each object. The basic single-object calculation is 2 RTT + the file's transmission time. In a persistent connection, multiple requests use the same TCP connection; repeating connection setup is avoided.

The request line carries the method, the resource path, and the version. The Host, User-Agent, Connection, and Accept-Language headers are given as examples. GET requests an object; POST sends data; HEAD requests the response headers. PUT and DELETE are also listed in the source. The response contains the status code, version, headers, and body.

Cookies help establish a relationship with previous interactions. A proxy/web cache stores objects on behalf of the client; the load on the access link and the response time may decrease. A conditional GET is used to check whether the cached copy is up to date; if it is unchanged, the object body is not sent again.

## FTP, e-mail, and DNS

In FTP, the control and data connections are separate; this structure is given as an example of out-of-band control. The control port is 21. E-mail consists of the user agent, the mail server, and SMTP. SMTP is for sending between servers; POP3 and IMAP give the recipient access to the mailbox. A HTTP-based mail interface is a separate form of access from these operations.

The DNS hierarchy consists of root, top-level domain, and authoritative servers; the local DNS resolver carries out the queries. The difference between recursive and iterative queries is shown in the drawings. The DNS record format is noted as (name, value, type, TTL). A gives the address, NS gives the authoritative server, CNAME gives the alias, and MX gives the mail server.

## P2P file sharing

The centralized directory, query flooding, and distributed hash table (DHT) approaches are compared. A file can be split into chunks; peers upload the chunks they have downloaded to others. In the BitTorrent notes, there are chunk selection and tit-for-tat exchange.

Let F be the file size, N the number of receivers, uₛ the server's upload rate, d_min the download rate of the slowest receiver, and uᵢ the upload rate of peer i:

- Dcs ≥ max(NF/uₛ, F/d_min).
- Dp2p ≥ max(F/uₛ, F/d_min, NF/(uₛ+Σuᵢ)).

In a DHT, keys are distributed to peers in the identifier space. Ring and shortcut connections determine the lookup path; when a peer departs, the successor information is updated.

## Reliable transfer: rdt and windowing

rdt1.0 assumes an error-free channel. rdt2.0 uses a checksum and ACK/NAK against bit errors. Because ACK/NAK can also be corrupted, sequence numbers and duplicate packet detection are needed. rdt2.2 uses duplicate ACKs instead of NAK. rdt3.0 adds a timer and retransmission for loss.

A stop-and-wait sender sends a packet and waits for the acknowledgment. The utilization is approximately (L/R)/(RTT+L/R). In the example of 1 Gbit/s, an 8000-bit packet, and 30 ms RTT, L/R = 8 µs; the utilization is approximately 0.000267, i.e., 0.0267%. Pipelining allows multiple packets to be in flight.

Go-Back-N uses a cumulative ACK; after a loss/timeout, the outstanding packets starting from the relevant packet are retransmitted. Selective Repeat uses individual ACKs and a receiver buffer, and requests retransmission of only the missing packets. The sender and receiver windows must be chosen appropriately for the sequence number space.

## TCP: header, RTT, and retransmission

The TCP header contains the source/destination ports, sequence number, ACK number, window, checksum, and flags. The sequence number counts bytes; the ACK number indicates the next expected byte. SYN, SYN-ACK, and ACK make up connection setup. FIN is shown in the context of connection closing.

- EstimatedRTT = (1−α)EstimatedRTT + α SampleRTT.
- DevRTT = (1−β)DevRTT + β|SampleRTT−EstimatedRTT|.
- TimeoutInterval = EstimatedRTT + 4 DevRTT.

The timer helps detect loss. Three duplicate ACKs can trigger fast retransmit. The receive window represents flow control, and the congestion window represents the sending limit based on network congestion. These are different mechanisms. In the source, slow start, congestion avoidance, and window changes after loss are drawn.

## Inside the router and buffers

Input ports examine the header, use the forwarding table, and access the switching fabric. Switching via memory, via a shared bus, and via a crossbar are compared. Memory and the bus can become shared resources; a crossbar supports simultaneous different input–output paths.

At the output, packets are queued. The first packet at the input waiting can block packets behind it that could go to other outputs: head-of-line blocking. For buffer size, the expressions RTT×C and, for many independent TCP flows, approximately RTT×C/√N are noted. Here C is the link capacity and N is the number of flows.

## DHCP and NAT

The DHCP sequence is given as Discover → Offer → Request → ACK. The client receives not only the IP address but also configuration information such as the network mask, default gateway, and DNS server. Time-limited address use is explained by the concept of a lease.

NAT keeps a translation table between local address/port and external address/port. The source address and port of an outgoing packet, and the destination of a returning packet, are translated. Many local clients can go out with a small number of public addresses. For connections initiated from outside, static mapping, UPnP/IGD, and intermediary/relay methods are noted.

## ICMP and IPv6

ICMP carries network error and status messages; it is covered in the context of ping and traceroute. IPv6 addresses are 128 bits, and the base header is 40 bytes. The traffic class/priority, flow label, payload length, next header, and hop limit fields are listed. The header checksum in IPv4 is absent from the IPv6 base header; additional features are carried with extension headers. In the transition scheme, the IPv6 packet is tunneled inside IPv4.

*Note: This post merges repeated photographs. Personal marginal notes were not transcribed. In the formulas, bit/byte and second units were separated; the calculation example was rechecked. The descriptions of old protocols and devices are in the historical context of the course.*
