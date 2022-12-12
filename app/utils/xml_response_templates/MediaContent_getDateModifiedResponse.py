from lxml import etree
from app import schemas
from typing import List
import json


from app.utils.helpers import MEDIACONTENT_COMMON_SHARED_OBJECT, \
    MEDIACONTENT_COMMON_XMLNS, COMMON_XSI, ENVELOPE_S_XMLNS, \
    BODY_XSD, BODY_XSI, ENVELOPE_NSMAP, BODY_NSMAP, ROOT_NSMAP

def xml_response(media_contents: List[schemas.MediaContent]):


    envelope = etree.Element("{http://www.w3.org/2003/05/soap-envelope}Envelope")
    etree.register_namespace("s", "http://www.w3.org/2003/05/soap-envelope")
 

    body = etree.Element('{http://www.w3.org/2003/05/soap-envelope}Body', nsmap=BODY_NSMAP)
    envelope.append(body)

    # for content in media_content:
    #     pass


    xml = b''
    for media_content in media_contents:
        root = etree.Element('MediaDateModified',
            xmlns=MEDIACONTENT_COMMON_XMLNS,
            nsmap=ROOT_NSMAP
        )

        productId = etree.Element('productId', xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/")
        productId.text = media_content.product_id
        root.append(productId)

        partID = etree.Element('partID', xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/")
        partID.text = media_content.part_id
        root.append(partID)

        body.append(root)

    xml = etree.tostring(envelope, pretty_print=True)


    return xml
