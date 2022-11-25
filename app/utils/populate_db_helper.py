# this is used to populate sqlite with dummy data

from app.database import get_session, engine, get_db
from random import randrange, choice
from secrets import token_hex, token_urlsafe
from datetime import datetime
from app import schemas

TRUE_OR_FALSE = [False, True]



def populate_database():
    print ('running')
    new_media_content = schemas.ProductData(**{
        'product_id' : token_hex(8),
        'product_name': token_hex(4),
        'location_decoration_array' : [],
        'product_marketing_point_array' : [],
        'product_keyword_array' : [],
        'export' : False,
        'product_category_array' : [],
        'related_product_array' : [],
        'product_part_array' : [],
        'last_change_date' : datetime.utcnow(),
        'creation_date' : datetime.utcnow(),
        'is_caution' : choice(TRUE_OR_FALSE),
        'is_closeout' : choice(TRUE_OR_FALSE),
        'line_name' : token_hex(6),
        'primary_image_url' : token_hex(6),
        'product_price_group_array' : [],
        'fob_point_array' : []        
    })



    # print (new_media_content.line_name)


    # db_session = get_session()

    db_session = yield get_db()
    print (engine.table_names())
    # print ('this ran')
    # print (db_session)


    # db_session.add(new_media_content)
    # db_session.commit()
# /
# 

    # db_session.refresh(new)


    # pass