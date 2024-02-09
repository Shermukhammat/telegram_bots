from loader import db, dp, bot, types, states, context
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler()
async def main_function(update : types.CallbackQuery, state : FSMContext):
    if update.data == "remove":
        await bot.delete_message(chat_id = update.from_user.id, message_id = update.message.message_id)
        # await bot.send_message(chat_id = update.from_user.id, text = "")
    
    else:
        request = update.data.split('?')
        if len(request) == 2:
            function = request[0]
            params = request[1].split('&')
            
            if function == 'get_video':
                print(params)