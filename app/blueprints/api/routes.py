import xmltodict
from flask import Blueprint, request, Response, abort

from app.utils.product_data_helper import ProductDataOperations
from app.utils.inventory_helper import InventoryOperations
from app.utils.media_content_helper import MediaContentOperations
from app.utils.ppc_helper import PPCOperations

from app.config import settings

from app.blueprints.errors.handlers import CustomXMLError

router = Blueprint('api', __name__, url_prefix='/api')


@router.route('/test_soap_request', methods=['POST', 'GET', 'PUT'])
def test_soap_request():
    request_xml =  request.data



    print('\n\n')
    print ('REQUEST XML')
    print (request_xml)
    print('\n\n')

    try:
        xml_dict = xmltodict.parse(request_xml)
    except Exception as e:
        print (e)
        raise CustomXMLError(999)

    return request_xml

@router.route('/test_soap_response', methods=['POST', 'GET', 'PUT'])
def test_soap_response():
    # response_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetMediaContentRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'cultureName': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'cultureName1'}, 'mediaType': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Image'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'classType': '1'}}}}
    # response_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetMediaContentRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'cultureName': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'cultureName1'}, 'mediaType': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Image'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'classType': '1'}}}}
    # response_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetMediaDateModifiedRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'cultureName': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'cultureName1'}, 'changeTimeStamp': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': '1900-01-01T01:01:01+00:00'}}}}}
    response_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetInventoryLevelsRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': '2.0.0'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'id1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'password1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'productId1'}, 'Filter': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', 'partIdArray': {'partId': ['partId1', 'partId2']}, 'LabelSizeArray': {'labelSize': ['2XL', '2XS']}, 'PartColorArray': {'partColor': ['partColor1', 'partColor2']}}}}}}

    
    request_xml = xmltodict.unparse(response_dict)


    response = Response(request_xml, content_type='text/xml', status=200)

    return response

@router.route('/product_data', methods=['POST', 'GET', 'PUT'])
def products():

    request_xml =  request.data

    #convert the xml to a python dict
    try:
        xml_dict = xmltodict.parse(request_xml)
    except Exception as e:
        raise CustomXMLError(999)
    # get the action type
    # for elem in xml_dict:
    #     action_type = elem

    print ('\n\n')
    print (xml_dict)
    print ('\n\n')

    action_type = ''
    response_xml = False
    # run the particular action 
    if action_type=='GetProductRequest':
        response_xml = ProductDataOperations.getProductRequest(xml_dict)

    if action_type=='GetProductDateModifiedRequest':
        response_xml = ProductDataOperations.getProductDateModifiedRequest(xml_dict)

    if action_type=='GetProductCloseOutRequest':
        response_xml = ProductDataOperations.getProductCloseOutRequest(xml_dict)

    if action_type=='GetProductSellableRequest':
        response_xml = ProductDataOperations.getProductSellableRequest(xml_dict)

    if (response_xml):
        response = Response(response_xml, content_type='text/xml')
        return response

    # check docs for what to do about total errors 
    raise CustomXMLError(160)



@router.route('/inventory', methods=['POST', 'GET', 'PUT'])
def inventory():
    request_xml =  request.data

    action_type = ''
    try:
        xml_dict = xmltodict.parse(request_xml)
        xml_body = xml_dict.get('s:Envelope').get('s:Body')
        for key in xml_body:
            if key[0] != '@':
                action_type = key
        xml_body_content = xml_body[action_type]
    except Exception as e:
        raise CustomXMLError(999)

    response_xml = False
    if action_type=='GetInventoryLevelsRequest':
        response_xml = InventoryOperations.getInventoryLevels(xml_body_content)

    if action_type=='GetFilterValuesRequest':
        response_xml = InventoryOperations.getFilterValues(xml_body_content)

    if (response_xml):
        response = Response(response_xml, mimetype='text/xml')
        return response


    raise CustomXMLError(160)
                                                                                                                       


@router.route('/media_content', methods=['POST', 'GET', 'PUT'])
def media_content():
    request_xml =  request.data

    action_type = ''
    try:
        xml_dict = xmltodict.parse(request_xml)
        xml_body = xml_dict.get('s:Envelope').get('s:Body')
        for key in xml_body:
            if key[0] != '@':
                action_type = key
        xml_body_content = xml_body[action_type]
    except Exception as e:
        raise CustomXMLError(999)

    response_xml = False
    print (action_type)
    if action_type=='GetMediaContentRequest':
        # response_xml = MediaContentOperations.getMediaContent(xml_dict)
        response_xml = MediaContentOperations.getMediaContent(xml_body_content)

    if action_type=='GetMediaDateModifiedRequest':
        response_xml = MediaContentOperations.getMediaDateModified(xml_body_content)

    if (response_xml):
        response = Response(response_xml, content_type='text/xml')
        return response

    raise CustomXMLError(160)


@router.route('/ppc', methods=['POST', 'GET', 'PUT'])
def ppc():
    request_xml =  request.data

    try:
        xml_dict = xmltodict.parse(request_xml)
    except Exception as e:
        raise CustomXMLError(999)

    for elem in xml_dict:
        action_type = elem

    response_xml = False
    if action_type=='GetAvailableLocationsRequest':
        response_xml = PPCOperations.getAvailableLocations(xml_dict)

    if action_type=='GetDecorationColorsRequest':
        response_xml = PPCOperations.getDecorationColors(xml_dict)

    if action_type=='GetFobPointsRequest':
        response_xml = PPCOperations.getFobPoints(xml_dict)

    if action_type=='GetAvailableChargesRequest':
        response_xml = PPCOperations.getAvailableCharges(xml_dict)

    if action_type=='GetConfigurationAndPricingRequest':
        response_xml = PPCOperations.getConfigurationAndPricing(xml_dict)

    if (response_xml):
        response = Response(response_xml, content_type='text/xml')
        return response

    # abort(404, description='yiks')
    # raise CustomXMLError(999)
    raise CustomXMLError(160)
