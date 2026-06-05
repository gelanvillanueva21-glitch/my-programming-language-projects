import qrcode

url = input("Enter URL: ").strip()
img = qrcode.make(url)
img.save("qrcode.png")
