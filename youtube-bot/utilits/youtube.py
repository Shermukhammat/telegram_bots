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
    

    def get_stream(self, yt : YouTube) -> dict:
        data = {'144p' : 2, '240p' : 2, '360p' : 2, '480p' : 2, '720p' : 2, '1080p' : 2, 'audio' : 2}

        for stream in yt.streams.filter(file_extension = 'mp4', adaptive = True):
            # print(stream, f"Size: {round((stream.filesize/1024)/1024, 1)} Mb")
            if data.get(stream.resolution) == 2 and stream.type == 'video':
                data[stream.resolution] = stream
    
            elif data.get(stream.type) == 2 and stream.mime_type == "audio/mp4":
                data[stream.type] = stream
        
        if data['audio'] == 2 and data['144p'] == 2:
            return None
        return data


url1 = "https://youtu.be/vMXg4V-fKGw?si=BRhjFnxQuwStMaM2"
url2 = "https://www.youtube.com/watch?v=vMXg4V-fKGw"

url3 = "https://youtu.be/_kaGG7tXChY?si=wrsomoCllmGGDU8Z"
url4 = "https://youtube.com/shorts/gLNu8V5KDuM?si=FV2OaYQLcGydhlbN"
k4 = "https://youtu.be/7PIji8OubXU?si=F4XKdo-GAhDbf_TL"

ytb = YouTuba()
id = ytb.url_checker(url = k4)
if id:
    yt = YouTube(url=f"https://www.youtube.com/watch?v={id}")
    streams = ytb.get_stream(yt)
    title = yt.title

    if streams:
        for stream in streams.items():
            print(stream)


qualitys = ['144p', '240p', '360p', '480p', '720p', '1080p']
# streams = [{'stream' : stream, 'res' : stream.resolution, 'size' : round((stream.filesize/1024)/1024, 1)} for stream in yt.streams.filter(file_extension = 'mp4', adaptive = True) if stream.resolution in qualitys]


# data = {'144p' : 2, '240p' : 2, '360p' : 2, '480p' : 2, '720p' : 2, '1080p' : 2, 'audio' : 2}
# for stream in yt.streams.filter(file_extension = 'mp4', adaptive = True):
#     # print(stream)
#     # print(f"Size: {round((stream.filesize/1024)/1024, 1)} Mb")
#     if data.get(stream.resolution) == 2 and stream.type == 'video':
#         data[stream.resolution] = stream
    
#     elif data.get(stream.type) == 2:
#         data[stream.type] = stream



# for stream in data.items():
#     print(stream)


#     print(f"Size: {round((stream.filesize/1024)/1024, 1)} Mb")




# stream = streams.get_by_itag(22)
# print((stream.filesize//1024)/1024)
# stream.download(output_path = 'data', filename = 'video.mp4')




