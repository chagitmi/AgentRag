from tools.asset_search_tool import AssetSearchTool
from utils.logger_config import logger


class AssetWorkerNode:

    def __init__(self):
        self.tool = AssetSearchTool()

    def execute(self, query):

        logger.info(f"Searching assets for query: {query}")

        result = self.tool.search_business_asset(query)

        logger.info(f"Search result: {result}")

        return result