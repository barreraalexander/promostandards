from flask import Flask, jsonify
from app.config import settings
from app import models
from app.database import engine

from app.utils.populate_db_helper import populate_database_location_decoration, populate_database_productdata, populate_database_media_content


def create_app(config_class=settings):
    models.Base.metadata.create_all(bind=engine)

    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.blueprints.api.routes import router as api_router
    app.register_blueprint(api_router)


    if (settings.debug):
        # while in debug, the database will reset everytime it's loaded up
        models.Base.metadata.drop_all(bind=engine)
        models.Base.metadata.create_all(bind=engine)

        populate_database_location_decoration()
        populate_database_productdata()
        populate_database_media_content()


        pass

    return app