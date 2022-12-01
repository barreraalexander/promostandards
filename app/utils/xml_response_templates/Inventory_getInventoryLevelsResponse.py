from lxml import etree
from app import schemas
from typing import List
import json

def xml_response(product_data):
    print ('ran')
    xsi = 'http://www.w3.org/2001/XMLSchema-instance'
    xmlns = 'http://www.promostandards.org/WSDL/Inventory/2.0.0/'

    root = etree.Element('GetInventoryLevelsResponse', xsi=xsi, xmlns=xmlns)

    Inventory = etree.Element('Inventory', xmlns=xmlns)


    productId = etree.Element('productId', xsi=xsi, xmlns=xmlns)
    productId.text = product_data.product_id
    Inventory.append(productId)


    root.append(Inventory)

    xml = etree.tostring(root, pretty_print=True)
    return xml