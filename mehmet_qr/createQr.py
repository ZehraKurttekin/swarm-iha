import qrcode
import json
import os

file_path = os.path.join(os.getcwd(), "swarm-iha/mehmet_qr/qr6.json")

with open(file_path) as f:
    data = json.load(f)

qr_text = json.dumps(data)

img = qrcode.make(qr_text)

img.save("qr_gorev6.png")

print("QR oluşturuldu")