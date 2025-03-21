import pyaudio
import wave
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

CHUNK = 1024
CHANNELS = 1
FORMAT = pyaudio.paInt16
RATE = 44100
RECORD_SECOND = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer=CHUNK)

print("음성 녹음을 시작합니다.")
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECOND)):
    data = stream.read(CHUNK)
    frames.append(data)
print("음성 녹음을 완료하였습니다.")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print("녹음된 파일을 재생합니다.")
playsound(WAVE_OUTPUT_FILENAME)