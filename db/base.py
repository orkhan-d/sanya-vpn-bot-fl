from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase
from settings import settings

engine = create_engine(settings.DB_ADDRESS)
session_factory = sessionmaker(bind=engine)
session = scoped_session(session_factory)


class Base(DeclarativeBase):
    pass
