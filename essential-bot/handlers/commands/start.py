from loader import dp, types



@dp.message_handler(state="*")
async def start_handler(update: types.Message):
    await update.answer("Wellcom to Essentila word bot", 
                        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = "Essential 1", web_app = types.WebAppInfo(url = "https://www.essentialenglish.review/apps/4000-essential-english-words-2/unit-1-the-twelve-months/#0"))]]) )
    
