from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        'Start Questionnaire 🚀',
        callback_data='start_questionnaire'
    )
    registration_button = InlineKeyboardButton(
        'Registration 🪪',
        callback_data='registration'
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    return markup


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        'Python 🚀',
        callback_data='python'
    )
    mojo_button = InlineKeyboardButton(
        'Mojo 🔥',
        callback_data='mojo'
    )
    markup.add(python_button)
    markup.add(mojo_button)
    return markup
