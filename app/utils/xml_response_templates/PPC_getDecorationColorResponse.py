from lxml import etree
from app import schemas
from typing import List
import json
from random import randrange

from app.utils.helpers import COMMON_XSI, PPC_COMMON_SHARED_OBJECT, PPC_COMMON_XMLNS

# get the media_product associated with the product_id
# get the decoration_array
# 

def xml_response(media_content):
    # root = etree.Element('Color', xsi="http://www.w3.org/2001/XMLSchema-instance", xmlns="http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/")


    color_array = [
        schemas.PPC_Color(
            color_name=f'Token{i}',
            color_id=randrange(1, 10),
        )
    for i in range(randrange(1, 10))]
 
    media_content.location_array = json.loads(media_content.location_array)
    xml = b''
    if color_array:
        for color in color_array:
            # location_schema = schemas.Location(**location)
            root = etree.Element('Color', xmlns=PPC_COMMON_XMLNS, xsi=COMMON_XSI)

            colorId = etree.Element('colorId', xmlns=PPC_COMMON_SHARED_OBJECT)
            colorId.text = str(color.color_id)                
            root.append(colorId)

            colorName = etree.Element('colorName', xmlns=PPC_COMMON_SHARED_OBJECT)
            colorName.text = str(color.color_name)                
            root.append(colorName)
            xml_part = etree.tostring(root, pretty_print=True)
            xml += xml_part
    return xml