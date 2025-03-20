# pip intsall qrcode
# pip install pillow
import qrcode

qr_data = 'www.notion.com'
qr_img = qrcode.make(qr_data)

save_path = '4. QR코드 생성기\\' + qr_data + '.png'
qr_img.save(save_path)
