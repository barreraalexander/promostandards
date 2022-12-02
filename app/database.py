from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

SQLITE_DATABASE_URL = "sqlite:///./app/sql_app.db"


if (settings.debug):
    print ('Made MYSQL Database')
    engine = create_engine(SQLITE_DATABASE_URL, connect_args={'check_same_thread': False})
else:
    # switch to mysql database for production
    print ('Made SQLITE Database')
    MYSQL_DATABASE_URL = f"mysql://{settings.database_username}:{settings.database_password}@{settings.database_port}/{settings.database_name}"
    engine = create_engine(MYSQL_DATABASE_URL, connect_args={'check_same_thread': False})


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_session():
    db = SessionLocal()
    return db