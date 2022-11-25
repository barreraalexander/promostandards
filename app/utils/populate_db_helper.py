# this is used to populate sqlite with dummy data

from app.database import get_session, engine, get_db
from random import randrange, choice
from secrets import token_hex, token_urlsafe
from datetime import datetime
from app import schemas
from app import models

TRUE_OR_FALSE = [False, True]




def populate_database_location_decoration():
    new_location_decoration = schemas.LocationDecoration(**{
        'location_name' : token_hex(6),
        'max_imprint_colors': randrange(0,6),
        'decoration_name': token_hex(6),
        'location_decoration_combo_default': choice(TRUE_OR_FALSE),
        'price_includes' : choice(TRUE_OR_FALSE)
    })

    new_model = models.LocationDecoration(**new_location_decoration.dict())

    db_session = get_session()



    db_session.add(new_model)
    db_session.commit()

    location_decorations = db_session.query(models.LocationDecoration).all()
    print (location_decorations)


def populate_database_productdata():
    new_product = schemas.ProductData(**{
        'product_id' : token_hex(8),
        'product_name': token_hex(4),
        'location_decoration_array' : [],
        'description' : token_hex(6),
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

    db_session = get_session()

    new_model = models.ProductData(**new_product.dict())

    # new


    new_model.location_decoration_array =  ",".join(new_product.location_decoration_array)
    new_model.product_marketing_point_array =  ",".join(new_model.product_marketing_point_array)
    new_model.product_keyword_array =  ",".join(new_product.product_keyword_array)
    new_model.product_category_array =  ",".join(new_product.product_category_array)
    new_model.related_product_array =  ",".join(new_product.related_product_array)
    new_model.product_part_array =  ",".join(new_product.product_part_array)
    new_model.product_price_group_array =  ",".join(new_product.product_price_group_array)
    new_model.fob_point_array =  ",".join(new_product.product_price_group_array)

    # print (new_model.location_decoration_array.split(','))

    db_session.add(new_model)
    # db_session.commit()
# /
# 

    # db_session.refresh(new)
    db_session.commit()

    products = db_session.query(models.ProductData).all()
    print (products)
    # pass

