import xmltodict
from flask import Blueprint, request, Response, abort

from app.utils.product_data_helper import ProductDataOperations
from app.utils.inventory_helper import InventoryOperations
from app.utils.media_content_helper import MediaContentOperations
from app.utils.ppc_helper import PPCOperations

from app.config import settings

from app.blueprints.errors.handlers import CustomXMLError
from app.oauth2 import auth_required

router = Blueprint('api', __name__, url_prefix='/api')

@router.route('/product_data', methods=['POST'])
def products():
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
    # run the particular action 
    if action_type=='GetProductRequest':
        response_xml = ProductDataOperations.getProductRequest(xml_body_content)

    if action_type=='GetProductDateModifiedRequest':
        response_xml = ProductDataOperations.getProductDateModifiedRequest(xml_body_content)

    if action_type=='GetProductCloseOutRequest':
        response_xml = ProductDataOperations.getProductCloseOutRequest(xml_body_content)

    if action_type=='GetProductSellableRequest':
        response_xml = ProductDataOperations.getProductSellableRequest(xml_body_content)

    if (response_xml):
        response = Response(response_xml, content_type='text/xml')
        return response

    # check docs for what to do about total errors 
    raise CustomXMLError(160)



@router.route('/inventory', methods=['POST'])
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
        response = Response(response_xml, content_type='text/xml')
        return response

    raise CustomXMLError(160)
                                                                                                                       


@router.route('/media_content', methods=['POST'])
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
    if action_type=='GetMediaContentRequest':
        response_xml = MediaContentOperations.getMediaContent(xml_body_content)

    if action_type=='GetMediaDateModifiedRequest':
        response_xml = MediaContentOperations.getMediaDateModified(xml_body_content)

    if (response_xml):
        response = Response(response_xml, content_type='text/xml')
        return response

    raise CustomXMLError(160)


@router.route('/ppc', methods=['POST'])
def ppc():
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
    if action_type=='GetAvailableLocationsRequest':
        response_xml = PPCOperations.getAvailableLocations(xml_body_content)

    if action_type=='GetDecorationColorsRequest':
        response_xml = PPCOperations.getDecorationColors(xml_body_content)

    if action_type=='GetFobPointsRequest':
        response_xml = PPCOperations.getFobPoints(xml_body_content)

    if action_type=='GetAvailableChargesRequest':
        response_xml = PPCOperations.getAvailableCharges(xml_body_content)

    if action_type=='GetConfigurationAndPricingRequest':
        response_xml = PPCOperations.getConfigurationAndPricing(xml_body_content)

    if (response_xml):
        response = Response(response_xml, content_type='text/xml')
        return response


    raise CustomXMLError(160)
