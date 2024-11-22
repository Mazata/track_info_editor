#/usr/bin python3

import os
import pandas as pd

from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

from getPlaylist import getPlaylist



def reNumberFileNames(directoryPath):
    os.chdir(directoryPath)
    for i in range(32,33):
        number = f'{i}'
        if i < 10:
            number = f'0{i}'
        currentFileName = f'Dowload--{number}.mp3'
        newFileName = f'Doownload-{number}.mp3'

        os.rename(currentFileName,newFileName)


def applyTrackInfo(filePath, trackInfo):
    mp3file = MP3(filePath, ID3=EasyID3)

    mp3file['title'] = trackInfo['Nom du titre']
    mp3file['album'] = trackInfo["Nom de l'album"]
    mp3file['albumartist'] = trackInfo["Nom(s) de l'artiste de l'album"]
    mp3file['artist'] = trackInfo["Nom(s) de l'artiste"]

    mp3file.save()

playlistDf = getPlaylist("/Users/theobernier/Music/Téléchargements/download_25_10_24/track_infos.csv")

for index, trackInfo in playlistDf.iterrows():
    number = f'{index+1}'
    if index < 9:
        number = f'0{index+1}'
    filePath = "/Users/theobernier/Music/Téléchargements/download_25_10_24/Doownload-%s.mp3" %(number)
    print(filePath)
    applyTrackInfo(filePath, trackInfo)
