from pytube import YouTube, extract




url = "https://www.youtube.com/watch?v=mpxwlItsDA8"

yt = YouTube(url=url, use_oauth=True)
for stream in yt.streams.filter(progressive=True):
    if stream.resolution == '720p':
        stream.download(output_path='data', filename = "video.mp4")


