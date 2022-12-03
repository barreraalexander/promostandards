from lxml import etree
from app import schemas
from typing import List


from app.utils.helpers import COMMON_XSI, PPC_COMMON_XMLNS, PPC_COMMON_SHARED_OBJECT

def xml_response(available_charges: List[schemas.AvailableCharge]):
    xml = b''
    for available_charge in available_charges:
        root = etree.Element('AvailableCharge', xmlns=PPC_COMMON_XMLNS, xsi=COMMON_XSI)
        
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

        xml_part = etree.tostring(root, pretty_print=True)
        xml += xml_part

    return xml