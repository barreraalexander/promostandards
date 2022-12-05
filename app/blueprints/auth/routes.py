import xmltodict
from flask import Blueprint, request, jsonify
from app import oauth2, models, schemas
from app.database import get_session
from secrets import token_hex
from app.utils.helpers import verify, hash

from app.blueprints.errors.handlers import CustomXMLError

router = Blueprint('auth', __name__, url_prefix='/auth')

@router.route('/login', methods=['POST'])
def login():
    db_session = get_session()

    login_user = schemas.UserLogin(
        username=request.form.get('username'),
        password=request.form.get('password')
    )

    user = db_session.query(models.User).filter(models.User.username == login_user.username).first()

    if not user:
        raise CustomXMLError(100)

    if not verify(login_user.password, user.password):
        raise CustomXMLError(105)

    # create a token
    access_token = oauth2.create_access_token(data = {"user_id" : user.id})

    return {
            "access_token" : access_token,
            "token_type" : "bearer"
        }, 200

    # access_token = oauth2.create_access_token(data = {"user_id" : user.id})


@router.route('/register', methods=['POST'])
def register():

    # request
    user_data =  request.get_json()



    new_user = schemas.UserCreate(
        username=user_data.get('username'),
        password=user_data.get('password')
    )


    hashed_passord = hash(new_user.password)
    new_user.password  = hashed_passord

    new_model = models.User(**new_user.dict())

    db_session = get_session()
    db_session.add(new_model)

    db_session.commit()
    db_session.refresh(new_model)

    user_out = schemas.UserOut(**new_model.__dict__)

    return jsonify(user_out.dict()), 201



