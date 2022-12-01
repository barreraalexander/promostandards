from lxml import etree
from app import schemas
from typing import List
import json

def xml_response(media_content):
    root = etree.Element('Color', xsi="http://www.w3.org/2001/XMLSchema-instance", xmlns="http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/")
    media_content.location_array = json.loads(media_content.location_decoration_array)
    # media_content.location_array = json.loads(media_content.color)
    if media_content.location_array:
        for location in media_content.location_array:
            location_schema = schemas.Location(**location)
            Location = etree.Element('Location')

            locationId = etree.Element('locationId', xmlns="http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/")
            locationId.text = str(location_schema.location_id)                
            Location.append(locationId)

            locationName = etree.Element('locationName', xmlns="http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/")
            locationName.text = str(location_schema.location_name)                
            Location.append(locationName)


            root.append(Location)
    
    xml = etree.tostring(root, pretty_print=True)
    return xml

# def xml_response()