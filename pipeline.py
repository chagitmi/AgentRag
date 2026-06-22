from nodes.llm_router_node import LLMRouterNode
from nodes.asset_worker_node import AssetWorkerNode
from nodes.llm_response_node import LLMResponseNode


router = LLMRouterNode()
worker = AssetWorkerNode()
llm = LLMResponseNode()


def run_pipeline(user_message):

    route_result = router.route(user_message)

    worker_result = worker.execute(
        route_result["route"],
        route_result.get("asset_query", user_message)
    )

    final = llm.generate_response(
        user_message,
        route_result,
        worker_result
    )

    return {
        "text": final,
        "image": worker_result["image_path"]
    }