from app.database import get_session, engine, get_db
from random import randrange, choice, random, uniform
from secrets import token_hex, token_urlsafe
from datetime import datetime, timedelta
from app import schemas
from app import models
import json

from app.utils.populate_db_procedures.random_dataset import TRUE_OR_FALSE



def populate(count=25):

    class_types = [
        schemas.ClassType(**{
            'class_type' : randrange(0, 10),
            'class_name' :f"Token{i}",
        }).dict()
        for i in range(10)
    ]

    decorations = [
        schemas.Decoration(**{
            'decoration_id' : randrange(0, 10),
            'decoration_name' :f"Token{i}",
        }).dict()
        for i in range(10)
    ]


    locations = [
        schemas.Location(**{
            'location_id' : randrange(0, 10),
            'location_name' :f"Token{i}",
        }).dict()
        for i in range(10)
    ]

    new_media_contents = [
        schemas.MediaContent(**{
            'product_id': f'Token{i}',
            'part_id':f"Token{i}",
            'url': token_urlsafe(6),
            'media_type':f"Token{i}",
            'class_type_array': class_types,
            'file_size': uniform(0, 10),
            'width':  randrange(0, 10),
            'height':  randrange(0, 10),
            'dpi':  randrange(0, 10),
            'color':f"Token{i}", 
            'decoration_array': decorations,
            'location_array': locations,
            'description':f"Token{i}",
            'single_part': choice(TRUE_OR_FALSE),
            'change_time_stamp': datetime.utcnow()

        })
        for i in range(count)
    ]

    new_models = [models.MediaContent(**new_media_content.dict())
        for new_media_content in new_media_contents]

    db_session = get_session()
    for new_model in new_models:

        new_model.class_type_array =  json.dumps(new_model.class_type_array, default=str)
        new_model.decoration_array =  json.dumps(new_model.decoration_array, default=str)
        new_model.location_array =  json.dumps(new_model.location_array, default=str)

        db_session.add(new_model)


    db_session.commit()


    media_contents = db_session.query(models.MediaContent).all()
    if (media_contents):
        return
