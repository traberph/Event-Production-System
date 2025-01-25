from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
DATABASE_URL = 'sqlite:///./test.db'
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine, autoflush=True, autocommit=False)


def create_tables():
    Base.metadata.create_all(engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
