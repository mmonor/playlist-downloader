from gui import PlaylistDownloaderGUI
import tkinter as tk
from yt_dlp import YoutubeDL
from urllib.parse import urlparse,parse_qs
import os


# URL PARSING
def extract_list_id(url):
    query= urlparse(url).query
    params = parse_qs(query)
    return params.get("list",[None])[0]




# Get the video urls
def get_videos(url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,

    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        video_url = [entry['url'] for entry in info['entries']]
        return video_url










def download_playlist(url):
    playlist_url = "https://www.youtube.com/playlist?list="
    playlist_list = extract_list_id(url)
    playlist_final = playlist_url + playlist_list
    videos_url = get_videos(playlist_final)


    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'test/%(title)s.%(ext)s',  # Save as title.mp3
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'ffmpeg_location': r'C:\ffmpeg\bin',

    }
    with YoutubeDL(ydl_opts) as ydl:
        for url in videos_url:
            ydl.download([url])



root = tk.Tk()
app = PlaylistDownloaderGUI(root,download_callback=download_playlist)

root.mainloop()