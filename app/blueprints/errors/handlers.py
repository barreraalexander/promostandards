from flask import Blueprint, Response
from lxml import etree
from app import schemas

router = Blueprint('errors', __name__)

from werkzeug.exceptions import HTTPException

descriptions = {
    100: 'ID (customerID) not found',
    104: 'This account is unauthorized to use this service.  Please contact the service provider',
    105: 'Authentication Credentials failed',
    110: 'Authentication Credentials required',
    115: 'wsVersion not found',
    120: 'The following field(s) are required [Comma Delimited field names]',
    125: 'Not Supported: [details]',
    130: 'Product Id not found',
    135: 'Product color not found',
    140: 'Part Id not found',
    145: 'Part color not found',
    150: 'Part size not found',
    155: 'Invalid Date Format',
    160: 'No Results Found',
    999: 'General Error - Contact System Service Provider',
    600: 'Product Id not found',
    610: """ Data violation: {0} (Occurs when a supplier does a pre-check on the data and finds that there is a mismatch of data and/or there are incorrect calculations)'}""",
    620: """ Field is not supported: {0} """,
    630: """ Part Id not found """,
}

inventory_specific_codes = {
    600: 'Product Id not found',
    610: """ Data violation: {0} (Occurs when a supplier does a pre-check on the data and finds that there is a mismatch of data and/or there are incorrect calculations)'}""",
    620: """ Field is not supported: {0} """,
    630: """ Part Id not found """,
}

def get_severity(code: int):
    if (100 < code < 199):
        return 'Information'

    if (200 < code < 299):
        return 'Success'

    if (200 < code < 299):
        return 'Redirect'

    if ( 400 < code < 499):
        return 'Client Error'

    if ( 500 < code < 599):
        return 'Server Error'

    if ( 600 < code < 699):
        return 'Web Service Error'

    return 'Not Specified'

def create_error_response(service_message: schemas.ServiceMessage):
    root = etree.Element('ServiceMessage')

    code = etree.Element('code')
    code.text = str(service_message.code)
    root.append(code)

    description = etree.Element('description')
    description.text = service_message.description
    root.append(description)

    severity = etree.Element('severity')
    severity.text = service_message.severity
    root.append(severity)

    xml = etree.tostring(root, pretty_print=True)
    if service_message.code < 200:
        pass

    response = Response(xml, 999, content_type='text/xml')
    return response


# custom errors
class CustomXMLError(HTTPException):
    code = 999

    def __init__(self, custom_code, custom_description=None):

        self.custom_code = custom_code 
        self.custom_description = custom_description 
        self.set_response()

    def set_response(self):
        if (self.custom_description):
            service_message = schemas.ServiceMessage(code=self.custom_code, description=self.custom_description, severity=get_severity(self.custom_code))
        else:
            service_message = schemas.ServiceMessage(code=self.custom_code, description=descriptions.get(self.custom_code), severity=get_severity(self.custom_code))
        
        self.response = create_error_response(service_message=service_message)




# def error_response(e):
#     root = etree.Element('ServiceMessage')

#     code = etree.Element('code')
#     code.text = str(e.code)
#     root.append(code)

#     description = etree.Element('description')
#     description.text = descriptions.get(e.code)
#     root.append(description)

#     severity = etree.Element('severity')
#     severity.text = get_severity(e.code)
#     root.append(severity)

#     xml = etree.tostring(root, pretty_print=True)
#     return xml, e.code

