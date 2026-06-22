import os
import json

from PIL import Image
import chromadb
from sentence_transformers import SentenceTransformer

from open_clip import create_model_and_transforms


# =========================
# Config
# =========================

IMAGE_FOLDER = "./images"
METADATA_FOLDER = "./metadata"
DB_PATH = "./chroma_db"

# =========================
# Models
# =========================

text_model = SentenceTransformer("all-MiniLM-L6-v2")

clip_model, _, preprocess = create_model_and_transforms("ViT-B-32", pretrained="laion2b_s34b_b79k")


# =========================
# Chroma DB
# =========================

client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_or_create_collection(
    name="business_assets"
)


# =========================
# Load metadata
# =========================

def load_metadata(file_name):
    meta_file = file_name.replace(".png", ".json")

    path = os.path.join(METADATA_FOLDER, meta_file)

    if not os.path.exists(path):
        return {"description": "", "tags": []}

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# =========================
# Build embedding
# =========================

def build_text_embedding(metadata):
    text = metadata.get("description", "") + " " + " ".join(metadata.get("tags", []))
    return text_model.encode(text).tolist()


# =========================
# Ingest
# =========================

def ingest():

    for img_file in os.listdir(IMAGE_FOLDER):

        if not img_file.endswith(".png"):
            continue

        img_path = os.path.join(IMAGE_FOLDER, img_file)

        metadata = load_metadata(img_file)

        # ---- IMAGE embedding (CLIP)
        image = preprocess(Image.open(img_path)).unsqueeze(0)
        image_embedding = clip_model.encode_image(image).detach().numpy()[0].tolist()

        # ---- TEXT embedding (metadata)
        text_embedding = build_text_embedding(metadata)

        # ---- combine embeddings
        combined_embedding = [
            (a + b) / 2
            for a, b in zip(image_embedding, text_embedding)
        ]

        collection.add(
            embeddings=[combined_embedding],
            ids=[img_file],
            documents=[metadata.get("description", "")],
            metadatas=[{
                "file": img_file,
                "type": metadata.get("type"),
                "tags": json.dumps(metadata.get("tags", []), ensure_ascii=False),
                "description": metadata.get("description", "")
            }],
            ids=[img_file]
        )

        print(f"Ingested: {img_file}")


if __name__ == "__main__":
    ingest()