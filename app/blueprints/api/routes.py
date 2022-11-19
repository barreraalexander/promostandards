import xmltodict
from flask import Blueprint, request

from app.utils.product_data_helper import ProductDataOperations
from app.utils.inventory_helper import InventoryOperations
from app.utils.media_content_helper import MediaContentOperations
from app.utils.ppc_helper import PPCOperations

router = Blueprint('api', __name__, url_prefix='/api')

# request parameters need to be xml
# returns need to be xml


@router.route('/product_data')
def products():
    # get the xml from the request
    request_xml =  request.data

    #convert the xml to a python dict
    xml_dict = xmltodict.parse(request_xml)

    # get the action type
    for elem in xml_dict:
        action_type = elem

    # run the particular action 
    if action_type=='GetProductRequest':
        response_xml = ProductDataOperations.getProductRequest(xml_dict)
        return response_xml    

    if action_type=='GetProductDateModifiedRequest':
        response_xml = ProductDataOperations.getProductDateModifiedRequest(xml_dict)
        return response_xml    

    if action_type=='GetProductCloseOutRequest':
        response_xml = ProductDataOperations.getProductCloseOutRequest(xml_dict)
        return response_xml

    if action_type=='GetProductSellableRequest':
        response_xml = ProductDataOperations.getProductSellableRequest(xml_dict)
        return response_xml

    # check docs for what to do about total errors 
    return 'error'



@router.route('/inventory')
def inventory():
    # get the xml from the request
    request_xml =  request.data

    #convert the xml to a python dict
    xml_dict = xmltodict.parse(request_xml)

    # get the action type
    for elem in xml_dict:
        action_type = elem


    return 'error'                                                                                                                                


@router.route('/media_content')
def media_content():
    # get the xml from the request
    request_xml =  request.data

    #convert the xml to a python dict
    xml_dict = xmltodict.parse(request_xml)

    # get the action type
    for elem in xml_dict:
        action_type = elem

    return 'error'                                                                                                                                



# product pricing and config
@router.route('/ppc')
def ppc():
    # get the xml from the request
    request_xml =  request.data

    #convert the xml to a python dict
    xml_dict = xmltodict.parse(request_xml)

    # get the action type
    for elem in xml_dict:
        action_type = elem
    return 'error'