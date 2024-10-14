from db.models import Payment
from db.base import session


def create_payment_db(payment_id: str, user_id: int, amount: int):
    payment = Payment(
        payment_id=payment_id,
        user_id=user_id,
        amount=amount
    )
    session.add(payment)
    session.commit()
    return payment


def set_payment_paid(payment_id: int):
    payment = session.query(Payment).filter(Payment.id == payment_id).first()
    payment.paid = True
    session.commit()
    return payment


def get_payments():
    return session.query(Payment).all()