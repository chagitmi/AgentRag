from tools.asset_search_tool import AssetSearchTool
from utils.logger_config import logger


class AssetWorkerNode:

    def __init__(self):
        self.tool = AssetSearchTool()

    def execute(self, route, query):
        logger.info(f"Route: {route}")
        logger.info(f"Search Query: {query}")
       
        result = self.tool.search_business_asset(query)

        return result

    def build_search_query(
        self,
        user_request,
        route
    ):

        mapping = {
            "email_signature": "email signature",
            "official_letter": "official document signature",
            "business_card": "business card logo",
            "logo": "company logo"
        }

        if route in mapping:
            return mapping[route]

        return user_request