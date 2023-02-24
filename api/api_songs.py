import json
import os
from urllib.parse import unquote

async def get_song_default(officialSong=0,gdps='robtop'):
    path = "api/gdps/{}/official_songs.json".format(gdps)
    isExist = os.path.exists(path)
    if isExist == False:path = "api/default_json/official_songs.json"
    with open(path,'r') as f:
        songs = json.load(f)
        try:nm,sg,sl = (songs[str(officialSong)]["name"],songs[str(officialSong)]["artist"],songs[str(officialSong)]["songLink"])
        except:nm,sg,sl = ("Unknown","Unknown","<None>")
    return nm,sg,sl


async def get_song(response,songID=0,officialSong=0,gdps='robtop'):
    """Return STR song data in format JSON (but no loaded)"""
    structure_song = {
        1:"songID",
        2:"songName",
        3:"songArtistID",
        4:"songAuthor",
        5:"songSize",
        6:"songVideoID",
        7:"songVideoURL",
        8:"songVerified",
        9:"songPriority",
        10:"songLink"
        }
    if songID == 0:
        nm,sg,sl = await get_song_default(officialSong+1,gdps)
        response_temp = '[{"songID":0,"songName":"'+nm+'","songAuthor":"'+sg+'","songArtistID:":0,"songSize":"?MB","songLink":"'+sl+'","songVerified":1}]'
        return response_temp
    try:
        if songID != 0:index_data = str(response.lower()).index('1~|~{}'.format(songID))
        else:index_data = str(response.lower()).index('1~|~')
    except:raise Exception("02_nodata")
    final = None
    if songID != 0:
        try:final = index_data + str(response[index_data:]).index('~:~')
        except:pass
    else:
        try:final = index_data + response.index('#')
        except:pass
    response = response[index_data:final]
    try:response = response[:int(response.index('#'))]
    except:pass
    splitted = response.split('~:~')
    text_api,songs = ("",[])
    for level in splitted:
        strres = level.split(f'~|~')
        text_api = ""
        for i in range(0,len(strres),2):
            try:strres[i] = structure_song[int(strres[i])]
            except ValueError:
                text_api = '"songID":0,"songName":"?","songAuthor":"?","songArtistID:":0,"songSize":"?MB","songLink":"https://www.newgrounds.com/audio/listen/1","songVerified":1,\n'
                break
            except KeyError:pass
            try:
                if strres[i+1] == "":continue
                elif strres[i] == "songName":strres[i+1] = "{}".format(str(strres[i+1]).replace('"',"¨"))
                elif strres[i] == "songAuthor":strres[i+1] = "{}".format(str(strres[i+1]).replace('"',"¨"))
                elif strres[i] == "songSize":strres[i+1] = "{}MB".format(strres[i+1])
                elif strres[i] == "songLink":strres[i+1] = "{}".format(unquote(strres[i+1]))
                try:text_api = text_api + f'"{strres[i]}":{int(strres[i+1])},\n'
                except:text_api = text_api + f'"{strres[i]}":"{strres[i+1]}",\n'
            except KeyError:
                try:text_api = text_api + f'"{strres[i]}":"{strres[i+1]}",\n'
                except:pass
            except IndexError:break
        level_cache = "{" + text_api[:-2] + "}"
        songs.append(level_cache)
        level_cache = ""
    data = "[\n" + str(",".join(songs)) + "\n]"
    return data
