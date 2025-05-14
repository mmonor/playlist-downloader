import tkinter as tk
from yt_dlp import YoutubeDL
from urllib.parse import urlparse, parse_qs
import os
from gui import PlaylistDownloaderGUI


# URL Parsing
def extract_list_id(url):
    query = urlparse(url).query
    params = parse_qs(query)
    return params.get("list", [None])[0]



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


# Download playlist
def download_playlist(url, progress_callback):
    playlist_url = "https://www.youtube.com/playlist?list="
    playlist_list = extract_list_id(url)
    playlist_final = playlist_url + playlist_list
    videos_url = get_videos(playlist_final)


    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'test/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'ffmpeg_location': r'C:\ffmpeg\bin',
        'progress_hooks': [lambda d: progress_hook(d, progress_callback)],
    }

    with YoutubeDL(ydl_opts) as ydl:
        for url in videos_url:
            ydl.download([url])


# Progress bar
def progress_hook(d, progress_callback):
    if d['status'] == 'downloading':
        percent = d['downloaded_bytes'] / d['total_bytes'] * 100
        progress_callback(percent)
    elif d['status'] == 'finished':
        progress_callback(100)



if __name__ == "__main__":
    root = tk.Tk()
    app = PlaylistDownloaderGUI(root, download_callback=download_playlist)
    root.mainloop()
