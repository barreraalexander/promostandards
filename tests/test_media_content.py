import xmltodict

def test_getMediaContentRequest_error(client):
    res = client.get('/api/media_content')

    assert res.status_code == 999

def test_getMediaContentRequest_successful(client):
    request_dict = {'GetMediaContentRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'cultureName': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'cultureName1'}, 'mediaType': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Image'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'classType': '1'}}
    xml_body = xmltodict.unparse(request_dict)
    res = client.get('/api/media_content', data=xml_body, content_type='text/xml')
    
    assert res.status_code == 200


def test_getMediaDateModifiedRequest_error(client):
    res = client.get('/api/media_content')

    assert res.status_code == 999

def test_getMediaDateModifiedRequest_successful(client):
    request_dict = {'GetMediaDateModifiedRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'Token1'}, 'cultureName': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': 'cultureName1'}, 'changeTimeStamp': {'@xmlns': 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/', '#text': '1900-01-01T01:01:01.0000000+00:00'}}}
    xml_body = xmltodict.unparse(request_dict)
    res = client.get('/api/media_content', data=xml_body, content_type='text/xml')
    
    assert res.status_code == 200

