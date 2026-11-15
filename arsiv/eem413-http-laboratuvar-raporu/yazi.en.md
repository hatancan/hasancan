---
baslik: EEM413 Computer Networks: HTTP Lab Report
ozet: HTTP Lab Report. Questions, explanations and documents from the course archive.
---

These are student lab reports from the course archive; student names, numbers and identity information have been removed. Where a document carries no date, the creation or last-modified date of the source file has been used. PDF copies of the documents prepared for the archive can be downloaded at the end of the post.

## HTTP report

Computer Networks Lab - 1

Report

**1.** Questions for http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html 1-) My browser uses HTTP 1.1. We can tell this from "HTTP/1.1" written next to the GET in the first URL line. From "request version: HTTP/ 1.1" on the server side, we can tell that the server also uses HTTP 1.1.

2-) As shown in the screenshot above, the language section reads:

Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.6,en;q=0.4\r\n

This shows us that both English and Turkish are accepted.

3-) 25 5.008299000 192.168.2.3 128.119.245.12 HTTP 458 GET /wireshark-labs/HTTP- wireshark-file1.html HTTP/1.1

Here, the IP address 192.168.2.3 belongs to my computer, while the IP address 128.119.245.12 belongs to the server.

4-) The status code sent is "HTTP/1.1 200 OK (text/html)".

5-) The last modification date is "Last-Modified: Sat, 02 Nov 2013 18:36:01 GMT\r\n", as stated here: 2 November 2013, 18:36.

6-) The content length is 128 bytes, as shown in the screenshot below.

7-) Although the headers are not visible in the packet list, every packet has a header, which becomes visible when you open the packet contents. For example, the highlighted part in the screenshot below shows the header.

**2.** Questions for http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html:

8-) No, I did not see an IF-MODIFIED-SINCE line.

9-) Yes, the server definitely returned the text content. We can tell this from the following structure inside the server's response. In the Line-based text data: text/html section of this tab, we see:

"Congratulations again! Now you've downloaded the file lab2-2.html. This file's last modification date will not change.

Thus if you download this multiple times on your browser, a complete copy will only be sent once by the server due to the inclusion of the IN-MODIFIED-SINCE field in your browser's HTTP GET request to the server."

This text appears there.

10-) The second GET contains an IF-MODIFIED-SINCE line, as shown in the screenshot below. According to the screenshot, it was last modified on 2 November 2013 at 19:29:01.

11-) The HTTP status after the second GET is 304, that is => Message: HTTP/1.1 304 Not Modified\r\n. Since there was no change in the information on the server, the content loaded by the first GET was served from the cache.

**3.** Answers to the questions for http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html:

12-) As seen in the screenshot, there is 1 GET message.

13-) Looking at the TCP tab, as in the screenshot below, 1452, 1452, 1452 and 447 bytes are used. TCP carries 4 data segments, and the total size, Content-Length, is 4500 bytes.

14-) The status code is 200, that is, OK.

15-) No, there is no other structure in HTTP or TCP that indicates any other status.

**4.** Answers to the questions for http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html:

16-) As seen in the screenshot below, there are 3 GET commands. There are 3 IP addresses they were sent to: 128.119.245.12, 165.193.140.14,

**128.** 119.240.90

17-) Looking at this structure, we see that two TCP connections were used for the two images, which shows that they were downloaded serially.

**5.** Answers to the questions for http://gaia.cs.umass.edu/wireshark-labs/protected_pages/HTTP-wireshark-file5.html:

18-) The first status code of the HTTP GET is 401, that is, "Authorization Required", as I indicate below.

19-) In the second GET, after the password is entered, the following line appears:

Authorization: Basic d2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms=\r\n

At the bottom of the lab questions, it is also stated that this encoding is not sent encrypted, and that for encrypted examples we should look at the "HTTP Access Authentication Framework" section.

![HTTP report: figures and calculation tables, page 1](belge-01-sekil-01.jpg "HTTP report, page 1")

![HTTP report: figures and calculation tables, page 2](belge-01-sekil-02.jpg "HTTP report, page 2")

![HTTP report: figures and calculation tables, page 4](belge-01-sekil-04.jpg "HTTP report, page 4")

![HTTP report: figures and calculation tables, page 6](belge-01-sekil-06.jpg "HTTP report, page 6")

*Note: An HTTP 304 response indicates that the requested object has not changed. It should not be confused with 404. The packet numbers in the report belong to this capture.*
