from app import schemas, models
from app.database import get_session
from app.utils.xml_response_templates.PPC_getAvailableLocationsResponse import xml_response as getAvailableLocationsResponse
from app.utils.xml_response_templates.PPC_getFobPointsResponse import xml_response as getFobPoints
from app.utils.xml_response_templates.PPC_getAvailableCharges import xml_response as getAvailableCharges
from app.utils.xml_response_templates.PPC_getConfigurationAndPricing import xml_response as getConfigurationAndPricing
from app.utils.xml_response_templates.PPC_getDecorationColorResponse import xml_response as getDecorationColor
from app.blueprints.errors.handlers import CustomXMLError
from pydantic import ValidationError


class PPCOperations:
    @staticmethod
    def getAvailableLocations(request_dict):
        try:
            request_schema = schemas.PPC_getAvailableLocationsRequest(**{
                'ws_version': request_dict.get('wsVersion').get('#text'),
                'id': request_dict.get('id').get('#text'),
                'password': request_dict['password']['#text'],
                'product_id': request_dict.get('productId').get('#text'),
                'localization_country': request_dict.get('localizationCountry').get('#text'),
                'localization_language': request_dict.get('localizationLanguage').get('#text')
            })
        except ValidationError as e:
            loc = e.json()
            raise CustomXMLError(120, custom_description=loc)
        except Exception as e:
            raise CustomXMLError(999)
            
        db_session = get_session()
        locations = db_session.query(models.AvailableLocation).all()
        if (not locations):
            raise CustomXMLError(custom_code=160)

        xml = getAvailableLocationsResponse(locations)

        return xml


    @staticmethod
    def getDecorationColors(request_dict):

        # request_dict = (xml_dict['GetDecorationColorsRequest'])
        try:                
            request_schema = schemas.PPC_getDecorationColorsRequest(**{
                'ws_version': request_dict.get('wsVersion').get('#text'),
                'id': request_dict.get('id').get('#text'),
                'password': request_dict.get('password').get('#text'),
                'location_id': request_dict.get('locationId').get('#text'),
                'product_id': request_dict.get('productId').get('#text'),
                'decoration_id': request_dict.get('decorationId').get('#text'),
                'localization_country': request_dict.get('localizationCountry').get('#text'),
                'localization_language': request_dict.get('localizationLanguage').get('#text'),
            })
        except ValidationError as e:
            loc = e.json()
            raise CustomXMLError(120, custom_description=loc)
        except Exception as e:
            raise CustomXMLError(999)

        db_session = get_session()
        if (request_schema.product_id):
            decoration_color = db_session.query(models.DecorationColor).filter(models.DecorationColor.product_id==request_schema.product_id).first()
            if (not decoration_color):
                raise CustomXMLError(custom_code=160)

            xml = getDecorationColor([decoration_color])
        else:
            decoration_colors = db_session.query(models.DecorationColor).all()
            xml = getDecorationColor(decoration_colors)
        if (not xml):
            raise CustomXMLError(custom_code=160)


        return xml

    @staticmethod
    def getFobPoints(request_dict):
        # request_dict = (xml_dict['GetFobPointsRequest'])
        try:
            request_schema = schemas.PPC_getAvailableLocationsRequest(**{
                'ws_version': request_dict.get('wsVersion').get('#text'),
                'id': request_dict.get('id').get('#text'),
                'password': request_dict['password']['#text'],
                'product_id': request_dict.get('productId').get('#text'),
                'localization_country': request_dict.get('localizationCountry').get('#text'),
                'localization_language': request_dict.get('localizationLanguage').get('#text')
            })
        except ValidationError as e:
            loc = e.json()
            raise CustomXMLError(120, custom_description=loc)
        except Exception as e:
            raise CustomXMLError(999)

        db_session = get_session()
        fob_data = db_session.query(models.FobPoint).filter(models.FobPoint.fob_id==request_schema.product_id).first()
        if (not fob_data):
            raise CustomXMLError(custom_code=160)


        xml = getFobPoints([fob_data])

        return xml


    @staticmethod
    def getAvailableCharges(request_dict):
        # request_dict = (xml_dict['GetAvailableChargesRequest'])

        try:
            request_schema = schemas.PPC_getAvailableLocationsRequest(**{
                'ws_version': request_dict.get('wsVersion').get('#text'),
                'id': request_dict.get('id').get('#text'),
                'password': request_dict['password']['#text'],
                'product_id': request_dict.get('productId').get('#text'),
                'localization_country': request_dict.get('localizationCountry').get('#text'),
                'localization_language': request_dict.get('localizationLanguage').get('#text')
            })
        except ValidationError as e:
            loc = e.json()
            raise CustomXMLError(120, custom_description=loc)
        except Exception as e:
            raise CustomXMLError(999)

                
        db_session = get_session()
        available_charge = db_session.query(models.AvailableCharge).all()
        # available_charge = db_session.query(models.AvailableCharge).filter(models.AvailableCharge)first()
        if (not available_charge):
            raise CustomXMLError(custom_code=160)


        xml = getAvailableCharges(available_charge)

        return xml

    @staticmethod
    def getConfigurationAndPricing(request_dict):
        try:                
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
        except ValidationError as e:
            loc = e.json()
            raise CustomXMLError(120, custom_description=loc)
        except Exception as e:
            raise CustomXMLError(999)

        db_session = get_session()
        configuration = db_session.query(models.Configuration).first()
        if (not configuration):
            raise CustomXMLError(custom_code=160)


        xml = getConfigurationAndPricing(configuration)

        return xml