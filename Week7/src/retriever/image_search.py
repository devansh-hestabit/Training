import os
import pickle
import faiss
import numpy as np
import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

IMAGE_DIR = "src/data/images"
CLIP_EMBED_PKL = "src/data/embeddings/clip_embeddings.pkl"

device = "cuda" if torch.cuda.is_available() else "cpu"
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

with open(CLIP_EMBED_PKL, "rb") as f:
    data = pickle.load(f)

image_records = data["image_embeddings"]
text_records = data["text_embeddings"]

image_vectors = np.array([r["embedding"] for r in image_records]).astype("float32")
text_vectors = np.array([r["embedding"] for r in text_records]).astype("float32")

dim = image_vectors.shape[1]

image_index = faiss.IndexFlatIP(dim)
image_index.add(image_vectors)

text_index = faiss.IndexFlatIP(dim)
text_index.add(text_vectors)

def embed_text(query: str):
    inputs = processor(
        text=[query],
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=77
    ).to(device)

    with torch.no_grad():
        output = model.get_text_features(**inputs)
        emb = output.pooler_output #Pooler output is the final embedding vector for the input text
        emb = emb / emb.norm(dim=-1, keepdim=True)

    return emb.cpu().numpy().astype("float32")

def embed_image(image_path: str):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt").to(device)

    with torch.no_grad():
        output = model.get_image_features(**inputs)
        emb = output.pooler_output
        emb = emb / emb.norm(dim=-1, keepdim=True)

    return emb.cpu().numpy().astype("float32")

def text_to_image(query: str, top_k: int = 5):
    query_vec = embed_text(query)
    k = min(top_k, len(image_records))
    scores, indices = image_index.search(query_vec, k)

    results = []
    for rank, idx in enumerate(indices[0]):
        rec = image_records[idx]
        results.append({
            "rank": rank + 1,
            "score": float(scores[0][rank]),
            "image_id": rec["id"],
            "image_path": os.path.join(IMAGE_DIR, rec["id"]),
            "metadata": rec["metadata"]
        })

    return results

def image_to_image(image_path: str, top_k: int = 5):
    query_vec = embed_image(image_path)
    k = min(top_k, len(image_records))
    scores, indices = image_index.search(query_vec, k)

    results = []
    for rank, idx in enumerate(indices[0]):
        rec = image_records[idx]
        results.append({
            "rank": rank + 1,
            "score": float(scores[0][rank]),
            "image_id": rec["id"],
            "image_path": os.path.join(IMAGE_DIR, rec["id"]),
            "metadata": rec["metadata"]
        })

    return results

def image_to_text(image_path: str, top_k: int = 3):
    query_vec = embed_image(image_path)
    k = min(top_k, len(text_records))
    scores, indices = text_index.search(query_vec, k)
    results = []
    for rank, idx in enumerate(indices[0]):
        rec = text_records[idx]
        results.append({
            "rank": rank + 1,
            "score": float(scores[0][rank]),
            "image_id": rec["id"],
            "ocr_text": rec["metadata"]["ocr_text"],
            "caption": rec["metadata"].get("caption"),
            "metadata": rec["metadata"]
        })

    return results

if __name__ == "__main__":
    print("\n--- TEXT → IMAGE ---")
    results = text_to_image("dog")
    for r in results:
        print(r)

    sample_image = results[0]["image_path"]

    print("\n--- IMAGE → IMAGE ---")
    for r in image_to_image(sample_image):
        print(r)

    print("\n--- IMAGE → TEXT ---")
    for r in image_to_text(sample_image):
        print(r["ocr_text"][:300])