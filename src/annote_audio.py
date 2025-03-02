#!/usr/bin/env python
#%%
import sys
import json

#%%
from pyannote.audio import Pipeline
with open("token.txt", "r") as f:
    token = f.read()
    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        use_auth_token=token)

# send pipeline to GPU (when available)
#%%
import torch
from torch import cuda
device = 'cuda' if cuda.is_available() else 'cpu'
pipeline.to(torch.device(device))

#%%
if len(sys.argv) != 2:
   print("Usage: " + sys.argv[0] + " <audio file>")
   exit(-1)
file_name = sys.argv[1]
# #%%
# file_name = "250221-lazanzara.wav"

#%%
# apply pretrained pipeline
diarization = pipeline(file_name)

#%%
annotate = []
# print the result
index = 0
for turn, _, speaker in diarization.itertracks(yield_label=True):
        annotate.append({'index':index, 'speaker': speaker, 'start': turn.start, 'end': turn.end})
        index = index+1

with open(file_name+'.annotate.json', 'w') as f:
    json.dump(annotate, f)
            
