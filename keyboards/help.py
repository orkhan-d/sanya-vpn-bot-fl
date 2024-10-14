from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

help_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Чат поддержки", url="https://t.me/d_orkhan")
        ],
        [
            InlineKeyboardButton(text="📜 Правила сервиса", callback_data="rules")
        ],
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="start")
        ],
    ]
)

rules_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="start")
        ],
    ]
)
