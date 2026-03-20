# /memory/vector_store.py

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class VectorStore:

    def __init__(self, dim: int = 384):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.dim = dim

        # FAISS index (L2 distance)
        self.index = faiss.IndexFlatL2(dim)

        # Store original texts
        self.texts = []

    def clear(self):
        """
        Reset vector memory
        """
        self.index.reset()
        self.texts = []

    def _embed(self, text: str):

        embedding = self.model.encode([text])[0]
        return np.array(embedding).astype("float32")

    def add(self, text: str):

        vector = self._embed(text)

        self.index.add(np.array([vector]))
        self.texts.append(text)

    def search(self, query: str, k: int = 3):

        if len(self.texts) == 0:
            return []

        query_vector = self._embed(query)

        distances, indices = self.index.search(
            np.array([query_vector]),
            k
        )

        results = []

        for idx in indices[0]:
            if idx < len(self.texts):
                results.append(self.texts[idx])

        return results

    def size(self):
        return len(self.texts)


def create_vector_store():

    return VectorStore()