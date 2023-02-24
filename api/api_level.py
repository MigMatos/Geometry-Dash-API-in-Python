import json
import os
from api.utils_api_gd import convert_bool, decode_str,get_demon, get_length, get_diff_bool, get_diff_num,decode_password,get_gameversion
from api.api_songs import get_song

structure_level = {1:"id",2:"name",3:"description",4:"data_level",5:"version",6:"playerID",8:"diff_rated",9:"diff_num",10:"downloads",11:"unused_11",12:"officialSong",13:"gameVersion",14:"likes",15:"length",16:"dislikes",17:"demon",18:"stars",19:"featured_score",25:"auto",26:"unused_26",27:"password",28:"uploadDate",29:"updateDate",30:"copiedID",31:"twoPlayer",35:"songID",36:"extraString",37:"coins",38:"verifiedCoins",39:"starsRequested",40:"ldm",41:"dailyNumber",42:"epic",43:"diff_demon",44:"isGauntlet",45:"objects",46:"editorTime",47:"editorTime_Copy",48:"unused_48"}

i=0
def convert_profile_author(data):
    txt = "{\n"
    for datas in data:
        list_str = datas.split('|')
        for i in list_str:
            data = i.split(':')
            txt = txt + '"{}":'.format(data[0])+'{"playerID":"'+data[0]+'","author":"'+data[1]+'","accountID":"'+data[2]+'"}\n,'
    txt = txt[:-1] + "}"
    return txt

async def get_diamonds(stars):
    if stars < 2:return 0
    else:return stars+2

async def get_cp(featured_score:int,is_epic:int,stars:int):
    cp = 0
    if featured_score >= 1:cp = cp + 1
    if is_epic >= 1:cp = cp + 1
    if stars >= 1:cp = cp + 1
    return cp

async def get_orbs(stars):
    orbs_get = {1:0,2:50,3:75,4:125,5:175,6:225,7:275,8:350,9:425,10:500}
    stars = int(stars)
    if stars >= 1:
        try:return orbs_get[stars]
        except KeyError:
            if stars < 0:return 0
            elif stars > 10:return 500 
    else:return 0

async def convert_song(officialSong:int,songID:int,data:str,gdps):
    data = await get_song(data,songID,officialSong)
    return data


async def get_difficulty_short_name(is_rated,name_diff,is_auto,is_demon):
    if is_rated == False:return "unrated"
    if is_demon==True:return "demon"
    elif is_auto==True:return "auto"
    else:return name_diff

async def get_difficulty_long_name(is_rated,name_diff,is_auto,is_demon,diff_demon):
    if is_rated == False:return "unrated"
    if is_demon==True:return "demon-{}".format(diff_demon)
    elif is_auto==True:return "auto"
    else:return name_diff

async def convert_diff_num(is_rated,name_diff,is_epic,is_auto,is_demon,diff_demon,featured_score,gdps):
    path = "api/gdps/{}/settings_api.json".format(gdps)
    isExist = os.path.exists(path)
    if isExist == False:path = "api/default_json/settings_api.json"
    with open(path,'r') as f:
        json_settings = json.load(f)
        if is_rated == False:return "unrated"
        if is_demon==True:name_diff = "demon-{}".format(diff_demon)
        elif is_auto==True:name_diff = "auto"
        if int(is_epic) >= 1:
            try:name_diff = "{}-{}".format(name_diff,json_settings["epic"][str(is_epic)])
            except KeyError:name_diff = "{}-epic".format(name_diff)
        elif int(featured_score) >= 1:
            try:name_diff = "{}-{}".format(name_diff,json_settings["diff_types"][str(featured_score)])
            except KeyError:name_diff = "{}-featured".format(name_diff)
        elif int(featured_score) == 0:name_diff = name_diff
    return name_diff

async def type_get(enum_get:int,data):
    """0 is decode_str\n\n1 is convert_bool\n\n2 is get_demon\n\n3 is get_length\n\n4 is get_diff_num\n\n5 is get_diff_bool\n\n6 is decode_password\n\n7 is get_gameversion"""
    if enum_get == 0:data = await decode_str(data)
    elif enum_get == 1:data = await convert_bool(data)
    elif enum_get == 2:data = await get_demon(int(data))
    elif enum_get == 3:data = await get_length(int(data))
    elif enum_get == 4:data = await get_diff_num(int(data))
    elif enum_get == 5:data = await get_diff_bool(int(data))
    elif enum_get == 6:data = await decode_password(data)
    elif enum_get == 7:data = await get_gameversion(int(data))
    return data
    
async def get_level(response,gdps='robtop'):
    """Returns a JSON of Data Level\n\nRaise Error if none data get"""
    try:index = response.index('1:')
    except:raise Exception("02_nodata")
    response=response[index:]
    #0Level-1Profiles-2Songs-3PagesInfo-4Unknown
    datas_list = response.split(f'#')
    enums_datas = {"description":0,"demon":1,"twoPlayer":1,"ldm":1,"verifiedCoins":1,"auto":1,"isGauntlet":1,"diff_demon":2,"length":3,"diff_num":4,"diff_rated":5,"password":6,"gameVersion":7}
    datas_list_level = datas_list[0].split(f'|')
    datas_list_profiles = json.loads(convert_profile_author(datas_list[1].split(f'|')))
    #print(datas_list_profiles)
    levels,text_api = ([],"")
    for lvl in datas_list_level:
        lvl_raw = lvl.split(f':')
        text_api = ""
        for i in range(0,len(lvl_raw),2):
            try:lvl_raw[i] = structure_level[int(lvl_raw[i])]
            except KeyError:pass
            try:
                try:
                    if lvl_raw[i] == "playerID":lvl_raw[i+1] = f"{str(datas_list_profiles[lvl_raw[i+1]])[1:-1]}"
                except KeyError:
                    lvl_raw[i+1] = '"playerID":"'+lvl_raw[i+1]+'","author":"-","accountID":"0"'
                if lvl_raw[i+1] == "":continue
                try:lvl_raw[i+1] = await type_get(enums_datas[lvl_raw[i]],lvl_raw[i+1])
                except KeyError:pass
                try:
                    if lvl_raw[i] in {"gameVersion"}:lvl_raw[i+1] = str(lvl_raw[i+1])
                    else:lvl_raw[i+1] = int(lvl_raw[i+1])
                except IndexError:break
                except ValueError:
                    if lvl_raw[i] in {"demon","diff_rated","twoPlayer","ldm","verifiedCoins","auto","isGauntlet"}:lvl_raw[i+1] = f'{lvl_raw[i+1]}'
                    elif lvl_raw[i] in {"playerID"}:lvl_raw[i] = ""
                    else:lvl_raw[i+1] = f'"{lvl_raw[i+1]}"'
                if lvl_raw[i] == "":text_api = str(lvl_raw[i+1]).replace("'",'"') + ',\n' + text_api
                else:text_api = f'"{lvl_raw[i]}":{lvl_raw[i+1]},\n' + text_api
            except ValueError:
                if text_api=="":raise Exception("02_nodata")
                break
        level_cache = "{" + text_api[:-2] + "}"
        levels.append(level_cache)
        level_cache = ""
    data = "[\n" + str(",".join(levels)) + "\n]"
    ##############################################
    #print(data)
    level_json = json.loads(data)
    i = 0
    items_probably_nodata = ["diff_rated","diff_demon","featured_score","demon","diff_num","auto","epic","songID","objects","version","officialSong"]
    items_remove = ["diff_rated","diff_demon","featured_score","demon","diff_num","auto"]
    for level_datas in level_json:
        #Items data additional
        for get_data_cache in items_probably_nodata:
            try:level_datas[get_data_cache]
            except KeyError as e:
                if e in {'demon','auto','diff_rated'}:level_json[i][get_data_cache] = False
                else:level_json[i][get_data_cache] = 0
        cache_data = await get_diamonds(level_datas["stars"])
        level_json[i]["diamonds"] = cache_data
        cache_data = await get_cp(level_datas["featured_score"],level_datas["epic"],level_datas["stars"])
        level_json[i]["cp"] = cache_data
        cache_data = await get_orbs(level_datas["stars"])
        level_json[i]["orbs"] = cache_data
        cache_data = await convert_diff_num(level_datas["diff_rated"],level_datas["diff_num"],level_datas["epic"],level_datas["auto"],level_datas["demon"],level_datas["diff_demon"],level_datas["featured_score"],gdps)
        level_json[i]["difficultyFace"] = cache_data
        cache_data = await get_difficulty_short_name(level_datas["diff_rated"],level_datas["diff_num"],level_datas["auto"],level_datas["demon"])
        level_json[i]["difficulty"] = cache_data
        cache_data = await get_difficulty_long_name(level_datas["diff_rated"],level_datas["diff_num"],level_datas["auto"],level_datas["demon"],level_datas["diff_demon"])
        level_json[i]["difficultyLong"] = cache_data
        try:
            for item_rem in items_remove:level_json[i].pop(item_rem)
        except:pass
        # Results pages
        try:
            datas_list_pages = datas_list[3].split(f':')
            if i == 0:
                level_json[i]["results"] = int(datas_list_pages[0])
                level_json[i]["pages"] = int(int(datas_list_pages[0])/2)
        except:pass
        ##Likes - Dislikes
        try:
            if level_json[i]["likes"] < 0:level_json[i]["disliked"] = True
            else:level_json[i]["disliked"] = False
        except:pass
        
        ###Song
        try:
            cache_data = await convert_song(level_datas["officialSong"],level_datas["songID"],response,gdps)
            cache_data = json.loads(cache_data)
            for cache_1,cache_2 in cache_data[0].items():
                level_json[i][cache_1] = cache_2
        except:
            cache_data = await convert_song(-1,0,False,gdps)
            cache_data = json.loads(cache_data)
            for cache_1,cache_2 in cache_data[0].items():
                level_json[i][cache_1] = cache_2
        i = i + 1
    #print(level_json)
    return level_json
