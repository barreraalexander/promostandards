from flask import Flask
from app.config import settings
from app import models
from app.database import engine

from app.utils.populate_db_procedures.ProductData_populate import populate as populate_productdata
from app.utils.populate_db_procedures.MediaContent_populate import populate as populate_mediacontent
from app.utils.populate_db_procedures.PPC_populate import populate as populate_ppc
from app.utils.populate_db_procedures.Inventory_populate import populate as populate_inventory

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

        populate_productdata(count=100)
        populate_mediacontent(count=50)
        populate_inventory(count=100)
        populate_ppc(count=50)

    return app