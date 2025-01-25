# Install qrcode module if not installed
# pip install qrcode[pil]

import qrcode

qr_img = qrcode.make("Hello World. I am Suraj Sahu")

qr_img.save("qr_img.jpg")
