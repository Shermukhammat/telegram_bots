from pytube import YouTube
import requests
import re
# respons = requests.get(url="http://yodsutdddssu.be/LY7f1a29lPo?si=3Ujpa3_vqSneqfF3")
# print(respons.status_code)

# yt = YouTube(url = "https://youtu.be/vMXg4V-fKGw?si=qZngFvt-uSh7-oW8")
# print(yt.title)
# print(yt.thumbnail_url)

# streams = yt.streams.filter(file_extension='mp4', type = 'video')
# for stream in streams:
#     print(stream)
    # print(stream.res)
# stream = streams.get_by_itag(itag = 18)
# stream.download(filename = 'video.mp4')


def youtube_url_validation(url : str):
    youtube_url = re.search(pattern = r'^https://(www.)?(youtube.com|youtu.be).*', string = url)
    # print(youtube_url)
    return youtube_url != None


def url_checker(url : str):
    respons = requests.get(url = url)
    return respons.status_code == 200


# print(url_checker("https://www.youtube.com/watch?v=vMXg4V-fKGw"))

url1 = "https://youtu.be/vMXg4V-fKGw?si=BRhjFnxQuwStMaM2"
url2 = "https://www.youtube.com/watch?v=vMXg4V-fKGw"


def url_checker(url):
    # Regular expression pattern to match YouTube video IDs
    pattern = re.compile(r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})')
    
    match = pattern.search(url)
    
    if match:
        id = match.group(1)
        respons = requests.get(url = f"https://youtube.com/oembed?url=http://www.youtube.com/watch?v={id}")
        
        return respons.status_code == 200
    return False

# Example usage:
print(extract_video_id(url = url1))
