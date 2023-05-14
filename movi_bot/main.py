from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultCachedVideo

API_TOKEN = "6080581500:AAHnIOY5m2wjqjE_uQUDMFAvLBC0L97eo20"
CHANEL_ID = '-1001942672781'
ADMINS = [1661189380]

def start_function(update, context):
    user_name = update.message.chat.first_name
    update.message.reply_text(f"Salom {user_name}!")
    # print(update.message.chat.id)

def core_function(update, context):
    # print(update)
    pass

def video_handler(update, context):
    user_id = update.message.chat.id
    
    if user_id in ADMINS:
        video = update.message.video
        if int(video.file_size / (1024*1024)) > 200:
            caption = update.message.caption
            vm_info = context.bot.send_video(CHANEL_ID, video, caption = caption)

            message_id = vm_info.message_id
            file_size = vm_info.video.file_size
            file_id = vm_info.video.file_id
            # print(vm_info)
        else:
            update.message.reply_text("Video xajmi 200 Mb dan kichkina!")


    # print(update.message)
    # chat_id = update.message.chat.id
    # message_id = update.message.message_id
    # video = update.message.video
    # print(video)
    
    # message_info = context.bot.send_video(chat_id, video)
    # print(message_info)

def query(update, context):
    query = update.inline_query.query
    # print(query)
    result = InlineQueryResultCachedVideo(
        id= '1',
        video_file_id = 'BAACAgIAAxkDAAIBBGRgkuVo9E-sqY0dTtCcXC0SmtsXAAJgBgACbFGpSmoxUbzbOm5RLwQ',
        title='Your Video Title',
        caption = "Bu kino ancha yasxshi!"
    )

    # Send the results to the user
    update.inline_query.answer([result])

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