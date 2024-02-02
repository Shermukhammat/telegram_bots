from loader import db, dp, bot, types, states, context
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler()
async def main_function(update : types.CallbackQuery, state : FSMContext):
    if update.data == "change_lang":
        await state.set_state(states.change_lang)
        await bot.delete_message(chat_id = update.from_user.id, message_id = update.message.message_id)
        await bot.send_message(chat_id = update.from_user.id, text = "")