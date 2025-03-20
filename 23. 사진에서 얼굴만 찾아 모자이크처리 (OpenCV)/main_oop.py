import cv2
import numpy as np 
import os

class FaceMosaic :
    def __init__(self,image_path, scale_factor, min_neighbors,
                mosaic_ratio):
        self.image_path = image_path
        self.scale_factor = scale_factor
        self.min_neighbors = min_neighbors
        self.mosaic_ratio = mosaic_ratio
        
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        
        self.img = self.loadImage() # 전처리 된 사진
        self.gray = cv2. cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        
    def loadImage(self):
        # 사진 전처리, 불러오기
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        ff = np.fromfile(self.image_path, np.uint8)
        img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
        img = cv2.resize(img, dsize=(0,0), fx= 1.0, fy = 1.0, interpolation=cv2.INTER_LINEAR)
        return img

            
    def apply_mosaic(self):
        # 모자이크 적용 - 사용자 입력 값으로
        faces = self.face_cascade.detectMultiScale(self.gray, self.scale_factor, self.min_neighbors)
        for (x, y, w, h) in faces:
            face_img = self.img[y:y+h, x:x+w]
            
            # 얼굴 부분을 축소 후 다시 확대하여 모자이크 효과 적용
            face_img = cv2.resize(face_img, dsize=(0, 0), fx=self.mosaic_ratio, fy=self.mosaic_ratio) 
            face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)
            self.img[y:y+h, x:x+w] = face_img
            
    
    def show_image(self, save_path="mosaic_output.jpg"):
        # 이미지를 보여주고, 저장
        cv2.imshow('Face Mosaic', self.img)
        cv2.imwrite(save_path, self.img)  
        print(f"이미지가 저장되었습니다: {save_path}")
        cv2.waitKey(0)
        cv2.destroyAllWindows()   
    
if __name__ == '__main__':
    mosaic = FaceMosaic('샘플사진.jpg', 1.2, 1, 0.1)
    mosaic.apply_mosaic()
    mosaic.show_image()
