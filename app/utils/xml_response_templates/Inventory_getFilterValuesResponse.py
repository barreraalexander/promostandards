from lxml import etree
from app import schemas
from typing import List
import json
from datetime import datetime


def xml_response(product_data: schemas.ProductData):
    xsi = 'http://www.w3.org/2001/XMLSchema-instance'
    xmlns = 'http://www.promostandards.org/WSDL/Inventory/2.0.0/'

    root = etree.Element('GetFilterValuesRequestResponse', xsi=xsi, xmlns=xmlns)

    product_data.product_part_array = json.loads(product_data.product_part_array)
    label_size_array = ['xl', 'm', 'l']
    part_color_array = ['red', 'green', 'blue']


    filter = schemas.Filter(**{
        'part_id_array' : [part['part_id'] for part in product_data.product_part_array],
        'label_size_array' : label_size_array,
        'part_color_array' : part_color_array,
    })
    Filter = etree.Element('Filter')


    partIdArray = etree.Element('partIdArray')
    for part_id in filter.part_id_array:
        partId = etree.Element('partId')
        partId.text = part_id
        partIdArray.append(partId)
    Filter.append(partIdArray)

    LabelSizeArray = etree.Element('LabelSizeArray')
    for label_size in filter.label_size_array:
        labelSize = etree.Element('labelSize')
        labelSize.text = label_size
        LabelSizeArray.append(labelSize)
    Filter.append(LabelSizeArray)



    PartColorArray = etree.Element('PartColorArray')
    for part_color in filter.part_color_array:
        PartColor = etree.Element('partColor')
        PartColor.text = part_color
        PartColorArray.append(PartColor)
    Filter.append(PartColorArray)



    root.append(Filter)

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