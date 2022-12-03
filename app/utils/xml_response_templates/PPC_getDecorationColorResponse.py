from lxml import etree
from app import schemas
from typing import List
import json

from app.utils.helpers import COMMON_XSI, PPC_COMMON_SHARED_OBJECT, PPC_COMMON_XMLNS

def xml_response(decoration_colors: List[schemas.DecorationColor]):

    xml = b''
    for decoration_color in decoration_colors:
        decoration_color.color_array = json.loads(decoration_color.color_array)
        decoration_color.decoration_method_array = json.loads(decoration_color.decoration_method_array)

        for color in decoration_color.color_array:
            color = schemas.PPC_Color(**color)

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
