# 자동차 / 번호판 모자이크 처리
import numpy as np
import os
import cv2

car_model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

os.chdir(os.path.dirname(os.path.abspath(__file__)))
file = np.fromfile('car.jpg', np.uint8)
img = cv2.imdecode(file, cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, dsize=(0,0), fx = 1.0, fy = 1.0, interpolation=cv2.INTER_LINEAR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # 이미지 흑백 변환 (Haar Cascade는 흑백 이미지를 입력으로 사용)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 번호판 검출
# plates = car_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))

cars = car_model.detectMultiScale(gray, 1.2, 5)

for (x, y, w, h) in cars:
    
    car_img = img[y:y+h, x:x+w]
    car_img = cv2.resize(car_img, dsize=(0,0), fx = 0.05, fy = 0.05)
    car_img = cv2.resize(face_img, (w,h), interpolation=cv2.INTER_AREA)
    img[y:y+h, x:x+w] = car_img
    
    
    # # 번호판 영역 자르기
    # plate_img = img[y:y+h, x:x+w]

    # # 모자이크 처리 (5% 크기로 축소 후 다시 확대)
    # plate_img = cv2.resize(plate_img, (0, 0), fx=0.05, fy=0.05)
    # plate_img = cv2.resize(plate_img, (w, h), interpolation=cv2.INTER_AREA)

    # # 원본 이미지에 모자이크된 번호판 적용
    # img[y:y+h, x:x+w] = plate_img

    # # 검출된 번호판에 테두리 그리기
    # cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# 결과 출력
cv2.imshow('License Plate Blur', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# import numpy as np
# import cv2
# import os
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascades_eye.xml')

# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# ff = np.fromfile('샘플사진.jpg', np.uint8)
# img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
# img = cv2.resize(img, dsize=(0,0), fx = 1.0, fy = 1.0, interpolation=cv2.INTER_LINEAR)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = face_cascade.detectMultiScale(gray, 1.2, 5)
# for(x,y,w,h) in faces:
#     face_img = img[y:y+h, x:x+w]
#     face_img = cv2.resize(face_img, dsize=(0,0), fx = 0.05, fy = 0.05)
#     face_img = cv2.resize(face_img, (w,h), interpolation=cv2.INTER_AREA)
#     img[y:y+h, x:x+w] = face_img
    
# cv2.imshow('face find', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()