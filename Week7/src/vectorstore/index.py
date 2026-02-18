import os
import pickle
import faiss
import numpy as np

EMBEDDINGS_PATH = "src/embeddings/embeddings.pkl"
VECTORSTORE_DIR = "src/vectorstore"
INDEX_PATH = "src/vectorstore/index.faiss"

os.makedirs(VECTORSTORE_DIR, exist_ok=True)

def build_faiss_index():
    with open(EMBEDDINGS_PATH, "rb") as f:
        embeddings, texts, metadata = pickle.load(f)

    embeddings = np.array(embeddings).astype("float32") #FAISS requires float32 format

    dimension = embeddings.shape[1] #number of dimensions in the embedding vectors
    index = faiss.IndexFlatL2(dimension) #L2 distance metric for similarity search for fast indexing and searching
    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)

    print("FAISS index created")
    print(f"Vectors indexed: {index.ntotal}")
    print(f"Vector dimension: {dimension}")


if __name__ == "__main__":
    build_faiss_index()
