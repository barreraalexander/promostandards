from lxml import etree
from app import schemas
from typing import List
import json

def xml_response(media_content):
    root = etree.Element('AvailableLocation', xsi="http://www.w3.org/2001/XMLSchema-instance", xmlns="http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/")
    
    print ('\n\n')
    print (media_content.location_array)
    print ('\n\n')

    locationId = etree.Element('locationId', xmlns="http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/")
    # locationId.text = media_content.location_id
    locationId.text = media_content.product_id
    root.append(locationId)

    locationName = etree.Element('locationName', xmlns="http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/")
    # locationName.text = media_content.location_name
    locationName.text = media_content.product_id
    root.append(locationName)
    
    xml = etree.tostring(root, pretty_print=True)
    return xml

# def xml_response()