import requests
from api.api_phpread import change_key_names, get_json_from_page
from api.gd_target_api import search_level

request_session = requests.Session()

async def post_name_demonlist(name_level:str,timeout=3):
    name_level = name_level.strip()
    headers = {'User-Agent': '','Content-Type':'application/json'}
    request_link = "https://pointercrate.com/api/v2/demons/?name={}".format(name_level.replace(" ","%20"))
    req = request_session.get(request_link, headers=headers, timeout=timeout)
    return req.json()

async def get_demonlist_rated(page:int,results=50,gdps="robtop",timeout=3):
    after,before = (((results*(page))-results),(results*(page)))
    if gdps == "robtop":
        headers = {'User-Agent': '','Content-Type':'application/json'}
        request_link = "https://pointercrate.com/api/v2/demons/listed?after={}&before={}".format(after,before)
        req = request_session.get(request_link, headers=headers, timeout=timeout)
        return req.json(),150,3
    elif gdps == "custom_gdps":
        return "Hello world"
        #You can set your custom code demonlist here
    else:raise Exception("gdps not found")



