__author__ = 'davidlarrimore'

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from twoweeks import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, convert_unicode=True, pool_recycle=1800)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()

Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()