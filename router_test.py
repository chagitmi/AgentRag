from nodes.router_node import RouterNode

router = RouterNode()

request = input("מה תרצי לעשות? ")

route = router.route(request)

print(f"Route: {route}")
