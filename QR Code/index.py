import qrcode
from PIL import Image

data = "https://www.instagram.com/mahmud_r_mmr/"

qr = qrcode.QRCode(version=1, box_size=10, border= 5)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill= "black", back_color="white")

image.save("qr_code_insta.png")
image.show("qr_code_insta.png")