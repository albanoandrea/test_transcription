#!/usr/bin/env python

# This approach doesn't work because it divide at every frame(? not clear the measure unit) with less energy than
# ehe expected, so too many times

# #%%
# import librosa
# import numpy as np
# import sys
# import soundfile as sf

# #%%
# if len(sys.argv) != 2:
#    print("Usage: " + sys.argv[0] + " <audio file>")
#    exit(-1)
# file_name = sys.argv[1]
# #%%
# file_name = "250221-lazanzara.wav"
# #%%
# y, sr = librosa.load(file_name)


# #%%
# #divide audio file based on silence with energy threshold
# # dbFS
# threshold = -40
# y_energy = librosa.feature.rms(y=y)[0]
# silence_indexes_1 = np.where(y_energy < librosa.db_to_amplitude(threshold))[0]

# print("silence_indexes_1:")
# print(silence_indexes_1)

# time_s_1 = librosa.frames_to_time(silence_indexes_1, sr=sr)

# print("time_s_1:")
# print(time_s_1)

# #%%
# silence_indexes_2 = librosa.effects.split(y, top_db=-threshold)

# print("silence_indexes_2:")
# print(silence_indexes_1)
# time_s_2 = librosa.frames_to_time(silence_indexes_2, sr=sr)

# print("time_s_2:")
# print(time_s_2)
# #%%
# audio_segments = []
# for i,val in enumerate(silence_indexes_1):
#     if(i == len(silence_indexes_1)-1):
#         break
#     start = val
#     end = silence_indexes_1[i+1]
#     audio_segments.append(y[start:end])

# #%%
# for i,val in enumerate(audio_segments):
#     new_file_name = f"{file_name}_1_{i}.wav"
#     print(new_file_name)
#     sf.write(new_file_name, val, sr, 'PCM_16')

# #%%
# audio_segments = []
# for i,val in enumerate(silence_indexes_2):
#     if(i == len(silence_indexes_2)-1):
#         break
#     start = val
#     end = silence_indexes_2[i+1]
#     audio_segments.append(y[start:end])


# for i,val in enumerate(audio_segments):
#     new_file_name = f"{file_name}_2_{i}.wav"
#     print(new_file_name)
#     sf.write(new_file_name, val, sr, 'PCM_16')

# This approach works better but still interrupt some speech in the middle
# Need to find a better way to divide files
#%%
from pydub import AudioSegment
from pydub.silence import split_on_silence
import sys
import os

#%%
if len(sys.argv) != 2:
   print("Usage: " + sys.argv[0] + " <audio file>")
   exit(-1)
file_name = sys.argv[1]
# #%%
# file_name = "250221-lazanzara.wav"

#%%
sound = AudioSegment.from_wav(file_name)

chunks = split_on_silence(
    sound,
    min_silence_len=500,  # Minimum length of silence in milliseconds
    silence_thresh=-40,  # Consider sound quieter than -40dBFS as silence
    keep_silence=250, # Keep some silence in the begining and end of the chunks.
)


#%%
for i, chunk in enumerate(chunks):
    output_file = f"output/{os.path.splitext(file_name)[0]}_{int(i):0{3}d}.wav"
    print(output_file)
    chunk.export(output_file, format="wav")

# %%
