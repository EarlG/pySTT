import speech_recognition as sr


# 3. Определить функцию, которая будет производить расшифровку аудиозаписи:

def transcribe_file(audio_file_path, output_file_path):
    """Transcribe the given audio file."""
    r = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_text = r.record(source)

    try:
        text = r.recognize_google(audio_text, language='ru-RU')
        with open(output_file_path, mode='w') as file:
            file.write(text)
        print("Transcription complete!")
    except Exception as e:
        print("Error: ", str(e))


# 4. Вызвать функцию transcribe_file и передать ей путь к файлу аудиозаписи и путь к файлу для записи расшифровки:

transcribe_file('file.mp3', 'transcription.txt')
