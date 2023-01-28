from flask import Blueprint, Response


router = Blueprint('wsdl', __name__, url_prefix='/wsdl')

@router.route('/')
def wsdl():
    response_xml = "hi"
    response = Response(response_xml, content_type='text/xml')
    return response