from lxml import etree
from app import schemas
from typing import List
import json
from datetime import datetime


from app.utils.helpers import COMMON_XSI, PPC_COMMON_XMLNS, PPC_COMMON_SHARED_OBJECT

def xml_response(configuration: schemas.Configuration):
    # root = etree.Element('Part')
    configuration.part_array = json.loads(configuration.part_array)
    configuration.fob_array = json.loads(configuration.fob_array)
    configuration.location_array = json.loads(configuration.location_array)
    xml = b''
    for part in configuration.part_array:
        part = schemas.PPC_Part(**part)
        
        root = etree.Element('Part', xsi=COMMON_XSI, xmlns=PPC_COMMON_XMLNS)

        partId = etree.Element('partId', xmlns=PPC_COMMON_XMLNS)
        partId.text = part.part_id
        root.append(partId)

        
        partDescription = etree.Element('partDescription', xmlns=PPC_COMMON_XMLNS)
        partDescription.text = part.part_description
        root.append(partDescription)

        PartPriceArray = etree.Element('PartPriceArray')
        for part_price in part.part_price_array:
            PartPrice = etree.Element('PartPrice')

            minQuantity = etree.Element('minQuantity')
            minQuantity.text = str(part_price.min_quantity)
            PartPrice.append(minQuantity)
            
            price = etree.Element('price')
            price.text = str(part_price.price)
            PartPrice.append(price)
            
            discount_code = etree.Element('discount_code')
            discount_code.text = part_price.discount_code
            PartPrice.append(discount_code)

            price_uom = etree.Element('price_uom')
            price_uom.text = part_price.price_uom
            PartPrice.append(price_uom)

            priceEffectiveDate = etree.Element('priceEffectiveDate')
            priceEffectiveDate.text = str(part_price.price_effective_date)
            PartPrice.append(priceEffectiveDate)            

            priceExpiryDate = etree.Element('priceExpiryDate')
            priceExpiryDate.text = str(part_price.price_effective_date)
            PartPrice.append(priceExpiryDate)
            
            PartPriceArray.append(PartPrice)
        root.append(PartPriceArray)

        partGroup = etree.Element('partGroup', xmlns=PPC_COMMON_XMLNS)
        partGroup.text = str(part.part_group)
        root.append(partGroup)

        nextPartGroup = etree.Element('nextPartGroup', xmlns=PPC_COMMON_XMLNS)
        nextPartGroup.text = str(part.next_part_group)
        root.append(nextPartGroup)

        partGroupRequired = etree.Element('partGroupRequired', xmlns=PPC_COMMON_XMLNS)
        partGroupRequired.text = str(part.part_group_required).lower()
        root.append(partGroupRequired)

        partGroupDescription = etree.Element('partGroupDescription', xmlns=PPC_COMMON_XMLNS)
        partGroupDescription.text = str(part.part_group_description)
        root.append(partGroupDescription)

        ratio = etree.Element('ratio', xmlns=PPC_COMMON_XMLNS)
        ratio.text = str(part.ratio)
        root.append(ratio)

        defaultPart = etree.Element('defaultPart', xmlns=PPC_COMMON_XMLNS)
        defaultPart.text = str(part.default_part).lower()
        root.append(defaultPart)

        LocationIdArray = etree.Element('LocationIdArray')
        for location_id in part.location_id_array:
            LocationId = etree.Element('LocationId')
            
            locationId = etree.Element('locationId', xmlns=PPC_COMMON_XMLNS)
            locationId.text = location_id

            LocationId.append(locationId)
            
            LocationIdArray.append(LocationId)

        root.append(LocationIdArray)

        xml_part = etree.tostring(root, pretty_print=True)
        xml += xml_part


    return xml
