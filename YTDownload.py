#Made by MScript 2025
import sys
from pytubefix import YouTube
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
from threading import Thread

# Variabele om de huidige pop-up bij te houden
current_popup = None

def on_download_complete(file_path):
    global current_popup

    def show_popup(dt):
        global current_popup
        # Sluit de huidige pop-up als die bestaat
        if current_popup:
            current_popup.dismiss()

        # Maak een nieuwe pop-up
        current_popup = Popup(title='Download Voltooid', content=Label(text='Download voltooid!'), size_hint=(None, None), size=(600, 400))
        current_popup.open()

    Clock.schedule_once(show_popup, 0)

def on_progress(stream, chunk, bytes_remaining):
    global current_popup

    def show_progress_popup(dt):
        global current_popup
        # Sluit de huidige pop-up als die bestaat
        if current_popup:
            current_popup.dismiss()

        # Maak een nieuwe pop-up
        filesize = stream.filesize
        current = ((filesize - bytes_remaining) / filesize)
        percent = ('{0:.1f}').format(current * 100)
        progress = int(50 * current)
        status = '█' * progress + '-' * (50 - progress)
        current_popup = Popup(title='Progress', content=Label(text=f'{percent}%'), size_hint=(None, None), size=(600, 400))
        current_popup.open()

    Clock.schedule_once(show_progress_popup, 0)

def YTDownload(url):
    yt = YouTube(url, on_progress_callback=on_progress)
    ys = yt.streams.get_audio_only()
    file_path = ys.download(output_path="temp/Download")
    on_download_complete(file_path)

def start_download(url):
    Thread(target=YTDownload, args=(url,)).start()
