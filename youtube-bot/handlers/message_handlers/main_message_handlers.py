from loader import db, dp, bot, types, inline, buttons, context, states, is_url, ytb
from aiogram.dispatcher import FSMContext

@dp.message_handler()
async def main_message_hanler(update : types.Message, state : FSMContext):
    if db.is_user(id = update.from_user.id):
        user = db.users[update.from_user.id]
        if update.text in ["🌐 Tilni o'zgartirish", "🌐 Изменить язык", "🌐 Change language"]:
            await state.set_state(states.change_lang)
            await update.answer(text = context.change_lang(lang = user['lang']), reply_markup = buttons.language_buttons(lang = user['lang']))

        
        

        else:
            url = is_url(update.text)
            if url:
                status, raise_id = ytb.check_availability(url)
                if status:
                    await update.answer("Valid")

                else:
                    await update.reply(context.show_url_status(raised = raise_id, lang = user['lang']))
                
                
                # else:
                #     await update.reply(text = context.this_invalid_url(lang = user['lang']))
                
            elif user['menu'] == False:
                user['menu'] = True
                await update.answer(text = context.head_menu(lang = user['lang']), 
                                reply_markup = buttons.head_menu(lang = user['lang']))
    
    elif db.is_admin(id = update.from_user.id):
        pass

    else:
        if update.from_user.language_code in ['uz', 'en', 'ru']:
            lang = update.from_user.language_code
        else:
            lang = 'en'
        
        db.registir(id = update.from_user.id, 
                    name = update.from_user.first_name, 
                    lang = lang)
        
        
        user = db.users[update.from_user.id]
        await update.answer(text = context.welcome_user(user), reply_markup = buttons.head_menu(lang = lang))