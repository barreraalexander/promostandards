# import pytest
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from app import create_app
# from app.database import get_session, Base

# SQLITE_DATABASE_URL = 'sqlite:///./sql_app_test.db'

# engine = create_engine(SQLITE_DATABASE_URL, connect_args={'check_same_thread': False})

# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# @pytest.fixture()
# def session():
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)
#     db = TestingSessionLocal()
#     return db
#     # try:
#     #     yield db
#     # finally:
#     #     db.close()


# @pytest.fixture()
# def client():
#     app = create_app()
#     app.testing = True
#     yield app.test_client()


