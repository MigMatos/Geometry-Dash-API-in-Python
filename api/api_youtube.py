from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

#You need this libraries
#pip install pytube
#pip install moviepy

async def download_in_mp3(cache_path:str,url:str,id_name:str):
    """Return output file and info for file"""
    yt = YouTube(url)
    out_file = yt.streams.filter(file_extension='mp4').first().download()
    try:filesize = yt.streams.filter(file_extension='mp4').first().filesize
    except:filesize = 30500000
    if filesize >= 30500000:return "","FILESIZE_ERROR"
    render = VideoFileClip(filename=out_file, verbose=False, logger=None)
    render.audio.write_audiofile("{}/{}.mp3".format(cache_path,id_name),verbose=False, logger=None)
    VideoFileClip.close(self=render)
    try:os.remove(out_file)
    except:pass
    return "{}/{}.mp3".format(cache_path,id_name),yt


