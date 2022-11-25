from api.utils_api_gd import convert_bool, decode_str,get_demon, get_length, get_diff_denom, get_diff_num,decode_password

api_replace = ["1:",":2:",":3:",":4:",":5:",":6:",":8:",":9:",":10:",":11:",":12:",":13:",":14:",":15:",":16:",":17:",":18:",":19:",":25:",":26:",":27:",":28:",":29:",":30:",":31:",":35:",":36:",":37:",":38:",":39:",":40:",":41:",":42:",":43:",":44:",":45:",":46:",":47:",":48:"]
structure_level = {1:"id",2:"name",3:"description",4:"data_level",5:"version",6:"playerID",8:"diff_rated",9:"diff_num",10:"downloads",11:"unused_11",12:"officialSong",13:"gameVersion",14:"likes",15:"length",16:"dislikes",17:"demon",18:"stars",19:"featured_score",25:"auto",26:"unused_26",27:"password",28:"uploadDate",29:"updateDate",30:"copiedID",31:"twoPlayer",35:"customSongID",36:"extraString",37:"coins",38:"verifiedCoins",39:"starsRequested",40:"ldm",41:"dailyNumber",42:"epic",43:"diff_demon",44:"isGauntlet",45:"objects",46:"editorTime",47:"editorTime_Copy",48:"unused_48"}
structure_song = {1:"songID",2:"songName",3:"songAuthorID",4:"songAuthor",5:"songSize",6:"songVideoID",7:"songYoutubeURL",8:"songVerified",9:"songPriority",10:"songLink"}
i=0
async def get_level(response):
    try:index = response.index('1:')
    except:raise Exception("02_nodata")
    response=response[index:]
    #0Level-1Profiles-2Songs-3PagesInfo-4Unknown
    datas_list = response.split(f'#')
    #LEVEL STRUCTURE
    datas_list_level = datas_list[0].split(f'|')
    datas_list_profiles = datas_list[1].split(f'|')
    datas_list_song = datas_list[2].split(f':')
    for song in datas_list_song:
        pass
    level_datas,text_api = ([],"")
    for lvl in datas_list_level:
        lvl_raw = lvl.split(f':')
        for structure in structure_level.items():
            api_num, api_str = structure
            for i in range(0,len(lvl_raw),2):
                if str(lvl_raw[i]) == str(api_num):lvl_raw[i] = api_str

        for i in range(0,100,2):
            try:
                if lvl_raw[i+1] == "":lvl_raw[i+1]="<None>"
                if lvl_raw[i] == "description":lvl_raw[i+1]=await decode_str(lvl_raw[i+1])
                elif lvl_raw[i] in {"demon","epic","twoPlayer","ldm","verifiedCoins","auto","isGauntlet"}:lvl_raw[i+1] = await convert_bool(lvl_raw[i+1])
                elif lvl_raw[i] == "diff_demon":lvl_raw[i+1]=await get_demon(int(lvl_raw[i+1]))
                elif lvl_raw[i] == "length":lvl_raw[i+1]=await get_length(int(lvl_raw[i+1]))
                elif lvl_raw[i] == "diff_num":lvl_raw[i+1]=await get_diff_num(int(lvl_raw[i+1]))
                elif lvl_raw[i] == "diff_rated":lvl_raw[i+1]=await get_diff_denom(int(lvl_raw[i+1]))
                elif lvl_raw[i] == "password":lvl_raw[i+1]=await decode_password(str(lvl_raw[i+1]))
                try:lvl_raw[i+1] = int(lvl_raw[i+1])
                except ValueError:lvl_raw[i+1] = f'"{lvl_raw[i+1]}"'
                text_api = f"{lvl_raw[i]}:{lvl_raw[i+1]},\n" + text_api
            except:
                if text_api=="":raise Exception("02_nodata")
                text_api = "{\n" + text_api[:-2] + "\n},"
                break
    return text_api