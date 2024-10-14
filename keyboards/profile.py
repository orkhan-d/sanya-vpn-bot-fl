from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

profile_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Чат поддержки", url="https://t.me/d_orkhan")
        ],
        [
            InlineKeyboardButton(text="Партнерская программа", callback_data="partner-program")
        ],
        [
            InlineKeyboardButton(text="Пополнить баланс",
                                 web_app=WebAppInfo(
                                     url="https://sanya-vpn.online",
                                 ))
        ],
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="start")
        ],
    ]
)

partner_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="profile")
        ],
    ]
)