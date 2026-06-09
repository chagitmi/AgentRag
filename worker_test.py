from nodes.asset_worker_node import AssetWorkerNode

worker = AssetWorkerNode()

asset_type = input("Asset Type: ")

result = worker.execute(asset_type)

print(result)
