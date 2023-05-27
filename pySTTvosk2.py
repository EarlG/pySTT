import os
import wave
import json
import vosk

import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np


# fs = 44100  # Sample rate
# seconds = 3  # Duration of recording
# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
# sd.wait()  # Wait until recording is finished
# write('output.wav', fs, myrecording.astype(np.int16))  # Save as WAV file in 16-bit format


def transcribe_file(audio_file_path, output_file_path, model_path):
    """Transcribe the given audio file."""
    sample_rate = 16000
    model = vosk.Model(model_path)
    rec = vosk.KaldiRecognizer(model, sample_rate)
    print("Loaded......")

    wf = wave.open(audio_file_path, 'rb')

    with open(output_file_path, 'w') as f:
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result['text']
                f.write(text + '\n')
    result = json.loads(rec.FinalResult())
    text = result['text']
    with open(output_file_path, 'a') as f:
        f.write(text + '\n')

    print('Transcription complete!')


# transcribe_file('output16_01.wav', 'output16_01.txt', 'vosk-model-small-ru-0.22')
transcribe_file('output16_03.wav', 'output16_03.txt', 'vosk-model-ru-0.42')
