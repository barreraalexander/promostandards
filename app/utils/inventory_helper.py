import xmltodict
from app.database import get_session
from app import schemas, models

from app.utils.xml_response_templates.Inventory_getInventoryLevelsResponse import xml_response as getInventoryLevels
from app.utils.xml_response_templates.Inventory_getFilterValuesResponse import xml_response as getFilterValues


class InventoryOperations:
    @staticmethod
    def getInventoryLevels(xml_dict):
        request_dict = (xml_dict['GetInventoryLevelsRequest'])
        request_schema = schemas.Inventory_getInventoryLevelsRequest(**{
            'ws_version': request_dict['wsVersion']['#text'],
            'id': request_dict['id']['#text'],
            'password': request_dict['password']['#text'],
            'product_id': request_dict['productId']['#text'],
            # 'filter': request_dict.get('Filter')
            'filter': schemas.Filter(
                part_id_array=request_dict['Filter']['partIdArray']['partId'],
                label_size_array=request_dict['Filter']['LabelSizeArray']['labelSize'],
                part_color_array=request_dict['Filter']['PartColorArray']['partColor']
            )
        })


        db_session = get_session()
        product_data = db_session.query(models.ProductData).filter(models.ProductData.product_id==request_schema.product_id).first()
        if (not product_data):
            return False


        xml = getInventoryLevels(product_data)
        return xml



    @staticmethod
    def getFilterValues(xml_dict):
        request_dict = (xml_dict['GetFilterValuesRequest'])

        request_schema = schemas.Inventory_getFilterValuesRequest(**{
            'ws_version': request_dict['wsVersion']['#text'],
            'id': request_dict['id']['#text'],
            'password': request_dict['password']['#text'],
            'product_id': request_dict['productId']['#text'],
        })


        db_session = get_session()
        product_data = db_session.query(models.ProductData).filter(models.ProductData.product_id==request_schema.product_id).first()
        if (not product_data):
            return False


        xml = getFilterValues(product_data)
        return xml
