from lxml import etree
from app import schemas
from typing import List

def xml_response(media_content_request: List[schemas.MediaContent_getMediaContentRequest]):
    # print (type(media_content_schema))

    # for xml_parent in media_content_schema:
    #     print ('\n\n')
    #     print (xml_parent)
    #     print ('\n\n')
    #     break

    # root = etree.Element('root')
    # root.append(etree.Element('child'))


    # # another child with text
    # child = etree.Element('child')
    # child.text = 'some text'
    # root.append(child)


    # xml = etree.tostring(root, pretty_print=True)


    root = etree.Element('MediaContent', xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/")
    root.append(etree.Element('productId', xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/"))
    root.append(etree.Element('partID', xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/"))
    
    # root = etree.Element('root')
    
    # qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "type")
    # # element = etree.Element('Element', qname: "some type")



    # another child with text
    child = etree.Element('child')
    child.text = 'some text'
    root.append(child)


    xml = etree.tostring(root, pretty_print=True)



    print (xml)


    return xml

    return f"""
    <MediaContent xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/">
        <productId xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/">{media_content_schema.product_id}</productId>
        <partId xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/">{media_content_schema.part_id}</partId>
        <url>{media_content_schema.url}</url>
        <mediaType xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/">{media_content_schema.product_id}</mediaType>
        <ClassTypeArray>
            <ClassType>
                <classTypeId>1</classTypeId>
                <classTypeName>Token1</classTypeName>
            </ClassType>
            <ClassType>
                <classTypeId>-2147483647</classTypeId>
                <classTypeName>Token2</classTypeName>
            </ClassType>
        </ClassTypeArray>
        <fileSize>1</fileSize>
        <width>1</width>
        <height>1</height>
        <dpi>1</dpi>
        <color>Token1</color>
        <DecorationArray>
            <Decoration>
                <decorationId>1</decorationId>
                <decorationName>Token1</decorationName>
            </Decoration>
            <Decoration>
                <decorationId>-2147483647</decorationId>
                <decorationName>Token2</decorationName>
            </Decoration>
        </DecorationArray>
        <LocationArray>
            <Location>
                <locationId>1</locationId>
                <locationName>Token1</locationName>
            </Location>
            <Location>
                <locationId>-2147483647</locationId>
                <locationName>Token2</locationName>
            </Location>
        </LocationArray>
        <decorationId>1</decorationId>
        <description>Token1</description>
        <singlePart>true</singlePart>
        <changeTimeStamp xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/">
            1900-01-01T01:01:01.0000000+00:00</changeTimeStamp>
    </MediaContent>
    <?xml version="1.0" encoding="utf-8"?>
    <MediaContent xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/">
        <productId xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/">Token1</productId>
        <partId xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/">Token1</partId>
        <url>Token1</url>
        <mediaType xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/">Image</mediaType>
        <ClassTypeArray>
            <ClassType>
                <classTypeId>1</classTypeId>
                <classTypeName>Token1</classTypeName>
            </ClassType>
            <ClassType>
                <classTypeId>-2147483647</classTypeId>
                <classTypeName>Token2</classTypeName>
            </ClassType>
        </ClassTypeArray>
        <fileSize>1</fileSize>
        <width>1</width>
        <height>1</height>
        <dpi>1</dpi>
        <color>Token1</color>
        <DecorationArray>
            <Decoration>
                <decorationId>1</decorationId>
                <decorationName>Token1</decorationName>
            </Decoration>
            <Decoration>
                <decorationId>-2147483647</decorationId>
                <decorationName>Token2</decorationName>
            </Decoration>
        </DecorationArray>
        <LocationArray>
            <Location>
                <locationId>1</locationId>
                <locationName>Token1</locationName>
            </Location>
            <Location>
                <locationId>-2147483647</locationId>
                <locationName>Token2</locationName>
            </Location>
        </LocationArray>
        <decorationId>1</decorationId>
        <description>Token1</description>
        <singlePart>true</singlePart>
        <changeTimeStamp xmlns="http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/">
            1900-01-01T01:01:01.0000000+00:00</changeTimeStamp>
    </MediaContent>
    """