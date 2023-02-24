from api.utils_api_gd import messageState,commentHistoryState,friendState

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
    47:"deathEffect",
    48:"deathEffect",
    49:"moderator",
    50:"commentHistory"
    }
i=0
async def get_profile(response,profile=""):
    try:index_data = str(response.lower()).index('1:{}'.format(profile))
    except:raise Exception("02_nodata")
    final = None
    try:final = index_data + str(response[index_data:]).index('|')
    except:pass
    if final == None:
        try:final = index_data + str(response[index_data:]).index('#')
        except:pass
    response = response[index_data:final]
    strres = response.split(f':')
    text_api = ""
    for i in range(0,len(strres),2):
        try:
            strres[i] = structure_level[int(strres[i])]
            if strres[i] == "messages":strres[i+1]=await messageState(int(strres[i+1]))
            elif strres[i] == "commentHistory":strres[i+1]=await commentHistoryState(int(strres[i+1]))
            elif strres[i] == "friendRequests":strres[i+1]=await friendState(int(strres[i+1]))
            elif strres[i+1] == "":strres[i+1]="<None>"
            try:text_api = text_api + f'"{strres[i]}":{int(strres[i+1])},\n'
            except:text_api = text_api + f'"{strres[i]}":"{strres[i+1]}",\n'
        except KeyError:text_api = text_api + f'"{strres[i]}":"{strres[i+1]}",\n'
        except IndexError:break
    text_api = text_api[:-2] + ""
    text_api = '{\n'+f'{text_api}'+'\n}'
    return text_api