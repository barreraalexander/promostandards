from app import schemas, models
from app.database import get_session

from app.utils.xml_response_templates.PPC_getAvailableLocationsResponse import xml_response as getAvailableLocationsResponse
from app.utils.xml_response_templates.PPC_getFobPointsResponse import xml_response as getFobPoints
from app.utils.xml_response_templates.PPC_getAvailableCharges import xml_response as getAvailableCharges
from app.utils.xml_response_templates.PPC_getConfigurationAndPricing import xml_response as getConfigurationAndPricing
from app.utils.xml_response_templates.PPC_getDecorationColorResponse import xml_response as getDecorationColor

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
            'localization_country': request_dict.get('localizationCountry').get('#text'),
            'localization_language': request_dict.get('localizationLanguage').get('#text')
        })

        db_session = get_session()
        media_content = db_session.query(models.MediaContent).filter(models.MediaContent.product_id==request_schema.product_id).first()
        if (not media_content):
            return False


        xml = getAvailableLocationsResponse(media_content)

        return xml


    @staticmethod
    def getDecorationColors(xml_dict):

        request_dict = (xml_dict['GetDecorationColorsRequest'])
        request_schema = schemas.PPC_getDecorationColorsRequest(**{
            'ws_version': request_dict['wsVersion']['#text'],
            'id': request_dict['id']['#text'],
            'password': request_dict['password']['#text'],
            'location_id': request_dict['locationId']['#text'],
            'product_id': request_dict['productId']['#text'],
            'decoration_id': request_dict.get('decorationId').get('#text'),
            'localization_country': request_dict.get('localizationCountry').get('#text'),
            'localization_language': request_dict.get('localizationLanguage').get('#text'),
        })

        db_session = get_session()
        if (request_schema.product_id):
            media_content = db_session.query(models.MediaContent).filter(models.MediaContent.product_id==request_schema.product_id).first()
            xml = getDecorationColor(media_content)
        else:
            xml = b''
            media_content = db_session.query(models.MediaContent).all()
            for content in media_content:
                # xml_part = getAvailableLocationsResponse(media_content)
                xml_part = getDecorationColor(media_content)
                xml+= xml_part
            
        if (not media_content):
            return False


        return xml

    @staticmethod
    def getFobPoints(xml_dict):
        request_dict = (xml_dict['GetFobPointsRequest'])

        request_schema = schemas.PPC_getFobPointsRequest(**{
            'ws_version': request_dict['wsVersion']['#text'],
            'id': request_dict['id']['#text'],
            'password': request_dict['password']['#text'],
            'product_id': request_dict['productId']['#text'],
            'localization_country': request_dict.get('localizationCountry').get('#text'),
            'localization_language': request_dict.get('localizationLanguage').get('#text')
        })

        db_session = get_session()
        product_data = db_session.query(models.ProductData).filter(models.ProductData.product_id==request_schema.product_id).first()
        if (not product_data):
            return False

        xml = getFobPoints(product_data)



        return xml


    @staticmethod
    def getAvailableCharges(xml_dict):
        request_dict = (xml_dict['GetAvailableChargesRequest'])

        request_schema = schemas.PPC_getAvailableChargesRequest(**{
            'ws_version': request_dict['wsVersion']['#text'],
            'id': request_dict['id']['#text'],
            'password': request_dict['password']['#text'],
            'product_id': request_dict['productId']['#text'],
            'localization_country': request_dict.get('localizationCountry').get('#text'),
            'localization_language': request_dict.get('localizationLanguage').get('#text')
        })

        db_session = get_session()
        product_data = db_session.query(models.ProductData).filter(models.ProductData.product_id==request_schema.product_id).first()
        if (not product_data):
            return False

        xml = getAvailableCharges(product_data)

        return xml

    @staticmethod
    def getConfigurationAndPricing(xml_dict):
        request_dict = (xml_dict['GetConfigurationAndPricingRequest'])

        request_schema = schemas.PPC_getConfigurationAndPricingRequest(**{
            'ws_version': request_dict['wsVersion']['#text'],
            'id': request_dict['id']['#text'],
            'password': request_dict['password']['#text'],
            'product_id': request_dict['productId']['#text'],
            'localization_country': request_dict.get('localizationCountry').get('#text'),
            'localization_language': request_dict.get('localizationLanguage').get('#text'),
            'part_id': request_dict['partId']['#text'],
            'currency': request_dict['currency']['#text'],
            'fob_id': request_dict['fobId']['#text'],
            'price_type': request_dict['priceType']['#text'],
            'configuration_type': request_dict['configurationType']['#text'],
        })

        db_session = get_session()
        product_data = db_session.query(models.ProductData).filter(models.ProductData.product_id==request_schema.product_id).first()
        if (not product_data):
            return False

        xml = getConfigurationAndPricing(product_data)

        return xml