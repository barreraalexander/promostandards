import xmltodict
from app import schemas, models
from app.database import get_session
from difflib import SequenceMatcher
from app.utils.helpers import unpack_elems
# from app.utils.xml_response_maker import MediaContentResponse_Maker

from lxml import etree
from typing import List


class MediaContentOperations:
    @staticmethod
    def getMediaContent(xml_dict):
        request_dict = (xml_dict['GetMediaContentRequest'])
        # response_dict = {'MediaContent': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/', 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'url': 'Token1', 'mediaType': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Image'}, 'ClassTypeArray': {'ClassType': [{'classTypeId': '1', 'classTypeName': 'Token1'}, {'classTypeId': '-2147483647', 'classTypeName': 'Token2'}]}, 'fileSize': '1', 'width': '1', 'height': '1', 'dpi': '1', 'color': 'Token1', 'DecorationArray': {'Decoration': [{'decorationId': '1', 'decorationName': 'Token1'}, {'decorationId': '-2147483647', 'decorationName': 'Token2'}]}, 'LocationArray': {'Location': [{'locationId': '1', 'locationName': 'Token1'}, {'locationId': '-2147483647', 'locationName': 'Token2'}]}, 'decorationId': '1', 'description': 'Token1', 'singlePart': 'true', 'changeTimeStamp': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': '1900-01-01T01:01:01.0000000+00:00'}}}

        request_schema = schemas.MediaContent_getMediaContentRequest(**{
            'ws_version': request_dict['wsVersion']['#text'],
            'id': request_dict['id']['#text'],
            'password': request_dict['password']['#text'],
            'culture_name': request_dict['cultureName']['#text'],
            'media_type': request_dict['mediaType']['#text'],
            'class_type': request_dict['classType'],
            'product_id': request_dict['productId']['#text'],
            'part_id': request_dict.get('partId').get('#text'),
        })

        db_session = get_session()
        media_content = db_session.query(models.MediaContent).filter(models.MediaContent.product_id==request_schema.product_id).first()
        # media_content = db_session.query(models.MediaContent).all()
        if (not media_content):
            return False
            
        print (media_content.product_id)
        # matched_list = [
        #     elem for elem in media_content
        #     if elem.product_id == request_schema['product_id']
        # ]

        

        # response
        # for match in matched_list:
        #     print (match.product_id)
        


        root = etree.Element('MediaContent', xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/")
        root.append(etree.Element('productId', xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/"))
        root.append(etree.Element('partID', xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/"))
        root.append(etree.Element('partID', xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/"))
        

        xml = etree.tostring(root, pretty_print=True)



        return xml

    @staticmethod
    def getMediaDateModified(xml_dict):
        

        response_dict = {'MediaDateModified': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/', 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}}}



        response_xml = xmltodict.unparse(response_dict)
        return response_xml



