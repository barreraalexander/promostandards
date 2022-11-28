from app import schemas
# from flask import 

from app.utils.xml_response_templates.MediaContent_getMediaContentResponse import create_MediaContent_response
from app.utils.helpers import unpack_elems

from typing import List


def MediaContentResponse_Maker(media_content_schemas):
# wrapper: <?xml version="1.0" encoding="utf-8"?>

    response_elements = [create_MediaContent_response(element) \
        for element in media_content_schemas] 

    # return response_elements
    return (response_elements)