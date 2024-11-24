from getPlaylist import getPlaylist
import webbrowser
import time
import audacityClient
from assignTrackID3Tags import applyTrackInfo

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

trackDurationInMsCol = "Durée du titre (ms)"
trackUrlCol = "URI du titre"
trackNameCol = "Nom du titre"
trackArtistCol = "Nom(s) de l'artiste"
safetyMarginInSeconds = 1




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
    time.sleep(track[trackDurationInMsCol] / 100000 + safetyMarginInSeconds )

def selectTrackLength(client, track):
    trackStart = 0
    trackEndInSeconds = round(track[trackDurationInMsCol] / 100000) + safetyMarginInSeconds
    client.write(f'SelectTime: End="{trackEndInSeconds}" RelativeTo="ProjectStart" Start="0"')

def exportToMp3(client, track):
    trackName = f'{track[trackNameCol].replace(" ", "_")}--{track[trackArtistCol].replace(" ", "_")}'
    client.write("SelectAll")
    client.write(f"Normalize: ApplyVolume=1 RemoveDcOffset=1 PeakLevel=-1 StereoIndependent=0")
    client.write(f"Export2: Filename={buildTrackFilePath(track)} NumChannels=1.0")
    time.sleep(4)
    client.write("SelectAll")
    client.write("RemoveTracks")

def getClientStatus(client):
    client.read()

def buildTrackFilePath(track):
    fileName = f'{track[trackNameCol].replace(" ", "_")}--{track[trackArtistCol].replace(" ", "_")}'
    return f"/Users/localadmin/Documents/Perso/Spotify_downloader/downloaded_tracks/{fileName}.mp3"

def assignTrackInfos(track):
    print("Assigning track infos")
    applyTrackInfo(buildTrackFilePath(track), track)


def main():
    spotifyClient = authenticateToSpotify()
    tracks = getPlaylist("/Users/localadmin/Downloads/track_infos.csv")
    client = audacityClient.PipeClient()

    for index, track in tracks.iterrows():
        playSpotifyTrack(track)
        recordTrack(client, track)
        spotifyClient.pause_playback()
        exportToMp3(client, track)
        assignTrackInfos(track)
        if(index == 6):
            break

if (__name__=="__main__"):
    main()
