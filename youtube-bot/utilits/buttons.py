from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton



class Inline:
    def __init__(self):
        pass

    


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


