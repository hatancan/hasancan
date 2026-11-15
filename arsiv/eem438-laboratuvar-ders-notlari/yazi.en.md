---
baslik: EEM438 Data Communications: DHCP, ICMP and IP Lab Course Notes
ozet: Short class notes on DHCP messages, ICMP fields, and IP fragmentation, with explanations of errors in the source.
---

These are brief anonymous notes taken during class. The source file is dated April 30, 2015; a UTF-8 copy of the text can be downloaded at the end of the post. Missing questions and answers are noted as such and preserved.

## DHCP

1. UDP is used.
2. Ports 67–68.
3. Identification by MAC in the first step: what is the host's MAC address?
4. The Discover and Request messages have different types.
5. Is the Transaction ID the same in the first group of four messages? Does it change when moving to another group? The note states that it is the same within the same group and different in another group.
6. Which address information is used between the host and the server in the first four messages?
7. Source IP address: 10.0.15.1.
8. The "your IP address / client IP address" field inside the Bootstrap message.
9. Subnets and relay agent: if the note contains relay information, it states that the address was obtained from a different subnet.
10. It shows which subnet mask the client will use.
11. Option 50: Requested IP Address; "it is the same."
12. Option 51: IP Address Lease Time, 10 days; the "why?" question is unanswered.
13. The DHCP server does not respond to the Release message; the note is written this way.
14. It is requested to clear the filter and examine the remaining packets; the explanation is incomplete.

*Note: A DHCP relay can mediate a client's access to a DHCP server on another subnet; this does not necessarily mean that the address given to the client belongs to a different subnet. The spelling "Transaction IP" has been rendered as Transaction ID.*

## ICMP

Target: www.ust.hk. The note states that 10 requests and 10 replies were observed.

1. Showing the source and destination IP addresses.
2. The statement "Port information is assigned at layer 3" appears.
3. Type and code fields; a short, incomplete explanation about the two identifier representations.
4. Type = 0, code = 0; examining the other fields and how many bytes they are.
5. Showing the IP addresses again.
6. "The code should have been 17 (the reply)" is written.
7. Checking that the ping request and the echo/ping packet are the same.
8. Examining the two reply messages.
9. Left blank.
10. The times in the command window are compared; possible explanations related to distance or loss are noted for why the time increases at one hop.

*Note: ICMP does not use TCP/UDP ports; it has type and code fields. In the IPv4 Protocol field, ICMP = 1 and UDP = 17. The layer/port statement and the value 17 in the notes are therefore erroneous or lack context. The two representations of the Identifier field are related to endianness; they are not explained by the direction of a written language.*

## IP and fragmentation

It is requested to examine the target gaia.cs.umass.edu using PingPlotter.

- Question 3: IP header length 20 bytes, total 56 bytes; the remaining 36 bytes.
- Question 4: The Flags and More Fragments fields are examined for fragmentation information. The source states "it would have been 1 if it had been fragmented."
- Packets are sorted by source address.

*Note: The payload calculation 56−20=36 bytes is correct. More Fragments = 0 alone does not prove that the packet was never fragmented; it is also 0 in the last fragment. It should be evaluated together with Fragment Offset.*
