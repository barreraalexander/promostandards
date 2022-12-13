from lxml import etree
from app import schemas
from typing import List

from app.utils.helpers import PPC_COMMON_XMLNS, PPC_COMMON_SHARED_OBJECT, BODY_NSMAP, ROOT_NSMAP

def xml_response(available_charges: List[schemas.AvailableCharge]):
    envelope = etree.Element("{http://www.w3.org/2003/05/soap-envelope}Envelope")
    etree.register_namespace("s", "http://www.w3.org/2003/05/soap-envelope")

    body = etree.Element('{http://www.w3.org/2003/05/soap-envelope}Body', nsmap=BODY_NSMAP)
    envelope.append(body)


    for available_charge in available_charges:
        root = etree.Element('AvailableCharge',
            xmlns=PPC_COMMON_XMLNS,
            nsmap=ROOT_NSMAP
        )        
        chargeId = etree.Element('chargeId', xmlns=PPC_COMMON_SHARED_OBJECT)
        chargeId.text = str(available_charge.charge_id)
        root.append(chargeId)

        chargeName = etree.Element('chargeName', xmlns=PPC_COMMON_SHARED_OBJECT)
        chargeName.text = available_charge.charge_name
        root.append(chargeName)

        chargeDescription = etree.Element('chargeDescription', xmlns=PPC_COMMON_SHARED_OBJECT)
        chargeDescription.text = available_charge.charge_description
        root.append(chargeDescription)

        chargeType = etree.Element('chargeType', xmlns=PPC_COMMON_SHARED_OBJECT)
        chargeType.text = available_charge.charge_type
        root.append(chargeType)

        body.append(root)

    xml = etree.tostring(envelope, pretty_print=True)

    return xml