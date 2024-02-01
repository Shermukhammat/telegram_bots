from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton



class Inline:
    def __init__(self):
        pass

    def start_presed(self, lang : str = 'uz') -> InlineKeyboardMarkup:
        """This function use for when user first time registred

        Args:
            lang (str, optional): Buttons language might be 'uz', 'en', 'ru'. Defaults to 'uz'.

        Returns:
            _type_: InlineKeybordMarkup
        """

        if lang == "uz":
            return InlineKeyboardMarkup(inline_keyboard = [[InlineKeyboardButton(text = "🌐 Tilni o'zgartirish", callback_data = "change_lang"), 
                                                            InlineKeyboardButton(text = "📖 Qo'lanma", callback_data = "manual")]])
        elif lang == 'ru':
            return InlineKeyboardMarkup(inline_keyboard = [[InlineKeyboardButton(text = "🌐 Изменить язык", callback_data = "change_lang"), 
                                                            InlineKeyboardButton(text = "📖 Помощь", callback_data = "manual")]])
        elif lang == 'en':
            return InlineKeyboardMarkup(inline_keyboard = [[InlineKeyboardButton(text = "🌐 Change language", callback_data = "change_lang"), 
                                                            InlineKeyboardButton(text = "📖 Manual", callback_data = "manual")]])


class Buttons:
    def __init__(self) -> None:
        pass
    inline = Inline()


    



