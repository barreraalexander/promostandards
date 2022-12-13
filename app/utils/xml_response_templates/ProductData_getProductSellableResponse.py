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

    root = etree.Element('GetProductSellableResponse',
        xmlns=PRODUCTDATA_COMMON_XMLNS,
        nsmap=ROOT_NSMAP
    )


    # root = etree.Element('GetProductSellableResponse', xsi=xsi, xmlns=PRODUCTDATA_COMMON_XMLNS)

    ProductSellableArray = etree.Element('ProductSellableArray')

    for product_data in product_datas:
        ProductSellable = etree.Element('ProductSellable')

        productId = etree.Element('productId', xmlns=PRODUCTDATA_COMMON_XMLNS)
        productId.text = product_data.product_id
        ProductSellable.append(productId)


        product_data.product_part_array = json.loads(product_data.product_part_array)

        for part in product_data.product_part_array:
            part_schema = schemas.ProductPart(**part)
            if part_schema.is_closeout:                
                partId = etree.Element('partId', xmlns=PRODUCTDATA_COMMON_XMLNS)
                partId.text = part_schema.part_id
                ProductSellable.append(partId)

        culturePoint = etree.Element('culturePoint', xmlns=PRODUCTDATA_COMMON_XMLNS)
        culturePoint.text = 'culturePoint'
        ProductSellable.append(culturePoint)

        ProductSellableArray.append(ProductSellable)

    root.append(ProductSellableArray)

    body.append(root)

    xml = etree.tostring(envelope, pretty_print=True)
    return xml
