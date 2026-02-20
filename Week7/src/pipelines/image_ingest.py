import os
import cv2
import pytesseract
import pickle
import torch
from PIL import Image
from pdf2image import convert_from_path
from transformers import BlipProcessor, BlipForConditionalGeneration

RAW_IMAGE_DIR = "src/data/raw_images"
IMAGE_STORE_DIR = "src/data/images"
OCR_STORE_DIR = "src/data/ocr"
OCR_PKL_PATH = "src/data/ocr/ocr_data.pkl"

os.makedirs(IMAGE_STORE_DIR, exist_ok=True)
os.makedirs(OCR_STORE_DIR, exist_ok=True)

# -----------------------------
# Load BLIP model
# -----------------------------
device = "cuda" if torch.cuda.is_available() else "cpu"

blip_processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
blip_model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
).to(device)


def ocr_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return pytesseract.image_to_string(gray).strip()


def generate_caption(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = blip_processor(image, return_tensors="pt").to(device)

    with torch.no_grad():
        out = blip_model.generate(**inputs, max_new_tokens=30)

    caption = blip_processor.decode(out[0], skip_special_tokens=True)
    return caption


def ingest_images():
    """
    Ingest images and scanned PDFs:
    - Save images
    - Extract OCR
    - Generate BLIP captions
    - Store structured metadata in PKL
    """

    records = []

    for file in os.listdir(RAW_IMAGE_DIR):
        path = os.path.join(RAW_IMAGE_DIR, file)

        # ---------- Image files ----------
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            img = Image.open(path)
            img_save_path = os.path.join(IMAGE_STORE_DIR, file)
            img.save(img_save_path)

            ocr_text = ocr_image(img_save_path)
            caption = generate_caption(img_save_path)

            records.append({
                "image_id": file,
                "image_path": img_save_path,
                "ocr_text": ocr_text,
                "caption": caption,
                "source": file,
                "page": None,
                "type": "image"
            })

        # ---------- Scanned PDFs ----------
        elif file.lower().endswith(".pdf"):
            pages = convert_from_path(path)

            for i, page in enumerate(pages):
                img_name = f"{file}_page_{i+1}.png"
                img_path = os.path.join(IMAGE_STORE_DIR, img_name)
                page.save(img_path)

                ocr_text = ocr_image(img_path)
                caption = generate_caption(img_path)

                records.append({
                    "image_id": img_name,
                    "image_path": img_path,
                    "ocr_text": ocr_text,
                    "caption": caption,
                    "source": file,
                    "page": i + 1,
                    "type": "scanned_pdf"
                })

    # -------- Save multimodal ingestion data --------
    with open(OCR_PKL_PATH, "wb") as f:
        pickle.dump(records, f)

    print("✅ Image ingestion completed")
    print(f"🧠 Records stored: {len(records)}")


if __name__ == "__main__":
    ingest_images()