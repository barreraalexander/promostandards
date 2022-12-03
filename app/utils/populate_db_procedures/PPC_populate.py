from app.database import get_session, engine, get_db
from random import randrange, choice, random, uniform
from secrets import token_hex, token_urlsafe
from datetime import datetime, timedelta
from app import schemas
from app import models
import json

from app.utils.populate_db_procedures.random_dataset import TRUE_OR_FALSE


# CREATE PPC ENTITIES
def populate(count=25):
    new_location_decorations = [schemas.LocationDecoration(**{
        'location_name' :f"Token{i}",
        'max_imprint_colors': randrange(0,6),
        'decoration_name': f"Token{i}",
        'location_decoration_combo_default': choice(TRUE_OR_FALSE),
        'price_includes' : choice(TRUE_OR_FALSE)
    }) for i in range(count)]

    new_models = [models.LocationDecoration(**new_location_decoration.dict())
        for new_location_decoration in new_location_decorations]

    db_session = get_session()
    for new_model in new_models:
        db_session.add(new_model)
    db_session.commit()
