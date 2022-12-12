from app import schemas, models
from app.database import get_session
from app.utils.xml_response_templates.MediaContent_getMediaContentResponse import xml_response as getMediaContentResponse
from app.utils.xml_response_templates.MediaContent_getDateModifiedResponse import xml_response as getDateModifiedResponse
from app.blueprints.errors.handlers import CustomXMLError
from pydantic import ValidationError
from typing import List

class MediaContentOperations:
    @staticmethod
    def getMediaContent(request_dict):
        try:                
            request_schema = schemas.MediaContent_getMediaContentRequest(**{
                'ws_version': request_dict['wsVersion']['#text'],
                'id': request_dict['id']['#text'],
                'password': request_dict['password']['#text'],
                'culture_name': request_dict['cultureName']['#text'],
                'media_type': request_dict['mediaType']['#text'],
                'class_type': request_dict['classType'],
                'product_id': request_dict['productId']['#text'],
                'part_id': request_dict.get('partId').get('#text'),
            })
        except ValidationError as e:
            loc = e.json()
            raise CustomXMLError(120, custom_description=loc)
        except Exception as e:
            raise CustomXMLError(999)

        db_session = get_session()
        media_content = db_session.query(models.MediaContent).filter(models.MediaContent.product_id==request_schema.product_id).first()
        # media_content = db_session.query(models.MediaContent).filter(models.MediaContent.product_id==request_schema.product_id).first()
        if (not media_content):
                raise CustomXMLError(custom_code=160)
            
        xml = getMediaContentResponse(media_content)

        return xml


    @staticmethod
    def getMediaDateModified(xml_dict):
        request_dict = xml_dict

        # Beginning date time since last change in UTC
        try:                
            request_schema = schemas.MediaContent_getMediaDateModifiedRequest(**{
                'ws_version': request_dict['wsVersion']['#text'],
                'id': request_dict['id']['#text'],
                'password': request_dict['password']['#text'],
                'culture_name': request_dict['cultureName']['#text'],
                'change_time_stamp': request_dict['changeTimeStamp']['#text'],
            })
        except ValidationError as e:
            loc = e.json()
            raise CustomXMLError(120, custom_description=loc)
        except Exception as e:
            raise CustomXMLError(999)
            
        db_session = get_session()
        # media_content = db_session.query(models.MediaContent).first()
        media_content = db_session.query(models.MediaContent).all()
        # media_content = db_session.query(models.MediaContent).filter(models.MediaContent.product_id==request_schema.product_id).first()
        if (not media_content):
            raise CustomXMLError(custom_code=160)
            
        # xml = b''
        # for content in media_content:
        #     data = getDateModifiedResponse(content)            
        #     xml += data
        xml = getDateModifiedResponse(media_content)
            

        return xml



