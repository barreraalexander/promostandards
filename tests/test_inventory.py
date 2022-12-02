import xmltodict

XML_BODY = """<GetInventoryLevelsRequest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.promostandards.org/WSDL/Inventory/2.0.0/">
  <wsVersion xmlns="http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/">2.0.0</wsVersion>
  <id xmlns="http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/">id1</id>
  <password xmlns="http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/">password1</password>
  <productId xmlns="http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/">Token1</productId>
  <Filter xmlns="http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/">
    <partIdArray>
      <partId>partId1</partId>
      <partId>partId2</partId>
    </partIdArray>
    <LabelSizeArray>
      <labelSize>2XL</labelSize>
      <labelSize>2XS</labelSize>
    </LabelSizeArray>
    <PartColorArray>
      <partColor>partColor1</partColor>
      <partColor>partColor2</partColor>
    </PartColorArray>
  </Filter>
</GetInventoryLevelsRequest>"""

def test_getInventoryLevels_error(client):

    # xml_dict = {'GetInventoryLevelsRequest'}
    xml_dict = xmltodict.unparse(XML_BODY)
    xml_body = xmltodict.unparse(xml_dict)


    # print (xml_body)
    res = client.get('/api/inventory', data=xml_body, content_type='text/xml')
    print ('\n\n')
    # res = client.get('/api/inventory')
    # print (xml_dict)
    print (xml_dict)
    print ('\n\n')

    # res_dict = xmltodict.parse(res)
    # print (res.get_data())
    # print (dir(res))
    # print (res_dict)

    # print ('\n\n')
    # print (res.get_data())
    # print ('\n\n')
    # print (res.data)
    # print ('\n\n')

    # print ('\n\n')

    # print (dir(client))
    # assert res.status_code == 500
    # assert True

def test_getInventoryLevels_successful(client):
    res = client.get('/api/inventory')
    # print (dir(res))
    # print (res.get_data())



    # assert res.status_code == 200
    assert True

# def test_getFilterValues(client):
#     res = client.get('/api/inventory')
#     # print (dir(res))
#     # assert res.status_code == 200
#     assert True