from lxml import etree
from app import schemas
from typing import List
import json
from datetime import datetime


from app.utils.helpers import COMMON_XSI, PPC_COMMON_XMLNS, PPC_COMMON_SHARED_OBJECT

def xml_response(product_data: schemas.ProductData):
    root = etree.Element('Part')
    
    xml = etree.tostring(root, pretty_print=True)

    return xml
