from pytube import YouTube
from pytube.exceptions import LiveStreamError, VideoUnavailable, VideoPrivate
from requests.models import PreparedRequest
import requests

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
    def __init__(self, videoSizeLimit : int = 1_900):
        self.limit = videoSizeLimit 

    
    def __write_log__(file_path : str = "data/logs.log", log : str = 'New text'):
        """This function helps you write logs

        Args:
        file_path (str, optional): You wnated write logs file. Defaults to None.
        log (str, optional): log text. Defaults to 'New text'.
        """
        with open(file_path, 'a') as file:
            file.write(log+"\n")
            file.close()


    def check_availability(self, url : str) -> (bool, str):
        try:
            yt = YouTube(url, use_oauth = True)
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



url = f"https://www.youtube.com/live/vQP8AwAFzI8?si=UjiUMv2Qs9SV6Grh"

ytb = YouTuba()
print(ytb.check_availability(url))
# yt = YouTube(url, use_oauth = True)
# yt.check_availability()
