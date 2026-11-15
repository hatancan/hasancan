---
baslik: EEM438 Data Communications: Network Security: SSL, IPsec, and Firewalls
ozet: Network Security: SSL, IPsec, and Firewalls. Questions, explanations, and documents from the course archive.
---


## Components of security and encryption

Confidentiality, authentication, message integrity, and availability are separate goals. Eavesdropping, impersonation, and denial-of-service threats are listed. The plaintext m, the encryption key Kₐ, and the decryption key Kᵦ are related by m = Kᵦ(Kₐ(m)). Examples of monoalphabetic and polyalphabetic substitution are explained.

![Components of security and encryption — handwritten, page 1](belge-299-sayfa-01.jpg "Components of security and encryption — handwritten, page 1")

![Components of security and encryption — handwritten, page 2](belge-299-sayfa-02.jpg "Components of security and encryption — handwritten, page 2")

![Components of security and encryption — handwritten, page 3](belge-299-sayfa-03.jpg "Components of security and encryption — handwritten, page 3")

![Components of security and encryption — handwritten, page 4](belge-299-sayfa-04.jpg "Components of security and encryption — handwritten, page 4")

## SSL handshake and record layer

For SSL, the handshake, certificate, key generation, data transfer, and closure phases are written out. Separate encryption and MAC keys can be used for the two directions. The record scheme shows the length, data, and MAC fields. The sequence number is included in the MAC computation to protect against reordering and replay attacks. The pre-master secret and nonces are mentioned as inputs to key derivation.

![SSL handshake and record layer — handwritten, page 5](belge-299-sayfa-05.jpg "SSL handshake and record layer — handwritten, page 5")

![SSL handshake and record layer — handwritten, page 6](belge-299-sayfa-06.jpg "SSL handshake and record layer — handwritten, page 6")

![SSL handshake and record layer — handwritten, page 7](belge-299-sayfa-07.jpg "SSL handshake and record layer — handwritten, page 7")

## VPN, IPsec, and security associations

VPNs are described as a way to protect traffic between organizations. Transport and tunnel modes are covered, and AH and ESP are compared. AH does not provide confidentiality; ESP is associated with encryption and authentication services. An SA is unidirectional; two associations are needed for bidirectional traffic. The SPI, endpoint addresses, algorithms, and keys are kept in the SA context. The SAD defines the existing associations, and the SPD defines the policy to be applied.

![VPN, IPsec, and security associations — handwritten, page 8](belge-299-sayfa-08.jpg "VPN, IPsec, and security associations — handwritten, page 8")

![VPN, IPsec, and security associations — handwritten, page 9](belge-299-sayfa-09.jpg "VPN, IPsec, and security associations — handwritten, page 9")

![VPN, IPsec, and security associations — handwritten, page 10](belge-299-sayfa-10.jpg "VPN, IPsec, and security associations — handwritten, page 10")

![VPN, IPsec, and security associations — handwritten, page 11](belge-299-sayfa-11.jpg "VPN, IPsec, and security associations — handwritten, page 11")

![VPN, IPsec, and security associations — handwritten, page 12](belge-299-sayfa-12.jpg "VPN, IPsec, and security associations — handwritten, page 12")

## Wireless security and access control

WEP is explained with an example of stream encryption using a shared key and an IV. IV repetition causes weakness. The relationships among the authentication server, AP, client, master key, and PMK are drawn. The concepts of EAP, EAPOL, and RADIUS are included.

A firewall filters packets by address, port, and protocol. A stateless filter keeps no state; a stateful filter tracks the connection state. An application gateway mediates application-level communication. An IDS looks for signs of intrusion by examining packet contents and traffic patterns.

![Wireless security and access control — handwritten, page 13](belge-299-sayfa-13.jpg "Wireless security and access control — handwritten, page 13")

![Wireless security and access control — handwritten, page 14](belge-299-sayfa-14.jpg "Wireless security and access control — handwritten, page 14")

![Wireless security and access control — handwritten, page 15](belge-299-sayfa-15.jpg "Wireless security and access control — handwritten, page 15")

![Wireless security and access control — handwritten, page 16](belge-299-sayfa-16.jpg "Wireless security and access control — handwritten, page 16")

![Wireless security and access control — handwritten, page 17](belge-299-sayfa-17.jpg "Wireless security and access control — handwritten, page 17")

![Wireless security and access control — handwritten, page 18](belge-299-sayfa-18.jpg "Wireless security and access control — handwritten, page 18")

*Note: The SSL and WEP explanations are historical course content. An IDS aims to detect attacks; it should not be inferred that every IDS blocks traffic directly. The missing handshake items in the source were not presented as if they were completed.*
