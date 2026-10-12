import qrcode  

url = input("Enter the URL: ").strip()
file_path = "/Users/sahmadnakumbe/GitHub/VSCode/Python/QRcode/QRcode2/QRcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code was generated!")
