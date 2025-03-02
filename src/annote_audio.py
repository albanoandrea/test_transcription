#!/usr/bin/env python
#%%
import sys
import os

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

# print the result
for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
