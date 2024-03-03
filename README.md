qrCodeGen.py uses vCard data to create a QR code (PNG & SVG) using python-qrcode and saves data to a vCard (VCF) file. Information on installing python qrcode can be found at https://github.com/lincolnloop/python-qrcode. Information regarding the vCard standard can be found at https://datatracker.ietf.org/doc/html/rfc6350. Examples of the BLANK output are included for a PNG, SVG, and vCard. 

This was written and originally run on Python 3.8.10 with qrcode 7.4.2

Photo & Logo

This functionality is commented out as it creates a very dense QR code which may not successfully scan well on older phones or in suboptimal lighting when printed on smaller items such as business cards. This will be less of a concern if you are printing on larger media. If you are getting error size 41 from python-qrcode it is because there is too much data in the QR code and it cannot fit the data with error correction. I was only able to get a logo or a photo to fit after resizing one down significantly.

Extra Fields

Not all contact managment apps will use the extra fields such as notes, catagories, secondary websites, etc that the vCard standard supports. It is best to rely on your primary contact info phone number, address, email.

