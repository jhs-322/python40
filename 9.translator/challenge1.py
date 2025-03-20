import googletrans
from gtts import gTTS
from playsound import playsound
import os

# 텍스트 파일을 업로드 -> 번역 (.txt) -> mp3, 재생

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# file_path = 'request.txt'

# translator = googletrans.Translator()

# try:
#     with open(file_path, 'rt') as f:
#         text = f.read()

#     result = translator.translate(text, dest='ko', src='auto')

#     with open('answer.txt', 'w', encoding='UTF8') as f:
#         f.write(result.text)

#     tts = gTTS(text=result.text, lang='ko')
#     tts.save("answer.mp3")

#     playsound("answer.mp3")

# except Exception as e:
#     print(f"Error: {e}")


os.chdir(os.path.dirname(os.path.abspath(__file__)))
file = 'hangeul.txt'
translator = googletrans.Translator() # 객체 만들고

try : 
    with open(file,'rt', encoding="UTF8") as f:
        line = f.read()
    result = translator.translate(line, dest='en', src='auto')
        
    with open('eng.txt', 'w', encoding="UTF8") as f:
        f.write(result.text)

    with open('eng.txt', 'rt', encoding="UTF8") as f:
        translated = f.read()

    tts = gTTS(text=translated, lang='en')
    tts.save("eng.mp3")
    playsound("eng.mp3")

except Exception as e : 
    print(f"Error : {e}")