# Before running this script, make sure to download it by clicking the "Download" button above.

# Next, install the assemblyai package.
# You can do this by opening your terminal and typing `pip3 install assemblyai` (macOS) or `pip install assemblyai` (Windows).

# To run this script, type `python3 ~/Downloads/transcribe-a-youtube-video.py` (macOS) or `python ./transcribe-a-youtube-video.py` (Windows) in your Terminal.

# Import the AssemblyAI module
import assemblyai as aai

# Your API token is already set here
aai.settings.api_key = "0c03f77e677f4b0ca8b385e8ca64957d"

# Create a transcriber object.
transcriber = aai.Transcriber()

# If you have a local audio file, you can transcribe it using the code below.
# Make sure to replace the filename with the path to your local audio file.
transcript = transcriber.transcribe("./file_en1.wav")

# Alternatively, if you have a URL to an audio file, you can transcribe it with the following code.
# Uncomment the line below and replace the URL with the link to your audio file.
# transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/espn-bears.m4a")

# After the transcription is complete, the text is printed out to the console.
print(transcript.text)