import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import pickle

# Load ICD data
df = pd.read_csv("medical_docs/icd10.csv")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings
embeddings = model.encode(df["Description"].tolist())

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index
faiss.write_index(index, "vector_db/icd10.index")

# Save dataframe
with open("vector_db/icd10.pkl", "wb") as f:
    pickle.dump(df, f)

print("Vector database created successfully!")