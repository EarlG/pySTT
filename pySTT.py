# Конечно! Для расшифровки файла mp3 произвольной длины с аудиозаписью речи в текстовый файл с расшифровкой речи,
# можно использовать бесплатный сервис распознавания речи Google Cloud Speech-to-Text.
# Для работы с этим сервисом нужно выполнить следующие шаги:

# 1. Установить библиотеку Google Cloud для Python, используя команду:

# pip install --upgrade google-cloud-speech


# 2. Создать учетную запись в Google Cloud и получить ключ API.

# 3. Создать файл Python и импортировать библиотеки:

import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="oval-relic-374617-4508c79c616b.json"

# from google.cloud import speech_v1
# from google.cloud.speech_v1 import enums

from google.cloud import speech_v1
from google.cloud import speech
# from google.cloud.speech_v1 import enums
from google.cloud.speech_v1 import types


# 4. Определить функцию, которая будет производить расшифровку аудиозаписи:

def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    client = speech_v1.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    # audio = speech_v1.types.RecognitionAudio(content=content)
    audio = speech.RecognitionAudio(content=content)
    config = speech_v1.types.RecognitionConfig(
        # encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='ru-RU')

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))


# 5. Вызвать функцию transcribe_file и передать ей путь к файлу аудиозаписи:

transcribe_file('file.mp3')


# 6. Результат расшифровки будет выведен в консоль. Чтобы записать его в текстовый файл, можно изменить функцию transcribe_file следующим образом:

def transcribe_file(speech_file, output_file):
    """Transcribe the given audio file."""
    client = speech_v1.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech_v1.types.RecognitionAudio(content=content)
    config = speech_v1.types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='ru-RU')

    response = client.recognize(config, audio)

    with io.open(output_file, 'w', encoding='utf-8') as out:
        for result in response.results:
            out.write('Transcript: {}\n'.format(result.alternatives[0].transcript))


# 7. Затем вызвать функцию transcribe_file с аргументами speech_file и output_file, например:

transcribe_file('file.mp3', 'transcription.txt')

# Эта программа будет расшифровывать аудиозапись и записывать результат в указанный текстовый файл.
