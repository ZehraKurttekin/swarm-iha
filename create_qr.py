import qrcode
import json

with open("qr_gorev1.json") as f:
    data = json.load(f)

qr_text = json.dumps(data)

img = qrcode.make(qr_text)

img.save("qr_gorev1.png")

print("QR oluşturuldu")