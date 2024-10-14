from aiogram import Router, F, types

from db.crud.tariffs import get_tariff_by_id
from db.crud.texts import get_text
from db.crud.users import get_user_by_id
from keyboards import profile as kb
from datetime import datetime as dt

router = Router()


@router.callback_query(F.data == 'profile')
async def on_start(query: types.CallbackQuery):
    user = get_user_by_id(query.from_user.id)
    if user.tariff_id is None:
        text = get_text('profile_no_sub').format(
            id=user.id,
            name=user.name,
            balance=user.balance,
            bonuses=user.bonuses
        )
    else:
        days_left = (user.subscription_due - dt.now()).days
        text = get_text('profile_has_sub').format(
            id=user.id,
            name=user.name,
            balance=user.balance,
            days=days_left if days_left > 0 else 'ключ не активен',
            bonuses=user.bonuses,
            tariff=user.tariff,
            next_tariff=user.tariff if user.tariff.price > 0 else get_tariff_by_id(2)
        )
    await query.message.answer(text, reply_markup=kb.profile_kb)


@router.callback_query(F.data == 'partner-program')
async def on_start(query: types.CallbackQuery):
    user = get_user_by_id(query.from_user.id)
    text = get_text('partner_main').format(
        id=user.id,
        friends=user.friends,
        bonuses=user.bonuses
    )

    await query.message.answer(text, reply_markup=kb.partner_kb)
