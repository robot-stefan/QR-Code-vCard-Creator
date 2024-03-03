import qrcode
import qrcode.image.svg
from datetime import datetime
import base64
from platform import python_version
from importlib.metadata import version

## qrCodeGen.py
# Creates a QR code (PNG & SVG), and VCF from vcard text block.
# For ADR all fields are optional and can be left blank to list only city, state, country is would look like (ADR;TYPE=work:;;;CITY;STATE;;COUNTRY)
# Not all contacts apps will keep categories or notes fields
# Additional entries such as calendar links can also be added see RFC 6350 and the wikipedia article to declare a different version if needed. 

## Grab Logo / Photo and Convert to base64
## Note not used as logo / photo size needs to be small to fit in QR size limits with error checking.
## To enable logo / photo this sections would need to be uncommented and PHOTO or LOGO would need to be added to vcard data block. 
## Having a logo or photo could force a high density QR code which may be hard for some phones to read if placed on a business card.
# logo_path = "logo.png"
# logo_file = open(logo_path, 'rb').read()  
# logo_base64 = base64.b64encode(logo_file).decode("ascii")

## vCard Text Block
# PHOTO;ENCODING=BASE64;TYPE=PNG:{logo_base64}
# LOGO;ENCODING=BASE64;TYPE=PNG:{logo_base64}
vcard = f"""BEGIN:VCARD
VERSION:3.0
N:LastName;FirstName;;;
FN:FirstName LastName
ADR;TYPE=work:P.O. Box #;APT#_SUITE#;STREET_ADDRESS;CITY;STATE;ZIP;COUNTRY
TEL;TYPE="cell,text,work":+1-###-###-####
TZ:America/New_York
EMAIL;TYPE=work:firstname.lastname@mycorp.mycorp
ORG:MyCorp
URL;TYPE=work:https://www.mycorp.mycorp
URL;TYPE=home:https://maybelinkedin?
CATEGORIES:something,something2,something3
PRODID:qrCodeGen.py//Python_v{python_version()}//qrcode_v{version('qrcode')}
REV:{datetime.now()}
END:VCARD"""

## Create vCard QR
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data(vcard)
qr.make(fit=True)

## Export PNG of QR Code
img = qr.make_image(fill_color="black", back_color="white")
img.save("vCard_QR.png")

## Export SVG of QR Code
qr.image_factory = qrcode.image.svg.SvgPathImage
svg = qr.make_image()
svg.save("vCard_QR.svg")

## Write vCard Contents to a vcf
file = open("vCard.vcf", "w")
file.write(vcard)
file.close