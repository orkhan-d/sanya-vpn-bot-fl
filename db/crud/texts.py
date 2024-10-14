from db.models import Text
from db.base import session


def get_text(title: str) -> str:
    text = session.query(Text).filter(Text.title == title).first()
    session.close()
    return text.text
