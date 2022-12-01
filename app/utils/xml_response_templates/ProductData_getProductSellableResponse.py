from lxml import etree
from app import schemas
from typing import List
import json

def xml_response(product_datas: List[schemas.ProductData]):
    xsi = 'http://www.w3.org/2001/XMLSchema-instance'
    xmlns = 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/'

    root = etree.Element('GetProductSellableResponse', xsi=xsi, xmlns=xmlns)

    ProductSellableArray = etree.Element('ProductSellableArray')

    for product_data in product_datas:
        ProductSellable = etree.Element('ProductSellable')

        productId = etree.Element('productId', xmlns=xmlns)
        productId.text = product_data.product_id
        ProductSellable.append(productId)


        product_data.product_part_array = json.loads(product_data.product_part_array)

        for part in product_data.product_part_array:
            part_schema = schemas.ProductPart(**part)
            if part_schema.is_closeout:                
                partId = etree.Element('partId', xmlns=xmlns)
                partId.text = part_schema.part_id
                ProductSellable.append(partId)

        culturePoint = etree.Element('culturePoint', xmlns=xmlns)
        # culturePoint.text = product_data.
        culturePoint.text = 'culturePoint'
        ProductSellable.append(culturePoint)

        ProductSellableArray.append(ProductSellable)

    root.append(ProductSellableArray)

    xml = etree.tostring(root, pretty_print=True)
    return xml
