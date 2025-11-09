import pyqrcode
from PIL import Image

phone_number = "254714983736"
link = f"https://wa.me/{phone_number}"

qr_code = pyqrcode.create(link)
qr_code.png("WhatsAppQR.png", scale=18)

Image.open("WhatsAppQR.png").show()
