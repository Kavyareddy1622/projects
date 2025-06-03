import qrcode

data=input('enter url:').strip()
filename=input('filename:').strip()
qr=qrcode.QRCode(box_size=15,border=4)
qr.add_data(data)
image=qr.make_image(fill_color='black')
image.save(filename)
print(f'qr saved to{filename}')




