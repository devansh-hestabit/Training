# MULTIMODAL-RAG ARCHITECTURE

## Overview
The system extends text-based RAG to support images, enabling retrieval and understanding
across vision + language.

The pipeline supports:
- OCR text extraction
- Image captioning
- Vision-language embeddings
- Multimodal similarity search


## Flow
```

Raw Images / Scanned PDFs
        |
        v
+----------------------+
| Image Ingestion      |
|----------------------|
| - OCR (Tesseract)    |
| - Captioning (BLIP)  |
| - Metadata creation |
+----------------------+
        |
        v
+----------------------+
| Multimodal Embedding |
|----------------------|
| - CLIP Image Embed   |
| - CLIP Text Embed    |
|   (OCR + Caption)   |
+----------------------+
        |
        v
+----------------------+
| Vector Index (FAISS) |
|----------------------|
| - Image vectors      |
| - Text vectors       |
+----------------------+
        |
        v
+----------------------+
| Multimodal Retrieval |
|----------------------|
| - Text → Image       |
| - Image → Image      |
| - Image → Text       |
+----------------------+

```

## Key Components

### 1. Image Ingestion (`image_ingest.py`)
Responsible for one-time preprocessing:
- Loads PNG / JPG / scanned PDFs
- Extracts OCR text using Tesseract
- Generates image captions using BLIP
- Stores structured records in `ocr_data.pkl`

Each record contains:
- image_id
- image_path
- ocr_text
- caption
- source
- page
- type


### 2. Multimodal Embeddings (`clip_embedder.py`)
Uses CLIP (ViT-B/32) to align images and text into a shared embedding space.

- Image embeddings → visual semantics
- Text embeddings → caption + OCR (truncated to 77 tokens)
- Normalized embeddings for cosine similarity
- Stored in `clip_embeddings.pkl`


### 3. Vector Store
- FAISS IndexFlatIP (cosine similarity)
- Separate indexes for:
  - Image embeddings
  - Text embeddings


### 4. Multimodal Retrieval (`image_search.py`)
Supports three query modes:

#### a) Text → Image
Example:

Query: "bar chart showing expenditure"

Returns most relevant images with similarity scores.

#### b) Image → Image
Example:

Query: uploaded chart image

Returns visually similar images.

#### c) Image → Text
Example:

Query: uploaded chart image

Returns OCR + caption text explaining the image.

Top-k control determines whether a single explanation or multiple contexts are returned.


## Limitations
- BLIP captions may be generic
- OCR quality depends on image clarity
