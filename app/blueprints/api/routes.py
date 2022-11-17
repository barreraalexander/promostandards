from flask import Blueprint, redirect, url_for, request, jsonify
import xmltodict

router = Blueprint('api', __name__, url_prefix='/api')


# inventory
# order status
# ship notices
# media
# product data
# purchase orders
# product configuration
# invoices

@router.route('/')
def root():
    return jsonify({'root' : 'root'})


# request parameters need to be xml
# returns need to be xml

@router.route('/inventory')
def inventory():
    # print (request)
    # print (dir(request))

    # print (request.method)
    request_xml = request.data




    # print (request_xml)
    xml_dict = xmltodict.parse(request_xml)
    print (xml_dict)




    return jsonify({'root' : 'root'})


                                                                                                                                