import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import create_app
from app.database import get_session, Base

SQLITE_DATABASE_URL = 'sqlite:///./sql_app_test.db'

engine = create_engine(SQLITE_DATABASE_URL, connect_args={'check_same_thread': False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

