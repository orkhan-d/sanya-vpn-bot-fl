from yookassa import Configuration, Payment
from yookassa.payment import PaymentResponse

from settings import settings

Configuration.account_id = settings.YOOKASSA_ACCOUNT_ID
Configuration.secret_key = settings.YOOKASSA_SECRET_KEY


def create_payment(amount: int) -> PaymentResponse:
    res = Payment.create(
        {
            "amount": {
                "value": f'{amount}',
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://t.me/sanya_vpn_bot"
            },
            "capture": True,
            "receipt": {
                "items": [
                    {
                        "description": "Пополнение баланса в сервисе интернет-безопасности",
                        "quantity": "1.00",
                        "amount": {
                            "value": f'{amount}',
                            "currency": "RUB"
                        },
                        "vat_code": "1",
                    },
                ]
            }
        }
    )

    return res


def get_payment(payment_id: str) -> PaymentResponse:
    return Payment.find_one(payment_id)
