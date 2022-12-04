import xmltodict
from flask import Blueprint, request, Response, abort

from app.utils.product_data_helper import ProductDataOperations
from app.utils.inventory_helper import InventoryOperations
from app.utils.media_content_helper import MediaContentOperations
from app.utils.ppc_helper import PPCOperations

from app.config import settings

from app.blueprints.errors.handlers import CustomXMLError

router = Blueprint('api', __name__, url_prefix='/api')


@router.route('/product_data')
def products():

    request_xml =  request.data

    #convert the xml to a python dict
    try:
        xml_dict = xmltodict.parse(request_xml)
    except Exception as e:
        raise CustomXMLError(999)
    # get the action type
    for elem in xml_dict:
        action_type = elem

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



@router.route('/inventory')
def inventory():
    request_xml =  request.data

    try:
        xml_dict = xmltodict.parse(request_xml)
    except Exception as e:
        raise CustomXMLError(999)

    for elem in xml_dict:
        action_type = elem

    if action_type=='GetInventoryLevelsRequest':
        response_xml = InventoryOperations.getInventoryLevels(xml_dict)

    if action_type=='GetFilterValuesRequest':
        response_xml = InventoryOperations.getFilterValues(xml_dict)

    if (response_xml):
        response = Response(response_xml, mimetype='text/xml')
        return response


    raise CustomXMLError(160)
                                                                                                                       


@router.route('/media_content')
def media_content():
    request_xml =  request.data

    try:
        xml_dict = xmltodict.parse(request_xml)
    except Exception as e:
        raise CustomXMLError(999)

    # xml_dict = xmltodict.parse(request_xml)

    for elem in xml_dict:
        action_type = elem

    if action_type=='GetMediaContentRequest':
        response_xml = MediaContentOperations.getMediaContent(xml_dict)
        if response_xml:
            response = Response(response_xml, mimetype='text/xml')
            return response

    if action_type=='GetMediaDateModifiedRequest':
        response_xml = MediaContentOperations.getMediaDateModified(xml_dict)
        if response_xml:
            response = Response(response_xml, mimetype='text/xml')
            return response

    if (response_xml):
        response = Response(response_xml, content_type='text/xml')
        return response

    raise CustomXMLError(160)


@router.route('/ppc')
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
