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
#'robtop' is the GDPS (you can select another GDPS custom)
#Query is the query in search level
#Page is the page selected
data = asyncio.run(search_level(server="robtop",query='"str":"Nine Circles"',page=0))
print(data)
#Send messages
#'robtop' is the GDPS (you can select another GDPS custom)
#title is the title of message
#message is the body of message
#accountIDtarget is the IDaccount is you sending message
data = asyncio.run(send_message(server="robtop",title="Hi",message="Hello world",accountIDtarget=16))
#return 1 if message send is sucess, 0 is error
print(data)

