import speech_recognition as sr 

try :
    while True:
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print(" 음성을 입력하세요")
            audio = r.record(source, offset=1, duration=3)
            
            try:
                print("음성 변환 : "+r.recognize_google(audio, language='ko-KR'))
            except sr.UnknownValueError:
                print("오디오를 이해할 수 없습니다.")
            except sr.RequestError as e:
                print(f"에러가 발생했습니다. 에러원인: {e}")
except KeyboardInterrupt:
    pass