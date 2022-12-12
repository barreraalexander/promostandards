import xmltodict
from app.database import get_session
from app import schemas, models

from app.utils.xml_response_templates.Inventory_getInventoryLevelsResponse import xml_response as getInventoryLevels
from app.utils.xml_response_templates.Inventory_getFilterValuesResponse import xml_response as getFilterValues
from app.blueprints.errors.handlers import CustomXMLError
from pydantic import ValidationError

class InventoryOperations:
    @staticmethod
    def getInventoryLevels(request_dict):
        try:                
            request_schema = schemas.Inventory_getInventoryLevelsRequest(**{
                'ws_version': request_dict['wsVersion']['#text'],
                'id': request_dict['id']['#text'],
                'password': request_dict['password']['#text'],
                'product_id': request_dict['productId']['#text'],
                'filter': schemas.Filter(
                    part_id_array=request_dict['Filter']['partIdArray']['partId'],
                    label_size_array=request_dict['Filter']['LabelSizeArray']['labelSize'],
                    part_color_array=request_dict['Filter']['PartColorArray']['partColor']
                )
            })
        except ValidationError as e:
            loc = e.json()
            raise CustomXMLError(120, custom_description=loc)
        except Exception as e:
            raise CustomXMLError(999)

        db_session = get_session()
        product_data = db_session.query(models.ProductData).filter(models.ProductData.product_id==request_schema.product_id).first()
        if (not product_data):
            raise CustomXMLError(custom_code=160)


        xml = getInventoryLevels(product_data)
        return xml



    @staticmethod
    def getFilterValues(request_dict):
        try:                
            request_schema = schemas.Inventory_getFilterValuesRequest(**{
                'ws_version': request_dict['wsVersion']['#text'],
                'id': request_dict['id']['#text'],
                'password': request_dict['password']['#text'],
                'product_id': request_dict['productId']['#text'],
            })
        except ValidationError as e:
            loc = e.json()
            raise CustomXMLError(120, custom_description=loc)
        except Exception as e:
            raise CustomXMLError(999)

        db_session = get_session()
        product_data = db_session.query(models.ProductData).filter(models.ProductData.product_id==request_schema.product_id).first()
        if (not product_data):
            raise CustomXMLError(custom_code=160)


        xml = getFilterValues(product_data)
        return xml
