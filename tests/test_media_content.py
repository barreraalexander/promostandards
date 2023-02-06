import xmltodict
import pytest
from app import schemas
from datetime import datetime

def test_getMediaContentRequest_error(client):
    res = client.post('/api/media_content')
    assert res.status_code == 999

def test_getMediaContentRequest_successful(authorized_client):    
    request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetMediaContentRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'cultureName': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'cultureName1'}, 'mediaType': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Image'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'classType': '1'}}}}
    
    xml_body = xmltodict.unparse(request_dict)
    res = authorized_client.post('/api/media_content', data=xml_body, content_type='text/xml', headers=authorized_client.headers)
    
    assert res.status_code == 200


def test_getMediaDateModifiedRequest_error(client):
    res = client.post('/api/media_content')

    assert res.status_code == 999

def test_getMediaDateModifiedRequest_successful(authorized_client):    
    request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetMediaDateModifiedRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'cultureName': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'cultureName1'}, 'changeTimeStamp': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': '1900-01-01T01:01:01+00:00'}}}}}

    xml_body = xmltodict.unparse(request_dict)
    res = authorized_client.post('/api/media_content', data=xml_body, content_type='text/xml', headers=authorized_client.headers)
    
    assert res.status_code == 200


@pytest.mark.parametrize("ws_version, id, password, culture_name, media_type, product_id, part_id, class_type, status_code", [
    (
        "version1", "user_id", "some_password",
        "some_culture", "some_media_type",
        "Token1", "some_part_id2", 1,
        200
    ),
    (
        "version2", "user_id2", "some_password2",
        "some_culture2", "some_media_type2",
        "Token12", "some_part_id2", 2,
        200
    ),
    (
        "version2", "user_id2", "some_password2",
        "some_culture2", "some_media_type2",
        "badtoken", "some_part_id2", 2,
        999
    ),
    (
        "bad_request", "bad_request", "bad_request",
        "bad_request", "bad_request",
        "Token120000", "bad_request", "bad_request",
        999
    ),
])
def test_getMediaContentRequest_validator(authorized_client, ws_version, id, password,
    culture_name, media_type, product_id, part_id, class_type, status_code):


    request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetMediaContentRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': ws_version}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': id}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': password}, 'cultureName': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': culture_name}, 'mediaType': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': media_type}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': product_id}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': part_id}, 'classType': class_type}}}}

    xml_body = xmltodict.unparse(request_dict)
    res = authorized_client.post('/api/media_content', data=xml_body, content_type='text/xml', headers=authorized_client.headers)

    response_xml = res.get_data() 
    response_dict = xmltodict.parse(response_xml)

    assert res.status_code == status_code



@pytest.mark.parametrize("ws_version, id, password, culture_name, change_timestamp, status_code", [
    (
        "version1", "user_id", "some_password",
        "some_culture", str(datetime.utcnow()),
        200
    ),
    (
        "version2", "user_id2", "some_password2",
        "some_culture2", str(datetime.utcnow()),
        200
    ),
    (
        "badrequest", "badrequest", "badrequest",
        "badrequest", "badtimestamp",
        999
    ),
    (
        "badrequest", "badrequest", "badrequest",
        "badrequest", "badtimestamp",
        999
    ),
])
def test_getMediaDateModifiedRequest_validator(authorized_client, ws_version, id, password, culture_name, change_timestamp, status_code):

    request_dict = {'s:Envelope': {'@xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/', 's:Body': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'GetMediaDateModifiedRequest': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': ws_version}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': id}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': password}, 'cultureName': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': culture_name}, 'changeTimeStamp': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': change_timestamp}}}}}

    xml_body = xmltodict.unparse(request_dict)
    res = authorized_client.post('/api/media_content', data=xml_body, content_type='text/xml', headers=authorized_client.headers)
    
    assert res.status_code == status_code
