from lxml import etree
from app import schemas
from typing import List
import json

def xml_response(media_content):

    root = etree.Element('MediaDateModified', xsi="http://www.w3.org/2001/XMLSchema-instance", xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/")

    productId = etree.Element('productId', xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/")
    productId.text = media_content.product_id
    root.append(productId)

    partID = etree.Element('partID', xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/")
    partID.text = media_content.part_id
    root.append(partID)

    xml = etree.tostring(root, pretty_print=True)
    return xml
