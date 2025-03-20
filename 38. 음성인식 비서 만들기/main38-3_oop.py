import speech_recognition as sr 

class speech2text:
    def __init__(self, language = 'ko-KR'):
        self.recognizer = sr.Recognizer()
        self.language = language # self.는 해당 클래스 내에서 사용 가능
    
    def process_audio(self):
        try:
            with sr.Microphone() as source: #오디오 입력
                print("음성을 입력하세요")
                audio = self.recognizer.listen(source) # 저장
            stt = self.recognizer.recognize_google(audio,
                                                    language=self.language)
            print("음성 변환: "+stt)
            self.handle_keywords(stt) #stt에 대해 적용
            
        except sr.UnknownValueError:
            print("오디오를 이해할 수 없습니다.")
        except sr.RequestError as e:
            print(f"에러가 발생했습니다. 에러 메시지 : {e}")

        
    def handle_keywords(self, text):
        if "안녕" in text:
            print("네 안녕하세요.")
        if "날씨" in text:
            print("정말 날씨가 좋네요.")
        
    def run(self):
        try:
            while True:
                self.process_audio()
        except KeyboardInterrupt: #Ctrl + c : 종료
            print("\n 프로그램을 종료합니다.")
 

if __name__ == '__main__':
    processor = speech2text(language='ko-KR')
    processor.run()