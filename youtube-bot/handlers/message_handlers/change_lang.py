from loader import types, db, dp, bot, inline, buttons, types, states, context
from aiogram.dispatcher import FSMContext


@dp.message_handler(state = states.change_lang)
async def change_language_handler(update : types.Message, state : FSMContext):
    if db.is_user(update.from_user.id):
        user = db.users[update.from_user.id]
        if update.text == "🇷🇺 Ruscha" or update.text == "🇷🇺 Russian":
            await state.finish()
            db.update_user_lang(id = update.from_user.id, lang = 'ru')
            await update.answer(text = "вы выбрали русский", reply_markup = buttons.head_menu(lang = 'ru'))

        elif update.text == "🇬🇧 Inglizcha" or update.text == "🇬🇧 Английский":
            await state.finish()
            db.update_user_lang(id = update.from_user.id, lang = 'en')
            await update.answer(text = "You chose English", reply_markup = buttons.head_menu(lang = 'en'))

        elif update.text  == "🇺🇿 Узбекский" or update.text == "🇺🇿 Uzbek":
            await state.finish()
            db.update_user_lang(id = update.from_user.id, lang = 'uz')
            await update.answer(text = "Siz o'zbek tilni tanladingiz", reply_markup = buttons.head_menu(lang = 'uz'))

        elif update.text == "⬅️ Orqaga" or update.text == "⬅️ Назад" or update.text == "⬅️ Back":
            await state.finish()
            await update.answer(text = context.head_menu(lang = user['lang']), reply_markup = buttons.head_menu(lang = user['lang']))

        else:
            await update.answer(text = context.change_lang(lang = user['lang']), 
                                reply_markup = buttons.language_buttons(lang = user['lang']))
            

    elif db.is_admin(update.from_user.id):
        pass