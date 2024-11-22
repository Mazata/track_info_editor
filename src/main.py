from getPlaylist import getPlaylist
import webbrowser
import time
import audacityClient

trackDurationInMsCol = "Durée du titre (ms)"
trackUrlCol = "URI du titre"
trackNameCol = "Nom du titre"
trackArtistCol = "Nom(s) de l'artiste"

def play_spotify_track(track):
    print('Playing ' + track[trackArtistCol] + ' - ' + track[trackNameCol] +' ... ')
    webbrowser.open(track[trackUrlCol])
    return

def startRecording(client):
    print('Recording ... ')
    client.write("Record2Mono: Filename=recording.wav")
    return

def getClientStatus(client):
    client.read()


def main():
    tracks = getPlaylist("/Users/localadmin/Downloads/track_infos.csv")
    client = audacityClient.PipeClient()

    for index, track in tracks.iterrows():
        safetyMarginInSeconds = 4
        startRecording(client)
        print(getClientStatus(client))
        play_spotify_track(track)
        time.sleep(track[trackDurationInMsCol] / 1000 + safetyMarginInSeconds)
        print(getClientStatus(client))

if (__name__=="__main__"):
    main()
