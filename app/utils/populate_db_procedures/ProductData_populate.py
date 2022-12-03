from app.database import get_session, engine, get_db
from random import randrange, choice, random, uniform
from secrets import token_hex, token_urlsafe
from datetime import datetime, timedelta
from app import schemas
from app import models
import json

from app.utils.populate_db_procedures.random_dataset import TRUE_OR_FALSE


def populate(count=25):
    db_session = get_session()

    location_decorations = [
        schemas.LocationDecoration(**{
            'location_name' :f"Token{i}",
            'max_imprint_colors': randrange(0,6),
            'decoration_name':f"Token{i}",
            'location_decoration_combo_default': choice(TRUE_OR_FALSE),
            'price_includes' : choice(TRUE_OR_FALSE)
        }) for i in range(count)
    ]

    product_marketing_points = [
        schemas.ProductMarketingPoint(**{
            'point_type':f"Token{i}",
            'point_copy':f"Token{i}"
        }).dict()
        for i in range(randrange(1, 30))
    ]

    product_keywords = [
        schemas.ProductKeyword(**{
            'keyword' :f"Token{i}"
        }).dict()
        for i in range(randrange(1, 30))
    ]


    product_categories = [
        schemas.ProductCategory(**{
            'category' :f"Token{i}",
            'sub_category' :f"Token{i}"
        }).dict()
        for i in range(randrange(1, 30))
    ]

    related_products = [
        schemas.RelatedProduct(**{
            'relation_type' :f"Token{i}",
            'product_id' :f"Token{i}",
            'part_id' :f"Token{i}"
        }).dict()
        for i in range(randrange(1, 30))
    ]

    colors = [
        schemas.Color(**{
            'color_name':f"Token{i}",
            'color' :f"Token{i}",
            'hex' :f"Token{i}",
            'approximate_pms' :f"Token{i}",
            'standard_color_name' :f"Token{i}"
        }).dict()
        for i in range(randrange(1, 30))
    ]

    
    specifications = [
        schemas.Specification(**{
            'specification_type' :f"Token{i}",
            'specification_uom' :f"Token{i}",
            'measurement_value' :f"Token{i}"
        }).dict()
        for i in range(randrange(1, 30))
    ]

    product_packagings = [
        schemas.ProductPackaging(**{
            'default': choice(TRUE_OR_FALSE),
            'package_type':f"Token{i}",
            'description':f"Token{i}",
            'quantity':  random(),
            'dimension_uom' :f"Token{i}",
            'depth' : random(),
            'height' : random(),
            'width' : random(),
            'weight_uom' :f"Token{i}",
            'weight' : uniform(1, 10)
        }).dict()
        for i in range(randrange(1, 30))
    ]


    shipping_packagings = [
        schemas.ShippingPackaging(**{
            'package_type':f"Token{i}",
            'description':f"Token{i}",
            'quantity':  random(),
            'dimension_uom' :f"Token{i}",
            'depth' : random(),
            'height' : random(),
            'width' : random(),
            'weight_uom' :f"Token{i}",
            'weight' : uniform(1, 10)
        }).dict()
        for i in range(randrange(1, 30))
    ]


    product_parts = [
        schemas.ProductPart(**{
            'part_id' :f"Token{i}",
            'description' : [token_hex(6) for i in range (randrange(1,10))],
            'country_of_origin' :f"Token{i}",
            'color_array' : colors,
            'primary_material' :f"Token{i}",
            'specification_array' : specifications,
            'shape'  :f"Token{i}",
            'apparel_size'  : schemas.ApparelSize(**{
                  'apparel_style' :f"Token{i}",
                  'label_size':f"Token{i}",
                  'custom_size':f"Token{i}"
            }).dict(),
            'dimension' : schemas.Dimension(**{
                'dimension_uom' :f"Token{i}",
                'depth': randrange(0, 10) * random(),
                'height': randrange(0, 10) * random(),
                'width': randrange(0, 10) * random(),
                'weight_uom':f"Token{i}",
                'weight': uniform(0, 100)
            }).dict(),
            'lead_time' : randrange(0, 10),
            'unspsc' :f"Token{i}",
            'gtin' :f"Token{i}",
            'is_rush_service' : choice(TRUE_OR_FALSE),
            'product_packaging_array': product_packagings,
            'shipping_packaging_array': shipping_packagings,
            'end_date': datetime.utcnow(),
            'effective_date': datetime.utcnow(),
            'is_closeout': choice(TRUE_OR_FALSE),
            'is_caution': choice(TRUE_OR_FALSE),
            'nmfc_code': uniform(0, 10),
            'nmfc_description':f"Token{i}",
            'is_on_demand': choice(TRUE_OR_FALSE),
            'is_hazmat': choice(TRUE_OR_FALSE),
            'primary_color': schemas.Color(**{
                'color_name':f"Token{i}",
                'hex':f"Token{i}",
                'approximate_pms':f"Token{i}",
                'standard_color_name':f"Token{i}"
            }).dict()
        }).dict()
        for i in range(randrange(1, 30))
    ]

    product_prices = [
        schemas.ProductPrice(**{
            'quantity_max': randrange(0, 10),
            'quantity_min': randrange(0, 10),
            'price' : uniform(1, 100),
            'discount_code' :f"Token{i}"
        }).dict()
        for i in range(randrange(1, 30))
    ]


    product_price_groups = [
        schemas.ProductPriceGroup(**{
            'group_name' :f"Token{i}",
            'currency' :f"Token{i}",
            'description' :f"Token{i}",
            'product_price_array' : product_prices
        }).dict()
        for i in range(randrange(1, 30))
    ]


    fob_points = [
        schemas.FobPoint(**{
            'fob_id' :f"Token{i}",
            'fob_postal_code' :f"Token{i}",
            'fob_city' :f"Token{i}",
            'fob_state' :f"Token{i}",
            'fob_country' :f"Token{i}",
        }).dict()
        for i in range(randrange(1, 30))
    ]

    new_products = [schemas.ProductData(**{
        'product_id': f"Token{i}",
        'product_name':f"Token{i}",
        'location_decoration_array': location_decorations,
        'description': [token_hex(6) for i in range (randrange(1,10))],
        'price_expires_date': datetime.utcnow(),
        'product_marketing_point_array': product_marketing_points,
        'product_keyword_array': product_keywords,
        'product_brand':f"Token{i}",
        'export' : False,
        'product_category_array': product_categories,
        'related_product_array': related_products,
        'product_part_array': product_parts,
        'last_change_date': datetime.utcnow(),
        'creation_date': datetime.utcnow(),
        'end_date': datetime.utcnow(),
        'effective_date': datetime.utcnow(),
        'is_caution': choice(TRUE_OR_FALSE),
        'caution_comment':f"Token{i}", 
        'is_closeout': choice(TRUE_OR_FALSE),
        'line_name':f"Token{i}",
        'primary_image_url':f"Token{i}",
        'product_price_group_array': product_price_groups,
        'compliance_info_available': choice(TRUE_OR_FALSE),
        'unspsc_commodity_code': randrange(randrange(1, 30)),
        'imprint_size' :f"Token{i}",
        'default_set_up_charge':f"Token{i}",
        'default_run_charge':f"Token{i}",
        'fob_point_array' :fob_points  
    }) for i in range(count)]

    new_models = [models.ProductData(**new_product.dict())
        for new_product in new_products]

    db_session = get_session()
    for new_model in new_models:
        new_model.description =  json.dumps(new_model.description, default=str)
        new_model.location_decoration_array =  json.dumps(new_model.location_decoration_array, default=str)
        new_model.product_marketing_point_array =  json.dumps(new_model.product_marketing_point_array, default=str)
        new_model.product_keyword_array =  json.dumps(new_model.product_keyword_array, default=str)
        new_model.product_category_array =  json.dumps(new_model.product_category_array, default=str)
        new_model.related_product_array =  json.dumps(new_model.related_product_array, default=str)
        new_model.product_part_array =  json.dumps(new_model.product_part_array, default=str)
        new_model.product_price_group_array =  json.dumps(new_model.product_price_group_array, default=str)
        new_model.fob_point_array =  json.dumps(new_model.fob_point_array, default=str)
        
        db_session.add(new_model)
        # print (new_model)

    db_session.commit()


    products = db_session.query(models.ProductData).all()
    if (products):
        return
