#/usr/bin python3

import os
import pandas as pd


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




playlistDf = getPlaylist("/Users/theobernier/Music/Téléchargements/download_25_10_24/track_infos.csv")

for index, trackInfo in playlistDf.iterrows():
    number = f'{index+1}'
    if index < 9:
        number = f'0{index+1}'
    filePath = "/Users/theobernier/Music/Téléchargements/download_25_10_24/Doownload-%s.mp3" %(number)
    print(filePath)
    applyTrackInfo(filePath, trackInfo)
