from pathlib import Path

transcript = Path(
    "transcripts/sample_transcript.txt"
).read_text()

prompt = Path(
    "prompts/soap_prompt.txt"
).read_text()

final_prompt = prompt.replace(
    "{transcript}",
    transcript
)

print(final_prompt)