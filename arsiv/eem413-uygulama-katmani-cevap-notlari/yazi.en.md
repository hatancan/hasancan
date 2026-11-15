---
baslik: EEM413 Computer Networks: Short-Answer Notes for the Application Layer
ozet: Short-Answer Notes for the Application Layer. Questions, explanations, and documents from the course archive.
---

These are short-answer notes prepared by a classmate in the course folder; personal information has been removed. They cover application architecture, HTTP, e-mail, and P2P topics. PDF copies of the documents can be downloaded at the end of the post.

## network-1

**2.** Computer network architecture divides the organization of communication into layers. Application architecture, on the other hand, is designed by an application developer and determines how the application will be structured.

**3.** Messaging first connects to a common server to determine the recipient's IP address. Then the message is sent directly between the recipient and the sender.

**6.** The recipient's IP address and the port number of the receiving socket.

before sending, it uses it if it changes the control packets. SMTP, on the other hand, is where HTTP is not present

**12.** In non-pipelined HTTP, the web browser first waits to receive an HTTP response from the server before issuing a new HTTP request. In pipelined HTTP, the web browser issues HTTP requests as needed, without waiting for a response from the server.

transfers to the LAN to which the server is connected. It also avoids delay for all objects and reduces the traffic on the links.

**16.** The message is sent from Alice's host to her mail server over HTTP. Alice's mail server sends the message to Bob's mail server using SMTP. Then Bob transfers the message from his own mail server to his host using POP3.

**20.** The network in a P2P file-sharing system consists of the nodes in the file-sharing system and the logical connections between these nodes. When Node A sends data directed to the IP address of Node B, a direct logical connection address is created from Node A to Node B. There is no router. When any node wants to join Gnutella, it first finds the IP addresses of other nodes that are already connected, and then sends a join message to these nodes. When the node receives confirmation, it becomes a member of the Gnutella network. Nodes determine their own logical connections through periodic refresh messages.

**21.** Kazaa, eDonkey, BitTorrent

*Note: The spelling "STMP" in the text should be understood as SMTP. These are student answers; the missing question numbers are also absent in the source.*
