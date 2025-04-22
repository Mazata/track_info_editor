from getPlaylist import getPlaylist
import webbrowser
import time
import audacityClient
from assignTrackID3Tags import applyTrackInfo

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

import io
import requests

load_dotenv()

trackDurationInMsCol = "Durée du titre (ms)"
trackUrlCol = "URI du titre"
trackNameCol = "Nom du titre"
trackArtistCol = "Nom(s) de l'artiste"
trackImageURL = "URL de l'image de l'album"
safetyMarginInSeconds = 1

dataFolder = "/Users/theobernier/Music/Downloads/spotify_download_22_4_25"
playlistFolder = "/Users/theobernier/Music/Downloads/spotify_download_22_4_25"



def authenticateToSpotify():
    scope = "user-modify-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return sp

def playSpotifyTrack(track):
    print('Playing ' + track[trackArtistCol] + ' - ' + track[trackNameCol] +' ... ')
    webbrowser.open(track[trackUrlCol])
    return

def startRecording(client):
    print('Recording ... ')
    client.write("Record2ndChoice")
    return

def stopRecording(client):
    print('Stopping recording')
    #client.write("Pause")
    client.write("DefaultPlayStop")
    print('Recording stopped')
    return

def recordTrack(client, track):
    selectTrackLength(client, track)
    startRecording(client)

def selectTrackLength(client, track):
    trackStart = 0
    trackEndInSeconds = round(track[trackDurationInMsCol] / 1000) + safetyMarginInSeconds
    client.write(f'SelectTime: End="{trackEndInSeconds}" RelativeTo="ProjectStart" Start="0"')

def waitForClient(client, statusSubstring):
    audacityStatus = getClientStatus(client)
    while statusSubstring not in audacityStatus.strip():
        print("status", audacityStatus)
        print("waiting for audacity operation to finish")
        time.sleep(1)
        audacityStatus = getClientStatus(client)
    print("client finished with status", audacityStatus)

def waitForClientNormalize(client):
    waitForClient(client, "BatchCommand finished: OK")

def waitForClientExport(client):
    waitForClient(client, "Exported to MP3")

def exportToMp3(client, track):
    trackName = f'{track[trackNameCol].replace(" ", "_")}--{track[trackArtistCol].replace(" ", "_")}'
    client.write("SelectAll")
    time.sleep(0.5)
    getClientStatus(client)
    client.write(f"Normalize: ApplyVolume=1 RemoveDcOffset=1 PeakLevel=-1 StereoIndependent=0")
    time.sleep(0.5)
    waitForClientNormalize(client)


    client.write(f"Export2: Filename={buildTrackFilePath(track)} NumChannels=1.0")
    waitForClientExport(client)
    client.write("SelectAll")
    client.write("RemoveTracks")
    time.sleep(0.5)

def getClientStatus(client):
    return client.read()

def buildTrackFilePath(track):

    fileName = "%s--%s" % \
               (
                   track[trackNameCol].replace(" ", "_").replace("\\", "-").replace("/", "_"),
                   track[trackArtistCol].replace(" ", "_").replace("\\", "-").replace("/", "_")
               )
    return f"{dataFolder}/{fileName}.mp3"

def assignTrackInfos(track):
    print("Assigning track infos")
    albumCover = getTrackAlbumCover(track)
    applyTrackInfo(buildTrackFilePath(track), track, albumCover=albumCover)



def getTrackAlbumCover(track):
    coverUrl = track[trackImageURL]
    data = requests.get(coverUrl).content
    return io.BytesIO(data)


def main():
    spotifyClient = authenticateToSpotify()
    tracks = getPlaylist(f"{playlistFolder}/track_infos.csv")[64:]
    client = audacityClient.PipeClient()

    for index, track in tracks.iterrows():
        if index < 72:
            continue
        recordTrack(client, track)
        playSpotifyTrack(track)
        time.sleep(track[trackDurationInMsCol] / 1000 + safetyMarginInSeconds)
        spotifyClient.pause_playback()
        exportToMp3(client, track)
        assignTrackInfos(track)

if (__name__=="__main__"):
    main()
