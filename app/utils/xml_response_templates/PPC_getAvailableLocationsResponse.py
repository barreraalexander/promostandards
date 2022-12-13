from lxml import etree
from app import schemas
from typing import List

from app.utils.helpers import PPC_COMMON_XMLNS, PPC_COMMON_SHARED_OBJECT, BODY_NSMAP, ROOT_NSMAP

def xml_response(locations_array: List[schemas.AvailableLocation]):
    envelope = etree.Element("{http://www.w3.org/2003/05/soap-envelope}Envelope")
    etree.register_namespace("s", "http://www.w3.org/2003/05/soap-envelope")
 

    body = etree.Element('{http://www.w3.org/2003/05/soap-envelope}Body', nsmap=BODY_NSMAP)
    envelope.append(body)


    for location in locations_array:

        root = etree.Element('AvailableLocation',
            xmlns=PPC_COMMON_XMLNS,
            nsmap=ROOT_NSMAP
        )

        locationId = etree.Element('locationId', xmlns=PPC_COMMON_SHARED_OBJECT)
        locationId.text = str(location.location_id)                
        root.append(locationId)

        locationName = etree.Element('locationName', xmlns=PPC_COMMON_SHARED_OBJECT)
        locationName.text = str(location.location_name)                
        root.append(locationName)

        body.append(root)


        # xml += xml_part
    xml = etree.tostring(envelope, pretty_print=True)

    return xml

# def xml_response()