from db.models import Server
from db.base import session


def get_server_by_id(server_id: int):
    payment = session.query(Server).filter(Server.id == server_id).first()
    session.add(payment)
    session.commit()
    return payment


def get_server_with_min_users():
    server = session.query(Server).order_by(Server.users).first()
    session.add(server)
    session.commit()
    return server
