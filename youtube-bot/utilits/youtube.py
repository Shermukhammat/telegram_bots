from pytube import YouTube
import requests
import re, uuid, os


class YouTuba:
    def __init__(self) -> None:
        # Regular expression pattern to match YouTube video IDs
        self.pattern = re.compile(r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/|youtube\.com\/shorts\/)([a-zA-Z0-9_-]{11})')


    def url_checker(self, url : str):    
        match = self.pattern.search(url)
    
        if match:
            id = match.group(1)
            respons = requests.get(url = f"https://youtube.com/oembed?url=http://www.youtube.com/watch?v={id}")
        
            if respons.status_code == 200:
                return id 


url1 = "https://youtu.be/vMXg4V-fKGw?si=BRhjFnxQuwStMaM2"
url2 = "https://www.youtube.com/watch?v=vMXg4V-fKGw"

url3 = "https://youtu.be/_kaGG7tXChY?si=wrsomoCllmGGDU8Z"
url4 = "https://youtube.com/shorts/gLNu8V5KDuM?si=FV2OaYQLcGydhlbN"


ytb = YouTuba()
id = ytb.url_checker(url = url4)


yt = YouTube(url=f"https://www.youtube.com/watch?v={id}")

streams= yt.streams.filter(progressive = True, mime_type = "video/mp4")
for stream in streams:
    print(stream)
    print(f"Size: {round((stream.filesize/1024)/1024, 1)} Mb")
    


# stream = streams.get_by_itag(22)
# print((stream.filesize//1024)/1024)
# stream.download(output_path = 'data', filename = 'video.mp4')




