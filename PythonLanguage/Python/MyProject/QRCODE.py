import qrcode as qr

data = "Google.com"
img = qr.make(data)
img.save("qrcode.png")