from pytube import YouTube
import re
from pytube.exceptions import LiveStreamError, VideoUnavailable, VideoPrivate
from http.client import IncompleteRead
import time

def write_log(file_path : str = "data/logs.log", log : str = 'New text'):
    """This function helps you write logs
        Args:
        file_path (str, optional): You wnated write logs file. Defaults to None.
        log (str, optional): log text. Defaults to 'New text'.
    """
    with open(file_path, 'a') as file:
        file.write(log+"\n")
        file.close()

class YouTuba:
    def __init__(self, downloanding_limit : int = 500):
        self.youtube_url_pattern = r'^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|live\/|v\/)?)([\w\-]+)(\S+)?$'
        self.limit = downloanding_limit
        
    
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
    
    def get_webm_info(self, streaming_data : YouTube.streaming_data, url : str = None):
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
            write_log(log = f"Youtuba class get_webm_info method IncompleteRead {url}", file_path = 'data/logs/Youtuba.log')
            
        except:
            write_log(log = f"Youtuba class get_webm_info method ERROR {url}", file_path = 'data/logs/Youtuba.log')
   
    def get_audio_info(self, streaming_data : YouTube.streaming_data):
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
            write_log(log = f"Youtuba class get_audio_info method IncompleteRead {url}", file_path = 'data/logs/Youtuba.log')
            
        except:
            write_log(log = f"Youtuba class get_audio_info method ERROR {url}", file_path = 'data/logs/Youtuba.log')
    
    def clear_resolution(self, text):
        """_summary_

        Args: this function can find
        resolutin. function can find 100 to 3999 betwin
        text (_type_): string

        Returns:
        str: if function find resolutino returns resolutn as string
        """
        
        resolt = re.search(r'[1-9][0-9][0-9]?[0-9]', text)
        if resolt:
            return text[resolt.start(): resolt.end()]+'p'
    
    def get_resolutions_data(self, streaming_data : YouTube.streaming_data, voise_size : int = 0, url = None):
        data = {'144p' : None, '240p' : None, '360p' : None, '480p' : None, '720p' : None, '1080p' : None, '1440p' : None, '2160p' : None}

        try:
            for format in streaming_data['adaptiveFormats']: #adaptiveFormats
                mimtype = format['mimeType'].split(";")[0]

                if mimtype == "video/mp4":
                    size = round((float(format['contentLength'])/1024)/1024 + voise_size, 1)
                    quality = self.clear_resolution(format['qualityLabel'])

                    if quality:                    
                        if data.get(quality) != None and data[quality]['size'] < size:
                            data[quality] = {'itag' : format['itag'], 'size' : size, 'mimeType' : mimtype, 'lastModified' : format['lastModified']}
                    
                        elif data.get(quality) == None:
                            data[quality] = {'itag' : format['itag'], 'size' : size, 'mimeType' : mimtype, 'lastModified' : format['lastModified']}  
            
                if data['144p'] != None:
                    # data['resolutions'] = [key for key, value in data.items() if value != None and key in ('144p', '240p', '360p', '480p', '720p', '1080p', '1440p') and value['size'] <= self.limit]
                    return data 
        
        except IncompleteRead:
            write_log(log = f"Youtuba class get_resolutions_data method IncompleteRead {url}", file_path = 'data/logs/Youtuba.log')
        except:
            write_log(log = f"Youtuba class get_resolutions_data method ERROR {url}", file_path = 'data/logs/Youtuba.log')
            
    
    def sort_resolutions(self, data : dict, exsepted_resolutions : tuple = ('144p', '240p', '360p', '480p', '720p', '1080p', '1440p')):
        return [key for key, value in data.items() if value != None and key in exsepted_resolutions and value['size'] <= self.limit]
    

    def getData(self, yt : YouTube, url_id : str = None) -> (list, dict, dict):
        audio_data = self.get_audio_info(yt.streaming_data)
        webm_data = self.get_webm_info(yt.streaming_data)
        if webm_data and audio_data:
            data = self.get_resolutions_data(yt.streaming_data, voise_size = webm_data['size'], url = url_id)
            if data:
                resolutions = self.sort_resolutions(data)
                return (resolutions, data, audio_data)
            
    
    async def download_music(self, yt : YouTube, title : str = None) -> bool:
        print("audio downloandig started")
        data = self.get_audio_info(yt.streaming_data)
        if data:
            stream = yt.streams.get_by_itag(data['itag'])
            if stream:
                stream.download(output_path = 'data', filename = f"{title}.mp3")
                return True
        
            

if __name__ == '__main__':
    # ytb = YouTuba(downloanding_limit = 2_000)
    start = time.time()
    
    yt = YouTube(url = f"https://youtu.be/FrA98gZGbDI?si=Q2g1DLh3aWRztOcj", use_oauth=True)
    print(yt.streaming_data.keys())
    
    end = time.time()
    print(f"Run time: {end-start}")



