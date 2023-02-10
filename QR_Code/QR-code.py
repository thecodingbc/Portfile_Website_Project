import qrcode
img = qrcode.make("https://coderbc.pythonanywhere.com/")
img.save("bcprofileQR.jpg")
