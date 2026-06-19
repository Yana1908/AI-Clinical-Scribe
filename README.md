# AI Clinical Scribe

## Project Overview

AI Clinical Scribe is an AI-powered healthcare documentation system that converts doctor-patient conversations into structured SOAP notes.

The project reduces manual clinical documentation by automatically transcribing medical conversations, identifying speakers, and generating SOAP (Subjective, Objective, Assessment, Plan) notes.

---

## Features

### Week 1: Audio Ingestion and Speaker Diarization
- Audio file upload
- Speech-to-text transcription using Whisper
- Speaker diarization using PyAnnote
- Distinguishes:
  - Speaker 1 (Doctor)
  - Speaker 2 (Patient)

### Week 2: Clinical Structuring
- SOAP prompt engineering
- Transcript processing
- Structured SOAP note generation
- FastAPI SOAP endpoint

---

## Technology Stack

### Backend
- Python
- FastAPI

### Speech Recognition
- OpenAI Whisper

### Speaker Diarization
- PyAnnote Audio

### API Testing
- Swagger UI

### Version Control
- Git
- GitHub

---

## Project Structure

AI_Clinical_Scribe/

├── audio/

│ ├── sample.wav

│ └── sample.mp3

├── data/

│ ├── cleaned_data.csv

│ └── Combined Data.csv

├── prompts/

│ └── soap_prompt.txt

├── transcripts/

│ └── sample_transcript.txt

├── test_whisper.py

├── test_diarization.py

├── soap_generator.py

├── main.py

├── requirements.txt

├── .gitignore

└── README.md

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_Clinical_Scribe.git

cd AI_Clinical_Scribe
```

### Create Virtual Environment

```bash
python -m venv venv311
```

### Activate Environment

Windows:

```bash
venv311\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running Whisper Transcription

```bash
python test_whisper.py
```

---

## Running Speaker Diarization

```bash
python test_diarization.py
```

---

## Running FastAPI Server

```bash
python -m uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## SOAP Note Example

### Subjective
Patient reports headache for 3 days.

### Objective
No fever reported.

### Assessment
Possible mild headache.

### Plan
Take paracetamol and stay hydrated.

---

## Week-wise Progress

### Week 1 Completed
- FastAPI setup
- Whisper integration
- Speaker diarization
- Audio processing pipeline

### Week 2 Completed
- SOAP prompt engineering
- Transcript management
- SOAP note generation
- FastAPI SOAP endpoint

### Upcoming

#### Week 3
- RAG for ICD-10 code recommendation

#### Week 4
- Human-in-the-loop dashboard
- Security improvements
- Final deployment

---

## Author

Internship Project

AI Clinical Scribe – Ambient Clinical Documentation System
