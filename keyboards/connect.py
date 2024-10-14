from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from db.models import Tariff


def tariffs_kb(tariffs: list[Tariff]):
    kb = []
    for tariff in tariffs:
        title = tariff.title if tariff.price == 0 else f'{tariff.title} | {tariff.price} руб.'
        kb.append([
            InlineKeyboardButton(text=title,
                                 callback_data=f'tariff_{tariff.id}')
        ])
    return InlineKeyboardMarkup(inline_keyboard=kb)


top_up_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Пополнить баланс",
                web_app=WebAppInfo(
                    url="https://sanya-vpn.online/",
                )
            )
        ]
    ]
)