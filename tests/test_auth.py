import pytest
from app import schemas
from jose import jwt
from app.config import settings

from secrets import token_hex

def test_login_user(client, test_user):
    res = client.post("/auth/login", data={
        "username" : test_user['username'],
        "password" : test_user['password']
    })

    login_res = schemas.Token(**res.json)
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])

    id = payload.get('user_id')

    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

