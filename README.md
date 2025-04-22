#Spotify downloader
Script that automatically plays back spotify tracks from a playlist export, records them with audacity and exports them as MP3 including metadata and ID3 tags
##Get started

### Setup
Required: Python 3 and a package manager  
#### Dependencies
This should work for any OS as long as you can find an equivalent to Soundflower
1. Install dependencies. Look up how to automise this step
2. Install Audacity v. 2.4.2 or newer and enable the [mod-script-pipe extension](https://manual.audacityteam.org/man/scripting.html)
3. Install [Soundflower](https://soundflower.en.softonic.com/mac)

#### SpotiPy
Set up a Spotipy client and follow instructions to set up a client get your credentials.
--> Populate your .env file

#### Exportify
Go to [exportify.app](exportify.app) (NOT exportify.net). Connect your Spotify account and choose a playlist you would like to export.
Your playlist metadata will be exported in CSV format. You can set your language to have the column headers follow a certain locale.
Once exported, go to main.py and set 
1. dataFolder path. This is where your tracks will be downloaded to
2. playlistFolder path. This is where your playlist csv export lives. 

### Download your playlist
1. Open Audacity onto an empty project
2. Open the spotify desktop app (not required, but it makes the whole process smoother if you have it installed)
3. In Settings, set sound output to Soundflower (2ch)
4. In audacity, set sound input to Soundflower(2ch)
5. Set the system volume to roughly 2/3 intensity
6. Start the download with `python3 src/main.py`
NOTE: There are a few `time.sleep()` statement in main.py. You might have to adjust those to fit the performance of your machine. I run this script on a 2013 Mac book Pro. Your machine will probably be much faster at executing these commands

⚠ The don'ts ⚠
1. Do not use the volume button while the script is running
2. Do not try to play music on your laptop or perform any actions that would trigger a sound from your laptop as it would end up being recorded
3. Do not play music from your spotify account on any other device as it would interrupt the current playback that is being recorded 