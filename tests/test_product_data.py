import xmltodict
import pytest
from datetime import datetime

def test_getProductRequest_fail(client):
    res = client.post('/api/product_data')

    assert res.status_code == 999

def test_getProductRequest_successful(authorized_client):
    request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetProductRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'T1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'T1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'colorName': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'ApparelSizeArray': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'ApparelSize': [{'apparelStyle': 'Unisex', 'labelSize': 'OSFA', 'customSize': 'Token1'}, {'apparelStyle': 'Youth', 'labelSize': '6XS', 'customSize': 'Token2'}]}}}}}

    xml_body = xmltodict.unparse(request_dict)
    res = authorized_client.post('/api/product_data', data=xml_body, content_type='text/xml', headers=authorized_client.headers)

    assert res.status_code == 200


def test_getProductDateModifiedRequest_fail(client):
    res = client.post('/api/product_data')

    assert res.status_code == 999

def test_getProductDateModifiedRequest_successful(authorized_client):
    request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetProductDateModifiedRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'changeTimeStamp': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '1900-01-01T01:01:01+00:00'}}}}}

    
    xml_body = xmltodict.unparse(request_dict)
    res = authorized_client.post('/api/product_data', data=xml_body, content_type='text/xml', headers=authorized_client.headers)
    
    assert res.status_code == 200


def test_getProductCloseOutRequest_fail(client):
    res = client.post('/api/product_data')

    assert res.status_code == 999

def test_getProductCloseOutRequest_successful(authorized_client):
    request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetProductCloseOutRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}}}}}

    xml_body = xmltodict.unparse(request_dict)
    res = authorized_client.post('/api/product_data', data=xml_body, content_type='text/xml', headers=authorized_client.headers)

    assert res.status_code == 200


def test_getProductSellableRequest_fail(client):
    res = client.post('/api/product_data')

    assert res.status_code == 999

def test_getProductSellableRequest_successful(authorized_client):
    request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetProductSellableRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'T1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'T1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'lineName': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'isSellable': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}}}}}

    xml_body = xmltodict.unparse(request_dict)
    res = authorized_client.post('/api/product_data', data=xml_body, content_type='text/xml', headers=authorized_client.headers)

    assert res.status_code == 200





@pytest.mark.parametrize("ws_version, id, password, localization_country, localization_language, product_id, part_id, color_name, apparel_size_array, status_code", [
    (
        "version1", "user_id", "some_password",
        "some_localization_country", "some_localization_language","Token1", "some_part_id", "some_color_name", "apparel_size_array",
        200
    ),
    (
        "version2", "user_id2", "some_password2",
        "some_localization_country2", "some_localization_language2","Token12", "some_part_id2", "some_color_name2", "apparel_size_array2",
        200
    ),
    (
        "version2", "user_id2", "some_password2",
        "some_localization_country2", "some_localization_language2","badtoken", "some_part_id2", "some_color_name2", "apparel_size_array2",
        999
    ),
    (
        "bad_request", "bad_request", "bad_request",
        "bad_request", "bad_request","bad_request", "bad_request", "bad_request", "bad_request",
        999
    ),
])
def test_getProductRequest_validator(authorized_client, ws_version, id, password,
    localization_country, localization_language, product_id, part_id,
    color_name, apparel_size_array, status_code):


    request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetProductRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': ws_version}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': id}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': password}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': localization_country}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': localization_language}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': product_id}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': part_id}, 'colorName': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': color_name}, 'ApparelSizeArray': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'ApparelSize': [{'apparelStyle': 'Unisex', 'labelSize': 'OSFA', 'customSize': 'Token1'}, {'apparelStyle': 'Youth', 'labelSize': '6XS', 'customSize': 'Token2'}]}}}}}


    xml_body = xmltodict.unparse(request_dict)
    res = authorized_client.post('/api/product_data', data=xml_body, content_type='text/xml', headers=authorized_client.headers)


    assert res.status_code == status_code




@pytest.mark.parametrize("ws_version, id, password, culture_name, change_time_stamp, status_code", [
    (
        "version1", "user_id", "some_password",
        "some_culture_name", str(datetime.utcnow()),
        200
    ),
    (
        "version2", "user_id2", "some_password2",
        "some_culture_name2", str(datetime.utcnow()),
        200
    ),
    (
        "bad_request", "bad_request", "bad_request",
        "bad_request", "bad_request",
        999
    ),
    (
        "version2", "user_id2", "some_password2",
        "some_culture_name2", "badtoken",
        999
    ),
])
def test_getProductDateModifiedRequest_validator(authorized_client, ws_version, id, password, culture_name, change_time_stamp, status_code):


    request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetProductDateModifiedRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': ws_version}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': id}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': password}, 'changeTimeStamp': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': change_time_stamp}}}}}


    xml_body = xmltodict.unparse(request_dict)
    res = authorized_client.post('/api/product_data', data=xml_body, content_type='text/xml', headers=authorized_client.headers)


    assert res.status_code == status_code



@pytest.mark.parametrize("ws_version, id, password, status_code", [
    (
        "version1", "user_id", "some_password",
        200
    ),
    (
        "version2", "user_id2", "some_password2",
        200
    ),
    (
        "bad_request", "bad_request", 0,
        999
    ),
])
def test_getProductCloseOutRequest_validator(authorized_client, ws_version, id, password, status_code):
    request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetProductCloseOutRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': ws_version}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': id}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': password}}}}}


    xml_body = xmltodict.unparse(request_dict)
    res = authorized_client.post('/api/product_data', data=xml_body, content_type='text/xml', headers=authorized_client.headers)


    assert res.status_code == status_code



@pytest.mark.parametrize("ws_version, id, password, localization_country, localization_language, product_id, part_id, line_name, is_sellable, status_code", [
    (
        "version1", "user_id", "some_password",
        "localization_country", "localization_language",
        "Token1", "part_id", "line_name", str(True),
        200
    ),
    (
        "version2", "user_id2", "some_password2",
        "localization_country2", "localization_language2",
        "Token12", "part_id2", "line_name2", str(False),
        200
    ),
    (
        "version4", "user_id4", "some_password4",
        "localization_country4", "localization_language4",
        "badtoken", "part_id4", "line_name4", "not_bool",
        999
    ),

])
def test_getProductSellableRequest_validator(authorized_client, ws_version, id,
    password, localization_country, localization_language,
    product_id, part_id, line_name, is_sellable, status_code):
    
    request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetProductSellableRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': ws_version}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': id}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': password}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': localization_country}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': localization_language}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': product_id}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': part_id}, 'lineName': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': line_name}, 'isSellable': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': is_sellable}}}}}


    xml_body = xmltodict.unparse(request_dict)
    res = authorized_client.post('/api/product_data', data=xml_body, content_type='text/xml', headers=authorized_client.headers)


    assert res.status_code == status_code




