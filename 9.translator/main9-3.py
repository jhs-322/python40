from os import linesep
import googletrans
import os

translator = googletrans.Translator()

os.chdir(os.path.dirname(os.path.abspath(__file__)))
read_file = "영어파일.txt"
write_file = "ko파일.txt"

with open(read_file, 'rt') as f:
    readLines = f.readlines()

for line in readLines:
    result1 = translator.translate(line, dest='ko')
    print(result1.text)
    with open(write_file, 'a', encoding='UTF8') as f:
        f.write(result1.text+ '\n')
