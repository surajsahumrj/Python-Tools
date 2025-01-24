# Install pytube if not installed
# pip install pytube

from pytube import YouTube

url = 'https://youtu.be/peBsfgbOlYM?si=XUvjCHK8XwLp0tGE'

yt = YouTube(url)

stream = yt.streams.get_highest_resolution()
stream.download()

print("Download completed!")
