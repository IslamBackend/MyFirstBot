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
    my_profile_button = InlineKeyboardButton(
        'My Profile 🗄️',
        callback_data='my_profile'
    )
    random_profiles_button = InlineKeyboardButton(
        'View Profiles 👤',
        callback_data='random_profiles'
    )
    reference_button = InlineKeyboardButton(
        'Reference Menu 💵',
        callback_data='reference_menu'
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(random_profiles_button)
    markup.add(reference_button)
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


async def like_dislike_keyboard(owner_tg_id):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        'Like ❤️',
        callback_data=f'liked_profile_{owner_tg_id}'
    )
    dislike_button = InlineKeyboardButton(
        'Dislike 💔',
        callback_data=f'random_profiles'
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup


async def referral_keyboard():
    markup = InlineKeyboardMarkup()
    generate_button = InlineKeyboardButton(
        'Generate link 🔗',
        callback_data='generate_link'
    )
    markup.add(generate_button)
    return markup
