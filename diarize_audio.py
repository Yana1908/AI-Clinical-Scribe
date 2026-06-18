import torchaudio
if not hasattr(torchaudio, 'set_audio_backend'):
    torchaudio.set_audio_backend = lambda *args, **kwargs: None
if not hasattr(torchaudio, 'get_audio_backend'):
    torchaudio.get_audio_backend = lambda: "soundfile"

import torch
from pyannote.audio import Pipeline

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1"
)

waveform, sample_rate = torchaudio.load("audio/sample.wav")
audio_input = {"waveform": waveform, "sample_rate": sample_rate}

diarization = pipeline(audio_input)

for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(f"{turn.start:.1f}s --> {turn.end:.1f}s : {speaker}")