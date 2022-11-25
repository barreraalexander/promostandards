from flask import Flask, jsonify
from app.config import settings
from app import models
from app.database import engine



def create_app(config_class=settings):
    models.Base.metadata.create_all(bind=engine)

    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.blueprints.api.routes import router as api_router
    app.register_blueprint(api_router)


    return app