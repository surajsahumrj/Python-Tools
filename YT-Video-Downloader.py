from pytube import YouTube

YouTube('https://youtu.be/peBsfgbOlYM?si=XUvjCHK8XwLp0tGE').streams.first().download()
