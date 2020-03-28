#!/usr/bin/python
# -*- coding: utf-8 -*-
import ssl
import shutil
from pytube import YouTube
from pytube import Playlist
import os
from moviepy.editor import *
from pytube.__main__ import YouTube

ssl._create_default_https_context = ssl._create_unverified_context

# The playlist wanted to download
playlist = "https://www.youtube.com/watch?v=ptnYBctoexk&list=PLb02MaZXm5_NlsfBLJ6pgkI-xjQ0do3rt"

pl = Playlist(playlist)
pathdir = 'Download-PlayList'
if not os.path.isdir(pathdir):
    os.mkdir(pathdir)

pl.download_all(pathdir)
print("Finidhed download the playlist!")