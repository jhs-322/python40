from playsound import playsound
from gtts import gTTS
text = "챗지피티를 이용해 챗봇을 만들어 보고 싶습니다."
tts = gTTS(text=text, lang='ko')
tts.save(r"./chatgpt.mp3")
playsound("chatgpt.mp3")