import os
import sys
import wave
import json
from vosk import Model, KaldiRecognizer

# Path to the Vosk model
model_path = ''  # Change this to your model's path
audio_file_path = 'path/to/your/audio/file.wav'  # Change this to your audio file path

if not os.path.exists(model_path):
    print(f"Model not found at {model_path}")
    sys.exit(1)

model = Model(model_path)
rec = KaldiRecognizer(model, 16000)

with wave.open(audio_file_path, "rb") as wf:
    if wf.getnchannels() != 1:
        print("Audio file must be mono.")
        sys.exit(1)
    if wf.getframerate() != 16000:
        print("Audio file must be 16kHz.")
        sys.exit(1)

    transcription = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            transcription.append(result['text'])
    
    # Get the last part of the recognition
    final_result = json.loads(rec.FinalResult())
    transcription.append(final_result['text'])

# Join all transcriptions and print
transcription_text = "\n".join(transcription)
print(transcription_text)

# Optionally, save to a text file or convert to SRT
with open('transcription.txt', 'w') as f:
    f.write(transcription_text)