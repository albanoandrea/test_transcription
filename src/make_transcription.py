#!/usr/bin/env python
# pip install librosa speechrecognition transformers

import librosa
import speech_recognition as sr
import sys

if len(sys.argv) != 2:
   print("Usage: " + sys.argv[0] + " <audio file>")
   exit(-1)

# y, sr = librosa.load(sys.argv[1])
r = sr.Recognizer()

with sr.AudioFile(sys.argv[1]) as source:
    audio_data = r.record(source)

try:
    text = r.recognize_google(audio_data, language="it-IT")
    print("Transcript:", text)
except sr.UnknownValueError:
    print("Impossibil recognize audio")
except sr.RequestError as e:
    print("Request error:", e)