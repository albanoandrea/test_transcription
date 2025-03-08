#!/usr/bin/env python
# pip install librosa speechrecognition transformers
#%%
import speech_recognition as sr
import sys
import os
#%%
if len(sys.argv) != 2:
   print("Usage: " + sys.argv[0] + " <folder with audio files>")
   exit(-1)

folder_path = sys.argv[1]

#%%
# folder_path = "output"
#%%
try:
    files = os.listdir(folder_path)
    files.sort()
    with open(folder_path + "/transcription.txt", "wt") as myfile:
        for file in files:
            print(file)
            r = sr.Recognizer()
            with sr.AudioFile(folder_path+"/"+file) as source:
                audio_data = r.record(source)
            try:
                text = r.recognize_google(audio_data, language="it-IT")
                print(file[-6:-4] + ": " + text)
                myfile.write(file[-6:-4] + ": " + text+"\n")
                myfile.flush()
            except sr.UnknownValueError:
                print("Impossible recognize audio")
            except sr.RequestError as e:
                print("Request error:", e)
except FileNotFoundError:
    print(f"Folder not found: ")
except NotADirectoryError:
    print(f"{sys.argv[0]} is not a directory.")



# %%
