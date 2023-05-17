from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultCachedVideo
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
    global n
    n+=1
    # user_id = update.message.chat.id
    # if n == 19:
    #     n = 0
    #     sleep = randint(30, 120)
        
    #     print(f"sleep {sleep} second...")
    #     time.sleep(sleep)

    # if user_id in ADMINS:
    #     try:
    #         video = update.message.video
    #         if int(video.file_size / (1024*1024)) > 100:
    #             caption = update.message.caption
    #             vm_info = context.bot.send_video(CHANEL_ID, video, caption = caption)

    #             message_id = vm_info.message_id
    #             file_size = vm_info.video.file_size
    #             file_id = vm_info.video.file_id
    #             database.add_movi(caption, file_id = file_id, size = file_size, message_id = message_id)
    #             # print(vm_info)
    #         else:
    #             update.message.reply_text("The video size is smoller then 100 Mb")
    #             print("! The video size is smoller then 100 Mb ")
    #     except:
    #         print(print('Video handler EROR ...'))


    # print(update.message)
    # chat_id = update.message.chat.id
    # message_id = update.message.message_id
    # video = update.message.video
    # print(video)
    
    # message_info = context.bot.send_video(chat_id, video)
    # print(message_info)

titles, movies_dataset, line_count = load_movi_data()
def query(update, context):
    query = update.inline_query.query
    
    movies = search_movi(query, titles, movies_dataset)
    answers = []
    id = 0
    for movie in movies:
        id+=1
        answers.append(InlineQueryResultCachedVideo(id = str(id),
                                                    video_file_id = movie['file_id'],
                                                    caption = movie['caption'],
                                                    title = movie['title'],
                                                    description = movie['caption']))
    # result = InlineQueryResultCachedVideo(
    #     id= '1',
    #     video_file_id = 'BAACAgIAAxkDAAIBBGRgkuVo9E-sqY0dTtCcXC0SmtsXAAJgBgACbFGpSmoxUbzbOm5RLwQ',
    #     title='Your Video Title',
    #     caption = "Bu kino ancha yasxshi!"
    # )

    # Send the results to the user
    update.inline_query.answer(answers)

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
    print("Starting bot ...")
    main()