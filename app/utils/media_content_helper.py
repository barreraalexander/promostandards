import xmltodict
from app import schemas

class MediaContentOperations:
    @staticmethod
    def getMediaContent(xml_dict):
        request_dict = (xml_dict['GetMediaContentRequest'])


        response_dict = {'MediaContent': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/', 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'url': 'Token1', 'mediaType': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Image'}, 'ClassTypeArray': {'ClassType': [{'classTypeId': '1', 'classTypeName': 'Token1'}, {'classTypeId': '-2147483647', 'classTypeName': 'Token2'}]}, 'fileSize': '1', 'width': '1', 'height': '1', 'dpi': '1', 'color': 'Token1', 'DecorationArray': {'Decoration': [{'decorationId': '1', 'decorationName': 'Token1'}, {'decorationId': '-2147483647', 'decorationName': 'Token2'}]}, 'LocationArray': {'Location': [{'locationId': '1', 'locationName': 'Token1'}, {'locationId': '-2147483647', 'locationName': 'Token2'}]}, 'decorationId': '1', 'description': 'Token1', 'singlePart': 'true', 'changeTimeStamp': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': '1900-01-01T01:01:01.0000000+00:00'}}}
        
        

        response_xml = xmltodict.unparse(response_dict)
        
        # id and password are for user auth

        # 

        print (request_dict['id']['#text'])
        print (request_dict['password']['#text'])
        print (request_dict['cultureName']['#text'])


        
        return response_xml

    @staticmethod
    def getMediaDateModified(xml_dict):
        

        response_dict = {'MediaDateModified': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/', 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}}}



        response_xml = xmltodict.unparse(response_dict)
        return response_xml



