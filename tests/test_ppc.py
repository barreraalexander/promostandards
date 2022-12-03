import xmltodict

# request_dict = {'GetAvailableChargesRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}}}
# request_dict = {'GetConfigurationAndPricingRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'currency': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'AFA'}, 'fobId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'priceType': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Customer'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}, 'configurationType': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Blank'}}}

def test_getAvailableLocationsRequest_error(client):
    res = client.get('/api/ppc')

    assert res.status_code == 500

def test_getAvailableLocationsRequest_successful(client):
    request_dict = {'GetAvailableLocationsRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}}}
    xml_body = xmltodict.unparse(request_dict)
    res = client.get('/api/ppc', data=xml_body, content_type='text/xml')
    
    assert res.status_code == 200


def test_getDecorationColorsRequest_error(client):
    res = client.get('/api/ppc')

    assert res.status_code == 500

def test_getDecorationColorsRequest_successful(client):
    request_dict = {'GetDecorationColorsRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'locationId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'decorationId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '1'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}}}
    xml_body = xmltodict.unparse(request_dict)
    res = client.get('/api/ppc', data=xml_body, content_type='text/xml')
    
    assert res.status_code == 200


def test_getFobPointsRequest_error(client):
    res = client.get('/api/ppc')

    assert res.status_code == 500

def test_getFobPointsRequest_successful(client):
    request_dict = {'GetFobPointsRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}}}
    xml_body = xmltodict.unparse(request_dict)
    res = client.get('/api/ppc', data=xml_body, content_type='text/xml')
    
    assert res.status_code == 200



def test_getAvailableChargesRequest_error(client):
    res = client.get('/api/ppc')

    assert res.status_code == 500

def test_getAvailableChargesRequest_successful(client):
    request_dict = {'GetAvailableChargesRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}}}
    xml_body = xmltodict.unparse(request_dict)
    res = client.get('/api/ppc', data=xml_body, content_type='text/xml')
    
    assert res.status_code == 200



def test_getConfigurationAndPricingRequest_error(client):
    res = client.get('/api/ppc')
    assert res.status_code == 500

def test_getConfigurationAndPricingRequest_successful(client):
    request_dict = {'GetConfigurationAndPricingRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'currency': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'AFA'}, 'fobId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'priceType': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Customer'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}, 'configurationType': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Blank'}}}
    xml_body = xmltodict.unparse(request_dict)
    res = client.get('/api/ppc', data=xml_body, content_type='text/xml')
    
    assert res.status_code == 200
