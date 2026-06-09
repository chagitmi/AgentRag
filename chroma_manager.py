import chromadb


class ChromaManager:

    def __init__(self, db_path, collection_name):

        self.client = chromadb.PersistentClient(path=db_path)

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_image(self, image_id, embedding, metadata):

        self.collection.add(
            ids=[image_id],
            embeddings=[embedding],
            metadatas=[metadata]
        )