# HackLaw

## What applications does computer science have in the field of law?

Most applications of computer science within law fall under forensics. In an increasingly digital world, we have so much information at our fingertips; even in well concealed crimes. One of the greatest advantages of computer science is how easy it is to iterate the same process. This makes it incredibly useful for investigating large amounts of data/evidence.

Please keep in mind that this presentation was primarily produced by HackMelbourne, a more computer science oriented club and may miss some of the more law focused ideas.

### Metadata analysis

Every time you take a picture, screenshot, video or even save a file to your computer; metadata is being stored. This ranges from something as simple as what the file contains, to your exact longditude, latitude and phone used for taking a photo. 

This can occasionally be useful for evidence in cases involving CSAM, family law and IP law. For cases where there is a large amount of photo evidence, it can be useful to programmatically analyse times, locations and devices that pictures may have been taken on. 

With a bit more math and programming, it's almost magical how well we can hone in on or rule out a suspect. In 2012, an individual posted an image on anonymous message board 4chan, attached was a picture of someone standing in plastic tubs filled with lettuce, captioned "This is the lettuce you eat at Burger King".  Within 15 minutes, 4chan users were able to identify the location of this image to the exact Burger King restaurant in Mayfield Heights, Ohio. This was done using EXIF data.

It's important to note that it is also trivially easy to modify the metadata of a file with a little bit of programming knowledge. 

### Using OCR to prepare documents
 
Let's say you've somehow stumbled upon a set of documents that you don't have access to a digital copy of. How in the world are you supposed to search for something in them!??! Sure, you can try to read the whole thing, but across 100s of documents? No way. This is where Optical Character Recognition (OCR) comes in. We basically use OCR to convert images into text. While this seems simple enough to do with something like Adobe Scan, it becomes pretty tedious when you're working with thousands of pages.

We can automate this process using the docling python package. 

### Using regex to fuzzy-match text

Regex is short for "regular expression", which is basically just a well structured way to define some characteristics of text.

Using regex, we can search for (not quite) exact matches of text strings. This is useful to account for things like typos, rearranged wordings or finding well formatted information. For example, how would you go about finding all email addresses across 100s of documents? It would be a pain to go through and ctrl-f "@". It would also give us false positives and take an incredibly long time to copy each address into whatever document we have.

We can simply use an email regex to find all emails in a document.

### Blockchain analysis for money laundering

The nature of blockchain technology and cryptocurrencies make them a prime money laundry for criminals. Because of the decentralized, P2P nature of blockchains, they're very frequently used as payment or escrow for illegal goods and services. In Australia, the most prominent example of this is in <a href = "https://www.trmlabs.com/resources/case-studies/australias-first-major-crypto-laundering-conviction-inside-operation-taipan"> Operation Taipan</a>. 

One of the most famous criminal cases involving cryptocurrencies was the case of Ross Ulbricht in 2013. Ulbricht ran a website on the dark web called "Silk Road", which specialised in selling illicit substances and services.

He has multiple wallet addresses that can be searched and connected to various criminal syndicates, Silk Road merchants and other sketchy individuals using python libraries like bit and bitcoinlib.

We've written some very basic code that can fetch wallet transactions and identify the tranactors in any bitcoin transaction. In theory, this is a VERY VERY VERY rudimentary version of the technology a lab like TRM would use to identify fraudulent transactions.
