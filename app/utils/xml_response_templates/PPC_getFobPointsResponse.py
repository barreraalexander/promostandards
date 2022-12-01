from lxml import etree
from app import schemas
from typing import List
import json

from app.utils.helpers import COMMON_XSI, PPC_COMMON_SHARED_OBJECT, PPC_COMMON_XMLNS

def xml_response(product_data: schemas.ProductData):
    # xsi = 'http://www.w3.org/2001/XMLSchema-instance'
    # xmlns = 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/'
    # xmlns_shared_objects = 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'


    product_data.fob_point_array = json.loads(product_data.fob_point_array)
    xml = b''
    if product_data.fob_point_array:
        for fob_point in product_data.fob_point_array:
            root = etree.Element('FobPoint', xsi=COMMON_XSI, xmlns=PPC_COMMON_XMLNS)
            fob_point_schema = schemas.FobPoint(**fob_point)
            
            fobId = etree.Element('fobId', xmlns=PPC_COMMON_SHARED_OBJECT)
            fobId.text = fob_point_schema.fob_id
            root.append(fobId)
            
            fobCity = etree.Element('fobCity')
            fobCity.text = fob_point_schema.fob_city
            root.append(fobCity)

            fobState = etree.Element('fobState')
            fobState.text = fob_point_schema.fob_state
            root.append(fobState)

            fobPostalCode = etree.Element('fobPostalCode', xmlns=PPC_COMMON_SHARED_OBJECT)
            fobPostalCode.text = fob_point_schema.fob_postal_code
            root.append(fobPostalCode)

            fobCountry = etree.Element('fobCountry')
            fobCountry.text = fob_point_schema.fob_country
            root.append(fobCountry)
            
            CurrencySupportedArray = etree.Element('CurrencySupportedArray')
            root.append(CurrencySupportedArray)

            ProductArray = etree.Element('ProductArray')
            Product = etree.Element('Product')
            productId = etree.Element('productId', xmlns=PPC_COMMON_SHARED_OBJECT)
            productId.text = product_data.product_id

            Product.append(productId)
            ProductArray.append(Product)

            root.append(ProductArray)
            
            xml_part = etree.tostring(root, pretty_print=True)
            xml += xml_part


    # xml = etree.tostring(root, pretty_print=True)
    # xml += xml
    return xml