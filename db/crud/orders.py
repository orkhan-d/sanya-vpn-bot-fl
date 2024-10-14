from db.models import Order
from db.base import session


def create_order(user_id: int, tariff_id: int):
    cancel_user_undone_orders(user_id)
    order = Order(
        user_id=user_id,
        tariff_id=tariff_id
    )
    session.add(order)
    session.commit()
    return order


def cancel_user_undone_orders(user_id: int):
    orders: list[Order] = (session.query(Order).filter(Order.user_id == user_id)
                           .filter(Order.done is False).filter(Order.canceled is False).all())
    for order in orders:
        order.canceled = True

    session.commit()


def get_all_orders():
    orders = session.query(Order).all()
    return orders


def get_user_order(user_id: int) -> Order | None:
    order = (session.query(Order).
             filter(Order.user_id == user_id).
             filter(Order.canceled is False).
             filter(Order.done is False).
             first())
    return order
