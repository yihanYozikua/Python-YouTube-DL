# -*- coding: utf-8 -*-
import ssl
from pytube import YouTube
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
        video = VideoFileClip(f"{yt.title}.mp4")
        video.audio.write_audiofile(f"{yt.title}.mp3")
        print(f"video {yt.title} finish download")

#rl = 'https://www.youtube.com/watch?v=6BR-DU4SWek'
#yt = YouTube(url, on_progress_callback=progress)
#video = yt.streams.first()
#video.download()

#url='https://www.youtube.com/watch?v=6BR-DU4SWek'
#url='https://www.youtube.com/watch?v=OPlJlPXDZJc&feature=youtu.be&t=2390'
#YouTube(url).streams.first().download()

#video = VideoFileClip('Nina Nesbitt - The Best You Had (Official Audio).mp4')
#video.audio.write_audiofile('test.mp3')

