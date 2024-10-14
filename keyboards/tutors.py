from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


all_tutors_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="iOS (iPhone, iPad)", callback_data="ios_tutor"),
        ],
        [
            InlineKeyboardButton(text="Android", callback_data="android_tutor"),
            InlineKeyboardButton(text="Huawei", callback_data="huawei_tutor"),
        ],
        [
            InlineKeyboardButton(text="Windows", callback_data="windows_tutor"),
            InlineKeyboardButton(text="Linux", callback_data="linux_tutor"),
        ],
        [
            InlineKeyboardButton(text="Android TV", callback_data="android_tv_tutor"),
            InlineKeyboardButton(text="Mac", callback_data="mac_tutor"),
        ],
        [
            InlineKeyboardButton(text="Роутер", callback_data="router_tutor"),
        ],
    ]
)

after_tutor_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Рекомендовать друзьям", callback_data="share"),
        ],
        [
            # TODO: set support chat link
            InlineKeyboardButton(text="Задать вопрос", url="https://t.me/"),
        ],
    ]
)