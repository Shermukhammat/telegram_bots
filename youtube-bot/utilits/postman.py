from telegraph import Telegraph
import requests

class Postman:
    def __init__(self, token: str = None, telgram_bot_token : str = None, bot_photo = '/file/f14e1e26c3e26c1d00217.jpg'):
        self.token = token
        self.tbot_token = telgram_bot_token
        self.bot_photo = bot_photo
        self.telegraph = Telegraph(access_token = token)
    
    def upload(self, data : dict, path = "Kop-Soraladigan-Savollar-11-24", title = "Ko'p So'raladigan Savollar", autor = "Grand Nasiya Bot"):
        html_content = f"<img src='{self.bot_photo}' alt='Uploaded Photo'>"
        n = 1
        for question, answer in data.items():
            html_content += f"<h4>{n}. {question}</h4>"
            html_content += f"<p><em>{answer}</em></p>"

            self.telegraph.edit_page(html_content = html_content, title = title, path = path, author_name = autor)

            n+=1
        
        return True

    def edit_bot_describtion(self, bot_description : str):   
        url = f'https://api.telegram.org/bot{self.tbot_token}/setMyShortDescription'
        params = {'short_description': bot_description}
        
        response = requests.post(url, params=params)
        return response.json()
    
    def edit_bot_what_cando(self, bot_can_description : str):   
        url = f'https://api.telegram.org/bot{self.tbot_token}/setMyDescription'
        params = {'description': bot_can_description}

        response = requests.post(url, params=params)
        return response.json()


if __name__ == '__main__':
    pass
    # postman = Postman(token = 'none')
    # data = {f"savol {n}" : 'javob' for n in range(10)}
    # print(data)
    # postman.upload(data=data)