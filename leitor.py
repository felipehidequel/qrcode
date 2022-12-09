from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("/home/hidequel/projetos/qrcode/saida/myqrcode.png")

result = decode(img)

print(result)
