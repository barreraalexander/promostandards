import xmltodict
from app.database import get_session
from app import schemas, models

from app.utils.xml_response_templates.Inventory_getInventoryLevelsResponse import xml_response as getInventoryLevels


class InventoryOperations:
    @staticmethod
    def getInventoryLevels(xml_dict):
        request_dict = (xml_dict['GetInventoryLevelsRequest'])
        request_schema = schemas.Inventory_getInventoryLevelsRequest(**{
            'ws_version': request_dict['wsVersion']['#text'],
            'id': request_dict['id']['#text'],
            'password': request_dict['password']['#text'],
            'product_id': request_dict['productId']['#text'],
            'filter': request_dict.get('Filter')
        })

        # return 'hi'
        db_session = get_session()
        product_data = db_session.query(models.ProductData).filter(models.ProductData.product_id==request_schema.product_id).first()
        if (not product_data):
            return False


        xml = getInventoryLevels(product_data)
        print (xml)
        return xml



    @staticmethod
    def getFilterValues(xml_dict):

        response_dict = {'GetFilterValuesRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': '2.0.0'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'id1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'password1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'productId1'}}}

        response_xml = xmltodict.unparse(response_dict)

        return response_xml
