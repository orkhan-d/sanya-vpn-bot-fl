from aiogram import Router, F, types

import utils.vpn
from db.crud.orders import create_order
from db.crud.servers import get_server_with_min_users
from db.crud.texts import get_text
from db.crud.tariffs import get_all_tariffs, get_tariff_by_id
from db.crud.users import get_user_by_id, set_user_subscription_due, set_user_server, set_user_subscription_link, \
    set_user_tariff
from keyboards import connect as kb
from keyboards import tutors as tutors_kb

router = Router()


@router.callback_query(F.data == 'connect')
async def on_start(query: types.CallbackQuery):
    user = get_user_by_id(query.from_user.id)
    tariffs = get_all_tariffs(user.new)
    text = get_text('select-tariff')
    await query.message.answer(text,
                               reply_markup=kb.tariffs_kb(tariffs))


@router.callback_query(F.data.regexp(r'^tariff_\d+$'))
async def on_start(query: types.CallbackQuery):
    user = get_user_by_id(query.from_user.id)
    tariff = get_tariff_by_id(int(query.data.replace('tariff_', '')))
    if tariff.price == 0 and user.new:
        if not user.server_id:
            server = get_server_with_min_users()
            link = await utils.vpn.add_user(user.id, server)
            set_user_server(user.id, server.id)
            set_user_subscription_due(user.id, tariff.duration)
            set_user_tariff(user.id, tariff.id)
            set_user_subscription_link(user.id, link)
        else:
            link = user.subscription_link
        await query.message.answer(
            get_text('on_connect').format(
                tariff=tariff.title,
                until_date=user.subscription_due,
                link=link
            ),
            reply_markup=tutors_kb.all_tutors_kb
        )
    else:
        create_order(user.id, tariff.id)
        if user.balance < tariff.price:
            text = (get_text('not_enough_balance_active_sub')
                    if user.has_active_subscription()
                    else get_text('not_enough_balance_inactive_sub'))
            await query.message.answer(
                text,
                reply_markup=kb.top_up_kb
            )
        else:
            text = (get_text('wait_for_connect_active_sub')
                    if user.has_active_subscription()
                    else get_text('wait_for_connect_inactive_sub'))
            await query.message.answer(
                text
            )
