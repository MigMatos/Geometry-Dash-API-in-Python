from api.utils_api_gd import messageState,commentHistoryState,friendState
#import asyncio 

#response = """""""
#for i in range(1):
    #strres = response.split(f':')
    #print(strres)

api_replace = ["1:",":2:",":3:",":4:",":5:",":6:",":8:",":9:",":10:",":11:",":12:",":13:",":14:",":15:",":16:",":17:",":18:",":19:",":25:",":26:",":27:",":28:",":29:",":30:",":31:",":35:",":36:",":37:",":38:",":39:",":40:",":41:",":42:",":43:",":44:",":45:",":46:",":47:",":48:",":49:",":50:"]

structure_level = {
    1:"username",
    2:"playerID",
    3:"stars",
    4:"demons",
    6:"rank_unused",
    7:"accountHighlight",
    8:"cp",
    9:"iconID",
    10:"col1",
    11:"col2",
    13:"coins",
    14:"iconType",
    15:"special_unused",
    16:"accountID",
    17:"userCoins",
    18:"messages",
    19:"friendRequests",
    20:"youtube",
    21:"icon",
    22:"ship",
    23:"ball",
    24:"ufo",
    25:"wave",
    26:"robot",
    27:"streak",
    28:"glow",
    29:"isRegistered",
    30:"rank",
    31:"friend_state",
    38:"messages_state",
    39:"friendRequests_state",
    40:"newFriend_state",
    41:"newFriendRequest_state",
    42:"age_levelScore",
    43:"spider",
    44:"twitter",
    45:"twitch",
    46:"diamonds",
    48:"deathEffect",
    49:"moderator",
    50:"commentHistory"
    }

i=0
async def get_profile(response):
    try:index = response.index('1:')
    except:raise Exception("02_nodata")
    response=response[index:]
    strres = response.split(f':')
    #print(strres)
    for structure in structure_level.items():
        api_num, api_str = structure

        for i in range(0,len(strres),2):
            if str(strres[i]) == str(api_num):
                strres[i] = api_str
    text_api = ""
    range_api = 100
    for i in range(0,range_api,2):
        try:
            if strres[i] == "messages":strres[i+1]=await messageState(int(strres[i+1]))
            elif strres[i] == "commentHistory":strres[i+1]=await commentHistoryState(int(strres[i+1]))
            elif strres[i] == "friendRequests":strres[i+1]=await friendState(int(strres[i+1]))
            elif strres[i+1] == "":strres[i+1]="<None>"
            try:strres[i+1] = int(strres[i+1])
            except ValueError:strres[i+1] = f'"{strres[i+1]}"'
            text_api = f'"{strres[i]}":{strres[i+1]},\n' + text_api
        except IndexError:
            if text_api=="":raise Exception("02_nodata")
            text_api = text_api[:-2] + ""
            break
    text_api = '{\n'+f'{text_api}'+'\n}'
    return text_api

#asyncio.run(get_profile(response))
