import base64
from operator import xor

#API LEVELS
async def encode_str(string: str) -> str:
    return base64.urlsafe_b64encode(string.encode()).decode()

async def decode_str(string: str) -> str:
    return base64.urlsafe_b64decode(string.encode()).decode()

async def get_diff_denom(data: int) -> int:
    if data == 0:return "false"
    elif data == 10:return "true"
    else:return "false"

async def get_length(data: int) -> int:
    if data == 0:return "Tiny"
    elif data == 1:return "Short"
    elif data == 2:return "Medium"
    elif data == 3:return "Long"
    elif data == 4: return "XL"
    else:return "Unknown"

async def convert_bool(data):
    if data == "" or data == " " or data == "0" or data == 0:return "false"
    elif data == "1" or data == 1:return "true"
    else:return "false"

async def get_demon(data:int) -> int:
    if data==3:return "Easy"
    elif data==4:return "Medium"
    elif data==0:return "Hard"
    elif data==5:return "Insane"
    elif data==6:return "Extreme"

async def get_diff_num(data:str) -> str:
    if data==0:return "Unrated"
    elif data==10:return "Easy"
    elif data==20:return "Normal"
    elif data==30:return "Hard"
    elif data==40:return "Harder"
    elif data==50:return "Insane"
    else:return "Unrated"

async def decode_password(data:str) -> str:
    key = "26364"
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key])))

#API PROFILES

async def messageState(data:int) -> int:
    if data==0:return "all"
    elif data==1:return "friends"
    elif data==2:return "off"
    else:return "off"

async def commentHistoryState(data:int) -> int:
    if data==0:return "all"
    elif data==1:return "friends"
    elif data==2:return "off"
    else:return "off"

async def friendState(data:int) -> int:
    if data==0:return "true"
    elif data==1:return "false"
    else:return "false"

