from pytube import YouTube
import requests
import re, uuid, os
import time
from http.client import IncompleteRead

def write_log(file_path : str = None, log : str = 'New text'):
    """This function helps you write logs

    Args:
        file_path (str, optional): You wnated write logs file. Defaults to None.
        log (str, optional): log text. Defaults to 'New text'.
    """
    with open(file_path, 'a') as file:
        file.write(log+"\n")
        file.close()



class YouTuba:
    def __init__(self, video_size_limit : int = 1_024) -> None:
        # Regular expression pattern to match YouTube video IDs
        self.pattern = re.compile(r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/|youtube\.com\/shorts\/)([a-zA-Z0-9_-]{11})')
        self.video_size_limit = video_size_limit

    def url_checker(self, url : str):    
        match = self.pattern.search(url)
    
        if match:
            id = match.group(1)
            respons = requests.get(url = f"https://youtube.com/oembed?url=http://www.youtube.com/watch?v={id}")
        
            if respons.status_code == 200:
                return id 
    

    def get_streams(self, yt : YouTube) -> dict:
        """This Function get stremas data 
        resolutions is  '144p', '240p', '360p', '480p', '720p', '1080p' and aslso hase 'audio' strems

        Args:
            yt (YouTube): Pytube's Youtube object

        Returns:
            dict: if can get strems returns strms as dictionr other whise return None
        """
        data = {'144p' : 2, '240p' : 2, '360p' : 2, '480p' : 2, '720p' : 2, '1080p' : 2, 'audio' : 2}
        
        try:
            for stream in yt.streams.filter(file_extension = 'mp4', adaptive = True):
                # print(stream, f"Size: {round((stream.filesize/1024)/1024, 1)} Mb")
                if data.get(stream.resolution) == 2 and stream.type == 'video' and round((stream.filesize/1024)/1024, 1) <= self.video_size_limit:      
                    data[stream.resolution] = stream 
    
                elif data.get(stream.type) == 2 and stream.mime_type == "audio/mp4":
                    data[stream.type] = stream 
        
            if data['audio'] == 2 and data['144p'] == 2:
                return 
            return data 
        
        except:
            pass

    def _get_webm_info(self, streaming_data):
        data = None
        try:
            for format in streaming_data['adaptiveFormats']:
                mim_type = format['mimeType'].split(';')[0]
                if mim_type == "audio/webm":
                    size = round((float(format['contentLength'])/1024)/1024, 1)
                    itag = format['itag']
                    # print(mim_type, size, 'Mb, itag:', itag)

                    if data != None and data['size'] < size:
                        data = {'itag' : itag, 'size' : size, 'mimeType' : mim_type, 'lastModified' : format['lastModified']}
                    
                    elif data == None:
                        data = {'itag' : itag, 'size' : size, 'mimeType' : mim_type, 'lastModified' : format['lastModified']}
            return data
            
        except IncompleteRead:
            print("! Incomplited read in Youtuba class's _get_webm_info method")

    def _get_audio_info(self, streaming_data):
        data = None
        try:
            for format in streaming_data['adaptiveFormats']:
                mim_type = format['mimeType'].split(';')[0]
                if mim_type == "audio/mp4":
                    size = round((float(format['contentLength'])/1024)/1024, 1)
                    itag = format['itag']
                    # print(mim_type, size, 'Mb, itag:', itag)

                    if data != None and data['size'] < size:
                        data = {'itag' : itag, 'size' : size, 'mimeType' : mim_type, 'lastModified' : format['lastModified']}
                    
                    elif data == None:
                        data = {'itag' : itag, 'size' : size, 'mimeType' : mim_type, 'lastModified' : format['lastModified']}
            return data
            
        except IncompleteRead:
            print("! Incomplited read in Youtuba class's _get_audio_info method")

    def get_vide_info(self, url : str):
        id = self.url_checker(url = url)
        if id:
            data = {'144p' : None, '240p' : None, '360p' : None, '480p' : None, '720p' : None, '1080p' : None, '1440p' : None, '2160p' : None, 'audio' : None}
            yt = YouTube(url=f"https://www.youtube.com/watch?v={id}")

            webm_data = self._get_webm_info(yt.streaming_data)
            audio_info = self._get_audio_info(yt.streaming_data)
            if webm_data and audio_info:
                voise_size = webm_data['size']
                data['audio'] = audio_info
                # print(audio_info)
                # print(webm_data)

                for format in yt.streaming_data['adaptiveFormats']: #adaptiveFormats
                    # print(format)
                    mimtype = format['mimeType'].split(";")[0]

                    if mimtype == "video/mp4":
                        size = round((float(format['contentLength'])/1024)/1024 + voise_size, 1)
                        quality = format['qualityLabel']
                        print(quality)

                        if data.get(quality) != None and data[quality]['size'] < size:
                            data[quality] = {'itag' : format['itag'], 'size' : size, 'mimeType' : mimtype, 'lastModified' : format['lastModified']}
                    
                        elif data.get(quality) == None:
                            data[quality] = {'itag' : format['itag'], 'size' : size, 'mimeType' : mimtype, 'lastModified' : format['lastModified']}  
                
                return data
            
            # for res, dat in data.items():
            #     print(res, dat)
            #     print("-"*35)



url1 = "https://youtu.be/vMXg4V-fKGw?si=BRhjFnxQuwStMaM2"
url2 = "https://www.youtube.com/watch?v=vMXg4V-fKGw"

url3 = "https://www.youtube.com/watch?v=vMXg4V-fKGw"
url4 = "https://youtube.com/shorts/gLNu8V5KDuM?si=FV2OaYQLcGydhlbN"
k4 = "https://youtu.be/7PIji8OubXU?si=F4XKdo-GAhDbf_TL"
long_url = "https://youtu.be/OO_-MbnXQzY?si=f1YM5xcqmBrn8DCH"
age = "https://youtu.be/-t5gvDd7HvY?si=ykWY5HZUDnerZxP-"

start = time.time()

ytb = YouTuba()
ytb.get_vide_info(url3)
# yt = YouTube(url3)

# stream = yt.streams.get_by_itag(136)
# stream.download(output_path='data', filename = 'test.mp4')

# yt = YouTube(url3)
