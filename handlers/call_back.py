from aiogram import types, Dispatcher
from config import bot, ADMIN_ID, SECRET_WORD
from keyboards.inline_buttons import questionnaire_keyboard


async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Python or Mojo ?',
        reply_markup=await questionnaire_keyboard()
    )


async def python_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='You are Python Developer 🚀',
    )


async def mojo_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='You are Mojo Developer 🔥',
    )


async def admin_call(message: types.Message):
    if message.from_user.id == int(ADMIN_ID):
        await message.delete()
        await bot.send_message(
            chat_id=message.from_user.id,
            text='Hello, admin 🤖'
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text='You are not admin ⛔️'
        )


def register_call_back_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == 'start_questionnaire')
    dp.register_callback_query_handler(python_call,
                                       lambda call: call.data == 'python')
    dp.register_callback_query_handler(mojo_call,
                                       lambda call: call.data == 'mojo')
    dp.register_message_handler(admin_call,
                                lambda word: SECRET_WORD in word.text)
