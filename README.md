# Work in progress
Till now this repository is just an experiment

# test_transcription
Make the transcription from an audio file identifying different people speaking

# Improvement

* Identify common speakers, like Parenzo and Cruciani, and tune pyannote to recognize them
* Evaluate if 16kHz is better than 48kHz


# Pyannote

https://github.com/pyannote/pyannote-audio

```
python3 -m venv pyannote_env
source pyannote_env/bin/activate 
pip install "numpy<2.0"
pip install pyannote.audio
```
Accept [pyannote/segmentation-3.0](https://huggingface.co/pyannote/segmentation-3.0) user conditions
Accept [pyannote/speaker-diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1)user conditions
Create access token at hf.co/settings/tokens.

Save token in the `token.txt` file.

