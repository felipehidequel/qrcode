import qrcode

data = 'Seu Codigo QR'

qr = qrcode.QRCode(version=1, box_size=10, border=4)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('/home/hidequel/projetos/qrcode/saida/myqrcode1.png')]