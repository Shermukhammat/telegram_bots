


class ConText:
    def __init__(self) -> None:
        self.welcome = {}
    
    def welcome_user(self, user : dict) -> str:
        data = {'uz' : f"🤖 Assalomu alykum {user['name']} xush kelibsiz. 📥Video yuklash uchun menga Youtube dan video linkni jo'nating",
                'ru': f"🤖 Здравствуйте, {user['name']}. 📥 Отправьте мне ссылку на видео с Youtube, чтобы скачать видео", #🌐🏁🇬🇧🇷🇺🇺🇿
                'en' : f"🤖 Hello {user['name']}. 📥 Send me video link from Youtube to download video"}
        
        return data.get(user['lang'])
    
    def change_lang(self, lang : dict) -> str:
        data = {'uz' : f"Ilimos, Tilni tanlang",
                'ru' : "Пожалуйста, выберите язык",
                'en' : "Please, select a language"}

        return data.get(lang)
    
    def head_menu(self, lang : str = None): 
        data = {'uz' : "🎛 Bosh menu",
                'ru' : "🎛 Главное меню",
                'en' : "🎛 Main menu"}
        
        return data.get(lang)
    

    
    



if __name__ == "__main__":
    user = {'name': 'Shermukhammad', 'lang': 'en', 'registred': '31.01.2024 17:11'}
    
    context = ConText()
    print(context.welcome_user(user))

    