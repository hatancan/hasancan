---
baslik: EEM413 Computer Networks: EEM342 Sample Midterm Exam (Fall 2002)
ozet: EEM342 Sample Midterm Exam (Fall 2002). Questions, notes and documents from the course archive.
---

This is a sample exam in English, stored in the EEM413 folder, with the heading "EEM342 Computer Networks (2002 fall)". The institution and the author are not stated in the document; there is no date, so the last-modified date of the source file was used for ordering in the archive. PDF copies of the documents can be downloaded at the end of the post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes, with the source credited. It will be removed upon the request of the rights holder.*

## Midterm-sample

Sample: Midterm 1 for EEM342 Computer Networks (2002 fall), 75 min.

PART-1: True/False questions. Explain why in one sentence (2 points each, 20 min).

___D___ When the Traffic Intensity approaches to 1, propagation delay will approach to infinity. ___D___ In the application layer protocols, client side and server side are fixed and are pre-defined. ______ In the UDP segment structure, if the checksum is wrong, the only action is to discard the packet. ___D___ DNS protocol uses only UDP segments because the it is not a critical network function. ______ HTTP / 1.1 protocol is stateless, in-band and can be both persistent and non- persistent. ______ In socket programming, the connection socket is also called the welcome socket. ______ Each router or switch can send feedback to the Sender side to perform the flow control in TCP protocol. ______ Both ATM and Internet protocols can perform end-end and network assisted congestion control.

P1 (4 points, 20 min). Consider a TCP sender and receiver with pipeline protocol. Assume that sender sequence number starts with 101 and receiver starts with 10. Also assume that sender’s window size is 10. Draw a sequence diagram that will show sender, receiver and the packets with sequence and acknowledge numbers and related header bits (when necessary) for the following scenarios: b) Sender sends 3 data segments and receives a cumulative ACK from receiver. c) Sender sends 2 more data segments while the second segment is not received by the receiver. Indicate clearly the response of the receiver and the sender until both segments will be received by the receiver successfully. d) Receiver initiates a TCP terminating process, proceed until the connection is closed in both sides. Explain briefly the difference between Go-back-N and Selective Repeat protocols.

P2 (5 points, 25 min). Consider a scenario in which host 1 wants to sent messages to hosts 2 and 3 at the same time. Host 1 is connected to hosts 2 and 3 such that when host 1 sends a packet, it is broadcasted towards both host 2 and 3. The packets sent can not be lost. Host 2 and host 3 can receive however, corrupted packets independently. When any of them receives a corrupted packet, It sends back a NACK packet. In this case, host 1 broadcasts the same packet again. If host 2 or 3 receives a packet that has been already received correctly before, it discards the packet. If host 1 will not receive a NACK packet in a certain time T (T>>RTT), It sends the next packet. Design a stop-and-wait with error correction protocol to handle the scenario. Show the FSM descriptions for host 1 and host 2 (host 3 will have the same FSM as host 2) Note that there is no positive acknowledgment packet, and if hosts 2 or 3 sends a NACK packet, it always arrives correctly to host 1 in less than T/2 time.

*Note: The D marks in the true/false fields are markings from the source; they should not be treated as a verified answer key.*
