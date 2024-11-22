from getPlaylist import getPlaylist
import webbrowser
import time

trackDurationInMsCol = "Durée du titre (ms)"
trackUrlCol = "URI du titre"
trackNameCol = "Nom du titre"
trackArtistCol = "Nom(s) de l'artiste"

def play_spotify_track(track):
    print('Playing ' + track[trackArtistCol] + ' - ' + track[trackNameCol] +' ... ')
    webbrowser.open(track[trackUrlCol])
    return

def startRecording():



def main():
    tracks = getPlaylist("/Users/theobernier/Music/Téléchargements/download_25_10_24/track_infos.csv")

    for index, track in tracks.iterrows():
        safetyMarginInSeconds = 4
        play_spotify_track(track)
        time.sleep(track[trackDurationInMsCol] / 1000 + safetyMarginInSeconds)

if (__name__=="__main__"):
    main()
