import qrcode

qr_img = qrcode.make("Hello World. I am Suraj Sahu")

qr_img.save("qr-img.jpg")
