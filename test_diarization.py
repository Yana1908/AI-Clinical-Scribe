from pyannote.audio import Pipeline

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    token="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"
)

print("Model Loaded Successfully")