import os
import pickle
import torch
import numpy as np
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

IMAGE_DIR = "src/data/images"
INGEST_PKL_PATH = "src/data/ocr/ocr_data.pkl"
CLIP_EMBED_PKL = "src/data/embeddings/clip_embeddings.pkl"

os.makedirs("src/data/embeddings", exist_ok=True)
device = "cuda" if torch.cuda.is_available() else "cpu"

model = CLIPModel.from_pretrained(
    "openai/clip-vit-base-patch32"
).to(device)

processor = CLIPProcessor.from_pretrained(
    "openai/clip-vit-base-patch32"
)

def normalize(x: torch.Tensor):
    return x / x.norm(dim=-1, keepdim=True) #L2 normalization dim = -1 means normalize across the feature dimension, keepdim=True keeps the original shape for broadcasting

def build_text_input(ocr_text: str, caption: str):
    text = f"{caption}. {ocr_text}" if ocr_text else caption
    return text.strip()

def generate_clip_embeddings():

    with open(INGEST_PKL_PATH, "rb") as f:
        records = pickle.load(f)

    image_embeddings = []
    text_embeddings = []

    for record in records:
        image_path = record["image_path"]

        if not os.path.exists(image_path):
            continue

        image = Image.open(image_path).convert("RGB")
        image_inputs = processor(
            images=image,
            return_tensors="pt"
        ).to(device)

        with torch.no_grad():
            img_output = model.get_image_features(**image_inputs)
            img_emb = normalize(img_output.pooler_output)

        combined_text = build_text_input(
            record.get("ocr_text", ""),
            record.get("caption", "")
        )

        text_inputs = processor(
            text=[combined_text],
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=77  #CLIP's maximum token length for text inputs
        ).to(device)

        with torch.no_grad():
            txt_output = model.get_text_features(**text_inputs)
            txt_emb = normalize(txt_output.pooler_output)

        image_embeddings.append({
            "id": record["image_id"],
            "embedding": img_emb.cpu().numpy()[0], #.cpu() moves the tensor to CPU memory, .numpy() converts it to a NumPy array, [0] extracts the single embedding vector from the batch
            "metadata": record
        })

        text_embeddings.append({
            "id": record["image_id"],
            "embedding": txt_emb.cpu().numpy()[0],
            "metadata": record
        })
    with open(CLIP_EMBED_PKL, "wb") as f:
        pickle.dump(
            {
                "image_embeddings": image_embeddings,
                "text_embeddings": text_embeddings
            },
            f
        )

    print("CLIP embeddings generated successfully")
    print(f"Image embeddings: {len(image_embeddings)}")
    print(f"Text embeddings: {len(text_embeddings)}")

if __name__ == "__main__":
    generate_clip_embeddings()