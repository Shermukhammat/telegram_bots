from pytube import YouTube, helpers
import requests
import re, uuid, os
import time
from http.client import IncompleteRead
from requests.models import PreparedRequest
import requests.exceptions


# proxy_handler = {
#     "http": "127.0.0.1:20304",
#     'https': '127.0.0.1:20304'
# }
# helpers.install_proxy(proxy_handler)

def write_log(file_path : str = "data/logs.log", log : str = 'New text'):
    """This function helps you write logs

    Args:
        file_path (str, optional): You wnated write logs file. Defaults to None.
        log (str, optional): log text. Defaults to 'New text'.
    """
    with open(file_path, 'a') as file:
        file.write(log+"\n")
        file.close()


def is_url(url):
    """this function checks url valid or invalid

    Args:
        url (_type_): _description_

    Returns:
        srt: returns url other wise None
    """
    prepared_request = PreparedRequest()
    try:
        prepared_request.prepare_url(url, None)
        return prepared_request.url
    except requests.exceptions.MissingSchema as e:
        write_log(log = f"check url function crash {e}")







class YouTuba:
    def __init__(self, video_size_limit : int = 1_024) -> None:
        # Regular expression pattern to match YouTube video IDs
        self.pattern = re.compile(r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/|youtube\.com\/shorts\/)([a-zA-Z0-9_-]{11})')
        self.video_size_limit = video_size_limit

    def is_live(self, url):
        live_match = re.search(r'(?:\/live\/|\/shorts\/)([a-zA-Z0-9_-]+)', url)
        if live_match:
            id = url[live_match.start(): live_match.end()].replace("/live/", '')
            respons = requests.get(url = f"https://youtube.com/oembed?url=http://www.youtube.com/watch?v={id}")
        
            if respons.status_code == 200:
                return id 

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
    
    def __get_resolution(self, text):
        """_summary_

        Args:
        text (_type_): this function can find
        resolutin. function can find 100 to 3999 betwin

        Returns:
        str: if function find resolutino returns resolutn as string
        """
        resolt = re.search(r'[1-9][0-9][0-9]?[0-9]', text)
        if resolt:
            return text[resolt.start(): resolt.end()]+'p'

    def get_vide_info(self, yt : YouTube):
            
        data = {'144p' : None, '240p' : None, '360p' : None, '480p' : None, '720p' : None, '1080p' : None, '1440p' : None, '2160p' : None, 'audio' : None}
        data['title'] = yt.title
        data['thumb'] = yt.thumbnail_url

        webm_data = self._get_webm_info(yt.streaming_data)
        audio_info = self._get_audio_info(yt.streaming_data)
        if webm_data and audio_info:
            voise_size = webm_data['size']
            data['audio'] = audio_info
            data['webm'] = webm_data
            # print(audio_info)
            # print(webm_data)
            try:
                for format in yt.streaming_data['adaptiveFormats']: #adaptiveFormats
                    # print(format)
                    mimtype = format['mimeType'].split(";")[0]

                    if mimtype == "video/mp4":
                        size = round((float(format['contentLength'])/1024)/1024 + voise_size, 1)
                        quality = self.__get_resolution(format['qualityLabel'])

                        if not quality:
                            continue

                        elif data.get(quality) != None and data[quality]['size'] < size:
                            data[quality] = {'itag' : format['itag'], 'size' : size, 'mimeType' : mimtype, 'lastModified' : format['lastModified']}
                    
                        elif data.get(quality) == None:
                            data[quality] = {'itag' : format['itag'], 'size' : size, 'mimeType' : mimtype, 'lastModified' : format['lastModified']}  
            
                if data['144p'] != None:
                    return data 
            except IncompleteRead:
                print("Incomplated read")
                
    
    def download_video(self, id : str = None, resolution : str = '360p', video_file : str = "video.mp4", audio_file : str = "audio.webm", output_path : str = "data"):
        url = f"https://www.youtube.com/watch?v={id}"

        try:
            if resolution == '360p' or resolution == '720p':
                # print(url)
                yt = YouTube(url, use_oauth=True)
            
                for stream in yt.streams.filter(progressive=True):
                    if stream.resolution == resolution:
                        stream.download(output_path = output_path, filename = video_file)
        

        
            else:
                yt = YouTube(url, use_oauth=True)
                data = self.get_vide_info(yt)

                if data:
                    # print(data)
                    audio = data.get('webm')
                    video = data.get(resolution)

                    if audio and video:
                        audio_stream = yt.streams.get_by_itag(audio['itag'])
                        video_stream = yt.streams.get_by_itag(video['itag'])

                        video_stream.download(output_path = output_path, filename = video_file)
                        audio_stream.download(output_path = output_path, filename = audio_file)
                        return True

                    else:
                        return False
            

                else:
                    return False
        
    

        
        except:
            write_log(log = f"Youtuba class downlaod_video method: downloading errr in this url {url}")
            return False
    
    

if __name__ == '__main__':
    print(os.listdir('data'))
    # yt = YouTuba()
    # status = yt.download_video(id = "o9-4zW_r9AE", video_file = "video.mp4", resolution = "1080p")
    # print(status)
    # url = "https://youtu.be/5USuekk16e0?si=nbQN-tSIP4h1izEd"
    # ytb = YouTuba()
    # id = ytb.url_checker(url)
    # id2 = ytb.is_live(url)
    # if id:
    #     print(id)

        # data = ytb.get_vide_info(id)
        # if data:
        #     for res, dat in data.items():
        #         print(res, dat)
        #         print("-"*35)

        
        # yt = YouTube(url, use_oauth = True)
        # stream = yt.streams.get_by_itag(249)
        # stream.download(output_path="data", filename="audio.webm")
        # yt = YouTube(url)
        # for stream in yt.streams.filter(adaptive=True):
        #     print(stream)
        #     print(round((float(stream.filesize))/1024/1024, 1), "Mb")