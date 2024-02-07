


class ConText:
    def __init__(self) -> None:
        self.__show_url_status__ = {
            'uz' : {"unavailable" : "Bunday video mavjud emas", 
                    "live" : "Iltimos jonli efir tugagandan keyin urunib ko'ring", 
                    "private" : "Bu yopqi video", 
                    "invalid" : "Yaroqsiz url"},

            'ru' : {"unavailable" : "такого видео не существует", 
                    "live" : "Пожалуйста, повторите попытку после прямой трансляции.", 
                    "private" : "Это частное видео", 
                    "invalid" : "Неверная ссылка"},

            'en' : {"unavailable" : "No such video exists", 
                    "live" : "Please try again after the live video ended", 
                    "private" : "This is private video", 
                    "invalid" : "Invalid url"}}
    
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
    

    def this_invalid_url(self, lang : str = None):
        data = {'uz' : "❌ Bu url yaroqsiz",
                'ru' : "❌ This url is invalid",
                'en' : "❌ Этот URL-адрес недействителен"}
        
        return data.get(lang)
    

    def show_url_status(self, raised : str = None, lang : str = 'uz'):
        return self.__show_url_status__[lang].get(raised)

    
    



if __name__ == "__main__":
    user = {'name': 'Shermukhammad', 'lang': 'en', 'registred': '31.01.2024 17:11'}
    
    context = ConText()
    print(context.welcome_user(user))

    