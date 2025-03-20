import numpy as np
import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

os.chdir(os.path.dirname(os.path.abspath(__file__)))
ff = np.fromfile('샘플사진.jpg', np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED) 
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.2,6)
for (x,y,w,h) in faces:
    face_img = img[y:y+h, x:x+w]
    # 축소
    face_img = cv2.resize(face_img, dsize=(0, 0), fx=0.1, fy=0.1) 
    # 확대 (손실되어서 모자이크 처리된다)
    face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA) 
    img[y:y+h, x:x+w] = face_img

cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()