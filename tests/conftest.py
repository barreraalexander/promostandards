import pytest
from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture
def test_user(client):
    user_data = {
        "username" : f"test@gmail.com",
        "password" : "password123"
    }
    res = client.post("/auth/register", json=user_data)
    
    assert res.status_code == 201

    new_user = res.json
    new_user['password'] = user_data['password']
    return new_user
