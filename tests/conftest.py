import pytest
from app import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.testing = True
    yield app.test_client()



# @pytest.fixture()
# def client():
#     app = create_app
#     app.testing = True
#     yield app.test_client()

