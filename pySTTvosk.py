import os
import sys
import json
import wave
import subprocess

from vosk import Model, KaldiRecognizer

# конвертируем аудиофайл mp3 в wav формат
# subprocess.call(['ffmpeg', '-i', './file.mp3', '-ar', '16000', 'audiofile1.wav'])

# загружаем модель Vosk
model = Model('vosk-model-small-ru-0.22')

# открываем аудиофайл
wf = wave.open("output4.wav", "rb")

# создаем объект распознавания
rec = KaldiRecognizer(model, wf.getframerate())

# читаем данные из аудиофайла и передаем их в распознаватель
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        pass

# получаем результат распознавания
result = json.loads(rec.FinalResult())

# записываем распознанный текст в файл
with open('output4.txt', 'w') as file:
    file.write(result['text'])