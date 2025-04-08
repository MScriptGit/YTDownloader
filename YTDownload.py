from pytubefix import YouTube
from pytubefix.cli import on_progress
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from pydub import AudioSegment

AudioSegment.converter = '/data/user/0/com.termux/files/usr/bin'

def on_download_complete(file_path):
    print("Download voltooid! Bestand opgeslagen in:", file_path)
    # Hier kun je een popup of andere melding geven
    popup = Popup(title='    Download Voltooid', content=Label(text='Download voltooid!'), size_hint=(None, None), size=(600, 400))
    popup.open()
    
def YTDownload(url):
    yt = YouTube(url, on_progress_callback=on_progress)
    ys = yt.streams.get_audio_only()
    file_path = ys.download(output_path="temp/Download")
    on_download_complete(file_path)

"""def YTDownload(url):
    #url = input("Enter URL: ")

    yt = YouTube(url, on_progress_callback=on_progress)

    ys = yt.streams.get_audio_only()
    ys.download(output_path="temp/Download")
    
    songBefore = AudioSegment.from_file("temp/Download/{yt.title}.m4a", "m4a")
    
    songBefore.export("{yt.title}.mp3", format="mp3")"""