import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load FAISS index
index = faiss.read_index("vector_db/icd10.index")

# Load ICD dataframe
with open("vector_db/icd10.pkl", "rb") as f:
    df = pickle.load(f)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Example diagnosis from SOAP Assessment
query = "Patient has headache"

# Convert query to embedding
query_embedding = model.encode([query])

# Search top 1 similar result
distance, indices = index.search(query_embedding, 1)

# Get matching row
result = df.iloc[indices[0][0]]

print("\n===== ICD Recommendation =====")
print("Disease :", result["Disease"])
print("ICD Code:", result["ICD10"])
print("Description:", result["Description"])