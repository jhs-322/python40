import qrcode

# 한 줄 한 줄 읽어들이기
# readlines()는 리스트로 반환, read_lines는 리스트.
# strip()은 탭이나 공백 모두 제거(\n도)
file_path = r'4. QR코드 생성기\qr코드모음.txt'
with open(file_path, 'rt', encoding='UTF8') as f : 
    read_lines = f.readlines()
    
    for line in read_lines:
        line = line.strip()
        print(line)
