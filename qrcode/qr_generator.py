import qrcode

# Data to encode
data = "https://www.youtube.com/watch?v=IUQVO97zcE0"

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # Size of QR code (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in QR grid
    border=4,  # Border thickness
)
qr.add_data(data)
qr.make(fit=True)

# Create and save QR code image
img = qr.make_image(fill="black", back_color="white")
img.save("qrcode.png")

print("QR Code generated and saved as 'qrcode.png'")
