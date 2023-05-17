from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultCachedVideo, InlineQueryResultPhoto, InputMessageContent, InputMediaPhoto
from db import Database
import time
from random import randint
from Google import search_movi
from PyMemory import load_movi_data

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
def query(update, context):
    query = update.inline_query.query
    movies = search_movi(query, titles, movies_dataset)
    answers = []
    for movie in movie:
        answers.append()
    
    
 
    
def main():
    updater = Updater(token = API_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_function))
    dispatcher.add_handler(MessageHandler(Filters.text, core_function))
    dispatcher.add_handler(MessageHandler(Filters.video, video_handler))
    dispatcher.add_handler(InlineQueryHandler(query))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    print("Starting bot ...")