from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultCachedVideo, InlineQueryResultPhoto, InputMessageContent, InputMediaPhoto
from db import Database
import time
from random import randint
from Google import search_movi
from PyMemory import load_movi_data
import requests

API_TOKEN = "6080581500:AAHnIOY5m2wjqjE_uQUDMFAvLBC0L97eo20"
CHANEL_ID = '-1001942672781'
ADMINS = [1661189380]

database = Database('database.db')
database.conect()

def start_function(update, context):
    user_name = update.message.chat.first_name
    update.message.reply_text(f"Salom {user_name}!")
    # print(update.message.chat.id)

def core_function(update, context):
    # print(update)
    pass

n = 0
def video_handler(update, context):
    pass

#AAMCAQADGQEAAg7hZGS6qOSrBko3wcVvJ2KEGrqE-LMAApkCAAIhxDlH6O_gdxKk1vkBAAdtAAMvBA

titles, movies_dataset, line_count = load_movi_data()
# response = requests.get('https://picsum.photos/100/100')
# response = response.url

def query(update, context):
    query = update.inline_query.query
    if len(query) > 3:
        global movies_dataset, titles
        indexs = search_movi(query, titles = titles, limt = 30)

        answers = []
        n = 0
        for index in indexs:
            # response = requests.get('https://picsum.photos/100/100')
            # response = response.url
            movie = movies_dataset[index]
            answers.append(InlineQueryResultArticle(id = str(n), 
                                        title = movie['title'],
                                        description = movie['caption'],
                                        input_message_content = InputTextMessageContent(f"/get {index}"),
                                        thumb_url = f'https://picsum.photos/id/{randint(10, 500)}/100/100',
                                        thumb_height = 100,
                                        thumb_width = 200))
            n+=1
        #     print(n)
        # print("answer")
        update.inline_query.answer(answers)

def get_movie(update, context):
    global movies_dataset
    id = update.message.chat.id
    message_id = update.message.message_id
    message = update.message.text
    index = message[5:]

    context.bot.delete_message(chat_id = id, message_id = message_id)
    if index.isdigit():
        movie = movies_dataset[int(index)]
        context.bot.send_video(chat_id = id, video = movie['file_id'], caption = movie['caption'])

        

    
def main():
    updater = Updater(token = API_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_function))
    dispatcher.add_handler(CommandHandler('get', get_movie))

    dispatcher.add_handler(MessageHandler(Filters.text, core_function))
    dispatcher.add_handler(MessageHandler(Filters.video, video_handler))

    dispatcher.add_handler(InlineQueryHandler(query))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    print("Starting bot ...")