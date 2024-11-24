
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

def applyTrackInfo(filePath, trackInfo):
    mp3file = MP3(filePath, ID3=EasyID3)

    mp3file['title'] = trackInfo['Nom du titre']
    mp3file['album'] = trackInfo["Nom de l'album"]
    mp3file['albumartist'] = trackInfo["Nom(s) de l'artiste de l'album"]
    mp3file['artist'] = trackInfo["Nom(s) de l'artiste"]

    mp3file.save()