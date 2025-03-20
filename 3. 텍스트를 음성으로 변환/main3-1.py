from gtts import gTTS

#pip install gtts
#pip install playsound==1.2.2
#pytho.exe -m pip install gtts playsound==1.2.2


# hi.mp3 생성
text = "안녕하세요. 이스트소프트 수강생 여러분, 오늘은 2025년 2월 20일입니다."
tts = gTTS(text=text, lang='ko')
tts.save(r"3. 텍스트를 음성으로 변환\hi.mp3")
