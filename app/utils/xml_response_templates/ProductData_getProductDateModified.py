from lxml import etree
from app import schemas
from typing import List
import json

def xml_response(product_data):
    xsi = 'http://www.w3.org/2001/XMLSchema-instance'
    xmlns = 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/'

    root = etree.Element('ProductDateModified', xsi=xsi, xmlns=xmlns)

    productId = etree.Element('productId', xsi=xsi, xmlns=xmlns)
    productId.text = product_data.product_id
    root.append(productId)


    product_data.product_part_array = json.loads(product_data.product_part_array)

    for part in product_data.product_part_array:
        part_schema = schemas.ProductPart(**part)
        if part_schema:                
            partId = etree.Element('partId', xsi=xsi, xmlns=xmlns)
            partId.text = part_schema.part_id
            root.append(partId)
        

    xml = etree.tostring(root, pretty_print=True)
    return xml
