from db.models import Tariff
from db.base import session


def get_all_tariffs(with_free: bool = True) -> list[Tariff]:
    if with_free:
        return session.query(Tariff).all()
    else:
        return session.query(Tariff).filter(Tariff.price > 0).all()


def get_tariff_by_id(tariff_id: int) -> Tariff:
    tariff = session.query(Tariff).filter(Tariff.id == tariff_id).first()
    session.expunge(tariff)
    return tariff
