import faiss
import pickle
from sentence_transformers import SentenceTransformer

# --------------------------
# Example SOAP Note
# --------------------------

soap_note = {
    "Subjective": "Patient has had headache for three days.",
    "Objective": "No fever. Blood pressure normal.",
    "Assessment": "Mild headache",
    "Plan": "Paracetamol and rest"
}

# --------------------------
# Load FAISS index
# --------------------------

index = faiss.read_index("vector_db/icd10.index")

# --------------------------
# Load ICD database
# --------------------------

with open("vector_db/icd10.pkl", "rb") as f:
    df = pickle.load(f)

# --------------------------
# Load embedding model
# --------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")

# --------------------------
# Convert Assessment into vector
# --------------------------

query = soap_note["Assessment"]

query_embedding = model.encode([query])

# --------------------------
# Search nearest ICD code
# --------------------------

distance, indices = index.search(query_embedding, 1)

result = df.iloc[indices[0][0]]

# --------------------------
# Final Output
# --------------------------

print("========== SOAP NOTE ==========")

for key, value in soap_note.items():
    print(f"{key}: {value}")

print("\n========== ICD Recommendation ==========")

print("Disease :", result["Disease"])
print("ICD Code:", result["ICD10"])
print("Description:", result["Description"])