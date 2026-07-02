# 🩺 AI Clinical Scribe & Automated SOAP Note Generator

## 📌 Project Overview

AI Clinical Scribe is a healthcare AI application that automatically converts doctor-patient conversations into structured clinical notes and recommends ICD-10 medical codes.

This project was developed as part of my AI Internship.

---

# 🚀 Features

## ✅ Week 1 - Audio Processing

- Audio ingestion
- FastAPI backend setup
- Whisper Speech-to-Text
- Speaker Diarization using PyAnnote
- Doctor & Patient speaker separation

---

## ✅ Week 2 - SOAP Note Generation

- Prompt Engineering
- Clinical transcript processing
- SOAP Note generation

SOAP Format:

- Subjective
- Objective
- Assessment
- Plan

FastAPI endpoint:

```
GET /soap
```

Returns SOAP Note in JSON format.

---

## ✅ Week 3 - RAG for ICD-10 Recommendation

Implemented Retrieval-Augmented Generation (RAG).

Workflow:

SOAP Assessment
↓

Sentence Transformer Embedding
↓

FAISS Vector Search
↓

Nearest ICD-10 Match
↓

ICD Recommendation

Current Features:

- ICD-10 Dataset
- FAISS Vector Database
- Sentence Transformers
- Semantic Search
- Automatic ICD Recommendation

Example:

Assessment:

```
Hypertension
```

Output:

```
Disease : Hypertension

ICD10 : I10

Description : High blood pressure
```

---

# 🏗 Project Structure

```
AI_Clinical_Scribe/

│

├── audio/

├── data/

├── medical_docs/

│ └── icd10.csv

│

├── prompts/

│ └── soap_prompt.txt

│

├── rag/

│ ├── vector_store.py

│ ├── retrieve_icd.py

│ └── rag_pipeline.py

│

├── transcripts/

├── vector_db/

│ ├── icd10.index

│ └── icd10.pkl

│

├── diarize_audio.py

├── soap_generator.py

├── test_whisper.py

├── main.py

├── requirements.txt

└── README.md
```

---

# ⚙ Technologies Used

- Python 3.11
- FastAPI
- OpenAI Whisper
- PyAnnote
- Hugging Face
- Sentence Transformers
- FAISS
- Pandas
- NumPy

---

# ▶ Installation

Clone repository

```
git clone https://github.com/Yana1908/AI-Clinical-Scribe.git
```

Go to project

```
cd AI_Clinical_Scribe
```

Create Virtual Environment

Windows

```
python -m venv venv311

venv311\Scripts\activate
```

Install Dependencies

```
pip install -r requirements.txt
```

---

# ▶ Run Project

Start FastAPI

```
uvicorn main:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

Click

```
GET /soap
```

Execute the endpoint to generate:

- SOAP Note
- ICD-10 Recommendation

---

# 📊 API Response

```json
{
  "SOAP_Note": {
    "Subjective": "Patient has high blood pressure.",
    "Objective": "Blood Pressure is 150/100.",
    "Assessment": "Hypertension",
    "Plan": "Amlodipine"
  },
  "ICD_Recommendation": {
    "Disease": "Hypertension",
    "ICD10": "I10",
    "Description": "High blood pressure"
  }
}
```

---

# 🔄 Project Workflow

Doctor-Patient Audio

↓

Whisper ASR

↓

Speaker Diarization

↓

Transcript

↓

SOAP Note Generation

↓

Assessment Extraction

↓

Sentence Transformer

↓

FAISS Search

↓

ICD-10 Recommendation

↓

FastAPI JSON Response

---

# 📅 Internship Progress

## ✅ Week 1

- Audio ingestion
- Whisper integration
- Speaker diarization
- FastAPI setup

## ✅ Week 2

- Prompt engineering
- SOAP note generation
- FastAPI SOAP endpoint

## ✅ Week 3

- ICD-10 dataset preparation
- Vector embeddings
- FAISS indexing
- Semantic search
- RAG integration
- Automatic ICD recommendation

## 🔜 Week 4 (Upcoming)

- Human-in-the-loop Dashboard
- Doctor review and editing
- Final SOAP approval
- Streamlit/React UI
- Security improvements

---

# 👩‍💻 Author

**Yana Midha**

AI Clinical Scribe Internship Project

GitHub:
https://github.com/Yana1908

---

## ⭐ Future Improvements

- Real-time audio streaming
- LLM-generated SOAP Notes
- Clinical summarization
- Multiple ICD recommendations
- Dashboard for doctors
- EHR Integration
- Secure authentication
