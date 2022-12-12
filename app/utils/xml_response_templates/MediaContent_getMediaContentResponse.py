from lxml import etree
from app import schemas
from typing import List
import json
import xmltodict

from app.utils.helpers import MEDIACONTENT_COMMON_SHARED_OBJECT, \
    MEDIACONTENT_COMMON_XMLNS, \
    BODY_NSMAP, ROOT_NSMAP

def xml_response(media_content: schemas.MediaContent):

    envelope = etree.Element("{http://www.w3.org/2003/05/soap-envelope}Envelope")
    etree.register_namespace("s", "http://www.w3.org/2003/05/soap-envelope")
 

    body = etree.Element('{http://www.w3.org/2003/05/soap-envelope}Body', nsmap=BODY_NSMAP)
    envelope.append(body)


    root = etree.Element('MediaContent',
        xmlns=MEDIACONTENT_COMMON_XMLNS,
        nsmap=ROOT_NSMAP
    )

    productId = etree.Element('productId', xmlns=MEDIACONTENT_COMMON_SHARED_OBJECT)
    productId.text = media_content.product_id
    root.append(productId)
    
    partID = etree.Element('partID', xmlns=MEDIACONTENT_COMMON_SHARED_OBJECT)
    partID.text = media_content.part_id
    root.append(partID)
    
    url = etree.Element('url')
    url.text = media_content.url
    root.append(url)


    mediaType = etree.Element('mediaType', xmlns=MEDIACONTENT_COMMON_SHARED_OBJECT)
    mediaType.text = media_content.media_type
    root.append(mediaType)

    ClassTypeArray = etree.Element('ClassTypeArray')
    media_content.class_type_array = json.loads(media_content.class_type_array)
    if media_content.class_type_array:
        for class_type in media_content.class_type_array:
            class_type_schema = schemas.ClassType(**class_type)
            ClassType = etree.Element('ClassType')

            classTypeId = etree.Element('classTypeId')
            classTypeId.text = str(class_type_schema.class_type)
            ClassType.append(classTypeId)

            classTypeName = etree.Element('classTypeName')
            classTypeName.text = class_type_schema.class_name
            ClassType.append(classTypeName)

            ClassTypeArray.append(ClassType)
    root.append(ClassTypeArray)

    fileSize = etree.Element('fileSize')
    fileSize.text = str(media_content.file_size)

    root.append(fileSize)

    width = etree.Element('width')
    width.text = str(media_content.width)

    root.append(width)

    height = etree.Element('height')
    height.text = str(media_content.height)

    root.append(height)

    dpi = etree.Element('dpi')
    dpi.text = str(media_content.dpi)

    root.append(dpi)

    color = etree.Element('color')
    color.text = str(media_content.color)

    root.append(color)


    DecorationArray = etree.Element('DecorationArray')
    media_content.decoration_array = json.loads(media_content.decoration_array)
    if media_content.decoration_array:
        for decoration in media_content.decoration_array:
            decoration_schema = schemas.Decoration(**decoration)
            Decoration = etree.Element('Decoration')

            decorationId = etree.Element('decorationId')
            decorationId.text = str(decoration_schema.decoration_id)                
            Decoration.append(decorationId)

            decorationName = etree.Element('decorationName')
            decorationName.text = str(decoration_schema.decoration_name)                
            Decoration.append(decorationName)

            DecorationArray.append(Decoration)

    root.append(DecorationArray)

    LocationArray = etree.Element('LocationArray')
    media_content.location_array = json.loads(media_content.location_array)
    if media_content.location_array:
        for location in media_content.location_array:
            location_schema = schemas.Location(**location)
            Location = etree.Element('Location')

            locationId = etree.Element('locationId')
            locationId.text = str(location_schema.location_id)                
            Location.append(locationId)

            locationName = etree.Element('locationName')
            locationName.text = str(location_schema.location_name)                
            Location.append(locationName)

            LocationArray.append(Location)

    root.append(LocationArray)


    DecorationId = etree.Element('DecorationId')
    DecorationId.text = str(1)
    root.append(DecorationId)
    

    description = etree.Element('description')
    description.text = media_content.description
    root.append(description)
    

    singlePart = etree.Element('singlePart')
    singlePart.text = str(media_content.single_part).lower()
    root.append(singlePart)
    

    ChangeTimeStamp = etree.Element('ChangeTimeStamp')
    ChangeTimeStamp.text = str(media_content.change_time_stamp).lower()
    root.append(ChangeTimeStamp)

    body.append(root)


    xml = etree.tostring(envelope, pretty_print=True, encoding='UTF-8')

    return xml
