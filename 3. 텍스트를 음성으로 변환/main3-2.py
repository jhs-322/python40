from gtts import gTTS
from playsound import playsound
import os

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))
"""
os.path.abspath(__file__) : 실행중인 파일의 절대 경로 가져오고
os.path.dirname : 해당 파일의 디렉토리를 가져오고
os.chdir : 그 경로를 현재 작업 디렉토리로 변경
작업 경로가 해당 디렉토리로 변경되었기 때문에,
같은 폴더에 위치한 다른 파일들의 접근이 쉬워진다
따라서 상대경로를 이용하여 코드 이식성을 높였다
다만, 이 코드가 필요한 이유는 playsound는 기본적으로
현재작업디렉토리(CWD)에서 실행파일을 찾기 때문이다.
그래서 파일 경로를 현재 작업 디렉토리로 설정해 준 것이다
 """

text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

tts = gTTS(text=text, lang='ko')
tts.save("hi.mp3")

playsound("hi.mp3")