import xmltodict
from app.database import get_session

class InventoryOperations:
    @staticmethod
    def getInventoryLevels(xml_dict):
        db = get_session()
        print (db)
        response_dict = {'GetInventoryLevelsResponse': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/', 'Inventory': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', 'productId': 'productId1', 'PartInventoryArray': {'PartInventory': [{'partId': 'partId1', 'mainPart': 'true', 'partColor': 'partColor1', 'labelSize': '2XL', 'partDescription': 'partDescription1', 'quantityAvailable': {'Quantity': {'uom': 'BX', 'value': '1'}}, 'manufacturedItem': 'true', 'buyToOrder': 'true', 'replenishmentLeadTime': '1', 'attributeSelection': 'attributeSelection1', 'InventoryLocationArray': {'InventoryLocation': [{'inventoryLocationId': 'inventoryLocationId1', 'inventoryLocationName': 'inventoryLocationName1', 'postalCode': 'postalCod1', 'country': 'AF', 'inventoryLocationQuantity': {'Quantity': None}, 'FutureAvailabilityArray': {'FutureAvailability': [{'Quantity': None, 'availableOn': '1900-01-01T01:01:01.0000000+00:00'}, {'Quantity': None, 'availableOn': '0001-01-01T00:00:00.0000000+00:00'}]}}, {'inventoryLocationId': 'inventoryLocationId2', 'inventoryLocationName': 'inventoryLocationName2', 'postalCode': 'postalCod2', 'country': 'AX', 'inventoryLocationQuantity': {'Quantity': None}, 'FutureAvailabilityArray': {'FutureAvailability': [{'Quantity': None, 'availableOn': '9999-12-31T23:59:59.9999999+00:00'}, {'Quantity': None, 'availableOn': '1899-11-30T01:01:01.0000000+00:00'}]}}]}, 'lastModified': '1900-01-01T01:01:01.0000000+00:00'}, {'partId': 'partId2', 'mainPart': 'false', 'partColor': 'partColor2', 'labelSize': '2XS', 'partDescription': 'partDescription2', 'quantityAvailable': {'Quantity': {'uom': 'CA', 'value': '-79228162514264337593543950335'}}, 'manufacturedItem': 'false', 'buyToOrder': 'false', 'replenishmentLeadTime': '-999', 'attributeSelection': 'attributeSelection2', 'InventoryLocationArray': {'InventoryLocation': [{'inventoryLocationId': 'inventoryLocationId3', 'inventoryLocationName': 'inventoryLocationName3', 'postalCode': 'postalCod3', 'country': 'AL', 'inventoryLocationQuantity': {'Quantity': None}, 'FutureAvailabilityArray': {'FutureAvailability': [{'Quantity': None, 'availableOn': '1900-02-02T01:01:01.0000000+00:00'}, {'Quantity': None, 'availableOn': '0001-02-02T00:00:00.0000000+00:00'}]}}, {'inventoryLocationId': 'inventoryLocationId4', 'inventoryLocationName': 'inventoryLocationName4', 'postalCode': 'postalCod4', 'country': 'DZ', 'inventoryLocationQuantity': {'Quantity': None}, 'FutureAvailabilityArray': {'FutureAvailability': [{'Quantity': None, 'availableOn': '9999-11-29T23:59:59.9999999+00:00'}, {'Quantity': None, 'availableOn': '1899-10-29T01:01:01.0000000+00:00'}]}}]}, 'lastModified': '0001-01-01T00:00:00.0000000+00:00'}]}}, 'ServiceMessageArray': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', 'ServiceMessage': [{'code': '1', 'description': 'Token1', 'severity': 'Error'}, {'code': '-2147483647', 'description': 'Token2', 'severity': 'Information'}]}}}

        response_xml = xmltodict.unparse(response_dict)

        return response_xml


    @staticmethod
    def getFilterValues(xml_dict):

        response_dict = {'GetFilterValuesRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': '2.0.0'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'id1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'password1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'productId1'}}}

        response_xml = xmltodict.unparse(response_dict)

        return response_xml
