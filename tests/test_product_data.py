import xmltodict

def test_getProductRequest_fail(client):
    res = client.get('/api/product_data')

    assert res.status_code == 500

def test_getProductRequest_successful(client):
    request_dict = {'GetProductRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'T1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'T1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'colorName': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'ApparelSizeArray': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'ApparelSize': [{'apparelStyle': 'Unisex', 'labelSize': 'OSFA', 'customSize': 'Token1'}, {'apparelStyle': 'Youth', 'labelSize': '6XS', 'customSize': 'Token2'}]}}}
    xml_body = xmltodict.unparse(request_dict)
    res = client.get('/api/product_data', data=xml_body, content_type='text/xml')

    assert res.status_code == 200


def test_getProductDateModifiedRequest_fail(client):
    res = client.get('/api/product_data')

    assert res.status_code == 500

def test_getProductDateModifiedRequest_successful(client):
    request_dict = {'GetProductDateModifiedRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'changeTimeStamp': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '1900-01-01T01:01:01.0000000+00:00'}}}
    xml_body = xmltodict.unparse(request_dict)
    res = client.get('/api/product_data', data=xml_body, content_type='text/xml')
    
    assert res.status_code == 200


def test_getProductCloseOutRequest_fail(client):
    res = client.get('/api/product_data')

    assert res.status_code == 500

def test_getProductCloseOutRequest_successful(client):
    request_dict = {'GetProductCloseOutRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}}}
    xml_body = xmltodict.unparse(request_dict)
    res = client.get('/api/product_data', data=xml_body, content_type='text/xml')

    assert res.status_code == 200


def test_getProductSellableRequest_fail(client):
    res = client.get('/api/product_data')

    assert res.status_code == 500

def test_getProductSellableRequest_successful(client):
    request_dict = {'GetProductSellableRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'T1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'T1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'lineName': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'isSellable': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}}}
    xml_body = xmltodict.unparse(request_dict)
    res = client.get('/api/product_data', data=xml_body, content_type='text/xml')

    assert res.status_code == 200