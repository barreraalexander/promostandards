from app import schemas, models
from app.database import get_session

from app.utils.xml_response_templates.PPC_getAvailableLocationsResponse import xml_response as getAvailableLocationsResponse

import xmltodict

class PPCOperations:
    @staticmethod
    def getAvailableLocations(xml_dict):
        request_dict = (xml_dict['GetAvailableLocationsRequest'])

        request_schema = schemas.PPC_getAvailableLocationsRequest(**{
            'ws_version': request_dict['wsVersion']['#text'],
            'id': request_dict['id']['#text'],
            'password': request_dict['password']['#text'],
            'product_id': request_dict['productId']['#text'],
            # 'part_id': request_dict.get('partId').get('#text'),
            'localization_country': request_dict.get('localizationCountry').get('#text'),
            'localization_language': request_dict.get('localizationLanguage').get('#text')
        })

        db_session = get_session()
        media_content = db_session.query(models.MediaContent).filter(models.MediaContent.product_id==request_schema.product_id).first()
        # media_content = db_session.query(models.MediaContent).filter(models.MediaContent.product_id==request_schema.product_id).first()
        if (not media_content):
            return False


        xml = getAvailableLocationsResponse(media_content)

        return xml


    @staticmethod
    def getDecorationColors(xml_dict):

        request_dict = (xml_dict['GetAvailableLocationsRequest'])

        request_schema = schemas.PPC_getDecorationColorRequest(**{
            'ws_version': request_dict['wsVersion']['#text'],
            'id': request_dict['id']['#text'],
            'password': request_dict['password']['#text'],
            'product_id': request_dict['productId']['#text'],
            'localization_country': request_dict.get('localizationCountry').get('#text'),
            'localization_language': request_dict.get('localizationLanguage').get('#text'),
            'decoration_id': request_dict.get('partId').get('#text'),
        })

        db_session = get_session()
        if (request_schema.product_id):
            # pass
            media_content = db_session.query(models.MediaContent).filter(models.MediaContent.product_id==request_schema.product_id).first()
            xml = getAvailableLocationsResponse(media_content)
        else:
            xml = b''
            media_content = db_session.query(models.MediaContent).all()
            for content in media_content:
                xml_part = getAvailableLocationsResponse(media_content)
                xml+= xml_part
            
        if (not media_content):
            return False


        return xml

    @staticmethod
    def getFobPoints(xml_dict):

        response_dict = {'FobPoint': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'fobId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'fobCity': 'fobCity1', 'fobState': 'fobState1', 'fobPostalCode': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'fobPostalCode1'}, 'fobCountry': 'fobCountry1', 'CurrencySupportedArray': {'CurrencySupported': [{'currency': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'AFA'}}, {'currency': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'ALL'}}]}, 'ProductArray': {'Product': [{'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}}, {'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token2'}}]}}}

        response_xml = xmltodict.unparse(response_dict)

        return response_xml


    @staticmethod
    def getAvailableCharges(xml_dict):
        response_dict = {'AvailableCharge': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'chargeId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '1'}, 'chargeName': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'chargeDescription': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'chargeType': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Order'}}}

        response_xml = xmltodict.unparse(response_dict)

        return response_xml


    @staticmethod
    def getConfigurationAndPricing(xml_dict):
        response_dict = {'Part': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'partDescription': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'PartPriceArray': {'PartPrice': [{'minQuantity': '1', 'price': '1', 'discountCode': '1', 'priceUom': 'BX', 'priceEffectiveDate': {'@xsi:nil': 'true'}, 'priceExpiryDate': {'@xsi:nil': 'true'}}, {'minQuantity': '-2147483647', 'price': '-79228162514264337593543950335', 'discountCode': '2', 'priceUom': 'CA', 'priceEffectiveDate': '1900-01-01T01:01:01.0000000+00:00', 'priceExpiryDate': '1900-01-01T01:01:01.0000000+00:00'}]}, 'partGroup': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '1'}, 'nextPartGroup': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '1'}, 'partGroupRequired': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'true'}, 'partGroupDescription': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'ratio': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '1'}, 'defaultPart': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'LocationIdArray': {'LocationId': [{'locationId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '1'}}, {'locationId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '-2147483647'}}]}}}

        response_xml = xmltodict.unparse(response_dict)

        return response_xml