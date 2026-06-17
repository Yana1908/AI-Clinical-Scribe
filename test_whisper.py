import whisper

try:
    model = whisper.load_model("base")
    result = model.transcribe("audio/sample.mp3")
    print(result["text"])
except Exception as e:
    print("Error:", e)
    print("Check if the audio file is valid and not corrupted.")