from app.database import get_session, engine, get_db
from random import randrange, choice, random, uniform
from secrets import token_hex, token_urlsafe
from datetime import datetime, timedelta
from app import schemas
from app import models
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