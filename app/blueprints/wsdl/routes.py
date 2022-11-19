import xmltodict
from flask import Blueprint, request

router = Blueprint('wsdl', __name__, url_prefix='/wsdl')
