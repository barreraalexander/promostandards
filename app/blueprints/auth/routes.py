import xmltodict
from flask import Blueprint, request

router = Blueprint('auth', __name__, url_prefix='/auth')

@router.route('/login')
def login():
    pass


@router.route('/register')
def register():
    pass


