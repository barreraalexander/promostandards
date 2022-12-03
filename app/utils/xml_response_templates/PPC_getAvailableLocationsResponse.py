from lxml import etree
from app import schemas
from typing import List
import json
from random import randrange, random

from app.utils.helpers import COMMON_XSI, PPC_COMMON_SHARED_OBJECT, PPC_COMMON_XMLNS


def xml_response(locations_array: List[schemas.AvailableLocation]):
    xml = b''

    if locations_array:
        for location in locations_array:
            # location_schema = schemas.Location(**location)
            root = etree.Element('AvailableLocation', xmlns=PPC_COMMON_XMLNS, xsi=COMMON_XSI)

            locationId = etree.Element('locationId', xmlns=PPC_COMMON_SHARED_OBJECT)
            locationId.text = str(location.location_id)                
            root.append(locationId)

            locationName = etree.Element('locationName', xmlns=PPC_COMMON_SHARED_OBJECT)
            locationName.text = str(location.location_name)                
            root.append(locationName)
            xml_part = etree.tostring(root, pretty_print=True)
            xml += xml_part
    return xml

# def xml_response()