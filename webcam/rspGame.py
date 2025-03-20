import torch
import cv2
import numpy as np
import random

# YOLO 모델 로드 (custom 모델 사용 가정)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='rps_yolov5.pt', force_reload=True)  # 학습된 가위바위보 모델

# 클래스 목록 (모델 학습 시 지정한 클래스)
class_names = ['scissors', 'rock', 'paper']  # YOLO 모델의 클래스 이름
kor_names = {'scissors': '가위', 'rock': '바위', 'paper': '보'}

def detect_rps(frame):
    results = model(frame)  # YOLO 모델 예측
    predictions = results.xyxy[0].cpu().numpy()  # 예측 결과
    result_labels = []
    
    for *box, conf, cls in predictions:
        label = class_names[int(cls)]  # 감지된 클래스
        result_labels.append(kor_names[label])  # 한글 변환
        
        # 박스 그리기
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, kor_names[label], (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    return frame, result_labels

# 웹캠 실행
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    what = ["가위", "바위", "보"]
    computer = random.choice(what)

    frame, result = detect_rps(frame)  # 가위바위보 감지
    cv2.imshow('YOLO RPS Detector', frame)  # 화면 출력
    print("Result:", result)  # 결과 출력
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # if (computer == "가위" and result == "바위") or (computer == "바위" and result == "보") or (computer == "보" and result =="가위"):
    #     print("컴퓨터 : "+computer, "\n 사용자 : "+result)
    #     break

cap.release()
cv2.destroyAllWindows()
