from app.database import get_session, engine, get_db
from random import randrange, choice, random, uniform
from secrets import token_hex, token_urlsafe
from datetime import datetime, timedelta
from app import schemas
from app import models
import json


def populate(count=25):
    pass
