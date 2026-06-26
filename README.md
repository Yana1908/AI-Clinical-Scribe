# 🩺 AI Clinical Scribe

An AI-powered Clinical Scribe system that converts doctor-patient conversations into structured clinical documentation. The project uses Automatic Speech Recognition (ASR), Speaker Diarization, Prompt Engineering, and Retrieval-Augmented Generation (RAG) to assist in generating SOAP notes and suggesting ICD-10 codes.

---

## 📌 Project Objective

The goal of this project is to automate medical documentation by:

- Converting doctor-patient audio into text.
- Identifying different speakers (Doctor & Patient).
- Generating structured SOAP notes.
- Suggesting ICD-10 diagnosis codes using a medical knowledge base.

---

## 🚀 Technologies Used

- Python 3.11
- FastAPI
- OpenAI Whisper
- Pyannote Audio
- Hugging Face
- Sentence Transformers
- FAISS
- Git & GitHub

---

# 📂 Project Structure

```
AI_Clinical_Scribe/
│
├── audio/
│   ├── sample.wav
│   └── sample.mp3
│
├── data/
│   ├── cleaned_data.csv
│   └── CombinedData.csv
│
├── medical_docs/
│   └── icd_reference.txt
│
├── prompts/
│   └── soap_prompt.txt
│
├── rag/
│   ├── rag_pipeline.py
│   └── icd_mapper.py
│
├── transcripts/
│
├── outputs/
│
├── main.py
├── soap_generator.py
├── test_whisper.py
├── test_diarization.py
├── load_data.py
├── clean_data.py
├── requirements.txt
└── README.md
```

---

# ✅ Week 1 - Audio Ingestion & Speaker Diarization

### Completed Tasks

- FastAPI backend setup
- Audio preprocessing
- Speech-to-Text using Whisper
- Speaker Diarization using Pyannote
- Audio testing
- GitHub integration

### Output

Doctor-Patient audio is converted into text and speakers are identified separately.

---

# ✅ Week 2 - Prompt Engineering & SOAP Generation

### Completed Tasks

- Designed SOAP Prompt Template
- Stored transcripts
- Integrated transcript with prompt
- Generated structured SOAP Notes
- Developed FastAPI SOAP endpoint

### SOAP Format

- Subjective
- Objective
- Assessment
- Plan

### API Endpoint

```
GET /soap
```

### Sample Output

```json
{
  "Subjective": "Headache for 3 days",
  "Objective": "No fever",
  "Assessment": "Mild headache",
  "Plan": "Paracetamol"
}
```

---

# ✅ Week 3 - Clinical Intelligence Layer (RAG)

### Completed Tasks

- Created Medical Knowledge Base
- Added ICD-10 Reference File
- Implemented Basic ICD Mapping
- Built RAG Project Structure
- Added ICD Recommendation API

### API Endpoint

```
GET /icd
```

### Sample Output

```json
{
  "diagnosis": "Headache",
  "icd10_code": "R51"
}
```

---

# 🔄 System Workflow

```
Doctor-Patient Audio
          │
          ▼
OpenAI Whisper
(Speech-to-Text)
          │
          ▼
Transcript
          │
          ▼
SOAP Prompt
          │
          ▼
SOAP Note Generator
          │
          ▼
FastAPI Backend
          │
          ▼
JSON Response
          │
          ▼
RAG Module
          │
          ▼
ICD-10 Recommendation
```

---

# ▶️ Running the Project

### Clone Repository

```bash
git clone <repository-url>
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

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run FastAPI

```bash
python -m uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

# 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home API |
| GET | /soap | Generate SOAP Note |
| GET | /icd | Recommend ICD-10 Code |

---

# 🎯 Future Improvements

- Real-time audio transcription
- Improved speaker diarization accuracy
- LLM-powered SOAP note generation
- Advanced RAG with vector database
- Human-in-the-loop dashboard
- Secure authentication
- EHR integration

---

# 👩‍💻 Author

**Yana Midha**

AI Clinical Scribe Internship Project

---

# ⭐ Project Status

- ✅ Week 1 Completed
- ✅ Week 2 Completed
- 🚧 Week 3 In Progress
- ⏳ Week 4 Pending
