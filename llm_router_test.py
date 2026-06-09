from nodes.llm_router_node import LLMRouterNode

router = LLMRouterNode()

request = input("Request: ")

result = router.route(request)

print(result)
print("Route:", result["route"])
print("Confidence:", result["confidence"])