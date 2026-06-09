from tools.asset_search_tool import AssetSearchTool

tool = AssetSearchTool()

query = input("What asset are you looking for? ")

result = tool.search_business_asset(query)

print(result)