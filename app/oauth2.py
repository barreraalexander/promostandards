from jose import JWTError, jwt
from datetime import datetime, timedelta
from app import schemas, database, models
from app.config import settings
from sqlalchemy.orm import Session
from functools import wraps
from app.blueprints.errors.handlers import CustomXMLError

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp" : expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception

        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception

    return token_data


def auth_required(router):
    @wraps(router)
    def authorize_cookie(**kwargs):
        print (dir(kwargs['request']))
        auth_token = kwargs['request'].cookies.get('Authorization')

        if (auth_token):
            token_type, jwt_token = auth_token.split(' ')
            verify_access_token(jwt_token, CustomXMLError(110), detail="Invalid Credentials")
            return router(**kwargs)
        raise CustomXMLError(110)
    return authorize_cookie
















# def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
#     credentials_exception = HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Could not validate credentials",
#             headers={"WWW-Authenticate" : "Bearer"}
#         )

#     token = verify_access_token(token, credentials_exception)

#     user = db.query(models.User).filter(models.User.id == token.id).first()
    

#     return user