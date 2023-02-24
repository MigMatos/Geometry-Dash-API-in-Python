import asyncio
from api.gd_target_api import get_search_profile,get_info_profile,search_level
#Search profile str
#First data is username and 'robtop' is the GDPS (you can select another GDPS custom)
json_data = asyncio.run(get_search_profile("obeygdbot","robtop"))
print(json_data)
#Search profile id account
#First data is ID Account and 'robtop' is the GDPS (you can select another GDPS custom)
json_data = asyncio.run(get_info_profile("17255842","robtop"))
print(json_data)

#Search levels
#First data is STR or IDlevel and 'robtop' is the GDPS (you can select another GDPS custom)
data = asyncio.run(search_level("nine circles","robtop"))
print(data)
