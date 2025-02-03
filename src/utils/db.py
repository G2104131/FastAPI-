from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#delcareing a path
SQLALCHEMY_DATABASE_URL='sqlite:///./blog.db'

#creating a engine
engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False })

#mapping
Base = declarative_base()

#creating a session
sessionlocal = sessionmaker (bind = engine, autoflush = False , autocommit = False)


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()