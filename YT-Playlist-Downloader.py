from pytube import Playlist

p = Playlist("https://youtube.com/playlist?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0&si=6Ir3PdWBgBayPDef")

for video in p.videos:
    video.streams.first().download()
