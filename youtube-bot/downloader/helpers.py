import requests




class Tasks:
    def __init__(self, api_url : str = "http://127.1.1.1:7070"):
        self.api_url = api_url
    
    def addMusicTask(self, ytid : int = None, userId : int = None, messageId : int = None) -> bool:
        try:
            respons = requests.get(f"{self.api_url}/addMusicTask?ytid={ytid}&userId={userId}&messageId={messageId}")

        except requests.exceptions.ConnectionError:
            print("API doesn't answer")
            return
            
        except:
            print("Somthing went wrong with API")
            return 
        
        if respons.status_code == 200:
            return respons.json().get('status') == 1
        
    
    def getFinishedTask(self):
        try:
            respons = requests.get(f"{self.api_url}/getFinishedTask?")

        except requests.exceptions.ConnectionError:
            print("API doesn't answer")
            return
            
        except:
            print("Somthing went wrong with API")
            return 
        
        if respons.status_code == 200:
            return respons.json()


if __name__ == '__main__':
    tasks = Tasks()
    # status = tasks.addMusicTask(ytid = "_P7JjijXlYg", userId = 99, messageId = 100)
    status = tasks.getFinishedTask()
    print(status)