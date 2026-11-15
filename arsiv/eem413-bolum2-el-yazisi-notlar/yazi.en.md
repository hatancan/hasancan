---
baslik: EEM413 Computer Networks: Chapter 2: Application Layer and HTTP
ozet: Chapter 2: Application Layer and HTTP. Questions, explanations, and documents from the course archive.
---


## Application architectures

Client–server and P2P architectures, communication between processes, IP address and port, and the socket as the interface between the application and transport layers are explained.

![Application architectures — handwritten, page 1](belge-113-sayfa-01.jpg "Application architectures — handwritten, page 1")

## Transport requirements of an application

Data integrity, timing, throughput, and security requirements are treated separately. File transfer is loss-sensitive, while real-time audio is delay-sensitive.

![Transport requirements of an application — handwritten, page 1](belge-114-sayfa-01.jpg "Transport requirements of an application — handwritten, page 1")

## TCP and UDP services

TCP is connection-oriented, reliable, and provides flow and congestion control. UDP is connectionless. Neither of them, by itself, guarantees a minimum transmission rate or a strict delay bound.

![TCP and UDP services — handwritten, page 1](belge-115-sayfa-01.jpg "TCP and UDP services — handwritten, page 1")

## HTTP connections

HTTP works with request and response messages. In a non-persistent connection, a connection is set up for each object. In a simple calculation, the response time is 2 RTT + object transmission time; a persistent connection reduces repeated setup.

![HTTP connections — handwritten, page 1](belge-116-sayfa-01.jpg "HTTP connections — handwritten, page 1")

## HTTP messages and status codes

The request line contains the method, path, and version. The Host, User-Agent, Connection, and Accept-Language headers are given as examples. The response carries a status code and a phrase; 200 (success), 301 (redirect), 400 (bad request), and 404 (resource not found) are examples.

![HTTP messages and status codes — handwritten, page 1](belge-117-sayfa-01.jpg "HTTP messages and status codes — handwritten, page 1")
