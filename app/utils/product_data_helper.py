import xmltodict
from app import schemas, models
from app.database import get_session

from app.utils.xml_response_templates.ProductData_getProductResponse import xml_response as getProduct
from app.utils.xml_response_templates.ProductData_getProductCloseOutResponse import xml_response as getProductCloseOut
from app.utils.xml_response_templates.ProductData_getProductSellableResponse import xml_response as getProductSellable
from app.utils.xml_response_templates.ProductData_getProductDateModified import xml_response as getProductDateModified

from app.blueprints.errors.handlers import CustomXMLError
from pydantic import ValidationError

class ProductDataOperations:
    @staticmethod
    def getProductRequest(request_dict):

        request_apparel_size_array = request_dict.get('ApparelSizeArray').get('ApparelSize')
        apparel_size_array = [schemas.ApparelSize(apparel_style=apparel['apparelStyle'], label_size=apparel['labelSize'], custom_size=apparel['customSize']) for apparel in request_apparel_size_array]
        try:
            request_schema = schemas.ProductData_getProductRequest(**{
                'ws_version': request_dict['wsVersion']['#text'],
                'id': request_dict['id']['#text'],
                'password': request_dict['password']['#text'],
                'localization_country': request_dict.get('localizationCountry').get('#text'),
                'localization_language': request_dict.get('localizationLanguage').get('#text'),
                'product_id': request_dict['productId']['#text'],
                'part_id': request_dict.get('partId').get('#text'),
                'color_name': request_dict.get('colorName').get('#text'),
                'apparel_size_array': apparel_size_array
            })
        except ValidationError as e:
            loc = e.json()
            raise CustomXMLError(120, custom_description=loc)
        except Exception as e:
            raise CustomXMLError(999)

        db_session = get_session()
        product_data = db_session.query(models.ProductData).filter(models.ProductData.product_id==request_schema.product_id).first()
        if (not product_data):
            return False
            
        xml = getProduct(product_data)

        return xml

    
    @staticmethod
    def getProductDateModifiedRequest(request_dict):
        try:                
            request_schema = schemas.ProductData_getProductDateModifiedRequest(**{
                'ws_version': request_dict['wsVersion']['#text'],
                'id': request_dict['id']['#text'],
                'password': request_dict['password']['#text'],
                'change_time_stamp': request_dict['changeTimeStamp']['#text'],
            })
        except ValidationError as e:
            loc = e.json()
            raise CustomXMLError(120, custom_description=loc)
        except Exception as e:
            raise CustomXMLError(999)

        db_session = get_session()
        product_datas = db_session.query(models.ProductData).all()
        if (not product_datas):
            raise CustomXMLError(custom_code=160)
            
        xml = getProductDateModified(product_datas)

        return xml

    
    @staticmethod
    def getProductCloseOutRequest(request_dict):
        try:                
            request_schema = schemas.ProductData_getProductCloseOutRequest(**{
                'ws_version': request_dict['wsVersion']['#text'],
                'id': request_dict['id']['#text'],
                'password': request_dict['password']['#text'],
            })
        except ValidationError as e:
            loc = e.json()
            raise CustomXMLError(120, custom_description=loc)
        except Exception as e:
            raise CustomXMLError(999)


        db_session = get_session()
        product_datas = db_session.query(models.ProductData).filter(models.ProductData.is_closeout==True).all()
        if (not product_datas):
            raise CustomXMLError(custom_code=160)
            

        xml = getProductCloseOut(product_datas)

        return xml
    
    @staticmethod
    def getProductSellableRequest(request_dict):

        try:                
            request_schema = schemas.ProductData_getProductSellableRequest(**{
                'ws_version': request_dict['wsVersion']['#text'],
                'id': request_dict['id']['#text'],
                'password': request_dict['password']['#text'],
                'localization_country': request_dict.get('localizationCountry').get('#text'),
                'localization_language': request_dict.get('localizationLanguage').get('#text'),
                'line_name': request_dict.get('lineName').get('#text'),
                'product_id': request_dict['productId']['#text'],
                'part_id': request_dict.get('partId').get('#text'),
                'line_name': request_dict.get('lineName').get('#text'),
                'is_sellable': request_dict.get('isSellable').get('#text'),
            })
        except ValidationError as e:
            loc = e.json()
            raise CustomXMLError(120, custom_description=loc)
        except Exception as e:
            raise CustomXMLError(999)


        db_session = get_session()
        # right now, filter is set to check closeout
        product_datas = db_session.query(models.ProductData).filter(models.ProductData.is_closeout==True).all()
        if (not product_datas):
            raise CustomXMLError(custom_code=160)
        
        xml = getProductSellable(product_datas)

        return xml