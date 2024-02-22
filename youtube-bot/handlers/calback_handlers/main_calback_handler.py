from loader import db, dp, bot, types, states, context, queues, ytb
from aiogram.dispatcher import FSMContext
import time
import asyncio
from pytube import YouTube
import re, unicodedata, os


def remove_file(file_name : str, directory : str = 'data'):
    files_list = os.listdir(directory)
    if file_name in files_list:
        os.remove(f"{directory}/{file_name}")


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value)
    return re.sub(r'[-\s]+', ' ', value).strip('-_')

@dp.callback_query_handler()
async def main_function(update : types.CallbackQuery, state : FSMContext):
    if db.is_user(update.from_user.id):
        if update.data == "remove":
            await bot.delete_message(chat_id = update.from_user.id, message_id = update.message.message_id)
            # await bot.send_message(chat_id = update.from_user.id, text = "")
    
        else:
            request = update.data.split('?')
            if len(request) == 2:
                function = request[0]
            
                if function == 'get_video':
                    params = request[1].split('&')
                    id, resolution = params[0], params[1]
                    
                    
                
                elif function == 'get_music':
                    id = request[1]
                    data_id = db.get_youtube_music(id)
                    
                    if data_id:
                        await bot.copy_message(chat_id = update.from_user.id, from_chat_id = db.data['data_chanel'], message_id = data_id)
                    
                    else:
                        if db.is_user_downloanding(update.from_user.id):
                            db.close_user_downlonding(update.from_user.id)
                            queues.set_music_queue(user_id = update.from_user.id, music_id = id)        
                        else:
                            await update.answer("Pleas expet unit you last file downloded", show_alert = True)
                            
                            