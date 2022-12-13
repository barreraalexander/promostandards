import xmltodict
import xmltodict
import pytest
from app import schemas
from datetime import datetime


# def test_getAvailableLocationsRequest_error(client):
#     res = client.post('/api/ppc')

#     assert res.status_code == 999

# def test_getAvailableLocationsRequest_successful(client):
#     request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetAvailableLocationsRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}}}}}
    
#     xml_body = xmltodict.unparse(request_dict)
#     res = client.post('/api/ppc', data=xml_body, content_type='text/xml')
    
#     assert res.status_code == 200


# def test_getDecorationColorsRequest_error(client):
#     res = client.post('/api/ppc')

#     assert res.status_code == 999

# def test_getDecorationColorsRequest_successful(client):
#     request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetDecorationColorsRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'locationId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'decorationId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '1'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}}}}}

#     xml_body = xmltodict.unparse(request_dict)
#     res = client.post('/api/ppc', data=xml_body, content_type='text/xml')
    
#     assert res.status_code == 200


# def test_getFobPointsRequest_error(client):
#     res = client.post('/api/ppc')

#     assert res.status_code == 999

# def test_getFobPointsRequest_successful(client):
#     request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetFobPointsRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}}}}}
    
#     xml_body = xmltodict.unparse(request_dict)
#     res = client.post('/api/ppc', data=xml_body, content_type='text/xml')
    
#     assert res.status_code == 200



# def test_getAvailableChargesRequest_error(client):
#     res = client.post('/api/ppc')

#     assert res.status_code == 999

# def test_getAvailableChargesRequest_successful(client):
#     request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetAvailableChargesRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}}}}}

#     xml_body = xmltodict.unparse(request_dict)
#     res = client.post('/api/ppc', data=xml_body, content_type='text/xml')
    
#     assert res.status_code == 200



# def test_getConfigurationAndPricingRequest_error(client):
#     res = client.post('/api/ppc')
#     assert res.status_code == 999

# def test_getConfigurationAndPricingRequest_successful(client):
#     request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetConfigurationAndPricingRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'currency': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'AFA'}, 'fobId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'priceType': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Customer'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}, 'configurationType': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Blank'}}}}}

#     xml_body = xmltodict.unparse(request_dict)
#     res = client.post('/api/ppc', data=xml_body, content_type='text/xml')
    
#     assert res.status_code == 200


# @pytest.mark.parametrize("ws_version, id, password, product_id, localization_country, localization_language, status_code", [
#     (
#         "version1", "user_id", "some_password",
#         "Token1", "some_localization_country",
#         "some_localization_language",

#         200
#     ),
#     (
#         "version2", "user_id2", "some_password2",
#         "Token12", "some_localization_country2",
#         "some_localization_language2",

#         200
#     ),
#     (
#         "version2", "user_id2", "some_password2",
#         000, "some_localization_country2",
#         "some_localization_language2",
#         999
#     ),


# ])
# def test_getAvailableLocationsRequest_validator(client, ws_version, id, password,
#     product_id, localization_country, localization_language, status_code):

#     request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetAvailableLocationsRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': ws_version}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': id}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': password}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': product_id}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': localization_country}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': localization_language}}}}}

#     xml_body = xmltodict.unparse(request_dict)
#     res = client.post('/api/ppc', data=xml_body, content_type='text/xml')

#     assert res.status_code == status_code



# @pytest.mark.parametrize("ws_version, id, password, product_id, localization_country, localization_language, decoration_id, location_id, status_code", [
#     (
#         "version1", "user_id", "some_password",
#         "Token1", "some_localization_country",
#         "some_localization_language", str(1), str(1),
#         200
#     ),
#     (
#         "version2", "user_id2", "some_password2",
#         "Token12", "some_localization_country2",
#         "some_localization_language2", str(12), str(12),
#         200
#     ),
#     (
#         "version2", "user_id2", "some_password2",
#         "badtoken", "some_localization_country2",
#         "some_localization_language2", str(12), str(12),
#         999
#     ),
# ])
# def test_getDecorationColorsRequest_validator(client, ws_version, id, password,
#     product_id, localization_country, localization_language, decoration_id, location_id, status_code):

#     request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetDecorationColorsRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': ws_version}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': id}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': password}, 'locationId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': location_id}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': product_id}, 'decorationId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': decoration_id}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': localization_country}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': localization_language}}}}}


#     xml_body = xmltodict.unparse(request_dict)
#     res = client.post('/api/ppc', data=xml_body, content_type='text/xml')

#     assert res.status_code == status_code





# @pytest.mark.parametrize("ws_version, id, password, product_id, localization_country, localization_language, status_code", [
#     (
#         "version1", "user_id", "some_password",
#         "Token1", "some_localization_country",
#         "some_localization_language",
#         200
#     ),
#     (
#         "version2", "user_id2", "some_password2",
#         "Token12", "some_localization_country2",
#         "some_localization_language2",
#         200
#     ),
#     (
#         "version2", "user_id2", "some_password2",
#         "badtoken", "some_localization_country2",
#         "some_localization_language2",
#         999
#     ),
#     (
#         "bad_request", "bad_request", "bad_request",
#         "bad_request", "bad_request",
#         "bad_request",
#         999
#     ),
    
# ])
# def test_getFobPointsRequest_validator(client, ws_version, id, password,
#     product_id, localization_country, localization_language, status_code):

#     request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetFobPointsRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': ws_version}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': id}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': password}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': product_id}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': localization_country}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': localization_language}}}}}

#     xml_body = xmltodict.unparse(request_dict)
#     res = client.post('/api/ppc', data=xml_body, content_type='text/xml')

#     assert res.status_code == status_code






# @pytest.mark.parametrize("ws_version, id, password, product_id, localization_country, localization_language, status_code", [
#     (
#         "version1", "user_id", "some_password",
#         "Token1", "some_localization_country",
#         "some_localization_language",
#         200
#     ),
#     (
#         "version2", "user_id2", "some_password2",
#         "Token12", "some_localization_country2",
#         "some_localization_language2",
#         200
#     ),
#     (
#         "bad_request", "bad_request", "bad_request",
#         0, "bad_request",
#         "bad_request",
#         999
#     ),
# ])
# def test_getAvailableChargeRequest_validator(client, ws_version, id, password,
#     product_id, localization_country, localization_language, status_code):

#     request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetAvailableChargesRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': ws_version}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': id}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': password}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': product_id}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': localization_country}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': localization_language}}}}}


#     xml_body = xmltodict.unparse(request_dict)
#     res = client.post('/api/ppc', data=xml_body, content_type='text/xml')

#     assert res.status_code == status_code






@pytest.mark.parametrize("ws_version, id, password, product_id, localization_country, localization_language, part_id, currency, fob_id, price_type, configuration_type, status_code", [
    (
        "version1", "user_id", "some_password",
        "Token1", "some_localization_country",
        "some_localization_language", "some_part_id",
        "some_currency", "some_fob_id", "some_price_type",
        "some_configuration_type",
        200
    ),
    (
        "version2", "user_id2", "some_password2",
        "Token12", "some_localization_country2",
        "some_localization_language2", "some_part_id2",
        "some_currency2", "some_fob_id2", "some_price_type2",
        "some_configuration_type2",
        200
    ),
    (
        "bad_request", "bad_request", "bad_request",
        0, "bad_request",
        "bad_request", "bad_request",
        "bad_request", "bad_request", "bad_request",
        "bad_request",
        999
    ),
])
def test_getConfigurationAndPricingRequest_validator(client, ws_version, id, password,
    product_id, localization_country, localization_language, part_id, currency,
    fob_id, price_type, configuration_type, status_code):

    request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetConfigurationAndPricingRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': ws_version}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': id}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': password}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': product_id}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': part_id}, 'currency': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': currency}, 'fobId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': fob_id}, 'priceType': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': price_type}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': localization_country}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': localization_language}, 'configurationType': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': configuration_type}}}}}


    xml_body = xmltodict.unparse(request_dict)
    res = client.post('/api/ppc', data=xml_body, content_type='text/xml')

    assert res.status_code == status_code

