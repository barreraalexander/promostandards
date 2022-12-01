from lxml import etree
from app import schemas
from typing import List
import json
from datetime import datetime

def xml_response(product_data):
    xsi = 'http://www.w3.org/2001/XMLSchema-instance'
    xmlns = 'http://www.promostandards.org/WSDL/Inventory/2.0.0/'

    root = etree.Element('GetInventoryLevelsResponse', xsi=xsi, xmlns=xmlns)

    Inventory = etree.Element('Inventory', xmlns=xmlns)


    productId = etree.Element('productId')
    productId.text = product_data.product_id
    Inventory.append(productId)


    PartInventoryArray = etree.Element('PartInventoryArray')


    product_data.product_part_array = json.loads(product_data.product_part_array)

    for part in product_data.product_part_array:
        # part_schema = schemas.ProductPart(**part)
        part['main_part'] = False
        part['manufactured_item'] = False
        part['buy_to_order'] = False
        part['inventory_location_array'] = [
            schemas.InventoryLocation(**{
                'inventory_location_id': f"Token{i}",
                'postal_code': f"Token{i}",
                'country': f"Token{i}",
                'inventory_location_quantity': schemas.Quantity(**{
                    'uom': f'Token{i}'
                }),
                'future_availability_array': [schemas.FutureAvailability(**{
                    'quantity': schemas.Quantity(**{
                        'uom' : f'Token{i}'
                    }),
                    'available_on': datetime.utcnow()
                }) for i in range(10)]
                
            
        })
        for i in range(10)
        ]
        
        part_schema = schemas.PartInventory(**part)
        if part_schema:                
            
            PartInventory = etree.Element('PartInventory')
            
            partId = etree.Element('partId')
            partId.text = part_schema.part_id
            PartInventory.append(partId)

            mainPart = etree.Element('mainPart')
            mainPart.text = str(part_schema.main_part).lower()
            PartInventory.append(mainPart)            

            partColor = etree.Element('partColor')
            partColor.text = part_schema.part_color
            PartInventory.append(partColor)

            labelSize = etree.Element('labelSize')
            labelSize.text = part_schema.label_size
            PartInventory.append(labelSize)        

            partDescription = etree.Element('partDescription')
            partDescription.text = part_schema.part_description
            PartInventory.append(partDescription)

            quantityAvailable = etree.Element('quantityAvailable')
            # quantityAvailable.text = part_schema.part_description
            
            Quantity = etree.Element('Quantity')
            
            uom = etree.Element('uom')
            uom.text = 'here'
            Quantity.append(uom)

            value = etree.Element('value')
            value.text = 'here'
            Quantity.append(value)
        
            quantityAvailable.append(Quantity)
        
            PartInventory.append(quantityAvailable)

            manufacturedItem = etree.Element('manufacturedItem')
            manufacturedItem.text = str(part_schema.manufactured_item)
            PartInventory.append(manufacturedItem)

            buyToOrder = etree.Element('buyToOrder')
            buyToOrder.text = str(part_schema.buy_to_order)
            PartInventory.append(buyToOrder)

            replenishmentLeadTime = etree.Element('replenishmentLeadTime')
            replenishmentLeadTime.text = str(part_schema.replenishment_lead_time)
            PartInventory.append(replenishmentLeadTime)
 

            attributeSelection = etree.Element('attributeSelection')
            attributeSelection.text = str(part_schema.attribute_selection)
            PartInventory.append(attributeSelection)
 
            InventoryLocationArray = etree.Element('InventoryLocationArray')
            # replenishmentLeadTime.text = str(part_schema.replenishment_lead_time)

            # for


            # product_data = json.loads(product_data.product_part_array)
            # inventory_location_array = part_schema.inventory_location_array
            for inventory_location in part_schema.inventory_location_array:
                InventoryLocation = etree.Element('InventoryLocation')

                inventoryLocationId = etree.Element('inventoryLocationId')
                inventoryLocationId.text = inventory_location.inventory_location_id
                InventoryLocation.append(inventoryLocationId)

                inventoryLocationName = etree.Element('inventoryLocationName')
                inventoryLocationName.text = inventory_location.inventory_location_name
                InventoryLocation.append(inventoryLocationName)                

                postalCode = etree.Element('postalCode')
                postalCode.text = inventory_location.postal_code
                InventoryLocation.append(postalCode)

                country = etree.Element('country')
                country.text = inventory_location.country
                InventoryLocation.append(country)

                inventoryLocationQuantity = etree.Element('inventoryLocationQuantity')
                Quantity = etree.Element('Quantity')
            
                inventoryLocationQuantity.append(Quantity)
                # print(inventory_location.inventory_location_quantity)

                InventoryLocation.append(inventoryLocationQuantity)

                FutureAvailabilityArray = etree.Element('FutureAvailabilityArray')
                for future_availability in inventory_location.future_availability_array:
                    FutureAvailability = etree.Element('FutureAvailability')
                    
                    Quantity = etree.Element('Quantity')
                    FutureAvailability.append(Quantity)

                    availableOn= etree.Element('availableOn')
                    availableOn.text = str(future_availability.available_on)
                    FutureAvailability.append(availableOn)


                    FutureAvailabilityArray.append(FutureAvailability)


                InventoryLocation.append(FutureAvailabilityArray)


                InventoryLocationArray.append(InventoryLocation)


            PartInventory.append(InventoryLocationArray)

            lastModified = etree.Element('lastModified')
            lastModified.text = str(datetime.utcnow())
            PartInventory.append(lastModified)


            PartInventoryArray.append(PartInventory)








    Inventory.append(PartInventoryArray)
    root.append(Inventory)

    ServiceMessageArray = etree.Element('ServiceMessageArray', xmlns=xmlns)
    service_messages = [schemas.ServiceMessage(**{
        'code' : i,
        'description' : f'description{i}',
        'severity' : f'severity{i}'
    }) for i in range(10)]


    for message in service_messages:
        ServiceMessage = etree.Element('ServiceMessage')

        code = etree.Element('code')
        code.text = str(message.code)
        ServiceMessage.append(code)

        description = etree.Element('description')
        description.text = message.description
        ServiceMessage.append(description)

        severity = etree.Element('severity')
        severity.text = message.severity
        ServiceMessage.append(severity)


        ServiceMessageArray.append(ServiceMessage)

    root.append(ServiceMessageArray)

    xml = etree.tostring(root, pretty_print=True)
    return xml