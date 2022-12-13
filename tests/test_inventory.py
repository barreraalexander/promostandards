import xmltodict
import pytest
from datetime import datetime

def test_getInventoryLevels_error(client):
    res = client.post('/api/inventory')

    assert res.status_code == 999

def test_getInventoryLevels_successful(client):
    request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetInventoryLevelsRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': '2.0.0'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'id1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'password1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'Token1'}, 'Filter': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', 'partIdArray': {'partId': ['partId1', 'partId2']}, 'LabelSizeArray': {'labelSize': ['2XL', '2XS']}, 'PartColorArray': {'partColor': ['partColor1', 'partColor2']}}}}}}

    xml_body = xmltodict.unparse(request_dict)
    res = client.post('/api/inventory', data=xml_body, content_type='text/xml')

    assert res.status_code == 200



def test_getFilterValues_error(client):
    res = client.post('/api/inventory')    
    assert res.status_code == 999

def test_getFilterValues_successful(client):
    request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetFilterValuesRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': '2.0.0'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'id1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'password1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'Token1'}}}}}

    xml_body = xmltodict.unparse(request_dict)
    res = client.post('/api/inventory', data=xml_body, content_type='text/xml')
    
    assert res.status_code == 200


@pytest.mark.parametrize("ws_version, id, password, product_id, filter, status_code", [
    (
        "version1", "user_id", "some_password",
        "Token1", "filter",
        200
    ),
    (
        "version2", "user_id", "some_password",
        "Token10", "filter",
        200
    ),
    (
        "version1", "user_id", "some_password",
        "badtoken", "filter",
        999
    ),
    (
        "bad_request", "bad_request", "bad_request",
        "bad_request", "bad_request",
        999
    ),
])
def test_getInventoryLevelsRequest_validator(client, ws_version, id, password, product_id, filter, status_code):

    request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetInventoryLevelsRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': ws_version}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': id}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': password}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': product_id}, 'Filter': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', 'partIdArray': {'partId': ['partId1', 'partId2']}, 'LabelSizeArray': {'labelSize': ['2XL', '2XS']}, 'PartColorArray': {'partColor': ['partColor1', 'partColor2']}}}}}}

    xml_body = xmltodict.unparse(request_dict)
    
    res = client.post('/api/inventory', data=xml_body, content_type='text/xml')


    assert res.status_code == status_code



@pytest.mark.parametrize("ws_version, id, password, product_id, status_code", [
    (
        "version1", "user_id", "some_password",
        "Token1",
        200
    ),
    (
        "version2", "user_id", "some_password",
        "Token10",
        200
    ),
    (
        "version1", "user_id", "some_password",
        "badtoken",
        999
    ),
    (
        "bad_request", "bad_request", "bad_request",
        "bad_request",
        999
    ),
])
def test_getFilterValues_validator(client, ws_version, id, password, product_id, status_code):

    request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetFilterValuesRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': ws_version}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': id}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': password}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': product_id}}}}}


    xml_body = xmltodict.unparse(request_dict)
    
    res = client.post('/api/inventory', data=xml_body, content_type='text/xml')


    assert res.status_code == status_code