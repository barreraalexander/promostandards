from app.database import get_session
from app import schemas, models
from secrets import token_hex
from random import choice, uniform, randrange
from datetime import datetime
import json
from app.utils.populate_db_procedures.random_dataset import TRUE_OR_FALSE, RANGE_MIN, RANGE_MAX


# CREATE PPC ENTITIES
def populate(count=25):
    
    # available locations
    new_locations = [
        schemas.AvailableLocation(
            location_id=i,
            location_name=f"Token{i}"
        )
        for i in range(count)
    ]

    new_models = [models.AvailableLocation(**new_location.dict())
        for new_location in new_locations]

    db_session = get_session()
    for new_model in new_models:
        db_session.add(new_model)
    db_session.commit()


    #decoration colors
    color_array = [
        schemas.PPC_Color(
            color_id=i,
            color_name=f"Token{i}",
        )
        for i in range(RANGE_MIN, RANGE_MAX)
    ]

    decoration_method_array = [
        schemas.DecorationMethod(
            decoration_id=i,
            decoration_name=f"Token{i}",
        )
        for i in range(RANGE_MIN, RANGE_MAX)
    ]


    new_decoration_colors = [
        schemas.DecorationColor(
            product_id=f"Token{i}",
            location_id=f"Token{i}",
            color_array=color_array,
            pms_match=choice(TRUE_OR_FALSE),
            full_color=choice(TRUE_OR_FALSE),
            decoration_method_array=decoration_method_array,
        )
        for i in range(count)
    ]


    new_models = [models.DecorationColor(**new_decoration_color.dict())
        for new_decoration_color in new_decoration_colors]

    db_session = get_session()
    for new_model in new_models:
        new_model.decoration_method_array = json.dumps(new_model.decoration_method_array, default=str)
        new_model.color_array = json.dumps(new_model.color_array, default=str)

        db_session.add(new_model)
    db_session.commit()

    # fob points
    currency_supported_array = [
        schemas.Currency(
            currency=f"Token{i}",
        )
        for i in range(RANGE_MIN, RANGE_MAX)
        if choice(TRUE_OR_FALSE)
    ]
    
    product_array = [
        schemas.PPC_Product(
            product_id=f"Token{i}",
        )
        for i in range(RANGE_MIN, RANGE_MAX)
        if choice(TRUE_OR_FALSE)
    ]

    new_fob_points = [
        schemas.PPC_FobPoint(
            fob_id=f"Token{i}",
            fob_postal_code=f"Token{i}",
            fob_city=f"Token{i}",
            fob_state=f"Token{i}",
            fob_country=f"Token{i}",
            currency_supported_array=currency_supported_array,
            product_array=product_array
        )
        for i in range(count)
    ]

    new_models = [models.FobPoint(**new_fob_point.dict())
        for new_fob_point in new_fob_points]

    db_session = get_session()
    for new_model in new_models:
        new_model.currency_supported_array = json.dumps(new_model.currency_supported_array, default=str)
        new_model.product_array = json.dumps(new_model.product_array, default=str)

        db_session.add(new_model)
    db_session.commit()

    # available charges
    available_charges = [
        schemas.AvailableCharge(
            charge_id=i,
            charge_name=f"Token{i}",
            charge_type=f"Token{i}",
            charge_description=f"Token{i}",
        )
        for i in range(RANGE_MIN, RANGE_MAX)
    ]
    
    new_models = [models.AvailableCharge(**available_charge.dict())
        for available_charge in available_charges]

    db_session = get_session()
    for new_model in new_models:

        db_session.add(new_model)
    db_session.commit()


    #configuratiion and pricing
    part_price_array = [
        schemas.PartPrice(
            min_quantity=randrange(RANGE_MIN, RANGE_MAX),
            price=uniform(RANGE_MIN, RANGE_MAX),
            discount_code=token_hex(10),
            price_uom=token_hex(10),
            price_effective_date=datetime.utcnow()
        )
        for i in range(randrange(RANGE_MIN, RANGE_MAX))
    ]

    location_id_array = [
        f"Token{i}" for i in range(randrange(RANGE_MIN, RANGE_MAX))
        if choice(TRUE_OR_FALSE)
    ]

    part_array = [
        schemas.PPC_Part(
            part_id=f"Token{i}",
            part_description=f"Token{i}",
            part_price_array=part_price_array,
            part_group=i,
            next_part_group=i,
            part_group_required=choice(TRUE_OR_FALSE),
            part_group_description=f"Token{i}",
            ratio=uniform(0, .9),
            default_part=choice(TRUE_OR_FALSE),
            location_id_array=location_id_array
        )
        for i in range(randrange(RANGE_MIN, RANGE_MAX))
        if choice(TRUE_OR_FALSE)
    ]


    location_array = [
        schemas.Location(
            location_id=i,
            location_name=f"Token{i}"
        )
        for i in range(randrange(RANGE_MIN, RANGE_MAX))
        if choice(TRUE_OR_FALSE)
    ]

    new_configurations = [
        schemas.Configuration(
            product_id=f"Token{i}",
            currency=f"Token{i}",
            price_type=f"Token{i}",
            fob_postal_code=f"Token{i}",
            part_array=part_array,
            location_array=location_array,
            fob_array=new_fob_points,
        )
        for i in range(count)
    ]

    new_models = [models.Configuration(**new_configuration.dict())
        for new_configuration in new_configurations]

    db_session = get_session()
    for new_model in new_models:
        new_model.part_array = json.dumps(new_model.part_array, default=str)
        new_model.location_array = json.dumps(new_model.location_array, default=str)
        new_model.fob_array = json.dumps(new_model.fob_array, default=str)

        db_session.add(new_model)
    db_session.commit()