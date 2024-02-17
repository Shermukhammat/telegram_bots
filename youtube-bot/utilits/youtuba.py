from pytube import YouTube, extract
from pytube.exceptions import LiveStreamError, VideoUnavailable, VideoPrivate
# import requests
import re
import asyncio

from http.client import IncompleteRead
# import requests.exceptions



class YouTuba:
    def __init__(self, videoSizeLimit : int = 1_900):
        self.limit = videoSizeLimit 
        self.youtube_url_pattern = r'^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|live\/|v\/)?)([\w\-]+)(\S+)?$'
        
    
    def __write_log__(file_path : str = "data/logs.log", log : str = 'New text'):
        """This function helps you write logs

        Args:
        file_path (str, optional): You wnated write logs file. Defaults to None.
        log (str, optional): log text. Defaults to 'New text'.
        """
        with open(file_path, 'a') as file:
            file.write(log+"\n")
            file.close()

    def is_url(self, url : str):
        """this function checks url valid or invalid

        Args:
            url (_type_): _description_

        Returns:
            srt: returns url other wise None
        """
        
        matche = re.search(self.youtube_url_pattern, url)
        if matche:
            return url[matche.start() : matche.end()]
        
    def check_availability(self, yt : YouTube) -> (bool, str):
        try:
            yt.check_availability()
            return True, yt.video_id

        except LiveStreamError:
            return False, "live"

        except VideoPrivate:
            return False, "private"

        except VideoUnavailable:
            return False, "unavailable"

        except:
            return False, "invalid"


    def _get_webm_info__(self, streaming_data):
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
            self.__write_log__(log = f"Incomplited read in Youtuba class's _get_webm_info__ method url")

    def _get_audio_info__(self, streaming_data):
        data = None
        try:
            for format in streaming_data['adaptiveFormats']:
                mim_type = format['mimeType'].split(';')[0]
                if mim_type == "audio/mp4":
                    size = round((float(format['contentLength'])/1024)/1024, 1)
                    itag = format['itag']
                    # print(mim_type, size, 'Mb, itag:', itag)

                    if data != None and data['size'] < size and size <= self.limit:
                        data = {'itag' : itag, 'size' : size, 'mimeType' : mim_type, 'lastModified' : format['lastModified']}
                    
                    elif data == None and size <= self.limit:
                        data = {'itag' : itag, 'size' : size, 'mimeType' : mim_type, 'lastModified' : format['lastModified']}
            return data
            
        except IncompleteRead:
            self.__write_log__(log = f"! Incomplited read in Youtuba class's _get_audio_info method")
    
    def __get_resolution__(self, text):
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
        
        data['channel'] = yt.author
        data['title'] = yt.title
        data['thumb'] = yt.thumbnail_url

        webm_data = self._get_webm_info__(yt.streaming_data)
        audio_info = self._get_audio_info__(yt.streaming_data)
        if webm_data and audio_info:
            voise_size = webm_data['size']
            data['audio'] = audio_info
            data['webm'] = webm_data
        #     # print(audio_info)
        #     # print(webm_data)
            try:
                for format in yt.streaming_data['adaptiveFormats']: #adaptiveFormats
                    mimtype = format['mimeType'].split(";")[0]

                    if mimtype == "video/mp4":
                        size = round((float(format['contentLength'])/1024)/1024 + voise_size, 1)
                        quality = self.__get_resolution__(format['qualityLabel'])

                        # if not quality:
                            # continue

                        if data.get(quality) != None and data[quality]['size'] < size:
                            data[quality] = {'itag' : format['itag'], 'size' : size, 'mimeType' : mimtype, 'lastModified' : format['lastModified']}
                    
                        elif data.get(quality) == None:
                            data[quality] = {'itag' : format['itag'], 'size' : size, 'mimeType' : mimtype, 'lastModified' : format['lastModified']}  
            
                if data['144p'] != None:
                    data['resolutions'] = [key for key, value in data.items() if value != None and key in ('144p', '240p', '360p', '480p', '720p', '1080p', '1440p') and value['size'] <= self.limit]
                    return data 
            except IncompleteRead:
                print("Incomplated read")
                
    
    
    def download_music(self, yt : YouTube) -> bool:
        # print("downloandig started")
        data = self._get_audio_info__(yt.streaming_data)
        if data:
            stream = yt.streams.get_by_itag(data['itag'])
            if stream:
                stream.download(output_path = 'data', filename = f"{yt.title}.mp3")
                return True
            
        
    




url = f"https://www.youtube.com/live/vQP8AwAFzI8?si=UjiUMv2Qs9SV6Grh"

yt = YouTube(url, use_oauth=True)
print(yt.title)
