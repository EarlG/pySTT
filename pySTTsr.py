import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write

# recording from the microphone
fs = 44100  # Sample rate
seconds = 3  # Duration of recording

sound = "output3.wav"
recognizer = sr.Recognizer()

with sr.AudioFile(sound) as source:
     recognizer.adjust_for_ambient_noise(source)
     print("Converting audio file to text...")
     audio = recognizer.listen(source)

     try:
          text = recognizer.recognize_google(audio, language = "ru-RU")
          print("The converted text:" + text)

     except Exception as e:
          print(e)