import pandas as pd

def getPlaylist(filePath):
    columns = ['Nom du titre', "Nom(s) de l'artiste de l'album", "Nom de l'album", "Nom(s) de l'artiste", "URI du titre", "Durée du titre (ms)", "URL de l'image de l'album"]
    playlist_df = pd.read_csv(filePath)
    return playlist_df[columns]