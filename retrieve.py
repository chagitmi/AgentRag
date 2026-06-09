from embedding_model import CLIPEmbeddingModel
from chroma_manager import ChromaManager

from config import (
    CHROMA_DB_PATH,
    COLLECTION_NAME,
    CLIP_MODEL_NAME,
    CLIP_PRETRAINED
)


class ImageRetriever:

    def __init__(self):

        self.embedding_model = CLIPEmbeddingModel(
            model_name=CLIP_MODEL_NAME,
            pretrained=CLIP_PRETRAINED
        )

        self.chroma_manager = ChromaManager(
            db_path=CHROMA_DB_PATH,
            collection_name=COLLECTION_NAME
        )

    def search(self, query, top_k=3):

        query_embedding = self.embedding_model.encode_text(query)

        results = self.chroma_manager.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        ids = results["ids"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        formatted_results = []

        for i in range(len(ids)):

            similarity = 1 / (1 + distances[i])

            formatted_results.append({
                "id": ids[i],
                "path": metadatas[i]["image_path"],
                "distance": distances[i],
                "similarity": similarity
            })

        best_result = formatted_results[0]

        return {
            "best_match": best_result,
            "all_results": formatted_results
        }