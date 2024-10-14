import wtforms.fields

from db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BIGINT, ForeignKey
from datetime import datetime as dt


class Server(Base):
    __tablename__ = 'servers'

    id: Mapped[int] = mapped_column(type_=BIGINT, primary_key=True)
    title: Mapped[str] = mapped_column()

    address: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()

    users: Mapped[int] = mapped_column(default=0)

    def __str__(self):
        return self.title


class Tariff(Base):
    __tablename__ = 'tariffs'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    duration: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column()

    def __str__(self):
        return f'{self.title}' + (f' | ({self.price} руб.)' if self.price > 0 else '')


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(type_=BIGINT, primary_key=True)

    name: Mapped[str] = mapped_column()
    username: Mapped[str | None] = mapped_column()
    balance: Mapped[int] = mapped_column(default=0)

    new: Mapped[bool] = mapped_column(default=True)

    subscription_due: Mapped[dt | None] = mapped_column()
    subscription_link: Mapped[str | None] = mapped_column()

    tariff_id: Mapped[int | None] = mapped_column(ForeignKey('tariffs.id'))
    tariff: Mapped[Tariff | None] = relationship(lazy='subquery')

    server_id: Mapped[int | None] = mapped_column(ForeignKey('servers.id'))
    server: Mapped[Server | None] = relationship(lazy='subquery')

    invited_by: Mapped[int | None] = mapped_column(ForeignKey('users.id'))
    friends: Mapped[int] = mapped_column(default=0)
    bonuses: Mapped[int] = mapped_column(default=0)

    def has_active_subscription(self):
        return self.subscription_due and self.subscription_due.date() >= dt.now().date()


class Payment(Base):
    __tablename__ = 'payments'

    id: Mapped[int] = mapped_column(type_=BIGINT, primary_key=True)
    payment_id: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    amount: Mapped[int] = mapped_column()
    paid: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[dt] = mapped_column(default=dt.now)


class Text(Base):
    __tablename__ = 'texts'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    text: Mapped[str] = mapped_column()


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    tariff_id: Mapped[int] = mapped_column(ForeignKey('tariffs.id'))
    tariff: Mapped[Tariff | None] = relationship(lazy='subquery')
    done: Mapped[bool] = mapped_column(default=False)
    canceled: Mapped[bool] = mapped_column(default=False)

    created_at: Mapped[dt] = mapped_column(default=dt.now)


models = [Server, User, Payment, Text, Tariff, Order]

modelviews = [
    {
        'model': Server,
        'column_list': Server.__table__.columns,
        'icon': 'fa-solid fa-server',
        'name': 'Сервер',
        'name_plural': 'Сервера'
    },
    {
        'model': User,
        'column_list': User.__table__.columns,
        'icon': 'fa-solid fa-user',
        'name': 'Пользователь',
        'name_plural': 'Пользователи'
    },
    {
        'model': Payment,
        'column_list': Payment.__table__.columns,
        'icon': 'fa-solid fa-cart-shopping',
        'name': 'Платеж',
        'name_plural': 'Платежи'
    },
    {
        'model': Text,
        'column_list': Text.__table__.columns,
        'icon': 'fa-solid fa-t',
        'name': 'Текст',
        'name_plural': 'Тексты',
        'form_overrides': {
            'text': wtforms.fields.TextAreaField
        },
        'column_formatters':
            {
                Text.text: lambda m, a: (m.text if len(m.text) < 100
                                         else f'{m.text[:100]}...')
            }
    },
    {
        'model': Tariff,
        'column_list': Tariff.__table__.columns,
        'icon': 'fa-solid fa-tag',
        'name': 'Тариф',
        'name_plural': 'Тарифы'
    },
    {
        'model': Order,
        'column_list': Order.__table__.columns,
        'icon': 'fa-solid fa-cart-shopping',
        'name': 'Заказ',
        'name_plural': 'Заказы'
    }
]
