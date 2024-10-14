import aiocron

from bot import bot
from db.crud.payments import get_payments, set_payment_paid
from db.crud.orders import get_user_order
from db.crud.tariffs import get_tariff_by_id
from utils.vpn import remove_user
from db.crud.users import top_up_user_balance, get_all_users, set_user_tariff, set_user_server
from utils.payments import get_payment
from datetime import datetime as dt


@aiocron.crontab('0-54/6 * * * *')
async def check_payments():
    payments = get_payments()
    for payment in payments:
        if get_payment(payment.payment_id).paid:
            top_up_user_balance(payment.user_id, payment.amount)
            set_payment_paid(payment.id)


@aiocron.crontab('2-56/6 * * * *')
async def check_deadlines():
    users = get_all_users()
    for user in users:
        days_left = user.subscription_due.date() - dt.now().date()
        if days_left < 0 and user.tariff_id:
            order = get_user_order(user.id)
            if order:
                tariff = get_tariff_by_id(order.tariff_id)
            else:
                tariff = get_tariff_by_id(max(user.tariff_id, 2))
            if user.balance >= tariff.price:
                top_up_user_balance(user.id, -tariff.price)
                set_user_tariff(user.id, tariff.id)
            else:
                await remove_user(user.id, user.server)
                set_user_tariff(user.id, None)
                set_user_server(user.id, None)
                await bot.send_message(
                    user.id,
                    'Ваша подписка закончилась. Пожалуйста, пополните баланс для продления подписки.'
                )