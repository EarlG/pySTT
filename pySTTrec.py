import os
import wave
import json
import vosk

import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np


fs = 16000  # Sample rate
seconds = 10  # Duration of recording
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
write('output16.wav', fs, myrecording.astype(np.int16))  # Save as WAV file in 16-bit format