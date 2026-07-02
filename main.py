from fastapi import FastAPI
import faiss
import pickle
from sentence_transformers import SentenceTransformer

app = FastAPI()

# ----------------------------
# Load FAISS Index
# ----------------------------
index = faiss.read_index("vector_db/icd10.index")

# ----------------------------
# Load ICD10 Data
# ----------------------------
with open("vector_db/icd10.pkl", "rb") as f:
    df = pickle.load(f)

# ----------------------------
# Load Embedding Model
# ----------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")


@app.get("/")
def home():
    return {
        "message": "AI Clinical Scribe API is Running Successfully!"
    }


@app.get("/soap")
def generate_soap():

    # ----------------------------
    # Example SOAP Note
    # Change ONLY the Assessment
    # ----------------------------

    soap_note = {
        "Subjective": "Patient has high blood pressure.",
        "Objective": "Blood Pressure is 150/100.",
        "Assessment": "Hypertension",
        "Plan": "Amlodipine"
    }

    # ----------------------------
    # Convert Assessment to Vector
    # ----------------------------

    query = soap_note["Assessment"]

    query_embedding = model.encode([query])

    # ----------------------------
    # Search FAISS
    # ----------------------------

    distance, indices = index.search(query_embedding, 1)

    result = df.iloc[indices[0][0]]

    # ----------------------------
    # Return JSON
    # ----------------------------

    return {
        "SOAP_Note": soap_note,
        "ICD_Recommendation": {
            "Disease": result["Disease"],
            "ICD10": result["ICD10"],
            "Description": result["Description"]
        }
    }