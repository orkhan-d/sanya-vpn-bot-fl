from db.models import User
from db.base import session
from datetime import datetime as dt, timedelta as td


def get_all_users() -> list[User]:
    return session.query(User).all()


def get_user_by_id(user_id: int) -> User:
    user = session.query(User).get(user_id)
    if user:
        session.expunge(user)
    return user


def create_user(user_id: int,
                name: str,
                username: str,
                invited_by: int | None = None) -> User:
    if user := get_user_by_id(user_id):
        return user
    user = User(
        id=user_id,
        name=name,
        username=username,
        invited_by=invited_by
    )
    session.add(user)
    session.commit()
    return user


def set_user_subscription_due(user_id: int, days: int) -> User:
    user = session.query(User).get(user_id)
    user.subscription_due = dt.now() + td(days=days)
    session.commit()
    return user


def set_user_subscription_link(user_id: int, link: str) -> User:
    user = session.query(User).get(user_id)
    user.subscription_link = link
    session.commit()

    print(user)
    return user


def set_user_balance(user_id: int, balance: float) -> User:
    user = session.query(User).get(user_id)
    user.balance = balance
    session.commit()
    return user


def top_up_user_balance(user_id: int, amount: float) -> User:
    user = session.query(User).get(user_id)
    user.balance += amount
    session.commit()
    return user


def set_user_server(user_id: int, server_id: int) -> User:
    user = session.query(User).get(user_id)
    user.server_id = server_id
    session.commit()
    return user


def set_user_tariff(user_id: int, tariff_id: int) -> User:
    user = session.query(User).get(user_id)
    user.tariff_id = tariff_id
    session.commit()
    if user.new:
        set_user_old(user_id)
    return user


def set_user_old(user_id: int) -> User:
    user = get_user_by_id(user_id)
    user.new = False
    session.commit()
    return user