---
baslik: EEM438 Data Communications: Network Models: OSI, TCP/IP and Addressing (Gazi University, Suat Özdemir)
ozet: Data Communications lecture slides by Suat Özdemir of Gazi University: the OSI and TCP/IP layered models, the functions of each layer, and physical, logical, port and specific addressing.
---

These are the Chapter 2 (Network Models) slides that Suat Özdemir of the Department of Computer Engineering at Gazi University prepared for the "Veri İletişimi / Data Communications" course (slide date: March 4, 2011; the footer reads BM 403 Data Communications). They are kept in the EEM438 folder as course material from a second instructor. The slide text is transcribed below; figures and tables taken from the textbook are not published, and slides without text are noted. The original PDF can be downloaded at the end of the post.

Scope: the OSI and TCP/IP layered models, the functions of each layer, and physical, logical, port and specific addressing.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution. It will be removed at the request of the rights holder.*

## Network Models

- A network is the totality of hardware and software that carries data from one point to another.
- Hardware consists of physical elements, and software consists of sets of instructions.
- The transmission of data from one point to another can be divided into many tasks.
- Each task can be represented as a layer. Example: sending a letter by mail.
- In computer networks, the OSI (Open Systems Interconnection) model was widely used until 1990.

## Network models

- Sending mail in the traditional way.

## OSI model

- An open system is a set of protocols that allows two systems to communicate regardless of their underlying architectures.
- OSI is not a protocol! OSI is a model used to design and understand a network architecture.
- OSI consists of 7 separate but related layers.
- Each layer performs certain processes assigned to it for communication.

## OSI model (2)

- When data travels between A and B, it may pass through many intermediate nodes.
- Each layer receives services from the layer below it and provides services to the layer above it.
- Between devices, layers at the same level communicate with each other (peer-to-peer process).
- Each layer adds its own information to the packet and passes it to the layer below. At each layer, the receiver removes that layer's information and passes the rest up to the next layer.
- There are interfaces between adjacent layers.
- Interfaces provide modularity.

## Interaction between OSI layers

*This slide contains only a figure/table; the image is in the original PDF.*


## OSI model layers

- The layers are grouped into 3 sets. The network support layers (physical, data link and network), the user support layers (session, presentation and application), and the transport layer, which links the two groups.
- The upper layers are implemented almost entirely in software, while the lower layers are generally implemented in software and hardware. The physical layer is mostly implemented in hardware.
- At each layer, a header and/or trailer is added to the data. The trailer is added at the data link layer.
- Each layer treats the entire unit from the layer above (header, trailer, data) as data. (Encapsulation)

## OSI model layers (2)

*This slide contains only a figure/table; the image is in the original PDF.*


## OSI model - Physical layer

- Performs the processes necessary to carry bits over the physical medium.
- Defines the mechanical and electrical characteristics of the interface and the transmission medium.
- Defines the representation of bits, i.e. how bits are encoded as signals.
- Defines the data rate (bps).
- Provides bit-level synchronization between the receiver and the sender.
- Defines the point-to-point or multipoint line configuration.
- Defines the topology (mesh, star, bus, ring).
- Defines the transmission mode (simplex, half-duplex, full-duplex).

## OSI model - Data link layer

- Turns the simple data transmission of the physical layer into a reliable link.
- Divides the bits received from the network layer into frames.
- Performs physical addressing. Adds a header (receiver and sender addresses) and a trailer (error control information) to the frames.
- Performs flow control on a per-frame basis.
- Performs error control. Lost and corrupted frames are retransmitted.
- Performs access control. Runs a protocol that governs how devices sharing a single link gain access to it.

## OSI model - Data link layer (2)

- Performs hop-to-hop (node-to-node) delivery.
- The figure shows data being sent between A and F.

## OSI model – Network layer

- Responsible for source-to-destination delivery of packets across multiple networks.
- While the data link layer delivers data between two nodes on the same network, the network layer delivers data between two networks.

## OSI model - Network layer

- Performs logical addressing. The logical addresses of the receiver and sender are added to the packet.
- Performs routing. Routes packets as they pass through different networks.

## OSI model - Transport layer

- Responsible for process-to-process delivery of the entire message. A process is an application program.
- The network layer does not establish a relationship among the packets it sends. The transport layer handles the entire message. It sequences packets and performs error control and flow control.

## OSI model - Transport layer (2)

- Performs service-point addressing. Addresses each application (port).
- Performs segmentation and reassembly. The message is divided into transmittable segments, and each is given a sequence number.
- Provides connection-oriented (TCP) and connectionless (UDP) communication.
- Performs end-to-end flow control for the entire message, whereas the data link layer does so for a single link.
- Performs process-to-process error control for the entire message.

## OSI model - Session layer

- Acts as a dialog controller.
- Allows a process to add checkpoints to the data (synchronization). When an error occurs, retransmission restarts from the last correctly delivered checkpoint.
- Allows two systems to hold a half-duplex or full-duplex dialog.
  - Example: sending a 1000-page document?

## OSI model - Presentation layer

- Defines the syntax and semantics of the data exchanged between two systems.
- Translation. Because different computers use different encoding techniques, the sending computer converts the information into a common format
  - char string → bit stream
- Encryption. Encrypts information to ensure its confidentiality and security.
- Compression. Data is represented with fewer bits to reduce network traffic.

## OSI model - Application layer

- Provides user interfaces for e-mail, remote access, file transfer, database management and distributed applications.
- Provides services such as the X.400 message handling (e-mail) service, the X.500 directory service, and the FTAM (file transfer and management) service.

## TCP/IP Protocol Architecture

- TCP/IP is the result of protocol research and development carried out on ARPANET; it is referred to as the "TCP/IP protocol suite" and consists of many protocols that are Internet standards.
- Because it was developed before the OSI model, its layers are different.
- The original TCP/IP has 4 layers (host-to-network, internet, transport and application of the TCP/IP protocol suite).
- The host-to-network layer is equivalent to the combination of the physical and data link layers in OSI.
- The internet layer is equivalent to the network layer in OSI.
- The application layer is equivalent to the session, presentation and application layers in OSI.
- As a result, TCP/IP is today described as having 5 layers: physical, data link, network, transport and application.

## TCP/IP protocol

*This slide contains only a figure/table; the image is in the original PDF.*


## TCP/IP protocol (2)

- The physical and data link layers do not support any specific protocol.
- The network layer supports IP (Internetworking Protocol). IP performs routing of datagrams and best-effort delivery (it does not perform error control).
- ARP (Address Resolution Protocol). Associates a logical address with a physical address.
- RARP (Reverse Address Resolution Protocol). Assigns an Internet address to a host that knows only its physical address. (Diskless computer)
- ICMP (Internet Control Message Protocol). Used to notify the sender of problems with datagrams.

## TCP/IP protocol (3)

- IGMP (Internet Group Message Protocol). Used to send a message to a group simultaneously.
- The transport layer supports UDP and TCP. UDP (User Datagram Protocol). Adds only the port address, error-check bits and the length of the data to the packet. Works connectionless. (ping)
- TCP (Transmission Control Protocol). Is reliable and works connection-oriented. Divides the data into segments, sequences them, and checks the sequence.
- SCTP (Stream Control Transmission Protocol). Supports new Internet applications (VoIP). It is a combination of UDP and TCP.

## Addressing

- The TCP/IP protocol suite uses 4 levels of addressing: physical, logical, port and specific.

## Addressing - Physical addressing

- Located within the frame at the data link layer. Its length differs depending on the network type. (6-byte NIC address for Ethernet, 1 byte for Apple LocalTalk)

## Addressing - Logical addressing

- The address information is located within the packet at the network layer.
- It is 32 bits long for the Internet (IPv4).
- IPv6 uses 128-bit addressing.

## Addressing - Logical addressing (2)

*This slide contains only a figure/table; the image is in the original PDF.*


## Addressing - Port addressing

- The IP address and the physical address are sufficient for source-to-destination communication between computers.
- However, today computers can run multiple programs at the same time.
- In TCP/IP, a port address is assigned to each application and is 16 bits long (0-65535).
- The physical address changes hop-to-hop, while the logical address and port address remain constant.

## Addressing - Port addressing (2)

*This slide contains only a figure/table; the image is in the original PDF.*


## Addressing - Specific addressing

- Some applications provide user-friendly addresses. (forouzan@fhda.edu, www.mhhe.com)
- Specific addresses are converted into port addresses and logical addresses.
