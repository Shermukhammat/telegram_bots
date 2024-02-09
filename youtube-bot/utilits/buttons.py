from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton



class Inline:
    def __init__(self):
        self.resolutions_template = ['144p', '240p', '360p', '480p', '720p', '1080p', '1440p']
    
    def video_resolotion_buttons(self, resolutions : list = None, id : str = None):
        if len(resolutions) <= 3:
            buttons = [[InlineKeyboardButton(text = f"📹 {resolution}", callback_data = f"get_video?{id}&{resolution}") for resolution in resolutions],
                        [InlineKeyboardButton(text = "🎵 mp3", callback_data = f"get_music?{id}")],
                        [InlineKeyboardButton(text = "❌", callback_data = "remove")]]

            return InlineKeyboardMarkup(inline_keyboard = buttons)
        elif len(resolutions) <= 6:
            buttons = [[InlineKeyboardButton(text = f"📹 {resolution}", callback_data = f"get_video?{id}&{resolution}") for resolution in resolutions[:3]],
                        [InlineKeyboardButton(text = f"📹 {resolution}", callback_data = f"get_video?{id}&{resolution}") for resolution in resolutions[3:]],
                        [InlineKeyboardButton(text = "🎵 mp3", callback_data = f"get_music?{id}")],
                        [InlineKeyboardButton(text = "❌", callback_data = "remove")]]

            return InlineKeyboardMarkup(inline_keyboard = buttons)

        elif len(resolutions) <= 8:
            buttons = [[InlineKeyboardButton(text = f"📹 {resolution}", callback_data = f"get_video?{id}&{resolution}") for resolution in resolutions[:3]],
                        [InlineKeyboardButton(text = f"📹 {resolution}", callback_data = f"get_video?{id}&{resolution}") for resolution in resolutions[3:6]],
                        [InlineKeyboardButton(text = f"📹 {resolution}", callback_data = f"get_video?{id}&{resolution}") for resolution in resolutions[6:]],
                        [InlineKeyboardButton(text = "❌", callback_data = "remove")]]
            buttons[2].append(InlineKeyboardButton(text = "🎵 mp3", callback_data = f"get_music?{id}"))

            return InlineKeyboardMarkup(inline_keyboard = buttons)


            
    


class Buttons:
    def __init__(self) -> None:
        pass
    
    def language_buttons(self, lang : str = None):
        if lang == 'uz':
            return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "🇷🇺 Ruscha"), KeyboardButton(text = "🇬🇧 Inglizcha")],
                                                            [KeyboardButton(text = "⬅️ Orqaga")]],
                                                            resize_keyboard = True)
        
        elif lang == 'ru':
            return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "🇺🇿 Узбекский"), KeyboardButton(text = "🇬🇧 Английский")],
                                                   [KeyboardButton(text = "⬅️ Назад")]],
                                                   resize_keyboard = True)

        elif lang == 'en':
            return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "🇷🇺 Russian"), KeyboardButton(text = "🇺🇿 Uzbek")],
                                                   [KeyboardButton(text = "⬅️ Back")]],
                                                   resize_keyboard = True)
    
    def head_menu(self, lang : str = 'uz'):
        if lang == 'uz':
            return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "📖 Qo'lanma"), KeyboardButton(text = "🌐 Tilni o'zgartirish")],
                                                            [KeyboardButton(text = "📈 Statistika")]],
                                                            resize_keyboard = True)
        
        elif lang == 'ru':
            return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "📖 Помощь"), KeyboardButton(text = "🌐 Изменить язык")],
                                                            [KeyboardButton(text = "📈 Статистика")]],
                                                            resize_keyboard = True)

        elif lang == 'en':
            return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "📖 Manual"), KeyboardButton(text = "🌐 Change language")],
                                                            [KeyboardButton(text = "📈 Statistics")]],
                                                            resize_keyboard = True)

    
    


    
if __name__ == '__main__':
    buttons = Buttons()
    print(buttons.head_menu(lang='ru'))


