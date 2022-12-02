import xmltodict

def test_getInventoryLevels_error(client):
    # request_dict = {'GetFilterValuesRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': '2.0.0'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'id1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'password1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'Token1'}}}
    # xml_body = xmltodict.unparse(request_dict)
    # res = client.get('/api/inventory', data=xml_body, content_type='text/xml')
    res = client.get('/api/inventory')

    assert res.status_code == 500

def test_getInventoryLevels_successful(client):
    request_dict = {'GetInventoryLevelsRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': '2.0.0'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'id1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'password1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'Token1'}, 'Filter': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', 'partIdArray': {'partId': ['partId1', 'partId2']}, 'LabelSizeArray': {'labelSize': ['2XL', '2XS']}, 'PartColorArray': {'partColor': ['partColor1', 'partColor2']}}}}
    xml_body = xmltodict.unparse(request_dict)
    res = client.get('/api/inventory', data=xml_body, content_type='text/xml')
    
    assert res.status_code == 200



def test_getFilterValues_error(client):
    # request_dict = {'GetFilterValuesRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': '2.0.0'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'id1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'password1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'Token1'}}}
    # xml_body = xmltodict.unparse(request_dict)
    # res = client.get('/api/inventory', data=xml_body, content_type='text/xml')
    res = client.get('/api/inventory')

    assert res.status_code == 500

def test_getFilterValues_successful(client):
    request_dict = {'GetInventoryLevelsRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': '2.0.0'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'id1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'password1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'Token1'}, 'Filter': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', 'partIdArray': {'partId': ['partId1', 'partId2']}, 'LabelSizeArray': {'labelSize': ['2XL', '2XS']}, 'PartColorArray': {'partColor': ['partColor1', 'partColor2']}}}}
    xml_body = xmltodict.unparse(request_dict)
    res = client.get('/api/inventory', data=xml_body, content_type='text/xml')
    
    assert res.status_code == 200



# def test_getInventoryLevels_fail_no_body(client):
#     request_dict = {'GetInventoryLevelsRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': '2.0.0'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'id1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'password1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', '#text': 'Token1'}, 'Filter': {'@xmlns': 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/', 'partIdArray': {'partId': ['partId1', 'partId2']}, 'LabelSizeArray': {'labelSize': ['2XL', '2XS']}, 'PartColorArray': {'partColor': ['partColor1', 'partColor2']}}}}
#     # xml_body = xmltodict.unparse(request_dict)
#     # res = client.get('/api/inventory', data=xml_body, content_type='text/xml')
#     res = client.get('/api/inventory')
    
#     assert res.status_code == 500