from retrieve import ImageRetriever
from config import SIMILARITY_THRESHOLD
from utils.logger_config import logger


class AssetSearchTool:

    def __init__(self):

        self.retriever = ImageRetriever()

    def search_business_asset(self, query):

        logger.info(f"Asset search query: {query}")

        results = self.retriever.search(query)

        best_match = results["best_match"]

        similarity = best_match["similarity"]

        logger.info(f"Best match: {best_match}")

        if similarity >= SIMILARITY_THRESHOLD:

            return {
                "found": True,
                "image_path": best_match["path"],
                "image_id": best_match["id"],
                "similarity": similarity
            }

        return {
            "found": False,
            "image_path": None,
            "image_id": None,
            "similarity": similarity
        }