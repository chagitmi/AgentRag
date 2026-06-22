from nodes.llm_router_node import LLMRouterNode
from nodes.asset_worker_node import AssetWorkerNode
from nodes.llm_response_node import LLMResponseNode
from utils.logger_config import logger
import os

router = LLMRouterNode()
worker = AssetWorkerNode()
response_node = LLMResponseNode()

user_request = input("מה תרצי לעשות? ")

logger.info(f"User Request: {user_request}")

route_result = router.route(user_request)

logger.info(f"Router Result: {route_result}")

print("\nROUTE:", route_result)

confidence = route_result["confidence"]

# if confidence < 0.8:

#     clarification = response_node.generate_clarification()

#     print("\nFINAL OUTPUT:\n")
#     print(clarification)

#     exit()
from utils.query_builder import build_asset_query

asset_query = build_asset_query(user_request, route_result["route"])

logger.info(f"Final Asset Query: {asset_query}")

worker_result = worker.execute(
    route_result["route"],
    asset_query
)

#worker_result = worker.execute(
#    route_result["asset_query"]  
#)

if worker_result.get("found"):
    
    image_path = worker_result.get("image_path")

if image_path:
    image_path = image_path = "/static/images/" + image_path.split("\\")[-1]
    logger.info(f"Opening image: {image_path}")
    
    os.startfile(image_path)
    
logger.info(f"Worker Result: {worker_result}")

final_response = response_node.generate_response(
    user_request=user_request,
    route_result=route_result,
    worker_result=worker_result
)

logger.info("Response generated successfully")

print("\nFINAL OUTPUT:\n")
print(final_response)