


class ConText:
    def __init__(self) -> None:
        self.welcome = {}
    
    def welcome_user(self, user : dict):
        data = {'uz' : f"Assalomu alykum {user['name']} xush kelibsiz. Men youtubedan video yuklovchi botman. Mendan foydalanshni o'rganish uchun yo'riqnoma tugmasni bosing. Agar tilin o'zgartirmoqchi bo'lsangiz tilni o'zgartrish tugmasni bosing.",
                'ru': f"Здравствуйте, {user['name']}, добро пожаловать. Я загружаю видео на YouTube. Нажмите кнопку «Обучение», чтобы узнать, как его использовать.",
                'en' : f"Hello {user['name']}, welcome. I am a youtube video uploader. Click the tutorial button to learn how to use it"}
        print(user)
        return data.get(user['lang'])
    


if __name__ == "__main__":
    user = {'name': 'Shermukhammad', 'lang': 'en', 'registred': '31.01.2024 17:11'}
    
    context = ConText()
    print(context.welcome_user(user))

    