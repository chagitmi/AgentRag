import os

from embedding_model import CLIPEmbeddingModel
from chroma_manager import ChromaManager

from config import (
    CHROMA_DB_PATH,
    COLLECTION_NAME,
    IMAGES_FOLDER,
    CLIP_MODEL_NAME,
    CLIP_PRETRAINED
)


def ingest_images():

    embedding_model = CLIPEmbeddingModel(
        model_name=CLIP_MODEL_NAME,
        pretrained=CLIP_PRETRAINED
    )

    chroma_manager = ChromaManager(
        db_path=CHROMA_DB_PATH,
        collection_name=COLLECTION_NAME
    )

    image_files = os.listdir(IMAGES_FOLDER)

    for image_file in image_files:

        image_path = os.path.join(IMAGES_FOLDER, image_file)

        print(f"Ingesting: {image_file}")

        embedding = embedding_model.encode_image(image_path)

        chroma_manager.add_image(
            image_id=image_file,
            embedding=embedding,
            metadata={
                "image_path": image_path
            }
        )

    print("Finished ingesting images.")


if __name__ == "__main__":

    ingest_images()