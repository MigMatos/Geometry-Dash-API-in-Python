import base64
import itertools
import os
import requests
import json
from api.api_profiles import get_profile
from api.api_level import get_level

def get_servers_target():
    """Return JSON for all GDPS servers settings"""
    servers_target = "api/servers.json"
    with open(servers_target,'r',encoding="utf8") as f:
        return json.load(f)

servers_target = "api/servers.json"
with open(servers_target,'r',encoding="utf8") as f:
    servers_target = json.load(f)


def get_pages(gdps:str,target:str):
    """Return STR for page selected <- target is name for page"""
    path = "api/gdps/{}/settings_api.json".format(gdps)
    isExist = os.path.exists(path)
    if isExist == False:path = "api/default_json/settings_api.json"
    with open(path,'r',encoding="utf8") as f:
        pages_target = json.load(f)
    try:return pages_target["pages"][target]
    except:
        with open("api/default_json/settings_api.json",'r',encoding="utf8") as f:
            pages_target = json.load(f)
            try:return pages_target["pages"][target]
            except:raise Exception("Page not found: {} in server: {}".format(target,gdps))


def get_alias_fromkey(gdps:str,target:str) -> str: 
    """Return STR alias for page selected <- target is name for page"""
    path = "api/gdps/{}/settings_api.json".format(gdps)
    isExist = os.path.exists(path)
    if isExist == False:path = "api/default_json/settings_api.json"
    with open(path,'r',encoding="utf8") as f:pages_target = json.load(f)
    try:return str(pages_target["alias"][target])
    except:
        with open("api/default_json/settings_api.json",'r',encoding="utf8") as f:
            pages_target = json.load(f)
            try:return str(pages_target["alias"][target])
            except:raise Exception("Alias not found: {} in server: {}".format(target,gdps))

profiles_target= ["getGJUsers","getGJUserInfo"]
headers = {'User-Agent': '','Connection': 'Close'}
request_loggin = requests.Session()

async def get_search_profile(profile,server="robtop"):
    if server in {"custom_22_gdps"}:
        data = {
        "gameVersion": servers_target[server]['gameVersion'],
        "binaryVersion": servers_target[server]['binaryVersion'],
        "secret": servers_target[server]['secret'],
        "str": f"{profile}",
        "gjp2": servers_target[server]['gjp2'],
        "accountID": servers_target[server]['accountID'],
        "page": "0",
        "sessionID": ""
    }
    else:
        data = {
        "gameVersion": servers_target[server]['gameVersion'],
        "binaryVersion": servers_target[server]['binaryVersion'],
        "secret": servers_target[server]['secret'],
        "str": f"{profile}",
    }
    try:req = request_loggin.post(f"{servers_target[server]['link']}{get_pages(server,profiles_target[0])}", data=data, headers=headers)
    except requests.exceptions.RequestException as e:raise Exception(e)
    profile = await get_profile(str(req.text),profile) 
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
    try:req = request_loggin.post(f"{servers_target[server]['link']}{get_pages(server,profiles_target[1])}", data=data, headers=headers)
    except requests.exceptions.RequestException as e:raise Exception(e)
    profile = await get_profile(str(req.text)) 
    return profile

level_page = ["getGJLevels"]

async def search_level(server="robtop",query='"str":""',page=0):
    data = "{" + '"gameVersion":'+str(servers_target[server]['gameVersion'])+',"binaryVersion":'+str(servers_target[server]['binaryVersion'])+',"secret":'+ f'"{servers_target[server]["secret"]}"' + f',{query},"page":{page}' + "}"
    data = json.loads(data)
    try:req = request_loggin.post(f"{servers_target[server]['link']}{get_pages(server,level_page[0])}", data=data, headers=headers,timeout=3)
    except requests.exceptions.RequestException as e:raise TypeError(e)
    level = await get_level(str(req.text),server)
    return level


msg_tar = ["uploadGJMessage"]


async def send_message(server="robtop",title="Hi",message="Hello world",accountIDtarget=0):
    key = "14251"
    def xor_cipher(string: str, key: str) -> str:
        return ("").join(chr(ord(x) ^ ord(y)) for x, y in zip(string, itertools.cycle(key)))
    code = xor_cipher(code,key)
    data = {
        "gameVersion": servers_target[server]['gameVersion'],
        "binaryVersion": servers_target[server]['binaryVersion'],
        "accountID": servers_target[server]['accountID'],
        "gjp": servers_target[server]['gjp'],
        "toAccountID": accountIDtarget,
        "subject": base64.b64encode(title.encode()).decode(),
        "body": base64.urlsafe_b64encode(message.encode()).decode(),
        "secret": servers_target[server]['secret']
    }
    try:dd_data = request_loggin.post(f"{servers_target[server]['link']}{get_pages(server,msg_tar[0])}", data=data, headers=headers)
    except requests.exceptions.RequestException as e:raise Exception(e)
    if dd_data.text in {1,"1"}:return True
    else:return False
