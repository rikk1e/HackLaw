# HackLaw

## What applications does computer science have in the field of law?

Most applications of computer science within law fall under forensics. In an increasingly digital world, we have so much information at our fingertips; even in well concealed crimes.

Please keep in mind that this presentation was primarily produced by HackMelbourne, a more computer science oriented club and may miss some of the more law focused ideas.


### Blockchain analysis for money laundering

The nature of blockchain technology and cryptocurrencies make them a prime money laundry for criminals. Because of the decentralized, P2P nature of blockchains, they're very frequently used as payment or escrow for illegal goods and services. In Australia, the most prominent example of this is in <a href = "https://www.trmlabs.com/resources/case-studies/australias-first-major-crypto-laundering-conviction-inside-operation-taipan"> Operation Taipan</a>. However, as the wallet addresses have not been made easily publicly accessibly, it is not suitable for today's demo.

One of the most famous criminal cases involving cryptocurrencies was the case of Ross Ulbricht in 2013. Ulbricht ran a website on the dark web called "Silk Road", which specialised in selling illicit substances and services.

We will be doing a brief demo exploring his web of crime.

### Metadata analysis

Every time you take a picture, screenshot, video or even save a file to your computer; metadata is being stored. This ranges from something as simple as what the file contains, to your exact longditude, latitude and phone used for taking a photo. 

This can occasionally be useful for evidence in cases involving CSAM, family law and IP law. For cases where there is a large amount of photo evidence, it can be useful to programmatically analyse times, locations and devices that pictures may have been taken on.

With a bit more math and programming, it's almost magical how well we can hone in on or rule out a suspect. 

It's important to note that it is also trivially easy to modify the metadata of a file with a little bit of programming knowledge. 

### Using OCR to prepare documents
 
Let's say you've somehow stumbled upon a set of documents that you don't have access to a digital copy of. How in the world are you supposed to search for something in them!??! Sure, you can try to read the whole thing, but across 100s of documents? No way. This is where Optical Character Recognition (OCR) comes in. We basically use OCR to convert images into text. While this seems simple enough to do with something like Adobe Scan, it becomes pretty tedious when you're working with thousands of pages.

We can automate this process using the EasyOCR python package. 

### Using regex to fuzzy-match text
