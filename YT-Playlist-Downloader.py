# Install pytube if not installed
# pip install pytube

from pytube import Playlist

playlist_url = "https://youtube.com/playlist?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0&si=6Ir3PdWBgBayPDef"

playlist = Playlist(playlist_url)

print(f"Downloading playlist: {playlist.title}")
print(f"Number of videos: {len(playlist.videos)}")

for video in playlist.videos:
    print(f"Downloading: {video.title}")
    stream = video.streams.get_highest_resolution()  
    stream.download()  
    print(f"Downloaded: {video.title}")

print("Playlist download completed!")
