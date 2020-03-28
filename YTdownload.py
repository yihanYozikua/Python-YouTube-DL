#!/usr/bin/python
# -*- coding: utf-8 -*-
import ssl
import shutil
from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *
from pytube.__main__ import YouTube

ssl._create_default_https_context = ssl._create_unverified_context

def progress(stream, chunk, file_handle, bytes_remaining):
    contentSize = video.filesize
    size = contentSize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % ('█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)),end='')

with open('downloadList.txt') as file:
    for line in file:
        yt = YouTube(line.rstrip())
        print(f"Downloading: {yt.title}")
        yt.streams.first().download()
        print(f"Converting {yt.title}.mp4 into .mp3")
        video = VideoFileClip(f"{yt.title}.mp4")
        video.audio.write_audiofile(f"{yt.title}.mp3")
        # move .mp3 & .mp4 into each directories
        shutil.move(f"/Users/xiaoyihan/Code/PythonYouTubeDL/{yt.title}.mp4", f"/Users/xiaoyihan/Code/PythonYouTubeDL/Download-mp4/{yt.title}.mp4")
        shutil.move(f"/Users/xiaoyihan/Code/PythonYouTubeDL/{yt.title}.mp3", f"/Users/xiaoyihan/Code/PythonYouTubeDL/Download-mp3/{yt.title}.mp3")
        print(f"video {yt.title} finish download")

#rl = 'https://www.youtube.com/watch?v=6BR-DU4SWek'
#yt = YouTube(url, on_progress_callback=progress)
#video = yt.streams.first()
#video.download()