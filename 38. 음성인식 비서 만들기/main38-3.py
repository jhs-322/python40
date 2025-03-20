import speech_recognition as sr 
from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
try:
    while True:
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("음성을 입력하세요.")
            audio = r.listen(source)
        try:
            stt = r.recognize_google(audio, language = 'ko-KR')
            print("음성변환: "+stt)
            if "하이" in stt:
                print("네 안녕하세요")
                text = "네 안녕하세요"
            elif "날씨" in stt:
                print("정말 날씨가 좋네요")
                text = "정말 날씨가 좋네요"
            elif "종료" in stt:
                print("네 종료할게요")
                text = "네 종료할게요"
                tts = gTTS(text = text, lang='ko')
                tts.save("answer2.mp3")
                playsound("answer2.mp3")
                break
            #추가    
            tts = gTTS(text = text, lang='ko')
            tts.save("answer.mp3")
            playsound("answer.mp3")
            
        except sr.UnknownValueError:
            print("오디오를 이해할 수 없습니다.")
        except sr.RequestError as e:
            print(f"에러가 발생하였습니다. 에러원인 : {e}")
except KeyboardInterrupt:
    pass
