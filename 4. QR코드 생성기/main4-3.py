import qrcode

file_path = r'4. QR코드 생성기\qr코드모음.txt'
with open(file_path, 'rt', encoding='UTF8') as f : 
    read_lines = f.readlines()
    
    for line in read_lines:
        line = line.strip()
        print(line)
        
        qr_data = line
        qr_img = qrcode.make(qr_data)

        save_path = '4. QR코드 생성기\\' + qr_data + '.png'
        qr_img.save(save_path)

# import qrcode

# file_path = r'4. QR코드 생성기\qr코드모음.txt'
# with open(file_path, 'rt', encoding=UTF8) as f:
#     qr_list = f.readlines()

#     for line in qr_list:
#         line = line.strip()
#         print(line)

#         #qr_data = line
#         qr_img = qrcode.make(line)
#         qr_img.save('4. QR코드 생성기\\' +qr_data+ '.png')