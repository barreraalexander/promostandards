from lxml import etree
from app import schemas
from typing import List
import json

from app.utils.helpers import PPC_COMMON_XMLNS, PPC_COMMON_SHARED_OBJECT, BODY_NSMAP, ROOT_NSMAP

def xml_response(decoration_colors: List[schemas.DecorationColor]):
    envelope = etree.Element("{http://www.w3.org/2003/05/soap-envelope}Envelope")
    etree.register_namespace("s", "http://www.w3.org/2003/05/soap-envelope")

    body = etree.Element('{http://www.w3.org/2003/05/soap-envelope}Body', nsmap=BODY_NSMAP)
    envelope.append(body)

    for decoration_color in decoration_colors:
        decoration_color.color_array = json.loads(decoration_color.color_array)
        decoration_color.decoration_method_array = json.loads(decoration_color.decoration_method_array)

        for color in decoration_color.color_array:
            color = schemas.PPC_Color(**color)

            root = etree.Element('Color',
                xmlns=PPC_COMMON_XMLNS,
                nsmap=ROOT_NSMAP
            )

            colorId = etree.Element('colorId', xmlns=PPC_COMMON_SHARED_OBJECT)
            colorId.text = str(color.color_id)                
            root.append(colorId)

            colorName = etree.Element('colorName', xmlns=PPC_COMMON_SHARED_OBJECT)
            colorName.text = str(color.color_name)                
            root.append(colorName)

            body.append(root)

    xml = etree.tostring(envelope, pretty_print=True)

    return xml
