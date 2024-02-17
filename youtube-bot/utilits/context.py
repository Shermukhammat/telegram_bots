


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
        self.__creat_video_caption__ = {'uz' : '\n\nYuklab olish sifatni tanlang 👇🏻',
                                        'ru' : "\n\nВыберите качество загрузки 👇🏻",
                                        "en" : "\n\nSelect download quality 👇🏻"}
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

    
    def creat_video_caption(self, title : str = None, resolutions : list = None, data : dict = None, chanel_name : str = "Noname chanel", lang : str = 'uz', audio_size : bool = None):
        context = f"📽 {title}"
        context += f"\n📡 {chanel_name}\n\n"

        for resolution in resolutions:
                context += f"\n⚡️ <b>{resolution} : {data[resolution]['size']} Mb</b>"
        context += f"\n🎧  <b>Mp3 : {audio_size} Mb</b>"

        return context + self.__creat_video_caption__[lang]



if __name__ == "__main__":
    user = {'name': 'Shermukhammad', 'lang': 'en', 'registred': '31.01.2024 17:11'}
    
    context = ConText()
    print(context.welcome_user(user))

    