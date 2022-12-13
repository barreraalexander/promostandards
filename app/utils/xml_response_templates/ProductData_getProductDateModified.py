from lxml import etree
from app import schemas
from typing import List
import json

from app.utils.helpers import PRODUCTDATA_COMMON_SHARED_OBJECT, PRODUCTDATA_COMMON_XMLNS, BODY_NSMAP, ROOT_NSMAP


def xml_response(product_datas: List[schemas.ProductData]):
    envelope = etree.Element("{http://www.w3.org/2003/05/soap-envelope}Envelope")
    etree.register_namespace("s", "http://www.w3.org/2003/05/soap-envelope")
 

    body = etree.Element('{http://www.w3.org/2003/05/soap-envelope}Body', nsmap=BODY_NSMAP)
    envelope.append(body)

    root = etree.Element('ProductDateModified',
        xmlns=PRODUCTDATA_COMMON_XMLNS,
        nsmap=ROOT_NSMAP
    )


    for product_data in product_datas:
        productId = etree.Element('productId', xmlns=PRODUCTDATA_COMMON_XMLNS, nsmap=BODY_NSMAP)
        productId.text = product_data.product_id
        root.append(productId)

        product_data.product_part_array = json.loads(product_data.product_part_array)
        for part in product_data.product_part_array:
            part_schema = schemas.ProductPart(**part)
            if part_schema:                
                partId = etree.Element('partId', xmlns=PRODUCTDATA_COMMON_XMLNS, nsmap=ROOT_NSMAP)
                partId.text = part_schema.part_id
                root.append(partId)
            
    body.append(root)

    xml = etree.tostring(envelope, pretty_print=True)
    return xml
