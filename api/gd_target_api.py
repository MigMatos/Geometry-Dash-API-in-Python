import requests
import json
from api.api_profiles import get_profile
from api.api_level import get_level

servers_target = "api/servers.json"
with open(servers_target,'r',encoding="utf8") as f:
    servers_target = json.load(f)

profiles_target= ["getGJUsers20.php","getGJUserInfo20.php"]
headers = {'User-Agent': ''}

async def get_search_profile(profile,server="robtop"):
    data = {
        "gameVersion": servers_target[server]['gameVersion'],
        "binaryVersion": servers_target[server]['binaryVersion'],
        "secret": servers_target[server]['secret'],
        "str": f"{profile}"
    }
    try:req = requests.post(f"{servers_target[server]['link']}{profiles_target[0]}", data=data, headers=headers)
    except requests.exceptions.RequestException as e:raise Exception(e)
    profile = await get_profile(str(req.text)) 
    return profile

async def get_info_profile(ID,server="robtop"):
    try:ID = int(ID)
    except:raise Exception("01_accountid")
    data = {
        "gameVersion": servers_target[server]['gameVersion'],
        "binaryVersion": servers_target[server]['binaryVersion'],
        "secret": servers_target[server]['secret'],
        "targetAccountID": f"{ID}"
    }
    try:req = requests.post(f"{servers_target[server]['link']}{profiles_target[1]}", data=data, headers=headers)
    except requests.exceptions.RequestException as e:raise Exception(e)
    profile = await get_profile(str(req.text)) 
    return profile

level_page = "getGJLevels21.php"

async def search_level(str_data="",server="robtop",diff="-",len="-",page="0",total="0",featured="0",original="0",twoPlayer="0",coins="0",epic="0"):
    data = {
        "gameVersion": servers_target[server]['gameVersion'],
        "binaryVersion": servers_target[server]['binaryVersion'],
        "secret": servers_target[server]['secret'],
        "type": "0",
        "str": str_data,
        "diff": diff,
        "len": len,
        "page": page,
        "total": total,
        "featured": featured,
        "original": original,
        "twoPlayer": twoPlayer,
        "coins": coins,
        "epic": epic
    }
    try:req = requests.post(f"{servers_target[server]['link']}{level_page}", data=data, headers=headers)
    except requests.exceptions.RequestException as e:raise Exception(e)
    level = await get_level(str(req.text)) 
    return level
