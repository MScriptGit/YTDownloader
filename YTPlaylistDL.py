#Made by MScript 2025
from pytubefix import Playlist
from pytubefix.cli import on_progress
from kivy.uix.popup import Popup
from kivy.uix.label import Label

def on_download_complete():
    print("Download voltooid!")
    # Hier kun je een popup of andere melding geven
    popup = Popup(title='    Download Voltooid', content=Label(text='Download voltooid!'), size_hint=(None, None), size=(600, 400))
    popup.open()

def YTPlaylistDL(url):
	pl = Playlist(url)
	prefixCounter = 1
	PLprefix = ""
	for video in pl.videos:
	    if prefixCounter < 10:
	    	PLprefix = "0" + str(prefixCounter) + ". "
	    else:
	    	PLprefix = "" + str(prefixCounter) + ". "
	    ys = video.streams.get_audio_only()
	    file_path = ys.download(output_path="temp/Downloaded_Playlists", filename_prefix=PLprefix)
	    prefixCounter +=1
	on_download_complete()
