import qrcode

# https://pypi.org/project/qrcode/ use the install "qrcode[pil]" for the ability to create images

webpage_url = input('enter a website you would like to make a qr code for: ').strip()
img_name = input('what would you like the image to be called?: ').strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(webpage_url)
img = qr.make_image(fill_color="black", back_color="white")
img.save(img_name + '.png')
print(f'file created called: {img_name}.png')