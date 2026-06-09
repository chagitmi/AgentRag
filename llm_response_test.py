from nodes.llm_response_node import LLMResponseNode

node = LLMResponseNode()

response = node.generate_response(
    user_request="תציגי לי חתימה למייל",
    route_result={
        "route": "signature",
        "confidence": 1
    },
    worker_result={
        "found": True,
        "image_path": "./images/email_signature.png",
        "similarity": 0.87
    }
)

print(response)