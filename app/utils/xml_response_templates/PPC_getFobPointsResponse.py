from lxml import etree
from app import schemas
from typing import List
import json

from app.utils.helpers import COMMON_XSI, PPC_COMMON_SHARED_OBJECT, PPC_COMMON_XMLNS

def xml_response(fob_points: List[schemas.PPC_FobPoint]):

    xml = b''
    for fob_point in fob_points:
        fob_point.currency_supported_array = json.loads(fob_point.currency_supported_array)
        fob_point.product_array = json.loads(fob_point.product_array)

        root = etree.Element('FobPoint', xsi=COMMON_XSI, xmlns=PPC_COMMON_XMLNS)
        fob_point_schema = fob_point
        
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
        for currency_supported in fob_point.currency_supported_array:
            currency_supported = schemas.Currency(**currency_supported) 
            
            CurrencySupported = etree.Element('CurrencySupported')

            currency = etree.Element('currency', xmlns=PPC_COMMON_XMLNS)
            currency.text = currency_supported.currency
            CurrencySupported.append(currency)

            CurrencySupportedArray.append(CurrencySupported)
        root.append(CurrencySupportedArray)


        ProductArray = etree.Element('ProductArray')
        for product in fob_point.product_array:
            product = schemas.PPC_Product(**product)

            Product = etree.Element('Product')

            productId = etree.Element('productId', xmlns=PPC_COMMON_XMLNS)
            productId.text = product.product_id
            Product.append(productId)

            ProductArray.append(Product)
        root.append(ProductArray)

        xml_part = etree.tostring(root, pretty_print=True)
        xml += xml_part

    return xml