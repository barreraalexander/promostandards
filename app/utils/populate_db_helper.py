# this is used to populate sqlite with dummy data

from app.database import get_session, engine, get_db
from random import randrange, choice, random, uniform
from secrets import token_hex, token_urlsafe
from datetime import datetime, timedelta
from app import schemas
from app import models
import json

TRUE_OR_FALSE = [False, True]

def populate_database_location_decoration(count=25):
    new_location_decorations = [schemas.LocationDecoration(**{
        'location_name' : token_hex(6),
        'max_imprint_colors': randrange(0,6),
        'decoration_name': token_hex(6),
        'location_decoration_combo_default': choice(TRUE_OR_FALSE),
        'price_includes' : choice(TRUE_OR_FALSE)
    }) for i in range(count)]

    new_models = [models.LocationDecoration(**new_location_decoration.dict())
        for new_location_decoration in new_location_decorations]

    db_session = get_session()
    for new_model in new_models:
        db_session.add(new_model)

    db_session.commit()


def populate_database_productdata(count=25):
    db_session = get_session()
    
    # location_decorations = db_session.query(models.ProductData).all()

    location_decorations = [schemas.LocationDecoration(**{
        'location_name' : token_hex(6),
        'max_imprint_colors': randrange(0,6),
        'decoration_name': token_hex(6),
        'location_decoration_combo_default': choice(TRUE_OR_FALSE),
        'price_includes' : choice(TRUE_OR_FALSE)
    }) for i in range(count)]

    product_marketing_points = [
        schemas.ProductMarketingPoint(**{
            'point_type': token_hex(6),
            'point_copy': token_hex(6)
        }).dict()
        for i in range(10)
    ]

    product_keywords = [
        schemas.ProductKeyword(**{
            'keyword' : token_hex(6)
        }).dict()
        for i in range(10)
    ]


    product_categories = [
        schemas.ProductCategory(**{
            'category' : token_hex(6),
            'sub_category' : token_hex(6)
        }).dict()
        for i in range(10)
    ]

    related_products = [
        schemas.RelatedProduct(**{
            'relation_type' : token_hex(6),
            'product_id' : token_hex(6),
            'part_id' : token_hex(6)
        }).dict()
        for i in range(10)
    ]

    colors = [
        schemas.Color(**{
            'color_name': token_hex(6),
            'color' : token_hex(6),
            'hex' : token_hex(6),
            'approximate_pms' : token_hex(6),
            'standard_color_name' : token_hex(6)
        }).dict()
        for i in range(10)
    ]

    
    specifications = [
        schemas.Specification(**{
            'specification_type' : token_hex(6),
            'specification_uom' : token_hex(6),
            'measurement_value' : token_hex(6)
        }).dict()
        for i in range(10)
    ]

    product_packagings = [
        schemas.ProductPackaging(**{
            'default': choice(TRUE_OR_FALSE),
            'package_type': token_hex(6),
            'description': token_hex(6),
            'quantity':  random(),
            'dimension_uom' : token_hex(6),
            'depth' : random(),
            'height' : random(),
            'width' : random(),
            'weight_uom' : token_hex(6),
            'weight' : uniform(1, 10)
        }).dict()
        for i in range(10)
    ]


    shipping_packagings = [
        schemas.ShippingPackaging(**{
            'package_type': token_hex(6),
            'description': token_hex(6),
            'quantity':  random(),
            'dimension_uom' : token_hex(6),
            'depth' : random(),
            'height' : random(),
            'width' : random(),
            'weight_uom' : token_hex(6),
            'weight' : uniform(1, 10)
        }).dict()
        for i in range(10)
    ]


    product_parts = [
        schemas.ProductPart(**{
            'part_id' : token_hex(6),
            'description' : token_hex(6),
            'country_of_origin' : token_hex(6),
            'color_array' : colors,
            'primary_material' : token_hex(6),
            'specification_array' : specifications,
            'shape'  : token_hex(6),
            'apparel_size'  : schemas.ApparelSize(**{
                  'apparel_style' : token_hex(6),
                  'label_size': token_hex(6),
                  'custom_size': token_hex(6)
            }).dict(),
            'dimension' : schemas.Dimension(**{
                'dimension_uom' : token_hex(6),
                'depth': randrange(0, 10) * random(),
                'height': randrange(0, 10) * random(),
                'width': randrange(0, 10) * random(),
                'weight_uom': token_hex(6),
                'weight': uniform(0, 100)
            }).dict(),
            'lead_time' : randrange(0, 10),
            'unspsc' : token_hex(6),
            'gtin' : token_hex(6),
            'is_rush_service' : choice(TRUE_OR_FALSE),
            'product_packaging_array': product_packagings,
            'shipping_packaging_array': shipping_packagings,
            'end_date': datetime.utcnow(),
            'effective_date': datetime.utcnow(),
            'is_closeout': choice(TRUE_OR_FALSE),
            'is_caution': choice(TRUE_OR_FALSE),
            'nmfc_code': uniform(0, 10),
            'nmfc_description': token_hex(6),
            'is_on_demand': choice(TRUE_OR_FALSE),
            'is_hazmat': choice(TRUE_OR_FALSE),
            'primary_color': schemas.Color(**{
                'color_name': token_hex(6),
                'hex': token_hex(6),
                'approximate_pms': token_hex(6),
                'standard_color_name': token_hex(6)
            }).dict()
        }).dict()
        for i in range(10)
    ]

    product_prices = [
        schemas.ProductPrice(**{
            'quantity_max': randrange(0, 10),
            'quantity_min': randrange(0, 10),
            'price' : uniform(1, 100),
            'discount_code' : token_hex(6)
        }).dict()
        for i in range(10)
    ]


    product_price_groups = [
        schemas.ProductPriceGroup(**{
            'group_name' : token_hex(6),
            'currency' : token_hex(6),
            'description' : token_hex(6),
            'product_price_array' : product_prices
        }).dict()
        for i in range(10)
    ]


    fob_points = [
        schemas.FobPoint(**{
            'fob_id' : token_hex(6),
            'fob_postal_code' : token_hex(6),
            'fob_city' : token_hex(6),
            'fob_state' : token_hex(6),
            'fob_country' : token_hex(6),
        }).dict()
        for i in range(10)
    ]

    new_products = [schemas.ProductData(**{
        'product_id': token_hex(6),
        'product_name': token_hex(6),
        'location_decoration_array': location_decorations,
        'description': token_hex(6),
        'price_expires_date': datetime.utcnow(),
        'product_marketing_point_array': product_marketing_points,
        'product_keyword_array': product_keywords,
        'product_brand': token_hex(6),
        'export' : False,
        'product_category_array': product_categories,
        'related_product_array': related_products,
        'product_part_array': product_parts,
        'last_change_date': datetime.utcnow(),
        'creation_date': datetime.utcnow(),
        'end_date': datetime.utcnow(),
        'effective_date': datetime.utcnow(),
        'is_caution': choice(TRUE_OR_FALSE),
        'caution_comment': token_hex(6), 
        'is_closeout': choice(TRUE_OR_FALSE),
        'line_name': token_hex(6),
        'primary_image_url': token_hex(6),
        'product_price_group_array': product_price_groups,
        'compliance_info_available': choice(TRUE_OR_FALSE),
        'unspsc_commodity_code': randrange(10),
        'imprint_size' : token_hex(6),
        'default_set_up_charge': token_hex(6),
        'default_run_charge': token_hex(6),
        'fob_point_array' :fob_points  
    }) for i in range(count)]

    new_models = [models.ProductData(**new_product.dict())
        for new_product in new_products]

    db_session = get_session()
    for new_model in new_models:
        new_model.location_decoration_array =  json.dumps(new_model.location_decoration_array, default=str)
        new_model.product_marketing_point_array =  json.dumps(new_model.product_marketing_point_array, default=str)
        new_model.product_keyword_array =  json.dumps(new_model.product_keyword_array, default=str)
        new_model.product_category_array =  json.dumps(new_model.product_category_array, default=str)
        new_model.related_product_array =  json.dumps(new_model.related_product_array, default=str)
        new_model.product_part_array =  json.dumps(new_model.product_part_array, default=str)
        new_model.product_price_group_array =  json.dumps(new_model.product_price_group_array, default=str)
        new_model.fob_point_array =  json.dumps(new_model.product_price_group_array, default=str)
        
        db_session.add(new_model)

    db_session.commit()


    products = db_session.query(models.ProductData).all()
    if (products):
        print ('Product Data Successfully Created')
        return

    

def populate_database_media_content(count=1):

    class_types = [
        schemas.ClassType(**{
            'class_type' : randrange(0, 10),
            'class_name' : token_hex(6),
        }).dict()
        for i in range(10)
    ]

    decorations = [
        schemas.Decoration(**{
            'decoration_id' : randrange(0, 10),
            'decoration_name' : token_hex(6),
        }).dict()
        for i in range(10)
    ]


    locations = [
        schemas.Location(**{
            'location_id' : randrange(0, 10),
            'location_name' : token_hex(6),
        }).dict()
        for i in range(10)
    ]

    new_media_contents = [
        schemas.MediaContent(**{
            'product_id': token_hex(6),
            'part_id': token_hex(6),
            'url': token_urlsafe(6),
            'media_type': token_hex(6),
            'class_type_array': class_types,
            'file_size': uniform(0, 10),
            'width':  randrange(0, 10),
            'height':  randrange(0, 10),
            'dpi':  randrange(0, 10),
            'color': token_hex(6), 
            'decoration_array': decorations,
            'location_array': locations,
            'description': token_hex(6),
            'single_part': choice(TRUE_OR_FALSE),
            'change_time_stamp': datetime.utcnow()
            # 'ws_version': token_hex(6),
            # 'id': token_hex(6),
            # 'password': token_hex(6),
            # 'culture_name': token_hex(6),
            # 'media_type': token_hex(6),
            # 'product_id': token_hex(6),
            # 'part_id': token_hex(6),
            # 'class_type': token_hex(6)
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
        print ('Media Content Data Successfully Created')
        return


    # db_session.commit()


