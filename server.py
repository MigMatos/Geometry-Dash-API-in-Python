import asyncio
from api.gd_target_api import get_search_profile,get_info_profile,search_level
#Search profile str
json_data = asyncio.run(get_search_profile("obeygdbot","robtop"))
print(json_data)
#Search profile id account
json_data = asyncio.run(get_info_profile("17255842","robtop"))
print(json_data)

#EXPERIMENTAL SEARCH LEVEL (BROKEN JSON)
#data = asyncio.run(search_level("nine circles"))
#print(data)